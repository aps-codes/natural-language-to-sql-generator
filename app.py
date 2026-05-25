from groq import Groq
import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv
import streamlit as st

# load env
load_dotenv()

# groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# page config
st.set_page_config(
    page_title="AI-Powered Text-to-SQL Generator",
    page_icon="database",
    layout="centered"
)

st.title("AI-Powered Text-to-SQL Generator")
st.write("Convert natural language into executable SQL queries using Groq LLM")

# ── schema info shown to user ────────────────────────────────────────────────
with st.expander("View Database Schema (STUDENTS table)"):
    st.code("""
Table: STUDENTS
Columns:
  student_id   INTEGER  (auto)
  student_name TEXT
  class        INTEGER  (9, 10, 11, 12)
  roll_no      INTEGER
  gender       TEXT     (Male / Female)
  maths_marks  INTEGER
  science_marks INTEGER
  english_marks INTEGER
  percentage   REAL
  attendance   INTEGER
  result       TEXT     (Pass / Fail)
    """)

# ── generate sql query ────────────────────────────────────────────────────────
def get_sql_query(question):
    prompt = f"""
You are an expert SQLite SQL query generator.

Convert the following English question into a valid SQLite SQL query.

Database: school.db
Table: STUDENTS
Columns: student_id, student_name, class, roll_no, gender,
         maths_marks, science_marks, english_marks, percentage, attendance, result

Important rules:
- Use only valid SQLite syntax.
- Use ROW_NUMBER() only for group-wise ranking queries (e.g. topper of each class or top 5 students of each class).
- For simple top N queries, use ORDER BY + LIMIT.
- Return ONLY the raw SQL query. No explanation, no markdown, no backticks.

Question: {question}
"""
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    query = response.choices[0].message.content
    # strip any accidental markdown fences
    query = query.replace("```sql", "").replace("```", "").strip()
    return query


# ── run sql and return (dataframe, error_message) ────────────────────────────
def run_sql_query(query):
    try:
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # get column names from the ACTUAL query result, not a hardcoded list
        col_names = [description[0] for description in cursor.description]
        connection.close()

        if not rows:
            return None, None, "Query executed successfully but returned no rows."

        df = pd.DataFrame(rows, columns=col_names)
        return df, None, None

    except Exception as e:
        return None, str(e), None


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("---")
question = st.text_input(
    "Enter Your Question",
    placeholder="e.g. show me top 5 students of each class"
)

if st.button("Generate Result", type="primary"):
    if not question.strip():
        st.warning("Please enter a question before clicking Generate Result.")
    else:
        with st.spinner("Generating SQL query..."):
            sql_query = get_sql_query(question)

        st.subheader("Generated SQL Query")
        st.code(sql_query, language="sql")

        with st.spinner("Running query on database..."):
            df, error, info = run_sql_query(sql_query)

        st.subheader("Query Result")

        if error:
            st.error(f"Error: {error}")
        elif info:
            st.info(info)
        else:
            st.success(f"{len(df)} row(s) returned")
            st.dataframe(df, use_container_width=True)
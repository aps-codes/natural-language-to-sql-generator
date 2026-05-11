from groq import Groq
import sqlite3
import os
from dotenv import load_dotenv
import streamlit as st

# load env
load_dotenv()

# groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# page title
st.set_page_config(page_title="Natural Language to SQL Query Generator using Groq LLM")

st.title("Natural Language to SQL Query Generator using Groq LLM")
st.write("Ask questions about school database")

# generate sql query
def get_sql_query(question):

    prompt = f"""
    You are an expert SQL query generator.

    Convert the following English question into a valid SQLite SQL query.

    Database Name: school.db

    Table Name: STUDENTS

    Columns:
    student_id
    student_name
    class
    roll_no
    gender
    maths_marks
    science_marks
    english_marks
    percentage
    attendance
    result

    Only give SQL query.
    Do not explain anything.

    Question:
    {question}
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    query = response.choices[0].message.content

    query = query.replace("```sql", "").replace("```", "").strip()

    return query

# run sql query
def run_sql_query(query):

    connection = sqlite3.connect("school.db")

    cursor = connection.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return rows

# input box
question = st.text_input("Enter Your Question")

# button
if st.button("Generate Result"):

    sql_query = get_sql_query(question)

    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")

    result = run_sql_query(sql_query)

    st.subheader("Query Result")

    for row in result:
        st.write(row)


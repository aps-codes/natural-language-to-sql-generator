# Natural Language to SQL Generator

Converts plain English questions into executable SQL queries instantly.  
Type a question → AI generates the SQL → results displayed from the database.

**Live Demo:** (https://aps-nl-to-sql.streamlit.app)

---

## Features

- Convert natural language input to SQL queries
- Execute queries directly on a SQLite database
- AI-powered SQL generation using Groq LLM
- Real-time query results via Streamlit interface
- No SQL knowledge required to query the database

---

## Preview

### Home Page
![Home Page](screenshots/homepage.png)

### Generated SQL Query
![Generated SQL Query](screenshots/query.png)

### Query Result
![Query Result](screenshots/result.png)

---

## Tech Stack

| Layer    | Technology                         |
|----------|------------------------------------|
| LLM      | Groq API (llama-3.3-70b-versatile) |
| Database | SQLite                             |
| Frontend | Streamlit                          |
| Language | Python 3.10+                       |

---

## How It Works

```
Input:  "Show students who scored above 80"
           ↓
Groq LLM → SELECT * FROM STUDENT WHERE MARKS > 80
           ↓
     Query runs on SQLite → Results displayed
```

The application uses prompt engineering techniques to generate accurate SQL queries from natural language input.

---

## Run Locally

```bash
git clone https://github.com/aps-codes/natural-language-to-sql-generator.git
cd natural-language-to-sql-generator
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_key_here
```

Get a free key at [console.groq.com](https://console.groq.com), then:

```bash
python database.py   # set up sample database
streamlit run app.py
```
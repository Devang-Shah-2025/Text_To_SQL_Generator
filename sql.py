from dotenv import load_dotenv

load_dotenv() ## Load environment variables from .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

##Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve query from the database

def read_sql_query(sql,db):
    connection= sqlite3.connect(db)
    cursor= connection.cursor()
    cursor.execute(sql)
    rows= cursor.fetchall()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt

prompt=[
    """
     You are an expert in converting English questions to SQL query !
     The SQL database has the name STUDENT and has the following columns:
     NAME, CLASS, SECTION \n\nFor example, \nExample 1- How many entries of the records are present?,
     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT; 
     \nExample 2- What are the names of the students in section A?, 
     the SQL command will be something like this SELECT NAME FROM STUDENT WHERE SECTION='A';
     \nExample 3- What are the names of the students in Data Science class?,
     the SQL command will be something like this SELECT NAME FROM STUDENT WHERE CLASS='Data Science';

     also the sql code should not have ``` in beginning or end and sql word in output

"""
]

## Streamlit App

st.set_page_config(page_title="I can retrieve Any SQL query", page_icon=":guardsman:", layout="wide")
st.header("Gemini App to Retrieve SQL Data")

question= st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If submit is clicked

if submit:
    response= get_gemini_response(question, prompt)
    print(response)
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")
    response= read_sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)
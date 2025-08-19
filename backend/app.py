import streamlit as st
from db_config import get_connection, create_user_table

st.set_page_config(page_title="Text to Speech App", layout="wide")
create_user_table()

def signup(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Signup successful! Please log in.")

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

st.title("🗣️ Text-to-Speech Dashboard")
page = st.sidebar.radio("Choose a page", ["Login", "Signup", "Dashboard"])

if page == "Signup":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if new_user and new_pass:
            signup(new_user, new_pass)
        else:
            st.warning("Please fill in both fields.")

elif page == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login(username, password)
        if user:
            st.session_state["user"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials.")

elif page == "Dashboard":
    if "user" in st.session_state:
        st.subheader(f"Welcome, {st.session_state['user']} 👋")
        text = st.text_area("Enter text to convert to speech:")
        if st.button("Convert"):
            st.audio(f"https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={text}", format="audio/mp3")
    else:
        st.warning("Please log in to view the dashboard.")

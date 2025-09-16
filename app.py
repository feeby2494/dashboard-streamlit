import streamlit as st
import streamlit_authenticator as stauth


# username = ""
# password = ""

# st.title("Hello Streamlit-er 👋")
# st.markdown(
#     """ 
#     This is a playground for you to try Streamlit and have fun. 

#     **There's :rainbow[so much] you can build!**
    
#     We prepared a few examples for you to get started. Just 
#     click on the buttons above and discover what you can do 
#     with Streamlit. 
#     """
# )

# st.title("testing for real")

# st.text_input(username, value="", max_chars=None, key=None, type="default", on_change=None, placeholder="username", disabled=False, width="stretch")
# st.text_input(password, value="", max_chars=None, key=None, type="password", on_change=None, placeholder=None, disabled=False, width="stretch")


# Dummy credentials
USERNAME = "admin"
PASSWORD = "password"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login form
def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# Main app content
def main_app():
    st.title("🎉 Welcome to the App")
    st.write("You're now logged in and can access the main content.")

# Render appropriate view
if st.session_state.logged_in:
    main_app()
else:
    login()
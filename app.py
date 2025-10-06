import streamlit as st
import bcrypt

import yaml
from yaml.loader import SafeLoader
from home_component import st_home
from about_component import st_about

# load the secure yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# print(config)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "about" not in st.session_state:
    st.session_state.about = False

if "home" not in st.session_state:
    st.session_state.home = False

# Login form
def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in config["credentials"]["usernames"]:


            # print(f"user entered password: {type(password.encode('utf-8'))}")
            # print(f"hashed password: {type(config['credentials']['usernames'][username]['password'])}")
            # print(f"hashed password: {config['credentials']['usernames'][username]['password'][2:-1].encode('utf-8')}")

            if bcrypt.checkpw(password.encode("utf-8"), config["credentials"]["usernames"][username]["password"][2:-1].encode("utf-8")):
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()  # 🔁 Force rerun to update UI
            else:
                st.error("Invalid Password")
        else:
            st.error("Invalid Username")

# Main app content
def main_app():
    nav()
    if st.session_state.about:
        about()
    elif st.session_state.home:
        home()
    else:
        home()

# Toggle Nav Switches
def switchToAbout():
    st.session_state.about = True
    st.session_state.home = False
    print("-------------------------------")
    print(f"Home: {st.session_state.home}")
    print(f"About: {st.session_state.about}")
    print("-------------------------------")

def switchToHome():
    st.session_state.home = True
    st.session_state.about = False
    print("-------------------------------")
    print(f"Home: {st.session_state.home}")
    print(f"About: {st.session_state.about}")
    print("-------------------------------")

# Components for UI
def nav():
    if st.session_state.about:
        st.button("Home", on_click=switchToHome)
    else:
        st.button("About", on_click=switchToAbout)

def home():
    st.title("🎉 Welcome to the App")
    st.write("You're now logged in and can access the main content.")
    v = st_home()
    st.write("Returned value:", v)

def about():
    st.title("About Our App")
    st.write("Our app....")
    v2 = st_about()
    st.write("Returned value:", v2)


# Render appropriate view
if st.session_state.logged_in:
    main_app()
else:
    login()

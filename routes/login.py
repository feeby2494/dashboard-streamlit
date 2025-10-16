from utilites.shared import st, bcrypt, os
from utilites.config_utils import load_config
from routes.register import register


# laod the config file with users:
config = load_config(os.path.join(os.getcwd(), "config.yaml"))



# Login form
def loginSubmit(username, password):
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

def login():
    if st.session_state.register:
        # show the register form:
        register()
    else:
        st.title("🔐 Login Page")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.button("Login", on_click=lambda u=username, p=password: loginSubmit(u, p))

        st.markdown("---")
        st.info("Don't have an account?")
        if st.button("Register"):
            st.session_state.register = True
            st.rerun()
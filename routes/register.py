from utilites.shared import st, bcrypt, os
from utilites.config_utils import load_config, save_config

def register():

    #need to load config with users first,so we can modify and overwrite with new updated config
    config = load_config(os.path.join(os.getcwd(), "config.yaml"))

    st.title("📝 Register New User")

    new_username = st.text_input("New Username")
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_password != confirm_password:
            st.error("Passwords do not match.")
            return
        
        if new_email in config["credentials"]["usernames"]:
            st.error("email already exists.")
            return

        # Check if email already exists among registered users
        for user_data in config["credentials"]["usernames"].values():
            if user_data.get("email") == new_email:
                st.error("Email already exists.")
                return

        hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())

        # Update config in memory
        config["credentials"]["usernames"][new_username] = {
            "email": new_email,  # optional
            "name": new_username,
            "password": str(hashed_pw)  # store as string
        }

        print(os.path.join(os.getcwd(), "config.yaml"))

        # Write back to config.yaml
        save_config(os.path.join(os.getcwd(), "config.yaml"), config)

        st.success("User registered successfully!")
        
        # go back to login page
        st.session_state.register = False
        st.rerun()

    if st.button("Have an Account?"):
        # go back to login page
        st.session_state.register = False
        st.rerun()
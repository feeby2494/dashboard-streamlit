from shared import st
import bcrypt
import os

import yaml
from yaml.loader import SafeLoader
from home_component import st_home
from about_component import st_about

from routes.map_route import map_route

# load the secure yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# print(config)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# list of routes
### Future dynamic route detection
print([route for route in os.listdir(os.path.join(os.getcwd(), "routes")) if route not in ("__init__.py", "__pycache__")])
pageRoutes = ["home", "about", "map"]

# init each route in st.session_state
for route in pageRoutes:
    if route not in st.session_state: # avoids running every streamlit iterration; only first time load
        if route == "home":
            #print("home is true")
            st.session_state[route] = True # home page is true on startup
        else:
            st.session_state[route] = False
        #print(f"Beginning:\nroute: {route}\nsession:{st.session_state[route]}")

#print(f"before logging in: {st.session_state}")

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
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.button("Login", on_click=lambda u=username, p=password: loginSubmit(u, p))

    


# Toggle Nav Switches

# main switch to route def
def switchToRoute(selected_page, routes):
    for route in routes:
        print(selected_page)
        print(route)
        if route is selected_page:
            print(f"nav: route set to true: {route}")
            st.session_state[route] = True # select the one route
        else: # deselect all other routes; one route at a time
            print(f"nav: route set to false: {route}")
            st.session_state[route] = False
        


# Components for UI
def nav(pageRoutes):
    for route in pageRoutes:  # want to show list of all routes that are set to false
        if st.session_state[route] == False:
            st.button(f"{route.capitalize()}", on_click=lambda r=route, p=pageRoutes: switchToRoute(r, p))

# individual Route Views
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

map = map_route


# stores our route views in definition ; will make from names of 'route' dir later
route_map = {
    "home": home,
    "about": about,
    "map": map
}


################################################################
#                         Main_app
################################################################
# Main app content
def main_app():
    nav(pageRoutes)
    #print(f"after losding navbar: {st.session_state}")
    #print(f"routes => {pageRoutes}")
    for route in pageRoutes:  # want to show the route set to true
        
        #print(f"ending:\nroute: {route}\nseesion:{st.session_state[route]}")


        if st.session_state[route] == True:
            #print(st.session_state[route])
            # run the method for that route that matches with route var


            view = route_map.get(route)
            if view:
                view()
            else:
                st.write("No Route Method Found!")
    #print(f"after: {st.session_state}")

# Render appropriate view
if st.session_state.logged_in:
    main_app()
else:
    login()

# dashboard-streamlit



# Steps to make a new custom componet using react.js
1. Make new folder in root directory of project:
    - mkdir <new componet name>
2. Move inside folder:
    - cd <new componet name>
3. Make the python streamlit wrapper for custom componet:
    - vim __init__.py
4. __init__.py example:
    import streamlit.components.v1 as components
    import os

    _componet_funct = components.declare_component(
        "example",
        path=os.path.join(os.path.dirname(__file__), "frontend", "dist")
    )

    def st_example():
        print("st_example works")
        print(os.path.join(os.getcwd(), "frontend", "dist"))
        component_value = _componet_funct()
        return component_value
5. Build the react "frontend" app inside <root of project>/<new componet name>/:
    - npm create vite@latest frontend
6. As of now, can only get npm library streamlit-component-lib to work with react 18 and react-dom 18:
    - We need to move inside "frontend" folder and edit the package.json file:
        - cd ./frontend
        - vim package.json
        - change these from 19.x.x to:
            - "react": "^18.3.1",
            - "react-dom": "^18.3.1",
            - "@types/react": "^18",
            - "@types/react-dom": "^18",
7. Install npm packages:
    - npm install
    - npm install streamlit-component-lib
8. Add streamlit-component-lib into <root of project>/<new componet name>/frontend/src/App.jsx:
    - 
        import { 
            Streamlit, 
            withStreamlitConnection,
        } from "streamlit-component-lib";

9. use react's useEffect hook to pass a test var back to streamlit and to fix the component height ( without this, componet will not show on streamlit side):
    - 
        useEffect(() => {
            Streamlit.setComponentValue("some value");
            Streamlit.setFrameHeight();
        }, []);

10. Pass the App component/function into the withStreamlitConnection hight-level function:
    - export default withStreamlitConnection(App);
11. Setup vite build to use relative paths for assets:
    - Inside <root of project>/<new componet name>/frontend/vite.config.js file:
    - inside the export default defineConfig({}) inner object add:
        - 
            base: '',
12. Move to: <root of project>/<new componet name>/frontend
13. npm run build
14. cd ../..
15. source ./venv/bin/activate
16. streamlit run app.py
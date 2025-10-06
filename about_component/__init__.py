import streamlit.components.v1 as components
import os

_component_funct = components.declare_component(
        "about_component",
        path=os.path.join(os.path.dirname(__file__), "frontend", "dist")
)

def st_about():
    print("st_example works")
    print(os.path.join(os.getcwd(), "frontend", "dist"))
    component_value = _component_funct()
    return component_value

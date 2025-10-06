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

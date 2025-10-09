from shared import st, pd
from map_component import st_map

def map_route():
    points = [
        {
            "name": "New York City",
            "latitude": 40.7128,
            "longitude": -74.0060
        },
        {
            "name": "Los Angeles",
            "latitude": 34.0522,
            "longitude": -118.2437
        },
        {
            "name": "Chicago",
            "latitude": 41.8781,
            "longitude": -87.6298
        },
        {
            "name": "Houston",
            "latitude": 29.7604,
            "longitude": -95.3698
        },
        {
            "name": "Miami",
            "latitude": 25.7617,
            "longitude": -80.1918
        }
    ]

    points_df = pd.DataFrame(points)

    if "points_df" not in st.session_state:
        st.session_state.points_df = pd.DataFrame(points)

    # with st.form("data_input"):
    #     st.write("future cvs/excel import feature")
    #     st.form_submit_button('Submit my picks')
    edited_df = st.data_editor(st.session_state.points_df, num_rows="dynamic")

    if st.button("update map:"):
        st.session_state.points_df = edited_df # save edits
    
    mapReturn = st_map(points_df=st.session_state.points_df) # want to pass in edited dataframe to map
    st.write("Returned value:", mapReturn)
    
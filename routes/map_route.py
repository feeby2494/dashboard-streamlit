from utilites.shared import st, pd, os
from map_component import st_map
from fastkml import KML

def map_route():
    points = [
        {
            "name": "Starbucks",
            "latitude": 32.97117531920037,
            "longitude": -96.99265809536793
        },
        {
            "name": "Ecclesia Bakery",
            "latitude": 32.95185254663749,
            "longitude": -96.95740144436381
        },
        {
            "name": "Paris Baguette",
            "latitude": 32.92747927396114,
            "longitude": -96.9943250809797
        },
        {
            "name": "Starbucks",
            "latitude": 32.97362385060124,
            "longitude": -97.03755090732481
        },
    ]

    points_df = pd.DataFrame(points)


    
    if "points_df" not in st.session_state:
        st.session_state.points_df = pd.DataFrame(points)

    ################## Can edit these point during session, but maybe not needed
    #edited_df = st.data_editor(st.session_state.points_df, num_rows="dynamic")
    #
    #if st.button("update map:"):
    #    st.session_state.points_df = edited_df # save edits
    ##################
    
    
    mapReturn = st_map(points_df=st.session_state.points_df) # want to pass in edited dataframe to map
    st.write("Returned value:", mapReturn)
    st.page_link("https://www.flaticon.com/free-icons/town", label="Town icons created by Zlatko Najdenovski - Flaticon", icon="🌎")
# Import required packages
from geopy.geocoders import ArcGIS
import folium
import streamlit as st
from streamlit_folium import st_folium

page_title = "Geo localistion of given place(s) and display respective coordinates on map"
layout = "centered"

def main():
    st.set_page_config(page_title = page_title, layout = layout)
    st.title(page_title)

if __name__ == '__main__':
    main()

# --- Hide Streamlit Style ---
hide_st_style = """
                <style>
                #MainMenu {Visibility: hidden;}
                footer {Visibility: hidden;}
                header {Visibility: hidden;}
                </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

nom=ArcGIS()

# User input number of places to Geo locate
nbr_places = st.number_input('Enter number of places to geo locate',\
                           min_value=1, max_value=10, value=2, step=1)


def geo_locate(lat, long, nameofplace):
    # Display the latitude and longitude coordinates of the given place
    st.write(f'Latitude of {nameofplace}: {lat}')
    st.write(f'Longitude of {nameofplace}: {long}')

    # center on place coordinates, add marker
    m = folium.Map(location=[lat, long], zoom_start=6)
    folium.Marker(
        [lat,long],popup=f'{nameofplace, lat, long}',icon=folium.Icon(color='purple')
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

# Function to get the latitude and longitude coordinates of a place
def calc_coordinates(place_name):
    # Function call to get the latitude and longitude coordinates of a place
    coord = nom.geocode(place_name)

    # Display map based on the place coordinates if place name is entered
    if coord:
        lat = coord.latitude
        long = coord.longitude
    
        # Call function to geo locate the place in the map
        place_in_map = geo_locate(lat, long, place_name)


i = 1
while i <= nbr_places:
      place_name = st.text_input(f"Enter the name of a place {i} 👇")

      if place_name != '':
        # Function call to get the latitude and longitude coordinates of a place
        calc_coordinates(place_name)
    
      i += 1
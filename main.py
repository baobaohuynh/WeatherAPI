import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))


if place:
    st.subheader(f"{option} for the next {days} days in {place}")
    filtered_data = get_data(place, days)

    temp_min = [dict["main"]["temp"] for dict in filtered_data]
    temp_list = []
    for temp in temp_min:
        temp_list.append(temp - 273.15)
    temp_min = min(temp_list)
    temp_min = str(temp_min)[:5]
    st.write(f"Min Temperature in {place} for the next {days} days is: {temp_min} C")

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        temp_list = []
        for temp in temperatures:
            temp_list.append(temp - 273.15)
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temp_list, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        for date, image in zip(dates, image_paths):
            st.image(image, width=115)
            st.write(f"{date}:")

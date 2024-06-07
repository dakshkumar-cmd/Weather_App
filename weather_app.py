import json
import requests
import streamlit as st
st.set_page_config(page_title="Weather App",page_icon=":tada:")

city = st.text_input("Enter your current city: ")
but = st.button("Submit")
if but:
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=41b5cc83d6ce41ee87142846240506&q={city}"
        a = requests.get(url)
        wdc = json.loads(a.text)

        # Extract location information
        location_name = wdc["location"]["name"]
        region = wdc["location"]["region"]
        country = wdc["location"]["country"]
        lat = wdc["location"]["lat"]
        lon = wdc["location"]["lon"]
        tz_id = wdc["location"]["tz_id"]
        localtime = wdc["location"]["localtime"]

        # Extract current weather information
        last_updated = wdc["current"]["last_updated"]
        temp_c = wdc["current"]["temp_c"]
        temp_f = wdc["current"]["temp_f"]
        is_day = wdc["current"]["is_day"]
        condition_text = wdc["current"]["condition"]["text"]
        condition_icon = wdc["current"]["condition"]["icon"]
        condition_code = wdc["current"]["condition"]["code"]
        wind_mph = wdc["current"]["wind_mph"]
        wind_kph = wdc["current"]["wind_kph"]
        wind_degree = wdc["current"]["wind_degree"]
        wind_dir = wdc["current"]["wind_dir"]
        pressure_mb = wdc["current"]["pressure_mb"]
        pressure_in = wdc["current"]["pressure_in"]
        precip_mm = wdc["current"]["precip_mm"]
        precip_in = wdc["current"]["precip_in"]
        humidity = wdc["current"]["humidity"]
        cloud = wdc["current"]["cloud"]
        feelslike_c = wdc["current"]["feelslike_c"]
        feelslike_f = wdc["current"]["feelslike_f"]
        windchill_c = wdc["current"]["windchill_c"]
        windchill_f = wdc["current"]["windchill_f"]
        heatindex_c = wdc["current"]["heatindex_c"]
        heatindex_f = wdc["current"]["heatindex_f"]
        dewpoint_c = wdc["current"]["dewpoint_c"]
        dewpoint_f = wdc["current"]["dewpoint_f"]
        vis_km = wdc["current"]["vis_km"]
        vis_miles = wdc["current"]["vis_miles"]
        uv = wdc["current"]["uv"]
        gust_mph = wdc["current"]["gust_mph"]
        gust_kph = wdc["current"]["gust_kph"]

        # Print all extracted information
        st.text(f"Location:")
        st.text(f"  Name: {location_name}")
        st.text(f"  Region: {region}")
        st.text(f"  Country: {country}")
        st.text(f"  Latitude: {lat}")
        st.text(f"  Longitude: {lon}")
        st.text(f"  Timezone: {tz_id}")
        st.text(f"  Local Time: {localtime}")

        st.text(f"\nCurrent Weather:")
        st.text(f"  Last Updated: {last_updated}")
        st.text(f"  Temperature: {temp_c}°C ({temp_f}°F)")
        st.text(f"  Is Day: {'Yes' if is_day else 'No'}")

        st.text(f"  Wind: {wind_mph} mph ({wind_kph} kph) from {wind_dir} ({wind_degree}°)")
        st.text(f"  Pressure: {pressure_mb} mb ({pressure_in} in)")
        st.text(f"  Precipitation: {precip_mm} mm ({precip_in} in)")
        st.text(f"  Humidity: {humidity}%")
        st.text(f"  Cloud Cover: {cloud}%")
        st.text(f"  Feels Like: {feelslike_c}°C ({feelslike_f}°F)")
        st.text(f"  Wind Chill: {windchill_c}°C ({windchill_f}°F)")
        st.text(f"  Heat Index: {heatindex_c}°C ({heatindex_f}°F)")
        st.text(f"  Dew Point: {dewpoint_c}°C ({dewpoint_f}°F)")
        st.text(f"  Visibility: {vis_km} km ({vis_miles} miles)")
        st.text(f"  UV Index: {uv}")
        st.text(f"  Gust Speed: {gust_mph} mph ({gust_kph} kph)")


    except Exception as e:
        st.error("Some Error Occured")



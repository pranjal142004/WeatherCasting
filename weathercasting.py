import requests
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

# Function to fetch weather data from OpenWeatherMap
def get_weather():
    location = com.get()
    if location:
        api_key = "791b484afde68d05802553f53ca8193d"  # Using the provided API key
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()
            print(data)  # Debugging line to see the response from the API

            if response.status_code == 200:
                city = data['city']['name']
                forecast_list = data['list'][:40:8]  # Fetching forecast for the next 5 days (1 entry per day, usually every 3 hours)

                weather_report = f"5-Day Weather Forecast for {city}:\n\n"

                for forecast in forecast_list:
                    # Extract relevant forecast data
                    timestamp = forecast['dt']
                    date = datetime.fromtimestamp(timestamp).strftime("%B %d, %Y")
                    time = datetime.fromtimestamp(timestamp).strftime("%I:%M %p")
                    weather = forecast['weather'][0]['description']
                    temperature_c = forecast['main']['temp']
                    temperature_f = (temperature_c * 9/5) + 32  # Convert to Fahrenheit
                    humidity = forecast['main']['humidity']
                    wind_speed = forecast['wind']['speed']

                    # Append each forecast to the weather report string
                    weather_report += (
                        f"Date: {date}\n"
                        f"Time: {time}\n"
                        f"Condition: {weather.capitalize()}\n"
                        f"Temperature: {temperature_c}°C / {temperature_f:.1f}°F\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s\n\n"
                    )

                messagebox.showinfo("5-Day Weather Forecast", weather_report)
            elif response.status_code == 401:
                messagebox.showerror("Error", "Invalid API key. Please check your API key.")
            else:
                error_message = data.get("message", "Location not found.")
                messagebox.showerror("Error", error_message)
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")
    else:
        messagebox.showwarning("Selection Error", "Please select a location.")

# Create the main window and GUI components
win = Tk()
win.title("SkyCast - Professional Weather App")
win.config(bg="#4c86a8")
win.geometry("500x550")

# Header
header_label = Label(win, text="SkyCast", font=("Helvetica", 32, "bold"), fg="white", bg="#4c86a8")
header_label.place(x=25, y=40, height=60, width=450)

# Tagline
tagline_label = Label(win, text="Your Personal Weather Companion", font=("Helvetica", 16), fg="white", bg="#4c86a8")
tagline_label.place(x=25, y=100, height=30, width=450)

# List of cities for selection
list_name = [
    # Cities from India (your original list)
    "Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai", 
    "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Vadodara",
    "Jaunpur", "Varanasi", "Ayodhya", "Gorakhpur", "Prayagraj",
    "Agra", "Mathura", "Meerut", "Noida", "Ghaziabad",
    "Aligarh", "Bareilly", "Moradabad", "Jhansi", "Firozabad",

    # Cities from other parts of the world
    "New York", "London", "Tokyo", "Paris", "Berlin", 
    "Sydney", "Toronto", "Moscow", "Los Angeles", "Beijing",
    "Rio de Janeiro", "Cape Town", "Seoul", "Dubai", "Mexico City", 
    "Cairo", "Singapore", "Istanbul", "Rome", "Buenos Aires", 
    "Madrid", "Bangkok", "Jakarta", "Lagos", "Hong Kong", 
    "Lima", "Manila", "Kuala Lumpur", "Tehran", "Karachi",
    "Baghdad", "Vienna", "Sao Paulo", "Nairobi", "Zurich"
]


# Dropdown menu for city selection
com = ttk.Combobox(win, values=list_name, font=("Helvetica", 16))
com.place(x=50, y=160, height=40, width=400)

# Button to fetch the weather
weather_button = Button(win, text="Check the weather", font=("Helvetica", 16, "bold"), bg="#2d5d77", fg="white", command=get_weather)
weather_button.place(x=100, y=230, height=50, width=300)

# Footer
footer_label = Label(win, text="Powered by OpenWeatherMap", font=("Helvetica", 10), fg="white", bg="#4c86a8")
footer_label.place(x=150, y=500, height=20, width=200)

# Main loop
win.mainloop()
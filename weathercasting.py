import requests
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

def get_weather():
    location = com.get()
    if location:
        api_key = "791b484afde68d05802553f53ca8193d" 
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                city = data['city']['name']
                forecast_list = data['list'][:40:8]  

                current_weather = forecast_list[0]
                current_temp = current_weather['main']['temp']
                current_condition = current_weather['weather'][0]['description'].capitalize()
                current_wind_speed = current_weather['wind']['speed']
                current_humidity = current_weather['main']['humidity']

                current_weather_label.config(
                    text=(
                        f"{city}\n"
                        f"Temperature: {current_temp}°C | {current_condition}\n"
                        f"Wind: {current_wind_speed} m/s | Humidity: {current_humidity}%"
                    )
                )

                for i, forecast in enumerate(forecast_list):
                    timestamp = forecast['dt']
                    date = datetime.fromtimestamp(timestamp).strftime("%A")  
                    temp = forecast['main']['temp']
                    condition = forecast['weather'][0]['description'].capitalize()

                    forecast_labels[i].config(text=f"{date}: {temp}°C | {condition}")

            elif response.status_code == 401:
                messagebox.showerror("Error", "Invalid API key. Please check your API key.")
            else:
                error_message = data.get("message", "Location not found.")
                messagebox.showerror("Error", error_message)
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")
    else:
        messagebox.showwarning("Selection Error", "Please select a location.")

win = Tk()
win.title("SkyCast - Professional Weather App")
win.config(bg="#4c86a8")
win.geometry("500x600")

header_label = Label(win, text="SkyCast", font=("Helvetica", 32, "bold"), fg="white", bg="#4c86a8")
header_label.place(x=25, y=40, height=60, width=450)

tagline_label = Label(win, text="Your Personal Weather Companion", font=("Helvetica", 16), fg="white", bg="#4c86a8")
tagline_label.place(x=25, y=100, height=30, width=450)

list_name = [
    "Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai", "Hyderabad", "New York", "London", "Tokyo", "Paris", 
    
]

com = ttk.Combobox(win, values=list_name, font=("Helvetica", 16))
com.place(x=50, y=160, height=40, width=400)

weather_button = Button(win, text="Check the weather", font=("Helvetica", 16, "bold"), bg="#2d5d77", fg="white", command=get_weather)
weather_button.place(x=100, y=230, height=50, width=300)

current_weather_label = Label(win, font=("Helvetica", 16), fg="white", bg="#4c86a8", justify=LEFT)
current_weather_label.place(x=50, y=300, height=100, width=400)

forecast_labels = []
for i in range(5):
    label = Label(win, font=("Helvetica", 14), fg="white", bg="#4c86a8", justify=LEFT)
    label.place(x=50, y=420 + (i * 30), height=30, width=400)
    forecast_labels.append(label)

footer_label = Label(win, text="Powered by OpenWeatherMap", font=("Helvetica", 10), fg="white", bg="#4c86a8")
footer_label.place(x=150, y=570, height=20, width=200)

win.mainloop()

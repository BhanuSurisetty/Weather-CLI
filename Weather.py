import requests
import json
import os
from colorama import init, Fore, Style
#from colorama import init,Fore, Style

# Initialize colorama
init(autoreset=True)

API_KEY = "b7411bc0d4b88bf5552cb0683e7978c6"  # Replace with your OpenWeatherMap API key
HISTORY_FILE = "history.json"

# Function to fetch weather data
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code ==200:
        data = response.json()
        return data
    else:
        print(Fore.RED + "Error fetching weather data.")
        return None
# Function to display weather data
def display_weather(data):
    if data:
         print(Fore.CYAN + f"\nWeather Report for {data['name']}, {data['sys']['country']}")
         print(Fore.YELLOW + f"Temperature: {data['main']['temp']}°C")
         print(Fore.GREEN + f"Humidity: {data['main']['humidity']}%")
         print(Fore.MAGENTA + f"Condition: {data['weather'][0]['description'].capitalize()}")

#function to save history
def save_history(city):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE,"r")as file:
              history= json.load(file)
              history.append(city)
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

# Function to load history
def show_history():
    if os.path.exists(HISTORY_FILE):
        print(Fore.WHITE + "\nSearch History:")
        with open(HISTORY_FILE,"r")as file:
            history = json.load(file)
            for i,city in enumerate(history[-5:], 1):
                print(f"{i}. {city}")
    else:
        print(Fore.WHITE + "\nNo search history found.")

# Main function
def main():
    print(Fore.BLUE + "Welcome to the Weather App!")
    while True:
        city = input(Fore.BLUE + "\nEnter a city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_data = fetch_weather(city)
        if weather_data and weather_data.get("main"):
            display_weather(weather_data)
            save_history(city)
        else:
            print(Fore.RED + "City not found. Please try again.")
        show_history()

if __name__ =="__main__":
    main()


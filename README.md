# 🌦️ Weather CLI App

A simple command-line Python application to fetch and display current weather information using the [OpenWeatherMap API](https://openweathermap.org/api). The app also saves your last 5 search histories in a JSON file for quick reference.

---

## 📦 Features

- ✅ Search weather by city name.
- ✅ Displays:
  - Country & City
  - Temperature in °C
  - Humidity
  - Weather Condition (description)
- ✅ Keeps last 5 searched cities in a `history.json` file.
- ✅ Colorful terminal output using `colorama`.

---

## 🚀 How to Run

### 1. Clone this Repository

'''bash
git clone https://github.com/BhanuSurisetty/Weather-CLI.git
cd weather-cli
'''

### 2. Install Dependencies
pip install requests colorama

### 3.Set Your OpenWeatherMap API Key
Open weather.py and replace:
API_KEY = "your_actual_api_key_here"

### 4. Run the App
python weather.py

---

## 📂 File Structure

weather-cli/
- ├── weather.py         # Main app
- ├── history.json       # Auto-created to store search history
- └── README.md          # You're reading it!

---

## 📌 Notes

- Make sure you have Python 3 installed.

- You need an API key from OpenWeatherMap.



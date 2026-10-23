import requests


def get_weather(city_name):
    # You can get your free API key by creating an account on https://openweathermap.org/api
    API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    try:
        # Build the request URL
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

        # Send request to OpenWeatherMap API
        response = requests.get(url)
        data = response.json()

        # Check for valid response
        if data["cod"] != 200:
            print(f"Error: City '{city_name}' not found.")
            return

        # Extract weather data
        temperature = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        weather = data["weather"][0]["main"]

        # Display results
        print(f"\nWeather Report for {city_name.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
        print(f"Weather: {weather}")

    except Exception as e:
        print(f"Error retrieving weather data: {e}")


if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)

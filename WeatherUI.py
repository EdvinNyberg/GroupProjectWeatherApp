
from City import City #-----------------Input Validering
from OpenWeatherApi import WeatherAPI #-------Väder API
from Weather_Presenter import Weather_Presenter #----All presentation
from search_history import save_history, read_history #------ Loggning

def main():
    print("Welcome to the Weather Application!")
    while True:
        print("\nMenu:")
        print("1. Get weather for a city")
        print("2. View search history")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city_name = input("Enter city name: ")
            city = City(city_name)
            weather_api = WeatherAPI()
            weather_data = weather_api.get_weather(city)
            presenter = Weather_Presenter()
            presenter.present(weather_data)
            save_history(city_name)
        elif choice == '2':
            history = read_history()
            print("\nSearch History:")
            for entry in history:
                print(entry)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
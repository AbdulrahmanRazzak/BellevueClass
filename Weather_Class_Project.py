# This program will gather and display weather forecast data and display it to the user
# based on a city name or zip code.
# Name: Abdulrahman Abdulrazzak
# Date: 05/01/2022
import requests # Imports the requests module which allow for HTTP requests in python.
# display a welcome message
app_intro = input("Welcome to the Weather Forecast App --- Press enter to continue")

# Define a function for Weather by City:

def wthr_city():
    city_input = input(" Please enter the City name to display Weather Information: ") # Get the City name from the user input
    api_url = 'https://api.openweathermap.org/data/2.5/weather?' # The main api call component
    api_key = '3e264feffd1ad080c3d5bda97dbb7358' # A variable to store the API key
    full_url = api_url + "q=" + city_input + "&appid=" + api_key # Full API call url
    results = requests.get(full_url) # A variable to store the API results
    format_data = results.json() # Converts and Transfers the results to JSON for readability
    print_data(format_data) # pass the converted data to the print_data function.

    again_question = input(' Do you want to find Weather data for another City? enter Yes or No:') # Asks the user wehter to go again or 
    if again_question =='Yes' or again_question =='yes': # An if statement to go back to the main function if the user answers yes
        main() # main function call
    if again_question =='No' or again_question =='no': # An if statement to exit the program if the user enters No
        print(" Thank you for using the Weather Forecast App") # print a thanks message
        exit() # Exit the program

# Define a function for Weather by City:
def wthr_zip():
    zipcode_input = input(" Please enter the Zip code to display Weather Information: ") # Get the Zip code from the user input
    api_url = 'https://api.openweathermap.org/data/2.5/weather?' # The main api call component
    api_key = '3e264feffd1ad080c3d5bda97dbb7358' # A variable to store the API key
    full_url = api_url + "zip=" + zipcode_input + "&units=imperial" + "&appid=" + api_key # Full API call url
    results = requests.get(full_url) # A variable to store the API results
    format_data = results.json() # Converts and Transfers the results to JSON for readability
    print_data(format_data) # pass the converted data to the print_data function.


    again_question = input(' Do you want to find Weather data for another City? enter Yes or No:') # Asks the user wehter to go again or 
    if again_question =='Yes' or again_question =='yes': # An if statement to go back to the main function if the user answers yes
        main() # main function call
    if again_question =='No' or again_question =='no': # An if statement to exit the program if the user enters No
        print(" Thank you for using the Weather Forecast App") # print a thanks message
        exit() # Exit the program


# Define a function to show data based on the user request.
def print_data(format_data): 
    temp = format_data['main']['temp'] # pull the Temperature from the results
    hightemp = format_data['main']['temp_max'] # pull the Highest Temperature from the results
    lowtemp = format_data['main']['temp_min'] # pull the Lowest Temperature from the results
    wind_speed = format_data['wind']['speed'] # pull the Wind Speed from the results
    pressure = format_data['main']['pressure'] # pull the Pressure from the results
    lat = format_data['coord']['lat'] # pull the Latitude from the results
    longt = format_data['coord']['lon'] # pull the longitude from the results
    humidity = format_data['main']['humidity'] # pull the Humidity from the results
    description = format_data['weather'][0]['description'] # pull the Description from the results

    print('Current Temperature : {} degrees fahrenheit'.format(temp)) # Print the Temperature  
    print('High Temperature : {} degrees fahrenheit'.format(hightemp)) # Print the Highest Temperature
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp)) # Print the Lowest Temperature
    print('Wind Speed : {} m/s'.format(wind_speed)) # Print the Wind Speed
    print('Pressure : {} hPa'.format(pressure)) # Print the Pressure
    print('Latitude : {}'.format(lat)) # Print the Latitude
    print('Longitude : {}'.format(longt))# Print the Longitude
    print('Humidity : {} %'.format(humidity)) # Print the Humidity
    print('Description : {}'.format(description)) # Print the Description

# Define the main function.
def main():
    choice = input("enter City to Display Weather Information by City, or enter Zip to Display Weather Information by Zip Code : ") # Get the user request type choice
    if choice == "City" or choice == "city": # An if statement to evaluate if the choice of the user is by city
        try:
            wthr_city() # Call the City Weather funciton
        except Exception: # Error handling string 
            print(" That did not work. Please Try again") # Displays an error to the user and prompts to try again
            wthr_city() # Call the City Weather funciton
    if choice == "Zip" or choice == "zip": # An if statement to evaluate if the choice of the user is by Zip Code
        try:
            wthr_zip() #  Call the Zip Code Weather funciton
        except Exception: # Error handling string
            print(" That did not work. Please Try again") # Display an error to the user and prompts to try again 
            wthr_zip() # Call the Zip Code Weather funciton
    else: # An else Statement to handle options that do not exist
        print("Sorry, the option that you chose is not supported. Please Try Again. ")
        main()


main() # Call the main Function
    

import random

summer_holiday_art = '''
       \    /  \  /
          .-.-./  / -.
        .   \  /-'.-   .
         \  /  /   \
          ||   |    \
    ___=======____===___
  / Fun in the  / \  City  \
 /  the Sun   /   \  Exploration  \
/___________/___\_________\
'''


# Dictionary for continents, countries and average temperatures (temperatures are no acurate and randomly assigned)

continents = { 
    "Africa": [ 
        {"country": "Morocco", "temperature": "Sunny Vacation"}, {"country": "Kenya", "temperature": "Sunny Vacation"}, {"country": "South Africa", "temperature": "Just Right"}, {"country": "Egypt", "temperature": "Really Hot"}, {"country": "Nigeria", "temperature": "Sunny Vacation"}, {"country": "Ghana", "temperature": "Sunny Vacation"}, {"country": "Algeria", "temperature": "Sunny Vacation"}, {"country": "Senegal", "temperature": "Just Right"}, 
    ], 
    "Asia": [ 
        {"country": "Thailand", "temperature": "Really Hot"}, {"country": "Japan", "temperature": "Just Right"}, {"country": "India", "temperature": "Sunny Vacation"}, {"country": "Vietnam", "temperature": "Sunny Vacation"}, {"country": "Indonesia", "temperature": "Really Hot"}, {"country": "China", "temperature": "Sunny Vacation"}, {"country": "South Korea", "temperature": "Just Right"}, {"country": "Sri Lanka", "temperature": "Sunny Vacation"}, 
    ], 
    "Europe": [ 
        {"country": "Spain", "temperature": "Sunny Vacation"}, {"country": "Italy", "temperature": "Just Right"}, {"country": "France", "temperature": "Sunny Vacation"}, {"country": "Germany", "temperature": "Just Right"}, {"country": "Greece", "temperature": "Sunny Vacation"}, {"country": "Netherlands", "temperature": "Sunny Vacation"}, {"country": "Sweden", "temperature": "Just Right"}, {"country": "Norway", "temperature": "Just Right"}, 
], 
    "North America": [ 
        {"country": "USA", "temperature": "Sunny Vacation"}, {"country": "Canada", "temperature": "Just Right"}, {"country": "Mexico", "temperature": "Sunny Vacation"}, {"country": "Costa Rica", "temperature": "Sunny Vacation"}, {"country": "Jamaica", "temperature": "Sunny Vacation"}, {"country": "Bahamas", "temperature": "Sunny Vacation"}, {"country": "Dominican Republic", "temperature": "Sunny Vacation"}, {"country": "Cuba", "temperature": "Sunny Vacation"}, 
    ], 
    "South America": [ 
        {"country": "Brazil", "temperature": "Sunny Vacation"}, {"country": "Argentina", "temperature": "Just Right"}, {"country": "Chile", "temperature": "Sunny Vacation"}, {"country": "Peru", "temperature": "Sunny Vacation"}, {"country": "Colombia", "temperature": "Sunny Vacation"}, {"country": "Ecuador", "temperature": "Sunny Vacation"}, {"country": "Bolivia", "temperature": "Sunny Vacation"}, {"country": "Venezuela", "temperature": "Sunny Vacation"}, 
    ], 
} 

# Dictionary of temperature ranges

temperature_ranges = { 
    "Really Hot":"Over 35°C", 
    "Sunny Vacation":"20-35°C", 
    "Just Right":"10-20°C", 
    "Cool":"Under 10°C (Maybe a winter ski trip is more up your alley!)",
}

# The start of the application
print(summer_holiday_art + "\n")
print("\nWelcome to the Summer Holiday Destination Picker App!\n\nLet's get started!\n")


# Function to get preferred temperature
def prefered_temperature():
    preferred_temperature_selection = input("What is your ideal temperature for your summer holiday?\n(Please choose between 'Really Hot', 'Sunny Vacation', 'Just Right', or 'Cool'):\n").strip().title()
    return preferred_temperature_selection

# Function to get preferred continent
def prefered_continent():
    for continent in continents.keys():
        print(continent)
    
    preferred_continent_selection = input("If you had to pick a continent to visit, where would you go? Please select from the list.\n" ).strip().title()
    return preferred_continent_selection

# Function to suggest destination
def suggested_destination(country_list, temperature):
    matching_countries = [country_info for country_info in country_list if country_info["temperature"] == temperature]
    
    if matching_countries:
        selected_country = random.choice(matching_countries)
        print(f"From all the information you have given me, I would suggest that you consider visiting" + selected_country['country'] + ".")
    else:
        print("Oh no, it seems there are no destinations matching your criteria.")


# Main application loop
while True:
    valid_selection = False
    # User choosing their preference for the type of holiday (sunny or a city getaway)
    while not valid_selection: 
        holiday_type = input("Are you looking to have Fun in the Sun or a City Getaway? (Enter 'S' for Fun in the Sun or 'C' for a City Getaway\n").strip().upper()
        if holiday_type == 'S':
            preferred_temperature_selection = prefered_temperature()
            preferred_continent_selection = prefered_continent()
            if preferred_continent_selection in continents:
                possible_destinations = continents[preferred_continent_selection]
                suggested_destination(possible_destinations, preferred_temperature_selection)
                valid_selection = True
            else:
                print("Oops, it seems you tried to enter a continent that doesn't exist on this planet. Maybe you should try again!")
        elif holiday_type == 'C':
            preferred_continent_selection = prefered_continent()
            if preferred_continent_selection in continents:
                possible_destinations = continents[preferred_continent_selection]
                if possible_destinations:
                    selected_country = possible_destinations[0]["country"]
                    print(f"Consider visiting {selected_country} for a city exploration.")
                    print(f"Might I suggest 3 things you could do while visiting {selected_country}:")
                    print("1. Visit famous landmarks and historical sites.")
                    print("2. Explore local museums and art galleries.")
                    print("3. Take guided tours to learn about the city's history and culture.")
                    valid_selection = True
                else:
                    print(f"Oh no, it seems this app's map got a bit sunburned and couldn't find any cities for {preferred_continent_selection}.")
                    print("How about trying a different continent where the cities are sunnier and easier to spot? 😄")
            else:
                print("Oops, it seems you tried to enter a continent that doesn't exist on this planet. Try again!")
        else:
            print("Whoa, it seems you're exploring uncharted territory! This app specializes in sunny holidays and city getaways.")
            print("Please enter 'S' for a sunny holiday or 'C' for a city getaway.")
            print("If you're in the mood for something chilly, maybe consider a trip to the Alps... in winter! 😉")
    # Ask if the user wants to restart
    restart = input("Would you like to restart and try again? (Enter 'yes' or 'no')\n").strip().lower()
    if restart != 'yes':
        break

# App rating
print("\nThank you for using the Summer Holiday Destination Picker App!")
rating = input("Please rate your experience from 1 (lowest) to 5 (highest) stars:\n").strip()
if rating == '1':
    print("We're sorry to hear that you didn't have a great experience. We'll strive to improve.")
elif rating == '2':
    print("Thank you for your feedback. We'll work on making the app better.")
elif rating == '3':
    print("We're glad you found the app helpful. Your feedback is valuable.")
elif rating == '4':
    print("Wow, a 4-star rating! Thank you for your support. We'll keep improving.")
elif rating == '5':
    print("Fantastic! A 5-star rating! We're thrilled that you enjoyed using the app.")
else:
        print("Invalid rating. Please enter a number from 1 to 5.")





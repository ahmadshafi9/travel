import requests

city_name = input("Enter city name: ")
category = input("Enter category: Filters result set based on property type. Valid options are hotels, attractions, restaurants, and geos ")

API_KEY = "****"

url = f"https://api.content.tripadvisor.com/api/v1/location/search?key={API_KEY}&searchQuery={city_name}&category={category}&language=en"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

location_id = input(f"Enter location id of {category} that ur interested in: ")


url2 = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details?key={API_KEY}&language=en&currency=AED"

headers = {"accept": "application/json"}

response2 = requests.get(url2, headers=headers)

print(response2.text)

userinput_price = input("do u want to know how much it would cost? (please enter yes or no) ").lower()
if userinput_price == "yes":
    print("\n--- Searching for 'price: ' using find() ---")
    price_index = response2.text.find('"price":') # Find the starting position of '"price":'

    if price_index != -1: # if find() returns -1, the substring was not found
        # Find the start of the value after ": "
        value_start_index = price_index + len('"price":')
      
        value_end_index = response2.text.find('"', value_start_index + 1) # Find the next quote after the start
        if value_end_index != -1:
            # Extract the text between the quotes
            price_range = response2.text[value_start_index + 1:value_end_index] # Add 1 to skip the opening quote
            print(f"Found price using find(): {price_range}")
        else:
            print("Found 'price:' but could not extract the value.")

    else:
        print("'price:' not found in the response text using find(). find it urself")
else:
    print("yeah thats broke ppl talk anyway")

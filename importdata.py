import json

# Function to load JSON and convert to text format
def importdata(json_file, text_file, format_function):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert each JSON entry to readable text
    formatted_texts = [format_function(entry) for entry in data]

    # Save to text file
    with open(text_file, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_texts))

    print(f"✅ Converted {json_file} to {text_file} successfully!")

# Formatting functions for each dataset
def format_hotel(hotel):
    return f"Hotel Name: {hotel['hotel_name']}, Location: {hotel['location']}, Price: {hotel['price']}, " \
           f"Amenities: {', '.join(hotel['amenities'])}, Reviews: {hotel['reviews']}."

def format_flight(flight):
    return f"Flight: {flight['airline']} {flight['flight_number']}, Route: {flight['source']} to {flight['destination']}, " \
           f"Price: {flight['price']}, Duration: {flight['duration']}."

def format_destination(destination):
    return f"Destination: {destination['destination']}, Country: {destination['country']}, Best Time to Visit: {destination['best_time_to_visit']}, " \
           f"Attractions: {', '.join(destination['attractions'])}."

# Convert and save text files
importdata("hotels.json", "hotels.txt", format_hotel)
importdata("flights.json", "flights.txt", format_flight)
importdata("destinations.json", "destinations.txt", format_destination)

print("✅ All JSON files converted successfully!")

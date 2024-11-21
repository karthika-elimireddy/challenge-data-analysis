import math
import pandas as pd
import openrouteservice
from openrouteservice import directions
import requests
import time


# Initialize the Google Maps client
client = openrouteservice.Client(key='5b3ce3597851110001cf6248b1b7d9a8cc394481b013668c54a57fcb')
# Example data: list of properties and cities
file_path = '~/Documents/GitProject/Immo2/utils/house_data_clean.csv'
df = pd.read_csv(file_path)
start_time = time.perf_counter()

cities = {
    "Brussels": (50.8467, 4.3513),
    "Antwerp": (51.2194, 4.4025),
    "Ghent": (51.0543, 3.7174),
    "Leuven": (50.8798, 4.7005),
    "Mechelen": (51.0259, 4.4777),
    "Liège": (50.6326, 5.5797),
    "Namur": (50.4674, 4.8718),
    "Mons": (50.4543, 3.9523),
    "Hasselt": (50.9307, 5.3322),
    "Bruges": (51.2093, 3.2247)
}

# Function to calculate travel time to cities





def get_travel_times(property_coords, cities, mode='driving'):
    times = {}
    for city, city_coords in cities.items():
        # Format the coordinates properly for the OSRM API
        origin = f"{property_coords[1]},{property_coords[0]}"  # lon,lat
        destination = f"{city_coords[1]},{city_coords[0]}"  # lon,lat
        
        try:
            # OSRM API request for calculating the travel time (in seconds) between two coordinates
            url = f"http://router.project-osrm.org/route/v1/{mode}/{origin};{destination}?overview=false"
            response = requests.get(url)
            data = response.json()
            
            if 'routes' in data and len(data['routes']) > 0:
                # Extract the duration (time in seconds)
                travel_time = data['routes'][0]['duration']
                times[city] = travel_time
                if travel_time <= 1200 : 
                    break
            else:
                print(f"No route found for {city}.")
                times[city] = None

        except Exception as e:
            print(f"Error fetching data for city {city}: {e}")
            times[city] = None
    
        
    return times

# Compute travel times for all properties
for row, (lat, lon) in enumerate(zip(df['latitude'], df['longitude'])):
    
    
    if not math.isnan(lat):
      
        property_coords = (lat,lon)
        
        
        travel_times = get_travel_times(property_coords, cities)
        
        city_shortest_time = min(travel_times, key = travel_times.get)
        shortest_time = min(travel_times.values())
        closest_city = f"'{city_shortest_time}': {shortest_time}"  # Shortest travel time to any city
        df.at[row, 'closest_city'] = str(closest_city) if closest_city else None
        df.to_csv('house_data_travel.csv', index=False)
        
execution_time = time.perf_counter()-start_time
print('it took: ' + str(execution_time) + ' to run this script')  

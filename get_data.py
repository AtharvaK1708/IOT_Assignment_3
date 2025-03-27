import requests

channel_ID = "2892314"
read_API_key = "8ILCSMS1YXGHOPK0"

url = f"https://api.thingspeak.com/channels/{channel_ID}/feeds/last.json?api_key={read_API_key}"

response = requests.get(url)
data = response.json()

print("Latest Sensor Values:")
print(f"Temperature: {data['field1']} °C")
print(f"Humidity: {data['field2']} %")
print(f"CO2: {data['field3']} ppm")

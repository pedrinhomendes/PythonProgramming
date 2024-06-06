weather = {"Monday": {"temperature": 20, "humidity": 60},  "Tuesday": {"temperature": 22, "humidity": 55},  "Wednesday": {"temperature": 19, "humidity": 65},  "Thursday": {"temperature": 23, "humidity": 50},  "Friday": {"temperature": 21, "humidity": 70}}

# 1

for day, details in weather.items():
    id = day
    temperature = details["temperature"]
    humidity = details["humidity"]
    print(f"Day: {day.capitalize()}, Temperature: {temperature}, Humidity: {humidity}")

# 2

highest_temp_day = max(weather, key=lambda day: weather[day]["temperature"])
highest_temp = weather[highest_temp_day]["temperature"]

print(f"The day with the highest temperature is {highest_temp_day} with a temperature of {highest_temp}")


# 3

highest_temp_day = min(weather, key=lambda day: weather[day]["temperature"])
highest_temp = weather[highest_temp_day]["temperature"]

print(f"The day with the highest temperature is {highest_temp_day} with a temperature of {highest_temp}")

# 4

weather["Wednesday"] = {"temperature": 25}
print(weather)

# 5

weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(weather)
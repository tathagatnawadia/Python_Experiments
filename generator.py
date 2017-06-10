# A simple generator
cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for location in cities:
    print(location)

# Using "next" and "iter"
city_iterator = iter(cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except Exception as e:
        print("Completed !!")
        break

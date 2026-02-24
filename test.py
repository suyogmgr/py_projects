countries = {"Nepal" : "Kathmandu",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Japan" : "Tokyo"}


for key, value in countries.items():
    print(f"{key} : {value}")

countries.update({"singapore" : "singapore"})

print(countries)

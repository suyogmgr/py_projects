def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key:10} : {value}")
        

address(Country="Nepal",
              Address="Kathmandu",
              Area="Kapan",
              Street="Sundarbasti")


              
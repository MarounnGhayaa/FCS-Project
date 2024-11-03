drivers = [(1, "maroun", "beirut"), (2, "georges", "zahle")]
cities = ["beirut", "akkar", "zahle", "jbeil", "saida"]
neighbors = {"akkar": ["jbeil"], "jbeil": ["akkar", "beirut"], "beirut": ["jbeil"], "zahle": ["saida"], "saida": ["zahle"]}
class Driver:
    def __init__ (self, driver_id, driver_name, start_city):
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.start_city = start_city
    def tuple_driver(self):
        new_driver = (self.driver_id, self.driver_name, self.start_city)
        drivers.append(new_driver)
def list_drivers():
    for driver in drivers:
        print(driver)
def sort_cities(list):
    sorted_list = sorted(list, reverse=True)
    print(sorted_list)
def drivers_main_menu():
    driver_id_counter = 3
    while True:
        print("\nDRIVERS' MENU")
        print("1. To view all the drivers")
        print("2. To add a driver")
        print("3. Check similar drivers")
        print("4. To go back to the main menu")
        option = int(input("\nEnter an option: "))
        if option == 1:
           list_drivers()
        elif option == 2:
            name = input("Enter driver's name: ")
            start_city = input("Enter driver's start city: ").lower()
            if start_city not in cities:
                city_question = input(start_city + " is not in the database. Do you want to add it to the list of start cities? y/n: ").lower()
                if city_question == "y":
                    cities.append(start_city)
                else:
                    print("Both driver and city were not added!")
                    continue
            driver_id = driver_id_counter
            new_driver = Driver(driver_id, name, start_city)
            new_driver.tuple_driver()
            driver_id_counter +=1
        elif option == 3:
            city_groups = {}
            for driver in drivers:
                city = driver[2]
                if city not in city_groups:
                    city_groups[city] = [driver]
                else:
                    city_groups[city].append(driver)
            for city in city_groups:
                group = city_groups[city]
                if len(group) > 1:
                    print (city, ":", group)
                else:
                    print(city, ":", group)
        elif option == 4:
            print("Back to main menu!")
            break
        else:
            print("Invalid option.")
def cities_main_menu():
    while True:
        print("\nCITIES' MENU")
        print("1. Show cities")
        print("2. Search city")
        print("3. Print neighboring cities")
        print("4. Drivers delivering to city")
        option = int(input("\nEnter an option: "))
        if option == 1:
           sort_cities(cities)
        elif option == 2:
            character = input("Enter a key: ").lower()
            for city in cities:
                if character in city:
                    print(city)
        elif option == 3:
            city_name = input("Enter a city to check neighbors: ").lower()
            if city_name not in cities:
                print("City not found.")
            else:
                found = False
                for city in neighbors:
                    if city_name == city:
                        found = True
                        print(neighbors[city])
                if not found:
                    print("City has no neighbors.")
        elif option == 4:
            dest_city = input("Enter a city to see who is delivering to it: ").lower()
            if dest_city not in cities:
                print("City not found.")
            else:
                destinations = []
                for driver in drivers:
                    destinations.append(driver[2])
                if dest_city in destinations:
                    for driver in drivers:
                        if driver[2] == dest_city:
                            print(driver, "is in this city")
                else:
                    print("No one is delivering to this city")
                for city in neighbors:
                    if dest_city in neighbors[city]: 
                        for driver in drivers:
                            if driver[2] == city:
                                print(driver, "can reach", dest_city, "from: ", city)
                    
        else:
            print("Invalid option.")
while True:
    print("\nWelcome to We Deliver! PLEASE CHOOSE AN OPTION: \n1. Drivers' menu \n2. Cities' menu \n3. Exit")
    option = int(input("\nEnter an option: "))
    if option == 1:
        drivers_main_menu()
    elif option == 2:
        cities_main_menu()
    elif option == 3:
        ("Thank you!")
        break
    else:
        print("Invalid option.")
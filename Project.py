drivers = [(1, "maroun", "beirut", "jbeil"), (2, "georges", "zahle", "saida")]
cities = ["beirut", "akkar", "zahle", "jbeil", "saida"]
cities_matrix = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
city_indices = {}
index = 0
for city in cities:
    city_indices[city] = index
    index += 1
class Driver:
    def __init__ (self, driver_id, driver_name, start_city, delivery_city):
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.start_city = start_city
        self.delivery_city = delivery_city
    def tuple_driver(self):
        new_driver = (self.driver_id, self.driver_name, self.start_city, self.delivery_city)
        drivers.append(new_driver)
class City:
    def __init__(self, name, next_city):
        self.name = name
        self.next_city = next_city
def sort_cities(list):
    sorted_list = sorted(list, reverse=True)
    print(sorted_list)
def add_city(city_name):
    cities.append(city_name)
    city_indices[city_name] = len(cities) - 1
    for row in cities_matrix:
        row.append(0)
    new_row = [0] * len(cities)
    cities_matrix.append(new_row)
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
           print(drivers)
        elif option == 2:
            name = input("Enter driver's name: ")
            start_city = input("Enter driver's start city: ").lower()
            delivery_city = input("Enter driver's destination city: ").lower()
            if start_city not in cities:
                city_question = input(start_city + " is not in the database. Do you want to add it to the list of start cities? (y/n): ").lower()
                if city_question == "y":
                    add_city(start_city)
                else:
                    print("Both driver and city were not added!")
                    break
            if delivery_city not in cities:
                delivery_question = input(delivery_city + " is not in the database. Do you want to add it to the list of delivery cities? (y/n): ").lower()
                if delivery_question == "y":
                    add_city(delivery_city)
            driver_id = driver_id_counter
            new_driver = Driver(driver_id, name, start_city, delivery_city)
            new_driver.tuple_driver()
            driver_id_counter += 1
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
                    print ("Drivers in ", city, ":", group)
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
            repeat = "y"
            while repeat == "y":
                character = input("Enter a key: ").lower()
                for city in cities:
                    if character in city:
                        print(city)
                repeat = input("Search for another city? (y/n): ").lower()
        elif option == 3:
            city_name = input("Enter city to check neighbors: ").lower()
            if city_name in cities:
                city_index = city_indices[city_name]
                neighbors = []
                for i in range(len(cities_matrix[city_index])):
                    if cities_matrix[city_index][i] == 1:
                        neighbors.append(cities[i])
                if neighbors:
                    print("Neighboring cities:", neighbors)
                else:
                    print("No neighbors")
            else:
                print("City not found.")
        elif option == 4:
            dest_city = input("Enter a city to see who is delivering to it: ")
            for driver in drivers:
                if dest_city == driver[3]:
                    print("\n", driver[1], " is delivering from: ", driver[2], " to: ", dest_city)
                    print("Driver info: ", driver)
        else:
            print("Invalid option.")
while True:
    print("\nWelcome to We Deliver! PLEASE CHOOSE AN OPTION: \n1. Drivers' menu | 2. Cities' menu | 3. Exit")
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
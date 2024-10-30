drivers = [(1, "maroun", "beirut"), (2, "georges", "zahle")]
cities = ["beirut", "tripoli", "zahle"]
class Driver:
    def __init__ (self, driver_id, driver_name, start_city):
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.start_city = start_city
    def tuple_driver(self):
        new_driver = (self.driver_id, self.driver_name, self.start_city)
        drivers.append(new_driver)
class City:
    def __init__(self, name, next_city):
        self.name = name
        self.next_city = next_city
def first_main_menu(n):
        while True:
            print("\nWelcome to We Deliver! Please enter an option:")
            print("1. Drivers' menu")
            print("2. Cities' menu")
            print("3. Exit")
            option = int(input("Enter an option by entering its number: "))
            if option == 1:
                drivers_main_menu(n)
            elif option == 2:
                print("Thank you!2")
            elif option == 3:
                print("Thank you!")
                break
            else:
                print("Invalid option.")
def drivers_main_menu(n):
    driver_id_counter = 3
    while True:
        print("\nDRIVERS' MENU")
        print("1. To view all the drivers")
        print("2. To add a driver")
        print("3. Check similar drivers")
        print("4. To go back to the main menu")
        option = int(input("Enter an option by entering its number: "))
        if option == 1:
           print(drivers)
        elif option == 2:
            name = input("Enter driver's name: ")
            start_city = input("Enter driver's start city: ") 
            driver_id = driver_id_counter
            new_driver = Driver(driver_id, name, start_city)
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
num = int(input("Welcome to WE DELIVER! enter any number to access the system: "))
first_main_menu(num)
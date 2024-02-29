import requests
import getpass

file_path="database.json"
first_time_login="True"

def fetch_data():
    response = requests.get('http://localhost:8000/get_data')  
    
    if response.status_code == 200:
        return response.json()  
    else:
        print("Failed to fetch data")
        return None
    
def search(dish):
    response = requests.get(f'http://127.0.0.1:8000/search?dish={dish}')  
    
    if response.status_code == 200:
        return response.json()  
    else:
        print("Failed to fetch data")
        return None    
    
def login(username:str,password:str):
    users=fetch_data()["users"]
    # print("users",type(users[0]))
    for element in enumerate(users):
        if element[1]["username"] == username and element[1]["password"]==password:
            return True
    return False    

def main():
    global first_time_login
    
    if(first_time_login=="True"):
        print("Welcome to our food tracking application")
    username = input('Enter username:') 
    password = input('Enter password:') 
    
    if(login(str(username),str(password))):
        print("Successfully logged in ")
        dish_or_restaurant = input('Search for restuarants or dishes\n') 
        available_restaurants=search( dish_or_restaurant);
        print("Available restaurants: " )
        for index, element in enumerate(available_restaurants['restaurants']):
            print(f"{index+1}: {element}")
        hotel_or_dish_option = input('Select from above restaurants\n')  
        if(int(hotel_or_dish_option) >= len(available_restaurants['restaurants'])+1):
            print("Invalid option,Please try again")  
        else:
            print("Nice")   
    else:
        print("Invalid credentials,please try again")
        first_time_login="False"
        main() 
           
 

if __name__ == "__main__":
    
    main()

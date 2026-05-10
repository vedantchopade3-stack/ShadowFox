Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]  
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=input("Enter the city name: ")
if city in Australia:
    print("The city is in Australia")
elif city in UAE:           
    print("The city is in UAE")
elif city in India:      
    print("The city is in India")          
else:   
    print("The city is not in the list")
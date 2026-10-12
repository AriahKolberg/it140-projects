rooms = {     
    "Foyer": {"north": "Attic", "west": "Library", "south": "Kitchen"},     
    "Attic": {"south": "Foyer"},     
    "Library": {"east": "Foyer", "south": "Ballroom"},     
    "Ballroom": {"north": "Library", "east": "Kitchen"},     
    "Kitchen": {"north": "Foyer", "west": "Ballroom", "south": "Dining Room"},     
    "Dining Room": {"north": "Kitchen", "east": "Study", "south": "Basement"},     
    "Study": {"west": "Dining Room", "south": "Garden"},     
    "Basement": {"north": "Dining Room", "east": "Garden"},     
    "Garden": {"north": "Study", "west": "Basement"}     
}     

current_room = "Foyer"          

while True:         
    
    print(f"\nYou are in the {current_room}.")                  
    
    command = input("Enter a direction (north, south, east, west) or 'exit' to quit: ").lower().strip()     
    
    if command == "exit":         
        print("Thanks for playing!")         
        break     
    elif command in rooms[current_room]:         
        current_room = rooms[current_room][command]         
       
        print(f"You moved to the {current_room}.")     
    else:         
        print("You cannot move in that direction.")

# Developer Name: Arthur L. Richardson
# Vinyl Reckoning 

import sys
import termios
import fcntl
import time
import os

# Prevent the User from typing during Output 
def print_with_text_animated(text):
    # Disable input
    fd = sys.stdin.fileno()
    old_attr = termios.tcgetattr(fd)
    new_attr = termios.tcgetattr(fd)
    new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new_attr)
    old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)

    try:
        # Print text with animation
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.04)
    finally:
        # Re-enable input
        termios.tcsetattr(fd, termios.TCSAFLUSH, old_attr)
        fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)

# Start Intro with Animated typing text
print_with_text_animated("""
Welcome to Vinyl Reckoning, the ultimate test of your music knowledge and quick thinking!
""")

#User Data Recall
First_Name_Request = input("Enter Your First Name: > ")
def enter_age():
    while True:
        age_input = input("Enter Your Age: > ")
        if age_input.isdigit():
            age = int(age_input)
            if 1 <= age <= 124:
                return age
            else:
                print("Please enter a number from 1 to 124.")
        else:
            print("Please enter a valid number from 1 to 124.")

Age_Request = enter_age()

Fav_Artist = input("Enter Your Favorite Song Name: > ")

print_with_text_animated(f"""
{(First_Name_Request.title())}, you've just received an exclusive invitation to a private Vinyl Record Collector Event at an 
old Tower Records warehouse hosted by your favorite Vinyl Record YouTuber, Biggie Shakur. Eager to attend, you go to the warehouse, 
only to find yourself trapped inside as the doors and windows lock behind you. A mysterious voice echoes through the room, 
revealing that your only means of escape is to prove your worth by collecting 6 precious vinyl records:

* Michael Jackson's "Thriller Vinyl"
* Cleo Sol's "Gold Vinyl"
* Faye Webster's "I Know I'm Funny haha Vinyl"
* T.I.'s "Trap Muzik Vinyl"
* The Weeknd's "Thursday Vinyl"
* Kanye West's "Yeezus Vinyl"

These records are hidden throughout the warehouse. {(First_Name_Request.title())} beware, a formidable music historian awaits in 
the final room, and you must gather all the records before facing them to secure your freedom. If not 
{(First_Name_Request.title())}, you will be locked in the warehouse forever!

{(First_Name_Request.title())} get ready to embark on a thrilling adventure where every trivia question is answered correctly, 
and every vinyl collected brings you one step closer to victory and your ultimate reckoning with the challenges ahead!""")

print_with_text_animated(f"""
{(First_Name_Request.title())}, to move throughout the game the movements you must type are: 

*  North
*  South
*  East
*  West

Once you leave the Store entrance, it is locked forver! Additionally, you will lose if you meet the music historian without 
all six vinyls. If you answer the trivia questions incorrectly too many times, you will lose. To track how many Vinyls you 
have enter the command STATUS when you are prompted to move. If you want to quit, type the command EXIT when you are prompted to move. Good Luck!""")

print()  # Added for spacing
print()  # Added for spacing

visited_rooms = []
collected_vinyls = 0

print()  # Added for spacing
print()  # Added for spacing

def current_status():
    print(f"{First_Name_Request.title()}'s Current Status:")
    print(f"Vinyls Collected: {collected_vinyls}")

print()  # Added for spacing
print()  # Added for spacing

def move(direction):
    global current_room
    global collected_vinyls  # Declare collected_vinyls as a global variable
    
    if direction == "exit":
        print_with_text_animated(f"{First_Name_Request.title()}, hate to see you go! Mahalo for playing!")
        exit()  # Exit the program
    
    # Check if the direction is valid for the current room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        if new_room is not None:
            current_room = new_room

            # Display Item Count Here
            print(f"Vinyls Collected: {collected_vinyls}")
            print()  # Added for spacing
            
            # Enter the room and display description
            print_with_text_animated(rooms[current_room]["description"])
            print()  # Added for spacing
            
            # Check if all vinyls collected before entering Future Room
            if current_room == "Future Room" and collected_vinyls != 6:
                print_with_text_animated("\n You don't have all six vinyls! Back to the entrance. You lose all collected items and must restart.")
                current_room = "Store Entrance"
                visited_rooms = []
                collected_vinyls = 0
                rooms["Hip Hop Room"]["item"] = "Trap Muzik by T.I. Vinyl."  # Reset collected items
                rooms["Alternative/Indie Room"]["item"] = "I Know Im Funny haha by Faye Webster Vinyl."
                rooms["Soul Room"]["item"] = "Gold by Cleo Sol Vinyl."
                rooms["R&B Room"]["item"] = "Thursday by The Weeknd Vinyl."
                rooms["Kanye Room"]["item"] = "Yeezus, Kanye West Vinyl."
                rooms["King of Pop Room"]["item"] = "Thriller by Michael Jackson Vinyl."

                # Check if all vinyls collected before entering Future Room
            if current_room == "Future Room" and collected_vinyls == 6:
                if "trivia_question" in rooms[current_room] and rooms[current_room]["item"] is not None:
                    attempts = 6  # Initial number of attempts
                    print_with_text_animated(rooms[current_room]["trivia_question"])  # Print the trivia question
                    while attempts > 0:
                        answer = ask_trivia(rooms[current_room]["trivia_answer"])
                        if answer:
                            print_with_text_animated(f"\nCorrect! Congrats! You won your freedom! Thanks for Playing {First_Name_Request.title()}!")
                            exit()  # End the game
                        else:
                            attempts -= 1
                            if attempts > 0:
                                print_with_text_animated(f"{First_Name_Request.title()}, that's not quite right. Try again! You have {attempts} attempts left \n")
                            else:
                                print_with_text_animated(f""" You've exhausted all attempts {First_Name_Request.title()}. Back to the entrance you go! 
                                                         Hand over any vinyls you won as well. Better luck next time! \n""")
                                break  # Exit the loop if all attempts are used

            # Check if the room has a trivia question and the vinyl has not been collected
            if "trivia_question" in rooms[current_room] and rooms[current_room]["item"] is not None:
                attempts = 6  # Initial number of attempts
                print_with_text_animated(rooms[current_room]["trivia_question"])  # Print the trivia question
                while attempts > 0:
                    answer = ask_trivia(rooms[current_room]["trivia_answer"])
                    if answer:
                        print_with_text_animated(f"\n Correct! Congrats! You won the ... {rooms[current_room]['item']}")
                        print()
                        collected_vinyls += 1  # Keep track of collected vinyls
                        rooms[current_room]["item"] = None  # Remove the item after it's been won
                        break  # Exit the loop if the answer is correct
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print_with_text_animated(f"{First_Name_Request.title()}, that's not quite right. Try again! You have {attempts} attempts left\n")
                        else:
                            print_with_text_animated(f""" You've exhausted all attempts {First_Name_Request.title()}. Back to the entrance you go! 
                                                         Hand over any vinyls you won as well. Better luck next time! \n""")
                            break  # Exit the loop if all attempts are used
        else:
            print_with_text_animated(f"{(First_Name_Request.title())}, you entered an invalid direction. Try again! \n")

def ask_trivia(answer_list):
    """
    This function asks a trivia question and checks the user's answer.
    """
    user_answer = input("> ").strip().lower()  # Convert the user's input to lowercase and remove leading/trailing spaces
    return user_answer in [ans.lower() for ans in answer_list]  # Check if the user's answer matches any answer in the answer list, ignoring case

# Defining the moves and description for each room with trivia questions added
rooms = {
  "Store Entrance": {
    "description": "You stand at the entrance of the dusty warehouse, sunlight filtering through cracks in the boarded-up windows. A faint musty smell of old vinyl fills the air.",
    "north": "Kanye Room",
    "south": None,
    "east":  None,
    "west":  "Hip Hop Room",
    "item":  None  
  },
  "Hip Hop Room": {
    "description": "Stacks of classic hip-hop albums line the shelves. A boombox blasts an old-school beat. You are in the Hip Hop Room!",
    "north": "Alternative/Indie Room",
    "south": None,
    "east":  None,
    "west":  None,
    "item":  "Trap Muzik by T.I. Vinyl.",
    "trivia_question": "On the song Swagger Like Us, which artist says: No one on the corner has swagger like moi. Church, but I'm too clean for the choir?",
    "trivia_answer": ["Lil Wayne", "Wayne", "Weezy", "Weezy F Baby"]
    },
  "Alternative/Indie Room": {
    "description": "Psychedelic posters adorn the walls. A vintage record player sits on a cluttered desk. You are in the Alternative/Indie Room!",
    "north": "Soul Room",
    "south": "Hip Hop Room",
    "east":  "Kanye Room",
    "west":  "Future Room",
    "item":  "I Know Im Funny haha by Faye Webster Vinyl.",
    "trivia_question": "What music artist sings, You make me wanna cry in a good way?",
    "trivia_answer": ["Faye Webster", "faye webster"] 
  },
  "Soul Room": {
    "description": "Warm light spills from a corner lamp, illuminating a collection of old and new soulful classics. You are in the Soul Room!",
    "north": None,  
    "south": "Alternative/Indie Room",
    "east":  "King of Pop Room",
    "west":  None,
    "item":  "Gold by Cleo Sol Vinyl.",
    "trivia_question": "Fill in the missing lyric. Are we really sure? Can a love that lasted for so long _?",
    "trivia_answer": ["Still endure", "still endure"] 
  },
  "R&B Room": {
    "description": "Silky smooth grooves emanate from hidden speakers. Rows of R&B albums gleam under the soft light. You are in the R&B Room!",
    "north": "King of Pop Room",  
    "south": "Kanye Room",
    "east":  None,
    "west":  None,
    "item":  "Thursday by The Weeknd Vinyl.",
    "trivia_question": "This artist famously sang, I only call you when it's half past five?",
    "trivia_answer": ["The Weeknd", "the weeknd"] 
  },
  "Kanye Room": {
    "description": "Yeezy himself seems to be watching you from every album cover. The air crackles with anticipation. You are in the Kanye Room!",
    "north": "R&B Room",
    "south": None,
    "east":  None,
    "west":  "Alternative/Indie Room",
    "item":  "Yeezus, Kanye West Vinyl.",
    "trivia_question": "Fill in the missing lyric. Mayonnaise-colored Benz I push _?",
    "trivia_answer": ["Miracle Whips", "Miracle Whip"]
  },
  "King of Pop Room": {
    "description": "A diamond incrusted golve hangs from the ceiling and glimmers. A loud He-He fills the room. You are in the King of Pop Room!",
    "north": None,
    "south": "R&B Room",
    "east":  None,
    "west":  "Soul Room",
    "item":  "Thriller by Michael Jackson Vinyl.",
    "trivia_question": "In the Thriller photoshoot for the album cover, Michael Jackson is wearing a white suit with an animal print pocket square. What type of animal is near his feet?",
    "trivia_answer": ["Tiger", "Tiger cub"] 
  },
  "Future Room": {
    "description": "An empty room that can go on for miles. A hanging lamp flickers and shows an outline of a floating being. It is the villain. He is wrapped in old assorted vinyl record covers. You are in the Future Room!", 
    "north": None,
    "south": None,
    "east":  "Alternative/Indie Room",
    "west":  None,
    "item":  "Your freedom!",
    "trivia_question": "What is considered Future's first R&B album?",
    "trivia_answer": ["HNDRXX", "hndrxx"] 
  },
}

current_room = "Store Entrance"

while True:
    command = input(f"{First_Name_Request.title()}, what do you want to do? Type a direction (North, South, East, West), 'status' to see your current status, or 'exit' to quit: ").lower()
    
    if command == "status":
        current_status()
    else:
        move(command)
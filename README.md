# Green Coding Escape Room Challenge v2.0
Welcome to the Green Coding Escape Room Challenge!

Please, find below all the instructions on how to access our portal, play, and win!

Good luck!!!

## Start the Challenge

1. Access the portal via the following link:  
   https://d2qozj430lax8h.cloudfront.net/.  
   You will be prompted with the following window:  
   <img width="590" height="457" alt="login screen" src="https://github.com/user-attachments/assets/8c1d201c-d548-4695-82fd-402d50f60734" />

2. Insert the password provided during this event.  
   If you don't have a password, please contact a member of the team.

3. Once a valid password is inserted, you will be able to create a player:  
   <img width="805" height="400" alt="create player" src="https://github.com/user-attachments/assets/b150ef01-ce8c-496d-a367-92f1cbc0f5d7" />

   > Naming restrictions are applied, so please follow the correct naming convention.

4. You will need to tick the **"I consent to the storage and use of my name related to my game progress"** box to be able to click **Create Player**.  
   *Note: No private information is gathered — only the nickname used and performance.*

5. If a valid username is inserted and the box is ticked, you will see the following screen:  
   <img width="880" height="490" alt="ready screen" src="https://github.com/user-attachments/assets/8c69a35c-f22d-4634-9ccb-f00fdb8a0c85" />

6. Click on **"Create Player"**

7. You're now in the Hallway of the challenge.

<img width="1741" height="912" alt="image" src="https://github.com/user-attachments/assets/fe5a8208-72b7-40b0-ab26-c34b8ddc020a" />


## Navigate the Hallway
Now that you're in the Hallway, you can navigate through the challenges!
See below what each button does.

<img width="1696" height="718" alt="Instruction1" src="https://github.com/user-attachments/assets/8ba81c4b-06d5-4dbf-a599-669815f055ac" />

- **A.** This is the **Landing Page**. It contains a summary of what you can find in the portal.

- **B.** The **Room** button expands to show the list of available rooms. Click on one of them to start the challenge!

- **C.** The **History** button provides an overview of your attempts.  
  - If selected while inside a room, it will show all your attempts in that specific room, with your best attempt highlighted at the top.

- **D.** The **Leaderboard** button offers two views:
  - **Global:** Displays all users who have completed the challenge and their positions on the leaderboard.
  - **Rooms:** Shows all user attempts for each room. You do not need to complete the challenge to view your own attempt here.
    *Note: The Leaderboard has a cache time of 10 minutes, so it will refresh automatically every 10 minutes. If you don't see your attempt right away, please, give time to refresh.*

- **E.** The **Help** button will redirect you to the **Landing Page** (see A).

- **F.** This is the **Reset** button. Use it **ONLY** if you want to completely reset your progress and create a new user.


## Navigate the Rooms
You're in one of the available rooms. Below, you'll find the explanation of the room interface.

<img width="1888" height="898" alt="Instruction2" src="https://github.com/user-attachments/assets/5a00231e-c2d7-44a6-b013-34f8e9d80eec" />

- **A.** In this text box, you can insert your code to feed the robot agent. (look at the example for the format)
- **B.** Click "Submit" to run your code.
- **C.** This is the player name.
- **D.** This is your health. Make sure to keep a close eye to it when you submit your code.
- **E.** These are your keys number. You will get **1** key everytime that you complete a room. Get all the keys and your performance will be displayed in the **Global Leaderboard**.
- **F.** Here you can see which room you are and a description of the challenge.
- **G.** Click "Available Methods" to see which methods are available for the room. The methods are what you need to construct an algorithm and produce an efficient solution!
- **H.** Click in any other option to have access to: **Rooms**, **History**, **Leaderboard**, **Information page**, **Reset** your run.

## Failing a Room
If you run a code that doesn't solve the room, you will be prompted with a new window saying **"You have not solved the room!"**.

<img width="904" height="678" alt="image" src="https://github.com/user-attachments/assets/bbc6301f-f566-4795-87b6-e088d745bd78" />

This is absolutely fine! Just close it and keep trying!

Remember that if you get stuck, just proceed to the next room.

## Solving a Room
If your code solves a room, you will be prompted with the following screen:

<img width="498" height="485" alt="image" src="https://github.com/user-attachments/assets/dd0ea281-c679-496c-ae77-2a889da34c51" />

Your details on the top of the screen will change, reflecting how much energy is left, and adding a key to your inventory like in the screenshot below:

<img width="1270" height="45" alt="image" src="https://github.com/user-attachments/assets/c4142a0a-fa6e-43ff-bb57-a5dbb0d74b0d" />

If you are not satisfied with the energy output produced from your solution, just use another algorithm.

The portall will correct your health bar with the new energy used if the algorithm is more efficient.


## Completing the Escape Room Challenge
To win the competition, you will have to gather all the keys from all the rooms.
You gather keys each time you solve a room.

If you complete all the rooms your name will enter in the **Global Leaderboard**. To see it navigate to **Leaderboard > Global**.

<img width="1735" height="388" alt="image" src="https://github.com/user-attachments/assets/e5aa1c5f-d380-4315-b2f5-7edc97fc2fec" />

You can keep try to improve the algorithm of any room, this will improve your position in the Leaderboard!

If you finish all the rooms... congratulation for escaping!


## Winning the Competition
Completing the challenge and escape will not be enough to win the competition.

The winning user/team needs to be first in the leaderboard for the event so they need to have consumed the less amount of energy.

In case of tie in terms of energy, the time will decide the winner. The user/team who took less  time to complete the challenge will be the winner.

Good luck to everyone, and have fun!!!


## Templates
Inside this repository you will be able to see a template for each of the room in a format that is either ***.py*** or ***.txt***.
Feel free to copy this repository in your device, and use a chosen code editor to workout the solution.
Use the template as base to resolve the rooms, or create your own code from scratch!

Some templates contains multiple versions, for example, a version may contain import and one without import. One of the two template will help produce a more efficient code.

**Each comment in the template** is there to tell you that something must be written instead of the comment.

### Code example
A code to solve a room will look like this:
```
def solve_room(do):
	from mylibrary import library

	start_info = do.look()
	if do.at_exit():
		return
	else:
		do.move()

solve_room(do)
```
From the code above we can note few crucial things:
- **The parameter of the function MUST be "(do)".**
- **If you decide to import a library, the library must be wrapped inside the function and** **NOT** **outside.**
- **Every available method needs a "do" in order to work (e.g. do.look()).**
- **Remember to call the function at the of the algorithm (e.g. solve_room(do)).**  

## Hints
These hints will help you solve the rooms. Some of them can be applied to more than one room.
Is up to your team understand which hint can be applied where.

### Hint 1
When working with multiple functions, lists, and lots of data, we want to always re-use things we have already worked out and filter down unneccesary data before passing it into another function. 
We don't want to be looping over items that we already know we don't need to check. Additionally, we might want to think about how we store our data. 
Lists hold the data, and hold the information of their order, we might not need to keep the order information of the list, therefore, we might want to consider a set or dictionary. 
A dictionary is particularly useful if we have pair of information, for example, an item with some information about that item. 
A dictionary can be created with curly braces as follows:
```
dictionary = {"item name": "item information", ...}
```
The item name is known as a key, and item information is known as a value, the value can be of any type - a string, list, int etc.

### Hint 2
There two different types of loops we can use, for loops and while loops. Additionally, we can nest loops. 
Loops are a major contributor to inefficiency, we don't want to loop any more than needed, so it is important to get everything we can out of each loop, and not loop more than we need to. 
For loops are good when we know exactly how many times we need to loop for, and only need to do each iteration just once. 
While loops are good when we are unsure of the number of loops and when we may want to repeat the same operation on the same items until a condition is met.

### Hint 3
Lists are a type of data structure that don't use a lot of energy to read, but require a lot of energy to change/add to. We want to minimize the number of times we add new items to a list. 
This can be achieved by using list comprehensions, which are a way of generating a whole list from a number of items in one go rather than adding each item one by one. 
This is done by inserting a loop inside the list. 
Take a look at the example below where we have a set of items that have an attribute "is_wanted":
```
list_to_be_filled = []
for item in item_set:
	if item.is_watanted():
		list_to_be_filled.append(item)
```	
This is very inefficient and can be greatly improved upon with a list comprehension:
```
list_to_be_filled = [item for item in item_set if item.is_wanted()]
```
### Hint 4
Investigate parallel processing techniques to explore multiple paths simultaneously, potentially reducing the time required.
Chosing a random value everytime may not be the best option.

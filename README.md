# Green Coding Escape Room Challenge v2.0
Welcome to the Green Coding Escape Room Challenge!

Please, find below all the instructions on how to access our portal, play, and win!

Good luck!!!

## Start the Challenge
1. Access the portal via the following link: https://d2qozj430lax8h.cloudfront.net/

You will be prompted with the following window:
<img width="590" height="457" alt="image" src="https://github.com/user-attachments/assets/8c1d201c-d548-4695-82fd-402d50f60734" />


2. Insert the password provided during this event - if you don't have a password, please, contact a member of the team.
3. Once a valid password is inserted, you will be able to create a player:

<img width="805" height="400" alt="image" src="https://github.com/user-attachments/assets/b150ef01-ce8c-496d-a367-92f1cbc0f5d7" />
Naming restrictions are applied, so please, follow name correct naming convention.
4. You will need to tick the "<i>I consent to the storage and use of my name related to my game progress</i>" box to be able to click <b>Create Player</b>.
<i>NOTE: No private information is gathered. only the nickname used and performance.</i>
5. If a valid username is inserted and the box ticked, you will see the following screen:
<img width="880" height="490" alt="image" src="https://github.com/user-attachments/assets/8c69a35c-f22d-4634-9ccb-f00fdb8a0c85" />
6. Click on <b>"Create Player"</b>
7. You're now in the Hallway of the challenge.

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/72241130-054a-46cf-9cac-17b1be00625c)


## Navigate the Hallway
Now that you're in the Hallway, you can navigate through the challenges!
See below what each button does.

![Untitled (8)](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/f187657b-8503-4b10-9185-3ba5ee7e9282)


- A. This is where you can enter one of the rooms and start to solve them! Click in one of the 4 rooms to start the challenge!
- B. Here you will find the lore of the challenge. Click to understand what is going on!
- C. This button does nothing since you're already in the Hallway.
- D. Here you can see your name displayed.
- E. This is the energy left for your robot agent. Keep an eye on it!
- F. Here you can find the total time of work of your robot agent.
- G. This is the total number of keys that you have retrieved. Solve a room to retrieve a key.
- H. Here you have the escape button! If you have all the 4 keys, it's time to escape! Click the button!


## Navigate the Rooms
You're in one of the 4 rooms available. Below, you'll find the explanation of the room interface.

![Untitled (9)](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/881deb0a-b923-4b9a-9dc2-9bc2eee50945)


- A. In this text box, you can insert your code to feed the robot agent. (look at the example for the format)
- B. This is the room name.
- C. Here you can find the explanation of the room.
- D. Click "Go To Hallway" to return to the Hallway interface and leave the room.
- E. Click "Run Code" to make your robot agent run code.
- F. Click "Available Methods" to see which methods are available for the room. The methods are what your robot agent needs to use to work out an efficient solution!
Clicking on this option opens a new window with the list of methods (see the example below)

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/7ef58a11-05e9-455d-aefe-1561236c96fb)


## Failing a Room
If you run a code that doesn't solve the room, you will be prompted with a new window saying "You have not cleared the room".

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/61b254a0-95d9-4796-a5a1-a42dc8bdf33c)

This is absolutely fine! Just click OK and keep trying!

Remember that if you get stuck, just proceed to the next room.


## Solving a Room
If your code solves a room, you will be prompted with the following screen:

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/3ab4316c-ff20-4bb2-9a93-f04753d4f4d4)

Your details on the left screen will change, reflecting how much energy is left, and adding a key to your inventory like in the screenshot below:

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/1dba7f7e-0a76-49bc-ac10-5209b2b2b441)

If you are not satisfied with the energy output produced from your solution, just use another algorithm.

The agent will correct your health bar with the new energy used if the algorithm is more efficient.


## Completing the Escape Room Challenge
To win the competition, you will have to gather all the keys from all the rooms.
You gather keys each time you solve a room.

In the screenshot below, you can see an example of somebody who completed all the rooms.

![image](https://github.com/GiuseppePerugia/Green_Coding_Escape_Room/assets/89920701/61366d9a-6c4a-4684-9fc7-4e8efe2aab17)

However the energy output is negative, (see "Energy: -50") indicating that the person did completed the room but not in a very efficient way.
The person can decide to re-start over and produce new efficient algorithm for one, or more of the rooms, and try to produce a better output.

Once the person will be satisfied with the result can click "Escape".

Your robot agent will produce an output file with the details of your teams and your algorithms. You will be also prompted with a message. Follow the instructions on the message and... congratulation for escaping!


## Winning the Competition
Completing the challenge and escape will not be enough to win the competition.

The winning team needs to satisfied different parameters listed below:

- They need to share their output file for review.

- They need to have produced algorithm that would work on different solution, e.g. would the algorithm find the exit of the Maze if I change the exit position?

- They need to have consumed the less amount of energy.

- In case of tie in terms of energy, the time will decide the winner. The team who took less  time to complete the challenge will be the winner.

Good luck to everyone, and have fun!!!

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

### Templates
Inside the Green_Coding_Escape_Room folder you will find 4 templates. One for each room.
The templates contain solutions to complete the rooms.
The solutions are incomplete or ineficient, and is up to you to complete or improve them.

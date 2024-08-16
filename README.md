# **Battle Bytes: Tic-Tac-Toe**

## **Introduction**

'Echoes of the Abyss' is a terminal-based, narrative driven horror game. The game blends classic survival horror elements with the interactive storytelling of a choose-your-own-adventure, creating a suspenseful experience where every decision affects your fate.

You play the part of an URBEX explorer and content creator who visits an abandoned research facility. The facility, once bustling with scientists and security personnel, is now eerily abandoned, its halls filled with the remnants of a hasty evacuation. The experiment was designed to study a mysterious and dangerous entity, but it broke free from containment, wreaking havoc on the facility. The few survivors sealed the creature in a containment room, but its intelligence and strength make it a constant threat. 

As the player, you must uncover the facility's dark secrets, avoid the lurking dangers, and find a way to escape before it's too late.


> **Note:** Please cmd-click (Mac) or ctrl-click (Windows) on any links to open them in a new tab.

Link to live website: 

[Echoes of the Abyss Live Site](https://echoes-of-the-abyss-8920634f42db.herokuapp.com/)


## UX

### User Stories

As a user...
* I want to play a game with multiple paths and endings.
* I want a game that I can play in a relatively short amount of time.
* I want to play a game that is suspenseful and interesting.
* I want to play a game that has consequences and that requires critical thinking skills.
* I want to play a game that is intuitive, giving help when I need, or letting me exit.

As a developer...
* I want to create a game with multiple possible storylines.
* I want to create an interactive game that allows players to learn the game lore and build an inventory.
* I want there to be consequences if a player doesn't collect the correct items.
* I want to create a game that's replayable without being boring.
* I want to create a game that is quick enough to progress through if the player dies and wants to try again.
* I want the player to be able to access different commands to allow for a comfortable gamining experience.

### Opportunities

| Opportunities | Importance | Viability/Feasibility |
|-----|:-----:|:-----:|
| Create multiple endings | 4 | 5 |
| Each room adds to game lore | 2 | 3 |
| Branching storylines | 4 | 4 |
| Character development | 2 | 3 |
| Inventory system | 5 | 5 |
| Puzzles | 2 | 2 |
| Time-sensitive decisions | 2 | 2 |
| Hint keyword | 1 | 1 |

The opportunites available in this project were endless, and narrowing them down was a challenge. Due to time constraints, I decided to build a branching story that is fairly linear, as only one room triggers the ending sequences.
More details about features I' dlove to add can be found in 'Future Developments', below the 'Development' section.

## Development
-----------------------------------------------
### File Organisation
Within this project are four Python files. 

#### 1. run.py
This file holds the main game functions, or the room functions. These functions act at starting points from which a player can progress through the story and make certain chices.

#### 2. helper_functions.py
This file holds functions that add to the player's experience. It is linked to the other python files and facilitates a more enjoyable experience for the user. 

#### 3. choices_functions.py
This file holds the functions that will be called if the player types in an object key word. Anythng that is interactable has its function here, and allows the player to learn more about the lore, interact with an item, or add an item to their inventory.

#### 4. ending_sequences.py
This file is only called in when the player reaches the Observation Room, Room 9. There are 7 possible endings in this file.


### Game Visuals & Environment

-----------------------------------------------
## Future Developments

As I mentioned before, there were an endless amount of opportunites to build and incorporate into this game. Sadly, I didn't have enough time to add all the features I would like, so below is a (long) list of additional changes and features I would like to make:

* I would like to create more interable objects to give the player the chance to learn more about the scientists, facility and the entity.

* I would like to create more endings, as only one rom at the moment triggers the ending sequences. I would like to create some novelty endings like 'falling through a hole', or 'electrocution'.

* I would like to create an achievements system, which can be printed at the end of the game when the player lives/dies. For example, letting them start from a certain point in the game to achieve a different ending.

* I want to create more inventory items, all with specific uses throughout the game. Some items currently don't have a function tied to the ending.

* I want to create a restricted inventory, forcing the plater to drop items if it's full, in turn affecting their survival.

* I want to include puzzles to increase interactivity and enocurage the player to interact with as many obejcts as possible.

* I want to create a summary of the player's pathing, allowing them to see what rooms the visited and in what order. 

* I want the room functions to update to remove items already collected and inform the player that they've already been there. 

* I would like the energy drink to play a bigger part after being consumed. For example, an ending where the player gets sick, or is too caffeinated to pay attention and dies somehow. 

* I would also like to add multiple levels, but this would require some restructuring as it would get very text-heavy if kept in the current format.

-----------------------------------------------
## Game Tree Structure


## How to Play

-----------------------------------------------
### Navigating through the game.

#### Input Options

##### User Commands

##### Choices

##### Inventory


-----------------------------------------------

## Testing
### Each room (run.py)


### Helper Functions


### Choices Functions


### Ending Sequences


-----------------------------------------------
## Deployment
Before deploying, I checked two things:
1. Is my requirements.txt up to date?
2. Have I pushed all pending changes to my GitHub repository?

Below are the steps I followed for deployment once I did the above:

1. Sign in to Heroku.
2. Navigate to your dashbord.
3. In the top right corner, click 'New'.
4. Click 'Create new app'.
5. Give your app a name and choose a region. Click 'save'.
6. Move to the settings tab.
7. Scroll down to 'buildpacks'.
8. Add Python, then JSON (in that order). Save changes.
9. Move to the deploy tab. 
10. Select GitHub and search for the repository name.
11. Choose between automatic or manual deploys. (I chose manual.)
12. Click deploy branch.
13. Wait for success message. 
(14. Follow link to live site.)


## Credits
### Content

* Storyline created by [ChatGPT](https://openai.com/chatgpt/).

* Background image from Adobe Stock. [Link to image used.](https://stock.adobe.com/ie/search/free?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Aimage%5D=1&filters%5Borientation%5D=horizontal&filters%5Bcontent_type%3A3d%5D=0&filters%5Bcontent_type%3Atemplate%5D=0&filters%5Bcontent_type%3Avideo%5D=0&filters%5Bfree_collection%5D=1&filters%5Border%5D=relevance&k=glitch&order=relevance&safe_search=1&limit=100&search_page=1&search_type=asset-type-change&acp=&aco=glitch&get_facets=1&asset_id=248081843)

* [text2art](https://pypi.org/project/art/) / art 6.1 from pypi.

* [utils](https://pypi.org/project/utils/) 1.0.2 from pypi.

* Favicon created with [Favicon](https://favicon.io/).

* [autopep8](https://pypi.org/project/autopep8/) for code strucutring.

### Testing Resources
The following were used for testing (during and after development):

* [Code Institute Python Linter](https://pep8ci.herokuapp.com/)

* GitPod

### Additional Resources
Below is a list of additional resources I used to help build my game.

* https://libguides.ntu.edu.sg/python/input#:~:text=The%20input%20function,-The%20input%20function&text=In%20Python%2C%20we%20request%20user%20input%20using%20the%20input()%20function.&text=This%20set%20of%20code%20is,math%20operators%20like%20addition%20%2F%20subtraction

* https://www.geeksforgeeks.org/enumerate-in-python/

* 
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1dK8HHJY)
```
            ____  __    ___    ____  ___________    ____  ______   ________  ________
           / __ )/ /   /   |  / __ \/ ____/ ___/   / __ \/ ____/  /_  __/ / / / ____/
          / __  / /   / /| | / / / / __/  \__ \   / / / / /_       / / / /_/ / __/   
         / /_/ / /___/ ___ |/ /_/ / /___ ___/ /  / /_/ / __/      / / / __  / /___   
        /_____/_____/_/__|_/_____/_____//____/___\____/_/ __  ___/_/_/_/ /_/_____/   
                / __ \/  _/ ___//  _/ | / / ____/  / ___// / / / | / /               
               / /_/ // / \__ \ / //  |/ / / __    \__ \/ / / /  |/ /                
              / _, _// / ___/ // // /|  / /_/ /   ___/ / /_/ / /|  /                 
             /_/ |_/___//____/___/_/ |_/\____/   /____/\____/_/ |_/                  
                                                                             
```

**COMP 1510 Term Project**

## Developer Information

**Name:** Jameel Mohammed  
**Student Number:** A01430376  
**GitHub Username:** JAMEEEL01

## Project Description

Blades of the Rising Sun is a text-based Single User Dungeon (SUD) adventure game set
in feudal Japan. Players choose between the path of the Samurai or Ronin, navigate a
10x10 grid-based world, face various challenges, and ultimately confront the final boss
at the Emperor's palace. The game features a rich narrative, character progression
through three levels, and multiple endings based on player choices.

<img width="1555" height="942" alt="image" src="https://github.com/user-attachments/assets/8e6abb48-b120-4b16-9f61-c88735b712c6" />
<img width="1555" height="823" alt="image" src="https://github.com/user-attachments/assets/b79e63e1-7a40-4bcb-8562-a2d118f49da7" />

## Game Objective

The primary objective of Blades of the Rising Sun is to navigate the 10 x 10 game
board and reach the Emperor's palace at coordinates (9, 9). However, the ending you play
depends on your chosen path and the decisions you make:

- **Ronin Path**: Reach the palace and defeat the Emperor to end his reign. You must
  reach Level 3 before you can enter the palace and face the final boss.
- **Samurai Path**: Reach the palace to protect the Emperor from the rising ronins.
  You must reach Level 3 before you can enter the palace and face your former friend
  Ryūichi, who leads the rebellion.

**Key Objectives:**
1. Navigate the 10 x 10 grid-based world, moving in cardinal directions
2. Encounter and overcome various challenges (combat, riddles, moral dilemmas, etc.)
3. Gain experience points through successful challenge completion
4. Level up from Level 1 to Level 3 (requires 5 XP for Level 2, 10 XP for Level 3)
5. Reach the palace at coordinates (9, 9) while at Level 3
6. Survive the final boss encounter to complete the game

**Game Over Conditions:**
- Your HP reaches 0 (You die)
- You successfully defeat the final boss (Victory!)

## Required Elements

| Required Element | File and Line Number |
|-----------------|---------------------|
| (a) Use of immutable data structures like tuples | `board.py` line 49, 62, 88 |
| (b) Use of mutable data structures | `board.py` 17, 45, `character.py` 28 |
| (c) Thoughtful use of exceptions | `movement.py` 30-39, `challenges.py` 139-140 |
| (d) Minimized scope and lifetime of variables | All modules |
| (e) Decomposition into small, atomic functions | All modules (`challenges.py` 24+ functions) |
| (f) Simple flat code | All modules |
| (g) Demonstration of comprehensions | `challenges.py` lines 132-135 |
| (h) Selection using if-statements | Throughout all files |
| (i) Repetition using for-loop/while loop | `board.py` lines 46-49, `game.py` line 71, `movement.py` line 23 |
| (j) Use of the membership operator | `movement.py` lines 36, 73, `game.py` line 63, `challenges.py` |
| (k) Appropriate use of the range function | `board.py` lines 46-47, 102-104, `movement.py` line 73 |
| (l) Thoughtful use of functions from itertools | `challenges.py` lines 5, 52 |
| (m) The random module | `board.py` line 5, `challenges.py` line 6 |
| (n) Function annotations | `character.py` line 8 |
| (o) Doctests and/or unit tests for every single function | `unit_tests/` directory |
| (p) ALL output formatted using f-strings/str.format/%-formatting | Throughout all files |

## Project Structure

```
TermProject/
├── Documents/
│   ├── aardwolf_progress.pdf
│   └── game.pdf
├── unit_tests/
│   ├── __init__.py
│   ├── board_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_check_if_goal_attained.py
│   │   ├── test_describe_current_location.py
│   │   └── test_make_board.py
│   ├── challenges_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_ambush_challenge.py
│   │   ├── test_assassin_challenge.py
│   │   ├── test_blessing_challenge.py
│   │   ├── test_bridge_challenge.py
│   │   ├── test_burning_village_challenge.py
│   │   ├── test_duel_of_honor_challenge.py
│   │   ├── test_execution_challenge.py
│   │   ├── test_feast_challenge.py
│   │   ├── test_final_boss_story.py
│   │   ├── test_gamble_challenge.py
│   │   ├── test_healer_challenge.py
│   │   ├── test_hostage_challenge.py
│   │   ├── test_merchant_challenge.py
│   │   ├── test_moral_challenge.py
│   │   ├── test_pilgrim_challenge.py
│   │   ├── test_riddle_challenge.py
│   │   ├── test_ryuichi_present.py
│   │   ├── test_sacrifice_challenge.py
│   │   ├── test_shrine_challenge.py
│   │   ├── test_spirit_challenge.py
│   │   ├── test_thief_challenge.py
│   │   ├── test_training_challenge.py
│   │   ├── test_traveler_challenge.py
│   │   └── test_wounded_soldier_challenge.py
│   ├── character_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_character_has_leveled.py
│   │   ├── test_execute_level_up.py
│   │   ├── test_is_alive.py
│   │   └── test_make_character.py
│   └── movement_unit_tests/
│       ├── __init__.py
│       ├── test_get_user_choice.py
│       ├── test_move_character.py
│       └── test_validate_move.py
├── board.py
├── challenges.py
├── character.py
├── game.py
├── movement.py
├── user_interface.py
├── requirements.txt
└── README.md
```

## How to Run

1. Ensure Python 3.x is installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python game.py
   ```

## Game Features

- **Two Paths**: Choose between Samurai (serve the Emperor) or Ronin (rebel against
  the throne)
- **Dynamic Challenges**: 24 different challenge types including combat, riddles,
  moral dilemmas, and more
- **Character Progression**: Level up from 1 to 3, improving health and attack power
- **Multiple Endings**: Story outcomes vary based on player choices, honor, and bond
  with companion
- **Rich Narrative**: Immersive text-based storytelling with ASCII art and
  slow-typing effects

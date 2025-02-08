"""
Week 4 Coding Assignment: The Inventory and the Dungeon of Choices

This code enhances the text-based adventure game by implementing an inventory system
and a dungeon exploration feature using lists and tuples.
"""

import random

def display_player_status(player_health):
    """Prints the player's current health to the console."""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Randomly chooses a path for the player with different outcomes."""
    player_path = random.choice(["left", "right"])
    if player_path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health += 10
        player_health = min(player_health, 100)
    elif player_path == "right":
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """Simulates the player's attack on the monster."""
    print("You strike the monster for 15 damage!")
    updated_monster_health = monster_health - 15
    return updated_monster_health

def monster_attack(player_health):
    """Simulates the monster's attack on the player."""
    critical_num = random.random()
    if critical_num < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        updated_player_health = player_health - 20
    else:
        print("The monster hits you for 10 damage!")
        updated_player_health = player_health - 10
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Manages combat until player or monster is defeated."""
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            break
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game Over!")
            has_treasure = False
            break
        display_player_status(player_health)
    return has_treasure

def check_for_treasure(has_treasure):
    """Checks if the player obtained treasure from the monster."""
    if has_treasure:
        print("The monster had the hidden treasure!")
    else:
        print("The monster did not have the treasure.")

def acquire_item(inventory, item):
    """Adds an item to the player's inventory."""
    inventory.append(item) # Using append() list method
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """Prints the player's current inventory."""
    if not inventory: # Checking if inventory is empty
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for index, item in enumerate(inventory): # Using enumerate for numbered list
            print(f"{index + 1}. {item}")

def handle_puzzle_challenge(player_health, challenge_outcome):
    """Handles the puzzle challenge logic."""
    print("You encounter a puzzle!")
    choice = input("Do you want to 'solve' or 'skip' the puzzle? ").lower()
    if choice == 'solve':
        if random.choice([True, False]):
            success_msg, _, health_change = challenge_outcome
            print(success_msg)
            player_health += health_change
        else:
            _, failure_msg, health_change = challenge_outcome
            print(failure_msg)
            player_health += health_change
            if player_health < 0:
                player_health = 0
                print("You are barely alive!")
    elif choice == 'skip':
        print("You decided to skip the puzzle.")
    else:
        print("Invalid choice, skipping the puzzle.")
    return player_health

def handle_trap_challenge(player_health, challenge_outcome):
    """Handles the trap challenge logic."""
    print("You see a potential trap!")
    choice = input("Do you want to 'disarm' or 'bypass' the trap? ").lower()
    if choice == 'disarm':
        if random.choice([True, False]):
            success_msg, _, health_change = challenge_outcome
            print(success_msg)
            player_health += health_change
        else:
            _, failure_msg, health_change = challenge_outcome
            print(failure_msg)
            player_health += health_change
            if player_health < 0:
                player_health = 0
                print("You are barely alive!")
    elif choice == 'bypass':
        print("You carefully bypass the trap.")
    else:
        print("Invalid choice, bypassing the trap.")
    return player_health


def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Allows dungeon exploration with challenges and items."""
    print("\nYou cautiously enter the Dungeon of Choices...")
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room

        print(f"\n{room_description}")

        if item:
            print(f"You found a {item} in the room.")
            inventory = acquire_item(inventory, item)

        if challenge_type == "puzzle":
            player_health = handle_puzzle_challenge(
                player_health, challenge_outcome)
        elif challenge_type == "trap":
            player_health = handle_trap_challenge(
                player_health, challenge_outcome)
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. "
                  "You move on.") # Line split for length

        display_inventory(inventory)

        # Demonstrating tuple immutability
        # try:
        #     room[1] = "modified item"
        # except TypeError as e:
        #     print(f"\nError: Cannot modify room details - {e}. "
        #           f"Tuples are immutable!") # Line split for length

    print("\nYou exit the Dungeon of Choices.")
    display_player_status(player_health)
    return player_health, inventory

def main():
    """Executes the main adventure game flow."""
    player_health = 100
    monster_health = 70
    has_treasure = random.choice([True, False])
    inventory = []

    # Dungeon rooms defined as a list of tuples
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle",
         ("You solved the ancient riddle!",
          "The riddle's complexity overwhelms you.", -10)), # Line split for readability
        ("A narrow passage with a creaky floor", None, "trap",
         ("You skillfully sidestep the pressure plates!",
          "You step on a hidden pressure plate and trigger darts!", -15)), # Line split
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A dark storage room", "map", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle",
         ("You cracked the code on the chest!",
          "The chest lock resists all your attempts.", -8)) # Line split for readability
    ]

    print("Welcome to the Adventure Game!")
    display_player_status(player_health)

    player_health = handle_path_choice(player_health)
    display_player_status(player_health)

    treasure_obtained_in_combat = combat_encounter(
        player_health, monster_health, has_treasure) # Line break for length

    if player_health > 0:
        check_for_treasure(treasure_obtained_in_combat)
        player_health, inventory = enter_dungeon(
            player_health, inventory, dungeon_rooms) # Line break for length
        print("\nFinal Health Status after Dungeon:")
        display_player_status(player_health)
        print("\nFinal Inventory:")
        display_inventory(inventory)
    else:
        print("Your adventure ends here.")


if __name__ == "__main__":
    main()

"""
File: mh_simulator.py

Description: see write-up project/program description

Student Name: Aziz Mutabanna

Student UT EID: aim2464

Course Name: CS 313E

Unique Number: 54595

Date Created: 11/10/25

Date Last Modified: 12/2/25
"""

import random

# add if necessary:
# import sys
# import numpy as np
# import matplotlib.pyplot as plt

class Door:
    """
    Creates Door objects with numerical labels that hide a prize.
    """
    def __init__(self, num, obj):
        self.num = num
        self.behind = obj

    def print_door(self):
        """
        Prints door's label and hidden prize.
        """
        print(f"Door {self.num}: {self.behind}")

    def open_door(self):
        """
        Returns door's hidden prize.
        """
        return self.behind


class Doors:
    """
    Creates lists of three doors each.
    Allows for easy access to each of the three doors during each round.
    """
    def __init__(self):
        self.door1 = Door(1, None)
        self.door2 = Door(2, None)
        self.door3 = Door(3, None)
        # requirement 1: data structure - list
        self.door_list = [self.door1, self.door2, self.door3]

    def set_up_doors(self):
        """
        Sets up list of three doors for each round of the game.
        """
        self.door1.behind = random.choice(["goat", "car"])

        if self.door1.open_door() == "car":
            self.door2.behind = "goat"
            self.door3.behind = "goat"
        else:
            self.door2.behind = random.choice(["goat", "car"])

            if self.door2.open_door() == "car":
                self.door3.behind = "goat"
            else:
                self.door3.behind = "car"

        self.door_list = [self.door1, self.door2, self.door3]

    def remove_door(self, revealed_door):
        """
        Removes a door revealed to have a goat behind it.
        """
        for door in self.door_list:
            if door == revealed_door:
                self.door_list.remove(door)
                break


class DecisionNode:
    """
    Represents how many times a particular decision has been made
    and links to the next two possible choices that can be made.
    """
    def __init__(self):
        self.count = 0
        self.next_goat = None
        self.next_car = None

    def decide(self):
        """
        Adds to the count of the number of times a decision has been made.
        """
        self.count += 1

    # requirement 2: algorithm - recursion
    def print_node(self, level = 0, label = ""):
        """
        Recursively prints a DecisionNode, its label,
        and its children with indentation.
        """
        # Recursively call for goat child, passing next level and goat label
        if self.next_goat is not None:
            self.next_goat.print_node((level + 1) * 2, label = "Goat")

        # Print the current node's label and count
        if label:
            print("    " * level, f"---> {label}: {self.count}")
        else:
            # For the root node, which has no label
            print(f"Start: {self.count}")

        # Recursively call for car child, passing next level and car label
        if self.next_car is not None:
            self.next_car.print_node((level + 1) * 2, label = "Car")


# requirement 1: data structure - tree
class DecisionTree:
    """
    Maps out results of making particular strategy choice after first guess.
    """
    def __init__(self):
        self.root = DecisionNode()

    def set_up_tree(self):
        """
        Sets up decision levels and nodes of decision tree.
        """
        self.root.next_goat = DecisionNode()
        self.root.next_car = DecisionNode()
        first_level = [self.root.next_goat, self.root.next_car]

        for node in first_level:
            node.next_goat = DecisionNode()
            node.next_car = DecisionNode()

    def make_guesses(self, first_door, second_door):
        """
        First step of recursive decision-making process.
        """
        self.root.decide()

        first_node = None
        if first_door.open_door() == "goat":
            first_node = self.root.next_goat
        elif first_door.open_door() == "car":
            first_node = self.root.next_car

        self.make_guesses_recursive(first_node, second_door)

    # requirement 2: algorithm - recursion
    def make_guesses_recursive(self, node, second_door):
        """
        Rest of the steps in the recursive decision-making process.
        """
        if node.next_goat is not None and node.next_car is not None:
            if second_door.open_door() == "goat":
                self.make_guesses_recursive(node.next_goat, second_door)
            elif second_door.open_door() == "car":
                self.make_guesses_recursive(node.next_car, second_door)

        node.decide()

    def print_tree(self):
        """
        Prints the entire decision tree structure, starting from the root.
        """
        self.root.print_node()



def montyhall_gameplay(strategy):
    """
    This function plays through one round of the game.
    """
    # set up doors
    doors = Doors()
    doors.set_up_doors()

    # know what's behind doors
    goat_door_list = []
    for door in doors.door_list:
        if door.open_door() == "goat":
            goat_door_list.append(door)

    # make first guess and return result later to simulator
    guess1 = random.choice(doors.door_list)

    # reveal a door with a goat and whittle down to 2 options
    if guess1.open_door() == "goat":
        door_revealed = None
        for goat_door in goat_door_list:
            if goat_door != guess1:
                door_revealed = goat_door
                break
    else:
        door_revealed = random.choice(goat_door_list)

    doors.remove_door(door_revealed)

    # make second guess and later return result to simulator
    # this is where strategy argument comes in
        # either keep first guess door or change to other remaining door
    if strategy == "keep":
        guess2 = guess1
    elif strategy == "change":
        guess2 = None
        for door in doors.door_list:
            if door != guess1:
                guess2 = door
                break
    else:
        guess2 = random.choice(doors.door_list)

    # return win or loss
    if guess2.open_door() == "car":
        return guess1, guess2, "win"
    return guess1, guess2, "lose"


def montyhall_simulator(strategy, n):
    """
    This function simulates the results of playing through n rounds of the game.
    """
    my_tree = DecisionTree()
    my_tree.set_up_tree()
    my_wins = 0

    for _ in range(n):
        first_guess, second_guess, result = montyhall_gameplay(strategy)
        my_tree.make_guesses(first_guess, second_guess)
        if result == "win":
            my_wins += 1

    my_wins_percent = my_wins  / n * 100

    return my_tree, my_wins_percent



def main():
    """
    Main function of the program. Combines functionality of all test cases.
    """
    # run the simulator and save results for later
    ktree, k_win_rate = montyhall_simulator("keep", 10000)
    ctree, c_win_rate = montyhall_simulator("change", 10000)
    rtree, r_win_rate = montyhall_simulator("random", 10000)

    # requirement 1: data structure - dictionary
    # get the percentage of times you win when you keep vs change vs randomize
    win_rates = {"keep": k_win_rate,
                "change": c_win_rate,
                "randomize": r_win_rate}
    best_strat = {"strategy": "", "percent_wins": 0}

    # choose the best strategy from between the 3
    for strat, win_rate in win_rates.items():
        if win_rate > best_strat["percent_wins"]:
            best_strat["strategy"] = strat
            best_strat["percent_wins"] = win_rate

    print()
    print(f"The best strategy is to {best_strat['strategy']} your", end = " ")
    print(f"guess due to its {best_strat['percent_wins']:.2f}% win rate.")
    print()

    # print the decision trees
    print("Tree of Counts when Keeping Original Guess:")
    ktree.print_tree()
    print()

    print("Tree of Counts when Changing Guess:")
    ctree.print_tree()
    print()

    print("Tree of Counts when Randomizing Guess:")
    rtree.print_tree()


if __name__ == '__main__':
    main()

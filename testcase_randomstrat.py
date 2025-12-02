"""
File: testcase_randomstrat.py

Description: Tests whether the simulator can successfully randomize
the second guess and whether the resulting DecisionTree object
is populated correctly.

Student Name: Aziz Mutabanna

Student UT EID: aim2464

Course Name: CS 313E

Unique Number: 54595

Date Created: 12/2/25

Date Last Modified: 12/2/25
"""

import mh_simulator as mhs

# run the simulator using a randomization strategy and save its results
rtree, r_win_rate = mhs.montyhall_simulator("random", 10000)

# output the results of randomizing the second guess
print()
print(f"The result of randomizing all guesses "
      f"is winning {r_win_rate:.2f}% of the time.")
print()

# print the decision tree that develops when the second guess is randomized
print("Tree of Counts when Randomizing All Guesses:")
rtree.print_tree()

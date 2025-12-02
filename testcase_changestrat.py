"""
File: testcase_changestrat.py

Description: Tests whether the simulator can successfully change
the second guess from the first guess and whether
the resulting DecisionTree object is populated correctly.

Student Name: Aziz Mutabanna

Student UT EID: aim2464

Course Name: CS 313E

Unique Number: 54595

Date Created: 12/2/25

Date Last Modified: 12/2/25
"""

import mh_simulator as mhs

# run the simulator using a change-second-guess strategy and save its results
ctree, c_win_rate = mhs.montyhall_simulator("change", 10000)

# output the results of changing the second guess
print()
print(f"The result of always changing the second guess "
      f"is winning {c_win_rate:.2f}% of the time.")
print()

# print the decision tree that develops when the second guess is changed
print("Tree of Counts when Changing Next Guess:")
ctree.print_tree()

"""
File: testcase_keepstrat.py

Description: Tests whether the simulator can successfully keep
the second guess the same as the first and whether
the resulting DecisionTree object is populated correctly.

Student Name: Aziz Mutabanna

Student UT EID: aim2464

Course Name: CS 313E

Unique Number: 54595

Date Created: 12/2/25

Date Last Modified: 12/2/25
"""

import mh_simulator as mhs

# run the simulator using a keep-original-guess strategy and save its results
ktree, k_win_rate = mhs.montyhall_simulator("keep", 10000)

# output the results of keeping the original guess
print()
print(f"The result of keeping the original guess "
      f"is winning {k_win_rate:.2f}% of the time.")
print()

# print the decision tree that develops when the original guess is kept
print("Tree of Counts when Keeping Original Guess:")
ktree.print_tree()

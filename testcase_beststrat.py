"""
File: testcase_beststrat.py

Description: Tests whether the program can help settle on
the correct solution to the Monty Hall Problem or not.

Student Name: Aziz Mutabanna

Student UT EID: aim2464

Course Name: CS 313E

Unique Number: 54595

Date Created: 12/2/25

Date Last Modified: 12/2/25
"""

import mh_simulator as mhs

# run the simulator and save results for later
ktree, k_win_rate = mhs.montyhall_simulator("keep", 10000)
ctree, c_win_rate = mhs.montyhall_simulator("change", 10000)
rtree, r_win_rate = mhs.montyhall_simulator("random", 10000)

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

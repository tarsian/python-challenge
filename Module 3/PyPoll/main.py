import os
import csv
import collections
from collections import Counter

# Create Lists
voters_candi = []
candi_vote = []

# Direct the resource file to pull
#===============================================================================
"""
# This code is for directing from anywhere

os.chdir(os.path.dirname(__file__))
election_data_csv_path = os.path.join("Resources", "election_data.csv")

with open(election_data_csv_path, newline="") as csvfile:
"""
#===============================================================================

# This code is from the class, need to be run from 'PyPoll' folder to run it
# C:Users\jacob\Desktop\Class Data\Challenge\Module 3\PyPoll>

budget_data_csv_path = os.path.join("Resources", "election_data.csv")
with open(budget_data_csv_path, 'r') as csvfile:

#===============================================================================

# Main coding
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print("============================================")
    print(f"Header: {csv_header}")
    for row in csv_reader:
        voters_candi.append(row[2])

    sorted_list = sorted(voters_candi, reverse=True) 
    arrange_list = sorted_list
    count_candi = Counter (arrange_list) 
    candi_vote.append(count_candi.most_common())

    for item in candi_vote:
        hana = format((item[0][1])*100/(sum(count_candi.values())),'.3f')
        dool = format((item[1][1])*100/(sum(count_candi.values())),'.3f')
        set = format((item[2][1])*100/(sum(count_candi.values())),'.3f')
    
# Results correctly display for PyPoll:
print("Election Results")
print("-----------------------------------------------------")
print(f"Total Votes:  {sum(count_candi.values())}")
print("-----------------------------------------------------")
print(f"{candi_vote[0][0][0]}: {hana}% ({candi_vote[0][0][1]})")
print(f"{candi_vote[0][1][0]}: {dool}% ({candi_vote[0][1][1]})")
print(f"{candi_vote[0][2][1]}: {set}% ({candi_vote[0][2][1]})")
print("-----------------------------------------------------")
print(f"Winner:  {candi_vote[0][0][0]}")
print("-----------------------------------------------------")

# The text file contains for Pypoll:
election_file = os.path.join("Analysis", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-----------------------------------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candi.values())}\n")
    outfile.write("-----------------------------------------------------\n")
    outfile.write(f"{candi_vote[0][0][0]}: {hana}% ({candi_vote[0][0][1]})\n")
    outfile.write(f"{candi_vote[0][1][0]}: {dool}% ({candi_vote[0][1][1]})\n")
    outfile.write(f"{candi_vote[0][2][0]}: {set}% ({candi_vote[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {candi_vote[0][0][0]}\n")
    outfile.write("-----------------------------------------------------\n") 

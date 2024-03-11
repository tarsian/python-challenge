import os
import csv

months = []
money_change_list = []

month_numbers = 0
previous_month_loss = 0
current_month_loss  = 0
money_change = 0
money_loss = 0

#===============================================================================
"""
# This code is for directing from anywhere

os.chdir(os.path.dirname(__file__))
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:
"""
#===============================================================================

#===============================================================================

# This code is from the class, need to be run from 'PyBank' folder to run it
# C:Users\jacob\Desktop\Class Data\Challenge\Module 3\PyBank>

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv_path, 'r') as csvfile:
#===============================================================================

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Successfully stores the header row (5 points)
    csv_header = next(csvfile)
    print("============================")
    print(f"Header: {csv_header}")
    
    for row in csv_reader:
        month_numbers += 1
        current_month_loss  = int(row[1])
        money_loss += current_month_loss 

        if (month_numbers == 1):
            previous_month_loss = current_month_loss 
        else:
            money_change = current_month_loss  - previous_month_loss
            months.append(row[0])
            money_change_list.append(money_change)
            previous_month_loss = current_month_loss 

    sum_profit_loss = sum(money_change_list)
    average_profit_loss = round(sum_profit_loss/(month_numbers - 1), 2)
    h_change = max(money_change_list)
    l_change = min(money_change_list)
    h_month_index = money_change_list.index(h_change)
    l_month_index = money_change_list.index(l_change)
    best_month = months[h_month_index]
    worst_month = months[l_month_index]

# Results correctly display for PyBank:
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months:  {month_numbers}")
print(f"Total:  ${money_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${h_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${l_change})")
print("-------------------------------------------------")

# The text file contains for PyBank:
budget_file = os.path.join("analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_numbers}\n")
    outfile.write(f"Total:  ${money_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${h_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${l_change})\n")
    outfile.write("----------------------------\n")



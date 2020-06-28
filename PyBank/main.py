# PyBank - Analyzting the financial records

import os
import csv

# Declare variables
month = 0
plTotal = 0
plChange = 0
plCtChange = 0
ctMonth = 0
prevMonth = 0
average = 0
greatestProfit = 0
greatestProfitMonth = ""
greatestLoss = 0
greatestLossMonth = ""

output = {}

# open the file, budget_data.csv for reading
fd = os.path.join('Resources','budget_data.csv')
with open(fd, 'r') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
      
    # Read the header row first
    csvHeader = next(csvReader)
         
    # read each row to do the data analysis
    for row in csvReader:
        try:
            month += 1 #increment the month counter
            ctMonth = float(row[1]) # save the profit/losses of current month
            plTotal += ctMonth  # print a list of strings
            if (month != 1):  # change is curent month-previous month, skipping first month
                plCtChange = ctMonth-prevMonth  # current month change compared to previous month
                plChange += plCtChange # changes in "Profit/Losses" 
               
            # find greatest profit and loss amount and date
            if (plCtChange > greatestProfit):
                greatestProfit = plCtChange
                greatestProfitMonth = row[0] # first column hs the date
            elif (plCtChange < greatestLoss):
                greatestLoss = plCtChange
                greatestLossMonth = row[0] # first column hs the date

            prevMonth = ctMonth # save the current month to the previous month before the next row read
        except ValueError:
            print("err0r" + row[0] + row[1])

average = plChange/(month-1) # change is calucated only from 2nd month

#Write the data to a dictionay
output["month"] = f"Total Months: {month}"
output["total"] = f"Total: ${round(plTotal)}"
output["average"] = f"Average Change: ${round(average,2)}"
output["gProfit"] = f"Greatest Increase in Profits: {greatestProfitMonth} (${round(greatestProfit)})"
output["gLoss"] = f"Greatest Decrease in Profits: {greatestLossMonth} (${round(greatestLoss)})"

#Write the summary report to the terminal
print("Financial Analysis")
print("-------------------------")
print(output["month"])
print(output["total"])
print(output["average"])
print(output["gProfit"])
print(output["gLoss"])

#Write the summary report to the output.txt file
with open("analysis/output.txt", "w") as txtFile:
    txtFile.write("Financial Analysis\n")
    txtFile.write("-------------------------\n")
    txtFile.write(output["month"] + "\n")
    txtFile.write(output["total"] + "\n")
    txtFile.write(output["average"] + "\n")
    txtFile.write(output["gProfit"] + "\n")
    txtFile.write(output["gLoss"] + "\n")
# PyPoll - Analyzting the election data

import os
import csv

# Declare variables
voterCt = 0
topVote = 0
voterList = []
voterDict = {}

# open the file, budget_data.csv for reading
fd = os.path.join('Resources','election_data.csv')
with open(fd, 'r') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
      
    # Read the header row first
    csvHeader = next(csvReader)
         
    # read each row to do the data analysis
    for row in csvReader:
        voterCt += 1 #increment the voterCt counter
        voterDict[row[2]]  = voterDict.get(row[2], 0) + 1
                      
percentage = 0.0  # variable to save the percentage of votes
winner = ""
winnerPercentage = 0
formatPercentage = 0

# find the percetage votes for each candidate and the winner
for x in voterDict:
    percentage = voterDict[x]/voterCt
    formatPercentage = "{:.3%}".format(percentage) # foramt the percentage
    
    if (percentage > winnerPercentage) :
        winnerPercentage = percentage  # find the top vote holder
        winner = x # find the winner of the election
         
    voterList.append(f"{x} : {formatPercentage} ({voterDict[x]})")
       
#Write the summary report to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voterCt}")
print("-------------------------")
for items in voterList:  # read total number of votes each candidate won
    print(items)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Write the summary report to the output.txt file
with open("analysis/output.txt", "w") as txtFile:
    txtFile.write("Election Results\n")
    txtFile.write("-------------------------\n")
    txtFile.write(f"Total Votes: {voterCt}\n")
    txtFile.write("-------------------------\n")
    for items in voterList:  # read total number of votes each candidate won
        txtFile.write(items + "\n")
    txtFile.write("-------------------------\n")
    txtFile.write(f"Winner: {winner}")
    txtFile.write("-------------------------\n")
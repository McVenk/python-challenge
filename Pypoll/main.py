# Declaring Dependencies
import os
import csv
from collections import Counter
import operator

# Declaring path to data
path = 'election_data.csv'

# Reading csv data file
with open(path,'r') as file:
    csvreader= csv.reader(file, delimiter = ',')
    voter_id =[]
    county = []
    candidate = []

# Computing various columns of the csv data file
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Condition for removing headers (if any) for further calculations
    if voter_id[0] == "Voter ID":
        voter_id.pop(0)
    if county[0] == "County":
        county.pop(0)
    if candidate[0]== "Candidate" :
        candidate.pop(0)

# Computing total number of votes    
    total_votes = len(voter_id)
    
# Computing a list of all the unique candidate names from candiate list  and their count of votes  
    candidate_names= list(Counter(candidate).keys())
    candidate_votes = list(Counter(candidate).values())

# Determining total number of candiates
    candidate_number= len(candidate_names)

# Declaring empty list for percetages of votes 
    votes_percentage=[]

# Computing(performing mathematical operations to the items of a list) & formatting percentages of votes list
    votes_percentage=[ "%.3f%%" %((i/total_votes)*100) for i in candidate_votes]

# Determining the winner by first locating the index of maximum votes and use the same index to determine the name of winner
    max_votes=max(candidate_votes)
    maxpos= candidate_votes.index(max_votes)
    winner= candidate_names[maxpos]

# Printing results in desired format using string concentation method in lists
    print("Election Results")
    print("------------------------------")
    print("Total Votes: "+str(total_votes))
    print("------------------------------")
    
    for num in range (0,len(candidate_names)):
        print(candidate_names[num] +": "+ votes_percentage[num]+" ("+ str(candidate_votes[num])+")")
    
    print("------------------------------")
    print("Winner: "+winner)
    print("------------------------------")

# Declaring path to save the results as a text file
    to_path= os.path.join(".",'Poll_Results.txt')

# Printing desired results into the text file
    with open(to_path,"w") as results_file:
        print("Election Results",file=results_file)
        print("------------------------------",file=results_file)
        print("Total Votes: "+str(total_votes),file=results_file)
        print("------------------------------",file=results_file)
        
        for num in range (0,len(candidate_names)):
            print(candidate_names[num] +": "+ votes_percentage[num]+" ("+ str(candidate_votes[num])+")",file=results_file)

        print("------------------------------",file=results_file)
        print("Winner: "+winner,file=results_file)
        print("------------------------------",file=results_file)

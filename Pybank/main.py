# Declaring Dependencies
import os
import csv

# Declaring path to read/access the csv file
path = 'budget_data.csv'

# Reading data from csv file and defining various columns(dates and profit_losses) for further calculation
with open(path,'r') as file:
    csvreader= csv.reader(file, delimiter = ',')

    dates =[]
    Profit_Losses= []
    
    # Filling dates and profit_losses columns
    for row in csvreader:
        dates.append(row[0])
        Profit_Losses.append(row[1])

    # Condition for removing headers (if any) for further calculations
    if dates[0] == "Date":
        dates.pop(0)
    if Profit_Losses[0] == "Profit/Losses":
        Profit_Losses.pop(0)
    
   
        
    # Computing and printing total months 
    total_months= len(dates)
    
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(total_months))


    # Computing and printing total profit/losses
    total= sum(int(i) for i in Profit_Losses)
    print("Total: $"+ str(total))

    # Writing a new list called "change" that computes month over month changes
    change=[int(Profit_Losses[i+1])-int(Profit_Losses[i]) for i in range(len(Profit_Losses)-1)]

    # Computing average change and rounding it upto 2 decimals
    total_change = sum(int(i) for i in change)
    average_change = round((total_change/len(change)),2)
    print("Average Change: $"+str(average_change))
    
    # Computing max change and the month at which this change occured
    greatest_increase= max(change)
    maxpos = change.index(max(change)) 
    increase_date = dates[maxpos+1]
    print("Greatest Increase in Profits: "+increase_date+ " ($"+str(greatest_increase)+")")
    
    # Computing min change and the month at which this change occured
    greatest_decrease= min(change)
    minpos = change.index(min(change)) 
    decrease_date = dates[minpos+1]
    print("Greatest Decrease in Profits: "+decrease_date+ " ($"+str(greatest_decrease)+")")

    # Declaring path to save the results in a text file
    to_path= os.path.join(".",'Financial_Analysis_Results.txt')

    # Accessing the text file and print desired results using string concentation
    with open(to_path,"w") as results_file:
        print("Financial Analysis",file=results_file)
        print("--------------------------------",file=results_file)
        print("Total Months: " + str(total_months),file=results_file)
        print("Total: $"+ str(total),file=results_file)
        print("Average Change: $"+str(average_change),file=results_file)
        print("Greatest Increase in Profits: "+increase_date+ " ($"+str(greatest_increase)+")",file=results_file)
        print("Greatest Decrease in Profits: "+decrease_date+ " ($"+str(greatest_decrease)+")",file=results_file)

    
        

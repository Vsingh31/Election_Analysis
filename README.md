# Election_Analysis
## Overview of Election Audit
In this project,I will figure out the voter trunout for each county,the percentage of votes from each country out of the total count,the county with the highest trunout.And also I will open a csv file and get  data from there. With the help of that data,i will write code to get the results and print the results on command line and write the results on text file too.Working from this module’s election_results.csv file, use for loops and conditional statements with membership and logical operators to find the requested results. Then,
print the results to the command line and save them to your election_results.txt file.

### Election-Audit Results
* In this congressional election **369,711** votes were cast.for getting total_votes i use this code.
  - with open(file_to_load) as election_data:
    -file_reader = csv.reader(election_data)
    - # Read the header
    - header = next(file_reader)
   -  # For each row in the CSV file.
   -  for row in file_reader:
   -   # Add to the total vote count
    -   total_votes = total_votes + 1
How many votes were cast in this congressional election?

Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Which county had the largest number of votes?
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
















#### Election-Audit Summary


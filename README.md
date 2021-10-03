# Election_Analysis
## Overview of Election Audit
In this project,I will figure out the voter trunout for each county,the percentage of votes from each country out of the total count,the county with the highest trunout.And also I will open a csv file and get  data from there. With the help of that data,i will write code to get the results and print the results on command line and write the results on text file too.Working from this module’s election_results.csv file, use for loops and conditional statements with membership and logical operators to find the requested results. Then, print the results to the command line and save them to your election_results.txt file.

### Election-Audit Results

*  In this congressional election  **369,711** votes were cast.for getting total_votes i used this code.
-**with open() function I opened my file and get data and put  it in election_data variable.then i read the election_data with csv module reader() function and put it in            file_reader variable.**
-with open(file_to_load) as election_data:
-file_reader = csv.reader(election_data)
-**Read the header**
-header = next(file_reader)
-**For each row in the CSV file.**
-for row in file_reader:
-**Add to the total vote count**
-total_votes = total_votes + 1
      
*Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

for county_name in county_votes:  
    **Retrieve vote count and percentage.**
    votes = county_votes[county_name]
    **print(candidate_name)**
    vote_percentage = float(votes) / float(total_votes) * 100
    **Print each candidate, their voter count, and percentage to the terminal.**
    county_percentage_vote = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    county_results = county_results + county_percentage_vote  
    
* Which county had the largest number of votes?
   if  vote_percentage > temp :
      temp = vote_percentage
      cname = county_name
        # Print the winning candidates' results to the terminal.
winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {cname}\n"
    f"-------------------------\n")
print(winning_county_summary)

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    #print(candidate_name)
    vote_percentage = float(votes) / float(total_votes1) * 100
    # Print each candidate, their voter count, and percentage to the terminal.
    # candidate_temp = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = candidate_results + (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(candidate_results) 
print(winning_candidate_summary)




#### Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script. (4 pt)

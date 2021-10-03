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
      

* For **Jefferson county**,number of votes were **38,855** and the percentage of the total votes were **10.5%**.For **Denver County**,number of votes were **306,055** and the    percentage of the total votes were **82.8%**.For **Alapahoe County**,number of votes were **24,801** and the percentage of the total votes were **6.7%**. I wrote code to get number of votes and the percentage of the total votes for each county.
  for county_name in county_votes:  
    **Retrieve vote count and percentage.**
    votes = county_votes[county_name] 
    vote_percentage = float(votes) / float(total_votes) * 100
    **Print each candidate, their voter count, and percentage to the terminal.**
    county_percentage_vote = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    county_results = county_results + county_percentage_vote 
    
    
* **Denver county had the largest number of votes.**
   if  vote_percentage > temp :
      temp = vote_percentage
      cname = county_name
        # Print the winning candidates' results to the terminal.
   winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {cname}\n"
    f"-------------------------\n")
  print(winning_county_summary)


* **Charles Casper Stockham candidate** received 85,213 votes and the percentage of the total votes were 23.0%. **Diana DeGette candidate** received 272,892 votes and the percentage of the total votes were 73.8%.**Raymon Anthony Doane** received 11,606 votes and the percentage of the total votes were 3.1%.I wrote code to get number of votes and the percentage of the total votes for each candidate.
  for candidate_name in candidate_votes:
    **Retrieve vote count and percentage.**
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes1) * 100
    **Print each candidate, their voter count, and percentage to the terminal.**
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = candidate_results + (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    
* **Diana DeGette** candidate won the election,Her vote count was **272,892** , her percentage of the total votes was **73.8%**.
   **code for winning candidate,winning vote count,and winning percentage.**
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
   **The winning candidates' results to the terminal.**
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(candidate_results) 
print(winning_candidate_summary)


**Results on Command Line**

![commandline_results](https://user-images.githubusercontent.com/90277142/135737673-ad8e6b26-da57-4d27-93da-58b9a0e8f413.png)


* **Results On Text File(election_analysis.txt)**
  For getting results on Text file,I open the text file with, with open() function in "W" mode.and then print the results and closed.My scripts for results on textfile.I put       this code at the end so after running my all program,I get this output.
  with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results) 
    txt_file.write(county_results)
    txt_file.write(winning_county_summary) 
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary) 

![textfile](https://user-images.githubusercontent.com/90277142/135737678-c388b831-70e8-4d7f-9f8e-3019e211cd7d.png)



#### Election-Audit Summary
* With the help of this script,election commission can get results of election on his test file.He have to change little bit in my script,change the my file path and put his file path to calculate the results according to county name or candidate name.
for example : my file path is "analysis", "election_analysis.txt".I am proving code where I **Assign a variable to save the file to a path.** Here my folder name is analysis and i am saving my data in election_analysis.txt file.so,He have to just change the my folder_name with his folder name and put the his file name with .txt extention to save his result. 
file_to_save = os.path.join("analysis", "election_analysis.txt")


* He can also load any csv file just change my path and put his csv file path and load the data and get the  result even in his file there are more different candidates.
 My file path is "Resources", "election_results.csv". Here my folder name is Resources and my csv file is inside of this folder. so I can load this file to work on and get result.I am proving code where I **Assign a variable to load a file from a path.** my code is this:-
file_to_load = os.path.join("Resources", "election_results.csv")



import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
total_votes1 = 0
temp = 0
cname = ""
county_results = ""
candidate_results = ""

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
county_list = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header
    header = next(file_reader)
    # For each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # 3: Extract the county name from each row.
        county_name = row[1]
        # 4a: if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vte count.
        county_votes[county_name] += 1
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

for county_name in county_votes:  
    # Retrieve vote count and percentage.
    votes = county_votes[county_name]
    #print(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the terminal.
    county_percentage_vote = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    county_results = county_results + county_percentage_vote  
    # Determine winning vote count, winning percentage, and candidate. 
    if  vote_percentage > temp :
      temp = vote_percentage
      cname = county_name
        # Print the winning candidates' results to the terminal.
winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {cname}\n"
    f"-------------------------\n")
print(winning_county_summary)
   

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes1 = total_votes1 + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        #county_name = row[1]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#with open(file_to_save, "w") as txt_file:
for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    #print(candidate_name)
    vote_percentage = float(votes) / float(total_votes1) * 100
    # Print each candidate, their voter count, and percentage to the terminal.
    # candidate_temp = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = candidate_results + (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
   
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

with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results) 
    txt_file.write(county_results)
    txt_file.write(winning_county_summary) 
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary) 
    #txt_file.write(winning_candidate_summary)
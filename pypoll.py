import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)
     # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("eanalysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
   # for row in file_reader:
    #    print(row[0])

# Using the with statement open the file as a text file.
 #with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("counties in the election\n-------------------------------------------------------------------\nArapahoe\nDenver\njefferson\n")
   # txt_file.write("Denver\n")
    #txt_file.write("jefferson\n")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
 #   txt_file.write("Hello World")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

from validate import input_yesno
from wordprocess import WordProcess


# Create new instance of the WordProcess class to perform the analysis.
word_process = WordProcess()
print("Welcome to the F&A text analysis program.\n")

# Continue to prompt until the user provides a file that can be read.
while True:
    input_file = input("What file do you want to analyze? ")
    successful_read = word_process.read_input_file(input_file)
    if successful_read:
        break

# Analyze the manuscript, passing in user's choice to suppress common words.
ok_to_suppress_common = input_yesno("Strip common words from the results?") == "yes"
word_process.analyze(ok_to_suppress_common)

# Print results of the analysis.
word_process.print_list()

# Save a log of the results, if user chooses to do so.
ok_to_save = input_yesno("Would you like to output these results to a file?") == "yes"
if ok_to_save:
    word_process.save_list()

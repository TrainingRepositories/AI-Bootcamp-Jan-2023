"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

import os
import sys
from time import strftime


def sort_by_value(item):
    """Create a key to be used to sort wordlist later."""
    return item[-1]


class WordProcess:
    """
    Class analyzes an input file and reports the number of times the most common words appear.
    """

    common_words = {"the", "be", "are", "is", "were", "was", "am",
                    "been", "being", "to", "of", "and", "a", "in",
                    "that", "have", "had", "has", "having", "for",
                    "not", "on", "with", "as", "do", "does", "did",
                    "doing", "done", "at", "but", "by", "from"}

    def __init__(self):
        """
        Construct class instance and load the word list.
        """

        self.wordlist = []
        self.words_in_manuscript = ""
        self.manuscript_file = ""
        self.word_count = {}
        self.results_list = []
    
        # Open and read the word list from the directory the script is in.
        wordlist_filename = "wordsEn.txt"
        wordlist_path = os.path.join(sys.path[0], wordlist_filename)
        
        print("  TO-DO: Open and read the word list from", wordlist_path)
        self.wordlist = ["one","two","three","four"]
 

    def read_input_file(self, input_file_name):
        """
        Read the specified input file.
        Returns True if file can be read; False if it cannot.
        """
        
        # Open and read the input file.
        self.manuscript_file = input_file_name
        
        print("  TO-DO: Open and read the manuscript from", self.manuscript_file)
        self.words_in_manuscript = ["one","two","three","four","TWO","Three","four","THREE", "Four","four"]  

        return True

    def analyze(self, suppress_common_words):
        """
        Compares input file to English wordlist and gets list of matches.
        """

        print("  Compiling results, one moment ... ", end="")

        # Generate word counts of all words in the manuscript.
        self.word_count = {}
        count = 0
        for word in self.words_in_manuscript:
            word = word.lower().strip(".,?!\"\';:()")  # Lowercase and strip punctuation.
            self.words_in_manuscript[count] = word
            count += 1
            if word in self.wordlist:
                if word not in self.word_count:
                    self.word_count[word] = 1
                else:
                    self.word_count[word] += 1

        print("read {} words from manuscript file.".format(count))

        # Uses reverse order to sort (most frequent first).
        items = sorted(self.word_count.items(), key=sort_by_value, reverse=True)

        # Get the word counts of the 50 words that appear most frequently in the manuscript.
        self.results_list = []
        for word in items[:50]:
            # Suppress common words if requested by user.
            if suppress_common_words and word[0] in self.common_words:
                continue
            result = word[0] + ": " + str(word[1]) + " times"
            self.results_list.append(result)

    def print_list(self):
        """
        Print analysis results to screen.
        """
        print("\nResults for {}".format(self.manuscript_file))
        for line in self.results_list:
            print("  " + line)

    def save_list(self):
        """
        Saves analysis results to log files.
        """

        # Get path to current user's desktop.
        desktop_folder = os.path.expanduser("~/Desktop")
        output_folder = os.path.normpath(os.path.join(desktop_folder, "Wordcount Output"))

        # Set output folder to be current working directory.
        print("  TO-DO: Set output folder to be", output_folder)

        # Save the results to log file and copy to an archive file.
        print("  TO-DO: Save the results to a log file and copy to an archive file.")
 
        # List files currently in the output folder
        print("  TO-DO: List files currently in", output_folder)

        return True

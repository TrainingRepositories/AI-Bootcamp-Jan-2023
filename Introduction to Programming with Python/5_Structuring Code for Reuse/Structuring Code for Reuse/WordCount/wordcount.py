"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}



read_input = ["This", "is", "a", "test!", "this", "is,", "another", "test.",
              "TesT", "value", "this", "!test", "is?"]
read_wordlist = ["this", "is", "a", "test"]

count = 0

for word in read_input:
    word = word.lower()
    # Removes common punctuation so it's not part of the word.
    read_input[count] = word.strip(".,?!\"\';:()")
    count += 1

word_count = {}

for word in read_input:
    word = word.lower()
    if word in read_wordlist:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    else:
        continue



choice = "n"
items = sorted(word_count.items())
results_list = []

# Truncates output if user wants to suppress common words.
for word in items[:50]:
    if choice == "y" and word[0] not in COMMON_WORDS:
        result = word[0] + ": " + str(word[1]) + " times"
        results_list.append(result)
        print(result)
    elif choice == "n":
        result = word[0] + ": " + str(word[1]) + " times"
        results_list.append(result)
        print(result)




while True:
    user_input = input("Please enter the path and name of the text file you want"
                       " to analyze. (E.g.: C:/Users/Monty/Desktop/file.txt):"
                       "\n")

    if user_input is False:
        print("The file you specified does not exist.\n")
        continue
    else:
        common_word = ""

        while common_word != "y" or common_word != "n":
            common_word = input("Would you like to strip common words from the results? "
                                "(Y/N) ").lower()

            if common_word == "y" or common_word == "n":
                break

        user_output = ""

        while user_output != "y" and user_output != "n":
            user_output = input("\nWould you like to output these results to a file? "
                                "(Y/N) ").lower()

            if user_output == "y":
                print("Success!")
                break
            elif user_output == "n":
                print("Exiting...")
                break

        break

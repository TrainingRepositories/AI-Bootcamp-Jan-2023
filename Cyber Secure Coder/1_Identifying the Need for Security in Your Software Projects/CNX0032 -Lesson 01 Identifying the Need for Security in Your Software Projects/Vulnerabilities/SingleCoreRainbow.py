# Single Core Password Table Generator

# import standard libraries

import hashlib              # Hashing the results
import time                 # Timing the operation
import itertools            # Creating controlled combinations

#
# Create a list of lower case, upper case, numbers
# and special characters to include in the password table
#

# Normally all the characters would be listed here.
# The character set was minimized to save class time.
upperCase = "ABCD"
lowerCase = "abcd"
numbers   = "01234"
special   = "!@#$"

# combine to create a final list
allCharacters = []

for character in upperCase:
    allCharacters.append(character)

for character in lowerCase:
    allCharacters.append(character)

for character in numbers:
    allCharacters.append(character)

for character in special:
    allCharacters.append(character)

# Define Directory Path for the password file

FILE = './Rainbow.txt'

# Define the allowable range of password length
PW_LOW  = 4
PW_HIGH = 5

# Mark the start time
startTime = time.time()

# Create an empty list to hold the final passwords
pwList = []

# create a loop to include all passwords
# within the allowable range

print("Generating Passwords ... Please Wait")

for r in range(PW_LOW, PW_HIGH):
    
    #Apply the standard library iterator
    for s in itertools.product(allCharacters, repeat=r):
        # append each generated password to the 
        # final list
        pwList.append(''.join(s))

# For each password in the list generate
# generate a file containing the
# hash, password pairs
# one per line

print("Generating Rainbow Table ... Please Wait")

try:
    # Open the output file
    fp = open(FILE, 'w')

    # process each generated password
    
    for pw in pwList:
        # Perform hashing of the password
        theHash = hashlib.sha256(str(pw).encode('utf-8'))
        theDigest = theHash.hexdigest()
        # Write the hash, password pair to the file
        fp.write(theDigest + ' ' + pw + '\n')
        del theHash
except:
    print('File Processing Error')
    fp.close()

# Now create a dictionary to hold the 
# Hash, password pairs for easy lookup

pwDict = {}

print("Loading Passwords into Dictionary ... Please Wait")

try:
    # Open each output file
    fp = open(FILE, 'r')
    # Process each line in the file which
    # contains key, value pairs
    for line in fp:
        # extract the key value pairs
        # and update the dictionary
        pairs = line.split()
        pwDict.update({pairs[0] : pairs[1]})
    fp.close() 
except:
    print('File Handling Error')
    fp.close()

# When complete calculate the elapsed time

elapsedTime = time.time() - startTime   
print('Elapsed Time: ', elapsedTime)
print('Passwords Generated: ', len(pwDict))


# print out a few of the dictionary entries
# as an example

print("Display Rainbow Table Sample Entries")

cnt = 0
for key,value in (pwDict.items()):
    print(key, value)
    cnt += 1
    if cnt > 10:
        break

# Demonstrate the use of the Dictionary to Lookup a password using a known hash
# Lookup a Hash Value

print("Searching the Rainbow Table Dictionary")

hashToFind = "HASH"
print('Looking for hash: ' + hashToFind)

try:
    pw = pwDict.get(hashToFind)
    print('FOUND password:   ' + pw)
except:
    print('NOT FOUND in rainbow table.')
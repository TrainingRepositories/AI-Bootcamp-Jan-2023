'''
Logical Operations CSC Course

Activity One - Ensure Strong Password Entry


RULE: A strong password requires

1) a minimum of 8 Characters
2) at least one UpperCase Letter
3) at least one LowerCase Letter
4) at least one Number
5) at least one Special Character
6) no sequence of 3 or more repeating characters
7) no out of range chars i.e. escape sequences < ord 0x20 and > 0x7f

'''
MIN_PW = 8

import hashlib          # Import Python STD Library hashing

'''
Simple function to validate the password meets the 
specified criteria
'''
def ValidateStrongPassword(password):
    
    # Set all checks to false
    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    # Assume three repeating characters not found
    noRpt = True

    # Assume characters are within acceptable range
    rng = True
    
    # Validate all conditions

    pwLen = len(password)
    if pwLen >= MIN_PW:
        cnt = True
        
    for eachChar in password:
        if eachChar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp = True
        elif eachChar in "abcdefghijklmnopqrstuvwxyz":
            low = True
        elif eachChar in "0123456789":
            num = True
        elif eachChar in "!@#$%^&*()_-=+/\';><,.>":
            spc = True
        else:
            continue
        '''
        check for triple repeats
        '''
    pos = 0
    for eachChar in password:
        if pos < pwLen-2:
            if eachChar == password[pos+1] and eachChar == password[pos+2]:
                noRpt = False
            else:
                pos += 1
    
    for eachChar in password:
        val = ord(eachChar)
        if val < 0x20 or val > 0x7f:
            rng = False
    
    if upp and low and num and spc and cnt and rng and noRpt:
        return True
    else:
        return False
    
'''
Simple Function to generate a SHA256 passed in password. Password is first changed to Unicode.

'''
def gen_pass_hash(password):
    try:
        string_to_hash = password
        hash_obj = hashlib.sha256(str(string_to_hash).encode('utf-8'))
        return True, hash_obj.hexdigest()
    except:
        return False, "Hashing Failure"
    
# Main Program Starts Here
#===================================

if __name__ == '__main__':
    
    '''
    Your final activity is as follows:
    1) Assume the ValidateStrongPassword Function
       password for storage using the gen_pass_hash
       function.  Experiment with several test passwords 
       and print the resulting hash value.
    2) The gen_pass_hash function is susceptible to
       rainbow table attacks.  Therefore, you need to come up
       with a modification that will make the generated hash
       value more resilient to such an attack.
    '''
    
    thePass = "\0NullIsB4d!"
    
    if ValidateStrongPassword(thePass):
        print(thePass, " Meets the Criteria")
        result, resultingHash = gen_pass_hash(thePass)
        if result:
            print("Hash: ", resultingHash)
        else:
            print(resultingHash)
    else:
        print(thePass, " Does not Meet the Criteria")

    

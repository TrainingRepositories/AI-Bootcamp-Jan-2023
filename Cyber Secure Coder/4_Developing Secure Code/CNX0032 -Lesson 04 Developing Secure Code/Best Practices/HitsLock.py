'''
Python Created Race Condition
Solved using thread locking
'''

import threading
import time

lock = threading.Lock()

hits = {}                               # Create a hits dictionary

def resetHits():
    ''' Function to set the hit count to zero'''
    hits['Value'] = 0

def getHits():
    ''' return the current hit value integer'''
    return hits['Value']

def setHits(count):
    ''' Set the current hit value input = integer count'''
    hits['Value'] = count

def ThreadRace(threadNumber):
    ''' Thread using locking mechanism to prevent raced condition'''
    
    ''' Read, increment and then Update the Hit Counter'''
    cnt = 0
    while cnt < 100:
        # Test for lock
        if lock.locked():
            # try again
            continue
        else:
            # Not locked then acquire the lock
            lock.acquire()
            
            # perform the hits updated
            curHits = getHits()
            curHits += 1
            setHits(curHits)
            
            # release the lock
            lock.release()
            
            # increment the completed cycles
            cnt += 1
        
def main():
    ''' Script main '''
    
    print("\nPython Simulated Race Condition")
    
    # Initialize the hit counter
    resetHits()
    
    # Unit Test: Create 100 independent Threads of Race Function
    threads = []
    
    for i in range(100):
        t = threading.Thread(target=ThreadRace, args=(i,))
        threads.append(t)
        t.start()
        
    # Join all threads to ensure completion
    for eachThread in threads:
        eachThread.join()
    
    # Once all the threads have completed 
    # get the final hit count
    
    totalHits = getHits()
    print("\nHits Results")
    print("Total Should be: 10000")
    print("Total Count  is: ", totalHits)
    
if __name__ == '__main__':
    main()
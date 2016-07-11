#!/usr/bin/python
"""
SwarmJob

A simple program for Running multiple processes in parallel

It takes a file as input

e.g.
SwarmJob.py executable


@author: Sanket Gupte, @DiaMuggles.com
"""

import threading
import os, sys
import argparse


semaphore = threading.Semaphore(20) # The number four here is the number of threads that can acquire the semaphore at one time. This limits the number of subprocesses that can be run at once.



def run_command(cmd):
    with semaphore:
        return os.system(cmd)

class myThread (threading.Thread):
    def __init__(self, name, cmd_str):#threadID, name, cmd_str):
        threading.Thread.__init__(self)
        #self.threadID = threadID
        self.name = name
        self.cmd_str = cmd_str
    def run(self):
        print "Starting " + self.name
        status=run_command(self.cmd_str)
        
        if status!=0:   #0 = Success , 1=Warning , rest=other errors
            print "Some Error"
        
        print "Exiting " + self.name
        

def main():
    
    """Start Script
    """
    parser = argparse.ArgumentParser(description='Program to run Swarm Jobs')    
    parser.add_argument('file-loc', help='/loc/of/file.batch') #This is the name of the shell script , My-process.sh or whatever
    args = parser.parse_args()
    
    threads=[]
    Num=0

    subjects= [] #insert subject IDs here (ARC numbers probably)
    
    print sys.argv[1]
    for sub in subjects:
	thread = myThread(Num,sys.argv[1]+' '+sub)
        Num=Num+1
        threads.append(thread)

    #Start the threads
    for t in threads:
        t.start()
        
    # Wait for all threads to complete
    for t in threads:
        t.join()
    print "Exiting Main Thread"

if __name__=="__main__":
    print 'Going in Main'
    sys.exit(main())

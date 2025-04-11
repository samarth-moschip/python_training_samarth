# Problem Statement:
# This script display timer 
# The user provides the total number of seconds 
# The script then prints a timer

#import the time module 
import time 
 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		##print(mins,secs)
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
t = input("Enter the time in seconds: ") 
countdown(int(t)) 

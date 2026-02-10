“Calculating Time Execution by using Python Decorators”

 
 Project Overview:

Welcome to my project! This project demonstrates how to use Python decorator functions to measure the time calculation of any function without modifying its internal logic.
The decorator captures the start time, end time, and calculates the total runtime in seconds.



🧠 Key Concept Used:

	Python Decorators

	Time measurement using time module

	Function wrapping



🧩 How the Code Works

The calc_time decorator takes a function as input.

Inside the decorator, a wrapper function (calculation) is defined.

	The wrapper:

	Records the start time

	Executes the original function

	Records the end time

	Calculates total execution time

	The decorator returns the wrapper function.

	Any function decorated with @calc_time automatically gets execution-time tracking.




Example Code:


import time

def calc_time(func):
    def calculation():
        start_time = time.time()
        print("Run started")
        func()
        end_time = time.time()
        print("Run ended")
        total_time = end_time - start_time
        print("Total time taken is:", total_time, "seconds")
        return "successfully calculated"
    return calculation

@calc_time
def run_function():
    time.sleep(0.5)

print(run_function())






📤 Sample Output


Run started

Run ended

Total time taken is: 0.5008 seconds

successfully calculated

 
 
 



Why This Approach Is Useful :


Reusable for multiple functions

Improves code readability and maintainability

Widely used in real-world Python applications such as:

	Performance analysis

	Monitoring the time calculation.

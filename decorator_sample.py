import time
def calc_time(func):
    def calculation():
        start_time=time.time()
        print("Run started")
        func()
        end_time=time.time()
        print("Run ended")
        total_time=end_time - start_time
        print("Total time taken is:",total_time,"seconds")
        return "succesfully calculated"
    return calculation
@calc_time
def run_function():
    time.sleep(0.5)
print(run_function())
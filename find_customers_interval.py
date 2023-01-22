### find customer in an interval
## time complexity O(n)
## space complexity O(1)

def find_customers_in_interval(arrival_times, intervals):
    ## customers count 
    customers_count = 0
    ## looping the arrivals time
    for arrival_time in arrival_times:
        ## checking if the arrival time is between given intervals
        if arrival_time >= intervals[0] and arrival_time <= intervals[1]:
            customers_count += 1
    ## if there is match then count will be added 
    return customers_count
        

arrival_times = [10, 12, 14, 15, 18, 20, 22]
intervals = [12, 18]
print(find_customers_in_interval(arrival_times, intervals))

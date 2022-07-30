# Python Assignment
## _How to run_

Run the `main.py` file to execute the program. You can use the command :
```
python -m dsAssignment.main
```

## _Problem Statement_
### Data Structure Implementation (Mysterious Safeguards)
It is summertime! We hope you enjoy some COOL moment in swimming pool!
To ensure safety, the pool owner hires N lifeguards, each of which has a shift that covers some contiguous interval of time during the day. The pool is open from time t=0 until time t=1,000,000,000 on a daily basis, so each shift can be described by two integers, giving the time at which a lifeguard starts and ends his/her shift. For example, a lifeguard starting at time t=5 and ending at time t=9 covers four units of time (note that the endpoints are "points" in time).
Unfortunately, the swimming pool owner hired 1 more lifeguard than he has the funds to support. Given that he must fire exactly one lifeguard, what is the maximum amount of time that can still be covered by the shifts of the remaining lifeguards? An interval of time is covered if at least one lifeguard is present. Please write program to find that mysterious lifeguard that has minimum impact on pool coverage. Please write the maximum coverage time to the output file.

**Input File**
The first line of input contains N (1≤N≤100,000). Each of the next N lines describes a lifeguard in terms of two integers in the range 0…1,000,000,000, giving the starting and ending point of a lifeguard's shift. All such endpoints are distinct. Shifts of different lifeguards might overlap.

*Sample Input (1.in):*
```
3
5 9
1 4
3 7
```
**Output File**
Write a single number, giving the maximum amount of time that can still be covered if the pool owner fires 1 lifeguard.

*Sample Output (1.out):*
```
7
```

## _Solution Approach_
- The total pool time coverage is calculated considering no life guard is to be fired (total_coverage).
- Now, for each life guard's shift (time interval), we calcute the loss of shift time coverage incurred.
- Further, the shift which incurs the least loss is removed from the initially calculated total_coverage.

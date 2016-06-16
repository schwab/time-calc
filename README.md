# Schedule Calc
Implements a schedule calcultor (intercept and elapased shift time) for a particular schedule format.

## Usage
The script is design to be run on jython, but also works on python 2.7 with no changes. Note, python 2.7 is about 5x faster, mainly because of the time it takes to load java on jython.   The script reads the schedule from the file schedule1.csv.  This can be easily modified have the actual schedule it should work against.  Each line is one day's schedule.  The result is printed directly console and contains the two values :
  * boolean - is in a scheduled period
  * number - seconds in since the last scheduled start or between the last scheduled period if the other value is false

To run use the command : 
```jython calculate.py```

It's also possible to see the output of the loader to check for problems or just to write it out to a file for later use : 
```jython load_sch.py``` 

## The task 

is to return 2 pieces of information given a schedule, a day of the week and the time of day.

The two pieces of information to be returned are:
1. Whether or not we are in the operational period in a shift (a boolean or bit value representing running or not running) 
2. The total number of seconds that the last shift that started has run.

The schedule is in the form of 336 integers that represent the hour, minute, and second of the start and end of a shift and the start and end of three breaks for two shifts for each of the 7 days of the week. Therefore each shift has a total of 4 start and end times (shift start and end, and three break start and ends - a total of 8 times), and each day has 8 start and end times (a total of 16 times) and each week has 7*8=56 start and end times (a total of 112 times). Since each time is composed of three values, an integer representing the hour, an integer representing the minute, and an integer representing the second, there are a total of 112*3=336 values which represent a schedule.

Given the schedule, the current day of the week and the current time, the script should return whether or not we are in a shift and how long the last shift that started has run.

Things to keep in mind:
1. Any unused component has the hour set to 24. Therefore on a day we are not running the 8 start end and times all have 24 entered for the hour.
2. The previous note also applies to breaks within a shift. For example, if there is only one break during a shift, the start and end times for the second and third break will have 24 entered for the hour.
3. Hours are in 24 hour format. Midnight is 0.
4. Shifts and/or breaks may span midnight. It still part of the same shift and/or break.
5. Shifts are known by the day of week on which the start. For example Tuesday swing shift starts at 5:00 p.m. on Tuesday and ends at 4:00 a.m. on Wednesday. It is considered a Tuesday shift.
6. Shifts will never overlap each other.
7. In between shifts, the total run time of the previous shift should be returned.

I have already written this computation in PLC ladder logic, but I do not have the time to learn enough about Python (Jython) to do it in that language.


I will add the code at the beginning of the script to assign values to your variables myself.


![ScheduleExamle][schedule]

[schedule]:Capture.PNG

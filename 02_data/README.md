##Files: solution.py (sample solution), squirrel census data (csv), startercode.py

### Assignment
  * title: **data**
  * Create an in-class assignment for using real world data.
  * Create a potential full-credit submission for your assignment.
  * To submit, create a folder in your classwork repository called **02_data**
    - Put all the files for your submission here.
    - Include any solution files (these may vary depending on the assignment).
    - Put the assignment instructions in a file called README.md
    - At the top, include a list of other files in this directory along with a description
  * You will be presenting this assignment to a small group next class.

---
The goal of this lesson is learning how to handle input, in the form of csv files,
using python's built-in csv capabilities. Students have been provided with the NYC Squirrel census 
and given the goal of finding the mean population center of Central Park's squirrels. 
Since this is designed to be an in-class assignment for a single period,
the goal is to learn how to handle input and iterate through it--I envision this as an
early sequence in a data-focused unit, since knowing how to handle data input is a fundamental skill to data analysis.

The lesson for this assignment might go like:

Do Now: Pull up a map of Central Park on Google. If you had to guess, where would the average squirrel
be located in the park? In other words, if you averaged all the x and y coordinates of all the squirrels in the park,
where would the "center" of the squirrel population be? 

Mini-lesson: Data input + Mean Population Center
Main Talking points:
+ What is a csv?
+ How do we use the built-in csv reader in python?
+ Why is closing a file important?
+ How can we use the statement "with()" to handle file closure?
+ What is a csv reader object? What can we do with it? 
+ What is "mean population center"? (Show example of US mean population center, changing over time)

After walking through an example as a class--using a different data set as an example--students will then work in groups to
read in the data from the squirrel dataset, and find the mean population center. 

**NOTE:** The file data.py contains an example of what a solution might look like.

*Students can check their work against the expected answer:*
The center of the squirrel population is at -73.96718384639169, 40.78085300645218

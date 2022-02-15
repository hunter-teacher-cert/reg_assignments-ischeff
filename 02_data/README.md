### Files:
solution.py (sample solution), squirrel census data (csv), startercode.py

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
and given the goal of finding the average location of any given squirrel in Central Park.
Since this is designed to be an in-class assignment for a single period,
the goal is to learn how to handle input and iterate through it--I envision this as an
early sequence in a data-focused unit, since knowing how to handle data input is a fundamental skill to data analysis.

The lesson for this assignment might go like:

Do Now: See/Think/Wonder with csv file of squirrel data! 

Mini-lesson: Data input w/csv in python
Main Talking points:
+ What is a csv?
+ How do we use the built-in csv reader in python?
+ Why is closing a file important?
+ How can we use the statement "with()" to handle file closure?
+ What is a csv reader object? What can we do with it?

After walking through an example as a class--using a different data set as an example--students will then work in groups to
read in the data from the squirrel dataset, and find the location of the average squirrel in Central Park.

**NOTE:** The file data.py contains an example of what a solution might look like.

*Students can check their work against the expected answer:*
The center of the squirrel population is at -73.96718384639169, 40.78085300645218

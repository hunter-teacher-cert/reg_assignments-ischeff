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
using python's built-in csv capabilities. Students have been provided with a handful
of datasets, ranging from the NYC Squirrel census to the current stats of all 2021-2022
NBA players. Since this is designed to be an in-class assignment for a single period,
the goal is to learn how to handle input--I envision this as an early sequence in a data-focused
unit, since knowing how to handle data input is a fundamental skill to data analysis.

The lesson for this assignment might go like:

Do Now: Every day, the world generates countless data points--from temperatures to points
scores in NBA games. Obviously, that data won't read or analyze itself--how do you predict
that data scientists (and computer programmers in general) turn that data into a form that
we can analyze? Sketch out a brainstorm or map of how this might be accomplished.

Mini-lesson: Data input
Main Talking points:
+ What is a csv?
+ How do we use the built-in csv reader in python?
+ Why is closing a file important?
+ How can we use the statement "with()" to handle file closure?

After walking through an example as a class, students will then work in groups to
read in a dataset of their choice--the goal is to construct a program that will read
and print the data, so that it is ready for further analysis (using traversals) tomorrow. 

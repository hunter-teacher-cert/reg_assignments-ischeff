## Final project

## Topic:
Parameters

## Standard(s):
9-12.CT.4
Implement a program using a combination of student-defined and third-party functions to organize the computation.

## Aim:
How can we use dance to model how parameters work?

---

## Do Now:
What metaphor might you use to explain how parameters work?
*The goal here is to elicit what students remember about parameters!*

**Formative Assessment**

Student-created metaphors should:
+ allow for parameters to change value (since they're variables)
+ incorporate a stand-in for arguments
+ include, somehow, the idea that parameters take in input, to pass to a function, where they serve some goal.

*An example might be the game of pass the hot potato, where the potato is an argument passed between multiple functions (i.e., people)*

---

## Mini-lesson

Using the whiteboard, I will explain how a parameter is basically like a hopper in minecraft - you can add things into it, to feed inputs into a function. The inputs can be of many different types, just like you can put things into a hopper.

Note: I plan to use a snippet of [this video](https://www.youtube.com/watch?v=XO0IKUsGiG8) to demonstrate how this works. (I'm relying on the fact that most, if not all, students at this point have played minecraft; the hopper has additional functionality that I won't focus on here.)

**Formative Assessment**

Let's make a quick t-chart to review what parameters and arguments are and what the difference is!

We will make a t-chart on the board, which should include the following:

Parameters:
+ provide inputs for functions
+ there can be one or many of these
+ they are variables in function declarations
+ they can take many types of inputs

Arguments:
+ they *are* the inputs for the Parameters
+ can be of many different types, but must match the type of the parameter
+ these appear in function calls, in place of the parameter variable

---

## Activity 1 Intro

Now, let's play a game!

(Note: we will use the instrumental from [Rapper's Delight by Sugar Hill Gang](https://www.youtube.com/watch?v=D9QIH2N-hnE))

The Zoom adaptation of this is as follows:
```
function clap(n):
  clap your hands n times
function snap (n):
  snap your fingers n times
function shimmy (n):
  shimmy your shoulders n times
function speak(n):
  pronounce n aloud
  ```

I'll demo each of these, for instance:
```
snap(5) means to snap your fingers 5 times in a row, while

snap(5)
clap(1)
means to snap 5 times in a row, then clap once, while

def dance1(n):
  snap(n)
  shimmy(n)
  clap(n)

def dance2(n)
  for i in range(n):
    snap(i)
    shimmy(i)
    clap(i)

def dance3(n):
  dance1(n)
  dance2(n)

```

Now make your own dance! (Give criteria and need to have a task sheet and rubric or checklsit for success? )
means to wiggle and clap in a loop, first doing each zero times, then once, then twice, then three times, and so on.

Note: feedback from Steve: to differentiate parameter and argument, an argument is only used when you call. When you call somebody a name, you usually have an argument. (Not true if you are declaring something! No one really argues!) I.e., calling someone a name causes an argument.

Feedback from Iulian: try it and share!

Laks: Come up with a shared set of possible actions, and then you can assess how well the program can be read.

You'd have the code, then have to write what it means.

Maybe also include cha cha slide?

Additional feedback from Laks: make this a two-day activity, where the first day is all unplugged, since they will make their own examples and present them to each other, and then the second day you turn this into code!

The following is a sketch of the teacher-delivered part of the lesson I'm working on.

I'd like to propose making an unplugged lesson about building functions that touches on the following standard:

9-12.CT.8
Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.

The goal I want to accomplish is create a really fun, engaging and informative unplugged activity to help students understand how conditional expressions work. My tentative idea is to do so through dance/choreography. I'm hoping to design some kind of game that will involve the following elements:

+ A condition that is easy to turn off/on in any classroom, such as the lights being on/off
+ A set of "moves" that are easy to replicate, such as simple dance moves involving different limbs (i.e., right leg, left leg, etc.)
---
### The end product will hopefully be a game that I can use when introducing conditionals next year that will be really sticky (I guess this would work kind of like Simon Says, but have a bit more complexity to it.) After introducing the rules of the game (whatever they turn out to be), and having students practice it with me leading a round, they would then get to design a "program" using the same tools, having their classmates attempt to "run" it, and then assess each other by comparing the intended result (i.e., dance choreography) with the actual result.
---
The Zoom adaptation of this is as follows:
```
function wiggle(n):
  wiggle your eyebrows n times
function smile (n):
  smile n times
function laugh (n):
  laugh n times
function clap(n):
  clap n times
function speak(n):
  pronounce n aloud
  ```

I'll demo each of these, for instance:
```
wiggle(5) means to wiggle your eyebrows 5 times in a row, while

wiggle(5)
clap(1)
means to wiggle your eyebrows 5 times in a row, then clap once, while

for (var i = 0; i < 5; i++){
  speak(i)
  wiggle(i)
  clap(i)
}
```
means to wiggle and clap in a loop, first doing each zero times, then once, then twice, then three times, and so on.

Note: feedback from Steve: to differentiate parameter and argument, an argument is only used when you call. When you call somebody a name, you usually have an argument. (Not true if you are declaring something! No one really argues!) I.e., calling someone a name causes an argument.

Feedback from Iulian: try it and share!

Laks: Come up with a shared set of possible actions, and then you can assess how well the program can be read.

You'd have the code, then have to write what it means.

Maybe also include cha cha slide? 

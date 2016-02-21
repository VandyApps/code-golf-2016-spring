CODE  GOLF
========

###Objective:

Solve as many coding problems as possible in the given time. Make sure to use as little code as possible to compute your solutions.  There are a total of 6 problems that need to be solved. Some problems are worth more points than others, so keep in mind that if you have more points than someone else, you will beat them even if your code golf score is worse. Each problem has a sample input and sample output file to test your coded. For the last 10 minutes of the competition, the final input files will be published for anyone to see and process. You have 10 minutes to go through the final input files and produce your final output files, which you should submit via email to [vandyapps@gmail.com](http://mailto:vandyapps@gmail.com).

###Submission Instructions

You will be submitting 2 files per problem that you attempt to solve, a file containing the output solution and another file containing the code used to compute the solution. Your code will not be executed or interpreted, but will be used to compute your code golf score.

The programming files that you submit must look something like:
* mcnamabd.4.js
* smithah.3.php

This contains your vunet id, followed by a dot, then the problem number this program is for, followed by another dot, and finally the executable extension. The extension is not important and not used (you can program in any language you would like).

Your solution files must be in the following format:
* pauljs.4s.txt
* mcnamabd.1s.txt

The solution files have a similar format to your program files, except each problem number must be followed by the "s" suffix, indicating "solution".

Submit these files to the vandyapps@gmail.com email with a subject line like "code golf" so that it is clear the solution is meant for code golf.

Please zip or tar your files before submitting them.

###1) Character Notation to Number (1 point)

####OVERVIEW

We can represent numbers in a type of character notation with the following rules:

* a indicates add 2
* d indicates decrement
* m indicates multiply by 2
* o indicates output

So the following notation maps to numbers:

* aao -> 4
* aaao -> 6
* aado -> 3
* aamamo -> 36

Note that the o character does not change the value of the number but just indicates that it should be outputted to the screen/file.

So, aaoa will output 4 since o shows up before the last a "add 2".


####PROBLEM
Create a program that converts a file of character notation values into a file of numbers.

The file `problem1.practice.txt` is sample input for this question and the file `problem1s.practice.txt` is sample output.

####Clarification
* Each string in character notation will have exactly 1 "o" character. However, that "o" character can appear anywhere in the string.

###2) The VandyNacci Sequence (1 point)

####OVERVIEW

In the Fibonacci sequence, each subsequent number in the sequence is the sum of the prior two numbers. In the *VandyNacci* sequence, each subsequent number in the sequence is the sum of the prior *three* numbers.

0, 1, 1, 2, 4, 7, 13, 24, 44 ...

####PROBLEM

Write a program that produces the sum of all the VandyNacci numbers that are both divisible by 3 **and** under a given number. For example, if given the number 30, your program should produce the result 24.

Warning: Your program should be able to handle the sum of a long sequence of numbers.

The file `problem2.practice.txt` is sample input for this question and the file `problem2s.practice.txt` is sample output.

###3) Recursion! (1 point)

####OVERVIEW

A recursive function is defined below:

```
F(0, n) = n + 1
F(m, 0) = F(m - 1, 1)
F(m, n) = F(m - 1, F(m, n - 1))
```

####PROBLEM

Write a program that, given values for `m` and `n`, produces the result of the recursive function.

Use the file `problem3.practice.txt` to test your program. The final test file will have the same format as the practice file.

The file `problem3.practice.txt` is sample input for this question and the file `problem3s.practice.txt` is sample output.

###4) Split the Difference (2 points)

####OVERVIEW

A string of numbers contains the numbers 0-9, in strictly increasing order. In between each number, there is a difference. So, for example, the string 025689 has the differences 2, 3, 1, 2, and 1, in order. The goal is to take the string of numbers and split it into two strings, where the sum of the differences is the same in each part. If you receive the string "01268", you should split this string of numbers into the parts "012" and "68" since they both have a sum of differences of 2.

####PROBLEM

You will receive a file containing many strings of numbers, separated by newlines. Your goal is to generate an output file containing the strings broken into substrings, separated by a space. Sample input and output files are given by `problem4.practice.txt` and `problem4s.practice.txt`, respectively.

####CLARIFICATION

You can assume all the strings you get as input CAN be broken into 2 strings with equal sums of differences. You can also assume that there is only one possible solution to each string of numbers.

###5) Can you make a palindrome? (2 points)

####OVERVIEW

A palindrome is a word that reads the same backward as forward.

####PROBLEM

Write a program that determines if it is possible to rearrange a given sequence of characters into a palindrome. For example, the string "abcabc" can be rearranged to be "abccba", a palindrome, so your program should return "yes". The string "abc" cannot be rearranged into a palindrome, so your program should return "no".

A single character is considered to be a palindrome. 

The file `problem5.practice.txt` is sample input for this question and the file `problem5s.practice.txt` is sample output.

###6) Number to Character Notation (3 points)

####OVERVIEW

This problem is the opposite of problem 1. Take a number and compute a Character Notation version of that number (using a's, d's, m's, and o's). See problem 1 for a description of character notation.

####PROBLEM

You will receive a text file containing a set of numbers separated by newlines. Your job is to generate an output file containing the character notations for those numbers. Keep in mind that there are multiple character notation values that map to the same number (i.e. aamo -> 8 and aaaao -> 8; don't forget to add the o to print out your solution).

You will receive a perfect "correctness" score if all of your number to
character count conversions are correct.

The non-whitespace length of your converted solutions will be added to your
"Code Golf" score. Therefore you want to produce the most optimal conversion so
that your code golf score remains low.

The file `problem6.practice.txt` is sample input for this question and the file `problem6s.practice.txt` is sample output.

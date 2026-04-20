# Assignment: Lists, Strings, and For Loops
**Track:** AI Engineer  
**Level:** Beginner to Intermediate  
**Topics:** Lists • Strings • `for` Loops • Basic Problem Solving

---

## Instructions
* Write all solutions in **Python**.
* Try solving each problem using what you have learned about **lists**, **strings**, and **`for` loops**.
* Avoid using advanced shortcuts unless the question allows them.
* Add short comments where your logic may not be obvious.
* Test your code with more than one input.

---

## Section 1: List Practice

### Problem 1: Sum of Elements
Given a list of numbers, print the total sum of all elements using a `for` loop.

Numbers = [2,4,6,8]

for i in Numbers
  sum=i + Numbers[0]
print(sum)
 

**Example input:** `[2, 4, 6, 8]`  
**Example output:** `20`

---

### Problem 2: Count Even Numbers
Given a list of integers, count how many numbers are even.

**Example input:** `[1, 2, 3, 4, 5, 6]`  
**Example output:** `3`

---

### Problem 3: Find the Largest Element
Given a list of numbers, find the largest element without using `max()`.

**Example input:** `[12, 4, 19, 7, 25, 3]`  
**Example output:** `25`

---

### Problem 4: Reverse a List
Given a list, create a new list with the elements in reverse order.

**Example input:** `[1, 2, 3, 4]`  
**Example output:** `[4, 3, 2, 1]`

---

### Problem 5: Remove Duplicates
Given a list, create a new list that contains only unique elements while keeping the original order.

**Example input:** `[1, 2, 2, 3, 4, 3, 5]`  
**Example output:** `[1, 2, 3, 4, 5]`

---

## Section 2: String Practice

### Problem 6: Count Vowels
Given a string, count how many vowels are present.

**Example input:** `"education"`  
**Example output:** `5`

---

### Problem 7: Reverse a String
Given a string, print the reversed version of it without using slicing (`[::-1]`).

**Example input:** `"python"`  
**Example output:** `"nohtyp"`

---

### Problem 8: Character Frequency
Given a string, count how many times each character appears.

**Example input:** `"banana"`  
**Example output:**  
`b: 1`  
`a: 3`  
`n: 2`

---

### Problem 9: Check Palindrome
Given a string, check whether it is a palindrome.

A palindrome reads the same forward and backward.

**Example input:** `"madam"`  
**Example output:** `Palindrome`

**Example input:** `"python"`  
**Example output:** `Not a palindrome`

---

### Problem 10: Find First Non-Repeating Character
Given a string, print the first character that appears only once. If no such character exists, print `"No unique character"`.

**Example input:** `"aabbcddee"`  
**Example output:** `"c"`

---

## Section 3: For Loop Challenges

### Problem 11: Multiplication Pattern
Using a `for` loop, print the multiplication table of a given number from 1 to 10.

**Example input:** `5`  
**Example output:**  
`5 x 1 = 5`  
`5 x 2 = 10`  
`...`  
`5 x 10 = 50`

---

### Problem 12: Student Score Analyzer
Given a list of student scores, use a `for` loop to:
1. Calculate the total score
2. Find the average score
3. Count how many students scored more than 75

**Example input:** `[67, 82, 91, 74, 88, 59]`  
**Example output:**  
`Total: 461`  
`Average: 76.83`  
`Students above 75: 3`

---

### Problem 13: List of Squares
Given a list of numbers, create a new list containing the square of each element using a `for` loop.

**Example input:** `[1, 2, 3, 4]`  
**Example output:** `[1, 4, 9, 16]`

---

### Problem 14: Common Elements
Given two lists, print the common elements present in both lists.

**Example input:**  
`list1 = [1, 2, 3, 4, 5]`  
`list2 = [3, 5, 7, 9]`

**Example output:** `[3, 5]`

---

### Problem 15: Longest Word
Given a sentence, find the longest word.

**Example input:** `"python makes problem solving easier"`  
**Example output:** `"problem"`

---

## Bonus LeetCode-Style Problems

### Problem 16: Two Sum (Easy Version)
Given a list of numbers and a target value, print the indices of the two numbers whose sum is equal to the target.

You may assume exactly one valid answer exists.

**Example input:**  
`nums = [2, 7, 11, 15]`  
`target = 9`

**Example output:** `[0, 1]`

---

### Problem 17: Running Sum
Given a list, create a new list where each element is the running sum up to that position.

**Example input:** `[1, 2, 3, 4]`  
**Example output:** `[1, 3, 6, 10]`

---

### Problem 18: Defanging an IP Address
Given an IP address string, replace every `.` with `[.]`.

**Example input:** `"192.168.0.1"`  
**Example output:** `"192[.]168[.]0[.]1"`

---

### Problem 19: Shuffle String
You are given a string and a list of indices. Rearrange the string so that the character at each position moves to the given index.

**Example input:**  
`s = "code"`  
`indices = [3, 1, 2, 0]`

**Example output:** `"eodc"`

---

### Problem 20: Maximum Consecutive Ones
Given a list containing only `0`s and `1`s, find the maximum number of consecutive `1`s.

**Example input:** `[1, 1, 0, 1, 1, 1]`  
**Example output:** `3`

---

## Submission Suggestion
Create one Python file or notebook and solve the problems in order:
* `problem_1`
* `problem_2`
* `problem_3`
* ...
* `problem_20`

---

## Practice Goal
By the end of this assignment, you should be comfortable with:
* Traversing lists using loops
* Building logic with strings
* Writing step-by-step problem-solving code
* Solving beginner-friendly LeetCode-style questions

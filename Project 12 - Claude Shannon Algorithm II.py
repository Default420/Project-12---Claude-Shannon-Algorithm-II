# -*- coding: utf-8 -*-
"""Copy of AT-Lesson 12 - Project_Question Copy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ONa92R57riYGym3E2l7qa1QP0_3OPPAx

### Instructions

#### Goal of the Project

This project is designed for you to practice and solve the activities that are based on the concepts covered in the following lessons:

1. While Loop, Data-Type Conversion and Conditional Statements.

2. Improving the Algorithm (Functions).

---

#### Getting Started:

1. Click on this link to open the Colab file for this project.

    Link on Panel?usp=sharing

2. Create a duplicate copy of the Colab file as described below.

  - Click on the **File menu**. A new drop-down list will appear.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/0_file_menu.png' width=500>

  - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/1_create_colab_duplicate_copy.png' width=500>

3. After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_Project12** format.

4. Now, write your code in the prescribed code cells.

---

### Activities

#### Activity 1: Find Prime Numbers from 2 to 50

Write a program that uses a `nested while` loop to find the prime numbers from 2 to 50.

A number that is divisible only by itself is known as a **prime number**.

Follow the steps given below to achieve the desired result:

- **Step 1**: Store the starting prime number i.e. `2` in a variable `num`.

- **Step 2**: Define the condition for `while` loop. This loop must be executed till `50`.

- **Step 3**: Inside this `while` loop, perform the following steps:

  1. Initialize a variable `j = 2`.

  2. Create another `while` loop as a nested loop with condition `j <= num`. Inside this while loop, check whether the number stored in variable `num` is divisible by `j` or not.

  3. If the number is divisible by `j` then break the inner `while` loop using `break` statement, otherwise increment the value of `j` by `1`.

  4. Inside the outer `while` loop, check whether the value of `j` is greater than `num/j` using an `if` condition. If the condition gets satisfied, then print that prime number in output.

  5. Also increment the value of `num` inside the outer `while` loop to check other numbers which are in range of 2 to 50, whether they are prime or not.
"""

# Write a program to find prime numbers from 2 to 50.
num = 2

while num <= 50:
    j = 2
    while j <= num:
        if num % j == 0:
            break
        j += 1
    if j > num/j:
        print(num)
    num += 1

"""---

#### Activity 2: Print `n` Digit Number

Write a function which takes a natural number $n$ (where $1\leq n \leq 9$) as an input and returns an $n$-digit number having the digit $n$ at all the places as an output.

**For example:**

- For $n = 1$, the required output is $1$

- For $n = 2$, the required output is $22$

- For $n = 3$, the required output is $333$

- For $n = 4$, the required output is $4,444$

  $\dots$

- For $n = 9$, the required sum is $999,999,999$

After creating the function, print the required outputs for all the numbers from 1 to 9.

Follow the steps given below to achieve the desired result:

- **Step 1**: Create a function, let's say `num_generator()` and pass `n` as a parameter in this function, where `n` is the number of digits to be printed.

  - **Step 2**: Initialize two variables `req_num = 0` and  `count = n - 1`.
   This `count` variable will be used to iterate using a `while` loop to generate the required number.

  - **Step 3**: Define a `while` loop with condition `count >= 0`. Inside the `while` loop, perform the following two tasks:
   
    1. Apply the formula `req_num = req_num + (10 ** count) * n` that will give the required `n` digit number.

    2. Decrement the value of `count` by `1`.

  - **Step 4**: Return the value stored in `req_num` as it is the desired result.

  -  **Step 5**: Call the function `num_generator()` inside a `for` loop that ranges from `1` to `9`.
"""

# Print n -digit number
def num_generator(n):
    req_num = 0
    count = n - 1
    while count >= 0:
        req_num = req_num + (10 ** count) * n
        count -= 1
    return req_num

# Testing the function
for i in range(1, 10):
    print(num_generator(i))

"""---

### Submitting the Project:

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, make sure that '**Anyone on the Internet with this link can view**' option is selected and then click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>

3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_Project12**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.
   
   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_Project12** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>

---
"""
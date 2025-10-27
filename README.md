MSCS532_Assignment1
Course: Algorithms and Data Structures (MSCS-532-B01)
Student: Shashwat Baral
Date: October 27, 2025
Project Overview

This repository contains Assignment 1 for the Algorithms and Data Structures course.
The purpose of this assignment is to set up the Python development environment using Visual Studio Code, configure GitHub for version control, and implement the Insertion Sort algorithm to sort data in monotonically decreasing order.

Steps Completed

Installed Python 3.12 and verified installation using python --version.

Installed and configured Visual Studio Code (VS Code) with:

Python Extension (by Microsoft)

Code Runner Extension

Created this public GitHub repository for version control and collaboration.

Wrote and tested the Insertion Sort algorithm that sorts values in decreasing order.

Made multiple commits to show the development process (setup → implementation → testing).

Code Description

File: insertion_sort_desc.py
This script implements the Insertion Sort algorithm in descending order.

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [5, 2, 9, 1, 7, 3]
print("Original array:", data)
insertion_sort_desc(data)
print("Sorted array (decreasing):", data)

Sample Output:
Original array: [5, 2, 9, 1, 7, 3]
Sorted array (decreasing): [9, 7, 5, 3, 2, 1]

How to Run

Clone this repository:

git clone https://github.com/shashwatbaral321/MSCS532_Assignment1.git


Navigate into the project directory:

cd MSCS532_Assignment1


Run the Python program:

python insertion_sort_desc.py

Learning Outcomes

Set up a Python development environment and IDE.

Learned to use Git and GitHub for version control.

Implemented and tested a divide-and-conquer-based sorting algorithm (Insertion Sort).

Practiced committing code in stages for better development tracking.

Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.

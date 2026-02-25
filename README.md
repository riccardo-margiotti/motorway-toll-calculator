# Motorway Toll Calculator

## Overview
This is a Python application developed as part of an academic project to calculate highway tolls based on bidirectional routes. The program reads data from text files, processes the entry and exit points for various vehicles, and computes the total cost of their travels.

## Key Features
- **Bidirectional Route Handling:** Dynamically calculates distances and prices regardless of travel direction using mirrored lists and dictionaries.
- **File Parsing:** Reads and processes formatted `.txt` files containing toll prices and car travel histories.
- **Algorithmic Logic:** Eliminates the need for complex `if/else` statements by implementing smart index-based calculations.
- **Data Sorting:** Automatically ranks vehicles based on the highest total toll paid.

## Technologies Used
- **Language:** Python 3
- **Concepts:** Data Structures (Dictionaries, Lists), File I/O, Error Handling (`try/except`), Sorting Algorithms.

## How it works
The program requires two input files:
1. `toll.txt`: Contains the segments of the highway and their respective prices.
2. `cars.txt`: Contains the license plates, number of entries, and the start/end points of each trip.

The main script reads these files, maps the routes, calculates the exact toll for each section covered, and outputs a detailed summary for each license plate.

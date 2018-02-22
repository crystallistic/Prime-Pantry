# Prime Pantry (v2)

Objective: Given a dictionary of items and their (integer, positive-valued) item weights, identify whether or not there is a subset that could fill a Prime Pantry Box to exactly 100% and report which items are in the subset.

## Python Version
Python 3.6.0

## How to Run
- Run file from IDLE. Then input the following commands, in the same or similar formats. 

\>>> import primePantryV2

\>>> primePantryV2.primePantryV2({'pepsi':55,'detergent':30,'chips':25,'cereal':15, 'chocolate' : 70, 'soy milk' : 45}, 6, 100)

- The program should return a list of all possible subsets and the number of items in each subset that match the criteria, and print a message if there are none. It will also print a message if the input is invalid.


## Efficiency
The program is more efficient than enumerating all possible subsets for the following reasons: 
- We utilize if-else statements to check the current sum before proceeding
- The moment that we find a combination of items whose weights add up to the total, we print it immediately.
- As soon as the current sum exceeds the total, we return and stop examining further additions to the list of items we're currently looking at to look at other combinations. Here's an example if this is confusing: If the current combination we're looking at proposes that we put in the box 3 items 'chocolate', 'cake', and 'banana' whose weights add up to 105, which is greater than 100, we stop looking at other possibilities that contain all these three items. Then, we wouldn't waste time considering ['chocolate', 'cake', 'banana', 'apple'], for example. 

## Project Collaborators
Asmita Gautam, Mai Ngo

#### Note
The project can be found on [Github](https://github.com/crystallistic/Prime-Pantry).

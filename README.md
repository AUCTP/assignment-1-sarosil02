# Bonus Assignment 1: Cafeteria Simulation

## Scenario
In this assignment, you will create a simulation of the university cafeteria where customers arrive, purchase items, and leave. The program should track the inventory of the items, simulate customer transactions, and generate a report of the day's sales.

## Tasks:

### 1. Initialize Inventory
- Create three separate lists to store product information:
  - `items`: List of product names.
  - `prices`: List of product prices.
  - `inventories`: List of product inventories.

### 2. Simulate Customer Arrivals
- Create a function `simulate_customers`:
  - Simulate a given number of students arriving in the university.
  - For each student, the chance of buying an item at the cafeteria is 50%.
  - For the students that buy an item, randomly select which item it is.
  - Check if there is still inventory for the item available and process the transaction (reduce the inventory, store the sale)
  - The function should return a list `sales` storing all item ids of the performed transactions

### 3. Process Sales
- Create a function `process_sales`:
  - Calculate the total revenue from the list of customer transactions (`sales`).`

### 4. Generate Sales Report
- Create a function `generate_report`:
  - Print a summary of the day's sales, including total revenue and remaining inventory.


### 5. Optional 1 (If you want to practice some more)
In reality, the cafeteria does not only care for the revenue but also for the left over items that can not be sold on the next day and have to be disposed of. Assume, that the production costs for each item are half the sales price. Write a function that calculates the costs of the left over items. Use the costs as well as the revenue to also calculate the profit for the day and include it in your daily report.

### 6. Optional 2 (If you want to practice even more)
Can you use your program to figure out the profit maximizing inventory quantity for each item?

## Example Code Structure
### Initialize Inventory

```python
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]
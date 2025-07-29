import random
import numpy as np


#Functions

def simulate_customers(items, inventories):
    sales = []
    indices = []
    studentsArrive = np.random.poisson(10)
    print(f"Number of students arrived today: {studentsArrive}")
    i = 0
    while i != studentsArrive:
        buyOrnot = random.randint(0,1)
        #index items that we want to buy in the items list 
        if buyOrnot == 1:
            itembought = random.choice(items)
            index = items.index(itembought)
            print(f"You want to buy a {itembought}, its index is: {index}")
        #check inventory
            if inventories[index] > 0:
                inventories[index] -= 1
                sales.append(itembought)
                indices.append(index)
            else: 
                print("Item is out of stock sadly.")
            i += 1
        # else: 
        #     print("No purchase will take place")
        #     i += 1
    print(f"Items sold today: {sales} and remaining inventory: {inventories}")
    return sales, indices 
    

def process_sales(prices, indices):
    revenue = 0
    for x in indices:
        revenue = revenue + prices[x] 
    return revenue


def sales_report(sales, inventories, revenue, costs, profit):
    print("\nSales Report")
    print(20*"-")
    print(f"items sold: {sales}")
    print(f"Remaining inventories: {inventories}")
    print(f"Revenue made: {revenue}")
    print(f"total costs: {sum(costs)}")
    print(f"Total operating profit for the day: {profit}")
    print(20*"-")


def cost_remaining_items(inventories, cost):
    costs = [(cost[0]*inventories[0]), cost[1]*inventories[1], cost[2]*inventories[2]]
    return costs


def total_profit(revenue, costs):
    profit = revenue - sum(costs)
    return profit 


#Main code
items = ["Sandwich", "Salad", "Cake"]
prices = [60, 40, 50]
inventories = [15, 5, 10]
cost = [(prices[0]/2), (prices[1]/2), (prices[2]/2)]
#cost = [30, 20, 25]


sales, indices = simulate_customers(items, inventories)
#print(sales)
#print(indices)
revenue = process_sales(prices, indices)
costs = cost_remaining_items(inventories, cost)
profit = total_profit(revenue, costs)

sales_report(sales, inventories, revenue, costs, profit)
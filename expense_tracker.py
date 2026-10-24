# Simple Expense Tracker with Chart - MyRealProject
import json
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    amount = float(input("Amount entha?: "))
    category = input("Category (Food/Travel/Shopping): ")
    note = input("Note emaina?: ")
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense save ayyindi!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet!")
        return
    total = 0
    print("\n--- Nee Expenses ---")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | Rs.{e['amount']} | {e['note']}")
        total += e['amount']
    print(f"\nTotal Spent: Rs.{total}")

def show_chart():
    expenses = load_expenses()
    if not expenses:
        print("No data for chart!")
        return
    data = defaultdict(float)
    for e in expenses:
        data[e['category']] += e['amount']
    
    plt.figure(figsize=(6,6))
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title("Nee Expense Chart - Kalpana's Tracker")
    plt.show()
    print("📊 Chart chupincha!")

# Main Program
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Chart")
    print("4. Exit")
    choice = input("Choose (1/2/3/4): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_chart()
    elif choice == "4":
        print("Bye Kalpana!")
        break
    else:
        print("Wrong choice!")
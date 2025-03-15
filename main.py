import json
import os
import uuid
import sys
import argparse
import calendar
from datetime import datetime

expense_tracker = "expense_tracker.json"

def load_expense():
    if not os.path.exists(expense_tracker):
        return {}
    try:
        with open(expense_tracker, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: The expense tracker file is empty or contains invalid JSON. Initializing with an empty list")
        return {}
    
def save_expense(expenses):
    with open(expense_tracker, "w") as file:
        json.dump(expenses, file,indent = 4)

def add_expense(amount,category):
    expenses = load_expense()
    expense_id = str (uuid.uuid4())
    now =  datetime.now().isoformat()
    expense = {"expense_id":expense_id,"amount":amount,"category":category,"created_at":now}
    expenses.append(expense)
    save_expense(expenses)
    print(f"Expense added : Rs{amount} for {category}")

def update_expense(expense_id,amount,category):
    expenses = load_expense()
    for exp in expenses:
        if exp["expense_id"] == expense_id:
            exp["amount"] = amount
            exp["category"] = category
            save_expense(expenses)
            print(f"Expense updated : Rs{amount} for {category}")
            return
    print("Expense not found")
    save_expense(expenses)

def delete_expense(expense_id):
    expenses = load_expense()
    
    for exp in expenses:
        if exp["expense_id"] == expense_id:
            expenses.remove(exp)
            save_expense(expenses)
            print(f"Expense deleted : Rs{exp['amount']} for {exp['category']}")
            return
    print("Expense not found")

def view_expenses():
    expenses = load_expense()
    print(f'{"ID":<5}{"Date":<15}{"Category":<20}{"Amount":<10}')
    print("-"*82)
    for i,expense in enumerate(expenses,start=1):
        date = expense['created_at'].split("T")[0]
        print(f"{i:<5}{date:<15}{expense['category']:<20}{expense['amount']:<10}")

def expense_summary():
    expenses = load_expense()
    total_expense = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses=: Rs{total_expense}")

def monthly_expense(month):
    expenses = load_expense()
    try:
        month_number = list(calendar.month_name).index(month.capitalize())
    except ValueError:
        print("Invalid month name")
        return
    total_expense = sum(expense["amount"] for expense in expenses if int(expense["created_at"].split("T")[0].split("-")[1]) == month_number)
    print(f"Total expenses for {month} = Rs{total_expense}")

def bulk_delete():
    confirmation = input("Are you sure you want to delete all expenses? (yes/no): ")
    if confirmation.lower() == "yes":
        expenses = load_expense()
        expenses.clear()
        save_expense(expenses)
        print("All expenses deleted")
    else:
        print("Bulk delete operation canceled")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help="Amount of the expense")
    add_parser.add_argument("category", type=str, help="Category of the expense")

    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("expense_id", type=str, help="ID of the expense to update")
    update_parser.add_argument("amount", type=float, help="Amount of the expense")
    update_parser.add_argument("category", type=str, help="Category of the expense")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("expense_id", type=str, help="ID of the expense to delete")

    view_parser = subparsers.add_parser("expense_list", help="View all expenses")

    summary_parser = subparsers.add_parser("expense_summary", help="View expense summary")

    month_parser = subparsers.add_parser("monthly_expense", help="View monthly expense")
    month_parser.add_argument("month", type=str, help="Month for which to view the expense")

    bulk_delete_parser = subparsers.add_parser("bulk_delete", help="Delete all expenses")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.category)
    elif args.command == "delete":
        delete_expense(args.expense_id)
    elif args.command == "update":
        update_expense(args.expense_id, args.amount, args.category)
    elif args.command == "expense_list":
        view_expenses()
    elif args.command == "expense_summary":
        expense_summary()
    elif args.command == "monthly_expense":
        monthly_expense(args.month)
    elif args.command == "bulk_delete":
        bulk_delete()
    else:
        parser.print_help()    
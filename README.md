# Expense Tracker

Expense Tracker is a command-line interface (CLI) application that helps you manage your expenses. You can add, update, delete, view, and summarize your expenses. Additionally, you can search for expenses by keyword and export your expenses to a CSV file.

## Features

- Add a new expense
- Update an existing expense
- Delete an expense
- View all expenses
- View a summary of total expenses
- View expenses for a specific month
- Delete all expenses (bulk delete)
- Search expenses by keyword
- Export expenses to a CSV file

## Usage

- Add a new expense:
``` sh
python [main.py] add <amount> <category>
```
- Update an existing expense:
``` sh
python [main.py] update <expense_id> <amount> <category>
```
- Delete an expense
```sh
python [main.py] delete <expense_id>
```
- View all expenses
```sh
python [main.py] expense_list
```
- View expense summary
```sh
python [main.py] expense_summary
```
- View expenses for a specific month
```sh
python [main.py] monthly_expense <month>
```
- Delete all expenses (bulk delete)
```sh
python [main.py](http://_vscodecontentref_/11) bulk_delete
```
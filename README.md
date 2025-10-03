Employee Payroll Management System 💰
Project Overview
The Employee Payroll Management System is a desktop application developed using Python and the Tkinter library. It provides a user-friendly graphical interface for managing employee personal details and calculating their monthly net payable salary based on inputs like basic salary, attendance, and allowances/deductions. It also features a built-in calculator and generates a printable salary receipt.

This system is ideal for small to medium businesses or HR departments needing a straightforward, visually intuitive tool for payroll processing.

Key Features ✨
Comprehensive Employee Details: Capture and manage essential information like Employee Code, Name, Designation, Contact, Hired Location, Proof ID, and Address.

Detailed Salary Calculation:

Input fields for Basic Salary, Total Days in the month, and Days Absent.

Allowance fields for Medical and Conveyance (Additions).

Deduction field for PF (Provident Fund).

Automatic calculation of Earnable Salary and Net Payable Salary.

Salary Receipt Generation: A detailed, formatted salary receipt is automatically generated upon calculation, ready for printing or viewing.

Built-in Calculator: A basic calculator utility is integrated into the GUI for quick computations.

Action Buttons: Functionality to Search (placeholder), Save Data (simulated), Clear All fields, and Print the receipt (simulated).

Intuitive GUI: Modern, organized layout with separate frames for Employee Details, Salary Details, and Calculator/Receipt.

Technical Stack 💻
Language: Python 3.x

GUI Library: tkinter (Standard Python Library)

Additional Tkinter Module: tkinter.ttk (Themed Tkinter Widgets)

Data Storage: (Simulated in this version; future versions could integrate SQLite or another database.)

How to Run the Project (Getting Started) 🚀
Prerequisites
You must have Python 3.x installed on your system. No external libraries are needed, as tkinter is part of Python's standard library.

Installation & Execution
Clone the Repository:

Bash

git clone [YOUR_REPO_URL]
cd employee-payroll-system
Run the Script:
Execute the Python file directly from your terminal:

Bash

python employee_payroll.py
# (Assuming you saved the code as employee_payroll.py)
A desktop window titled "Employee Payroll Management System" will appear.

Usage Guide 📋
1. Employee Details (Left Frame)
Enter the Employee Code to uniquely identify the employee (required for search and saving).

Fill in personal details such as Designation, Name, D.O.B, D.O.J, Age, Gender, Email, Contact No, Hired Location, Proof ID, and Address.

2. Employee Salary Details (Top Right Frame)
Input the relevant Month and Year for the payroll.

Enter the monthly Basic Sal.

Specify the Total Days in the month (e.g., 30 or 31) and the employee's Absents.

Enter amounts for allowances: Medical (Add) and Convence (Add).

Enter the amount for deductions: PF (Deduct).

3. Calculate and Generate Receipt
Click the Calculate button.

The Net Salary field will update, and a detailed Salary Receipt will appear in the bottom-right frame.

4. Actions
Save Data: (Simulated) Records a success message indicating the data has been collected. In a production environment, this would save all data to a database.

Clear All: Resets all input fields and the receipt area to their default values.

Print: (Simulated) Provides a status message, simulating the action of sending the receipt content to a printer.

Core Logic (Calculation Breakdown) 💡
The net salary is calculated based on the following formulas implemented in the calculate method:

Paid Days:

Paid Days=Total Days−Absent Days
Per Day Salary:

Per Day Salary= 
Total Days
Basic Salary
​
 
Earnable Salary:

Earnable Salary=Paid Days×Per Day Salary
Gross Salary:

Gross Salary=Earnable Salary+Medical Allowance+Convence
Net Payable Salary:

Net Payable Salary=Gross Salary−PF Deduction
Future Enhancements 🛠️
Database Integration: Implement a persistent backend using SQLite3 or another database to store and retrieve employee records permanently.

Search Functionality: Wire up the Search button to fetch existing employee data by Employee Code from the database.

Update/Delete Functionality: Add buttons and logic for updating an employee's existing record or deleting a record.

Report Generation: Allow export of payroll data to CSV/Excel formats.

Date Picker: Replace simple text entries for D.O.B and D.O.J with a calendar widget for improved user experience.


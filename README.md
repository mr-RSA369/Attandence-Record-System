# Attandence-Record-System
A python program that record attandance of employees in encrypted text file, store details of employees in encrypted text file and the file will be decrypted by the pin code which is used to make attandence. 
Program Featues:
Main Menu: Choose from Make Attendance, Add Employee, or View Employees.

1. Add Employee:

Ask for name, unique employee code, and 4-digit PIN (twice to confirm).

Saves the name and code to data.txt.

Creates a personalized encrypted attendance file, using the PIN as the password.

2. Make Attendance:

Asks for employee code and PIN.

Verifies credentials, decrypts their attendance file, and records IN/OUT time.

Attendance is considered "OUT" if 8+ hours passed since last "IN".

3. View Employees: Shows list of employees without exposing PINs.

Encryption: Attendance files are AES-encrypted using the employee’s PIN.

import os
import sys
import datetime
from getpass4 import getpass

# Directories
base_dir = os.path.dirname(os.path.abspath(__file__))
employee_dir = os.path.join(base_dir, "employees")
attendance_dir = os.path.join(base_dir, "attendance")
record_file = os.path.join(base_dir, "employees.txt")

# Ensure directories exist
os.makedirs(employee_dir, exist_ok=True)
os.makedirs(attendance_dir, exist_ok=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_employee(name, code, pin):
    emp_file = os.path.join(employee_dir, f"{code}.txt")
    with open(emp_file, "w") as f:
        f.write(f"{name}\n{code}\n{pin}")
    with open(record_file, "a") as f:
        f.write(f"{name},{code}\n")

def verify_employee(code, pin):
    emp_file = os.path.join(employee_dir, f"{code}.txt")
    if not os.path.exists(emp_file):
        return False, None
    with open(emp_file) as f:
        lines = f.read().splitlines()
        if len(lines) < 3:
            return False, None
        if lines[2] == pin:
            return True, lines[0]
    return False, None

def add_employee():
    name = input("Enter employee name: ").strip()
    code = input("Enter unique employee code: ").strip()
    pin1 = getpass("Set 4-digit PIN: ")
    pin2 = getpass("Confirm PIN: ")
    while pin1 != pin2 or len(pin1) != 4 or not pin1.isdigit():
        print("PIN mismatch or invalid. Try again.")
        pin1 = getpass("Set 4-digit PIN: ")
        pin2 = getpass("Confirm PIN: ")
    save_employee(name, code, pin1)
    print(f"Employee '{name}' added successfully.")

def record_attendance():
    code = input("Enter employee code: ").strip()
    pin = getpass("Enter PIN: ").strip()
    valid, name = verify_employee(code, pin)
    if not valid:
        print("Invalid code or PIN.")
        return
    now = datetime.datetime.now()
    att_file = os.path.join(attendance_dir, f"{code}_attendance.txt")
    if os.path.exists(att_file):
        with open(att_file, "r") as f:
            lines = f.readlines()
            if lines and "OUT" not in lines[-1]:
                # Calculate time difference
                last_in_str = lines[-1].split(" - ")[0]
                last_in = datetime.datetime.strptime(last_in_str, "%Y-%m-%d %H:%M:%S")
                time_diff = now - last_in
                if time_diff.total_seconds() >= 8 * 3600:
                    with open(att_file, "a") as fa:
                        fa.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - OUT\n")
                        print(f"OUT time recorded for {name} at {now.strftime('%I:%M %p')}")
                    return
    with open(att_file, "a") as f:
        f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - IN\n")
        print(f"IN time recorded for {name} at {now.strftime('%I:%M %p')}")

def view_employees():
    if not os.path.exists(record_file):
        print("No employees found.")
        return
    print("\n--- Employee List ---")
    with open(record_file) as f:
        for line in f:
            name, code = line.strip().split(",")
            print(f"Name: {name}, Code: {code}")

def main_menu():
    while True:
        print("\n==== Employee Attendance System ====")
        print("1. Make Attendance")
        print("2. Add Employee")
        print("3. View Employees")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        clear()
        if choice == "1":
            record_attendance()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()

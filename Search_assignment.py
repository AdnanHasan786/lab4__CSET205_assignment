class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self, employees):
        self.employees = employees

    def search_by_age(self, target_age):
        result = []
        for employee in self.employees:
            if employee.age == target_age:
                result.append(employee)
        return result

    def search_by_name(self, target_name):
        result = []
        for employee in self.employees:
            if employee.name == target_name:
                result.append(employee)
        return result

    def search_by_salary(self, comparison, target_salary):
        result = []
        for employee in self.employees:
            if comparison == '>' and employee.salary > target_salary:
                result.append(employee)
            elif comparison == '<' and employee.salary < target_salary:
                result.append(employee)
            elif comparison == '>=' and employee.salary >= target_salary:
                result.append(employee)
            elif comparison == '<=' and employee.salary <= target_salary:
                result.append(employee)
        return result

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    emp_db = EmployeeDatabase(employees)

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        target_age = int(input("Enter the age to search: "))
        result = emp_db.search_by_age(target_age)
    elif choice == "2":
        target_name = input("Enter the name to search: ")
        result = emp_db.search_by_name(target_name)
    elif choice == "3":
        comparison = input("Enter the salary comparison (> or < or >= or <=): ")
        target_salary = int(input("Enter the target salary: "))
        result = emp_db.search_by_salary(comparison, target_salary)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching records found.")
    else:
        print("Matching Records:")
        for employee in result:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    main()

from abc import ABC,abstractmethod

class IRepository(ABC):
    @abstractmethod
    def create_employee(self, employee):
        """
        Creates a new employee in the database.
        Args:
            employee: Employee object containing the employee details.
        Returns:
            The created employee object.
        Example:
            >>> repo.create_employee(employee)
        """
        pass

    @abstractmethod
    def get_employee(self):
        """
        Retrieves all employees from the database.
        Returns:
            A list containing all employee records.
        Example:
            >>> repo.get_all_employees()
        """
        pass

    @abstractmethod
    def get_employee(self, employee_id):
        """
        Retrieves a single employee using the employee ID.
        Args:
            employee_id: The unique ID of the employee to retrieve.
        Returns:
            The employee object if the employee exists.
            Returns None if the employee is not found.
        Example:
            >>> repo.get_employee(101)
        """
        pass

    @abstractmethod
    def update_employee(self, employee_id, first_name, last_name, department, salary, hire_date, performance_score, email):
        """
        Updates the details of an existing employee.
        Args:
            employee_id: The unique ID of the employee to update.
            first_name: The updated first name of the employee.
            last_name: The updated last name of the employee.
            department: The updated department of the employee.
            salary: The updated salary of the employee.
            hire_date: The updated joining date of the employee.
            performance_score: The updated performance score.
            email: The updated email address of the employee.
        Returns:
            The updated employee object if the employee exists.
            Returns None if the employee is not found.
        Example:
            >>> repo.update_employee(
            ...     101,
            ...     "Gowri",
            ...     "Priya",
            ...     "IT",
            ...     80000,
            ...     "2026-10-12",
            ...     5,
            ...     "gowripriya@gmail.com"
            ... )
        """
        pass
    
    @abstractmethod
    def delete_employee(self, student_id):
        """
        Deletes an employee from the database using the employee ID.
        Args:
            employee_id: The unique ID of the employee to delete.
        Returns:
            True if the employee was successfully deleted.
            False if the employee was not found.
        Example:
            >>> repo.delete_employee(101)
            True
        """
        pass
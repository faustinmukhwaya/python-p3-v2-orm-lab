#!/usr/bin/env python3

from __init__ import CONN, CURSOR
import random
from department import Department
from employee import Employee
from review import Review
import ipdb
from faker import Faker  # Import Faker


def reset_database():
    Review.drop_table()
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()
    Review.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    employee1 = Employee.create("Lee", "Manager", payroll.id)
    employee2 = Employee.create("Sasha", "Manager", human_resources.id)
    Review.create(2023, "Efficient worker", employee1.id)
    Review.create(2022, "Good work ethic", employee1.id)
    Review.create(2023, "Excellent communication skills", employee2.id)


reset_database()

# Test Faker functionality
fake = Faker()
print(fake.name())  # This will print a fake name

ipdb.set_trace()
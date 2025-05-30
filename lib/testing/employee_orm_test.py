from lib.__init__ import CONN, CURSOR
from lib.employee import Employee
from lib.department import Department
from faker import Faker
import pytest

fake = Faker()


class TestEmployee:
    '''Class Employee in employee.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop tables prior to each test.'''

        CURSOR.execute("DROP TABLE IF EXISTS employees")
        CURSOR.execute("DROP TABLE IF EXISTS departments")

        Department.all = {}
        Employee.all = {}

    def test_faker_import(self):
        fake = Faker()
        assert fake.name() is not None

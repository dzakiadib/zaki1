class Employee:
    """Mewakili seorang karyawan."""

    def __init__(self, first_name, last_name, annual_salary):
        """Menyimpan nama depan, nama belakang, dan gaji tahunan."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambah gaji tahunan. Kenaikan bawaan adalah 5000."""
        self.annual_salary += amount


from employee import Employee


def test_give_default_raise():
    """Kenaikan bawaan harus 5000."""
    karyawan = Employee("Budi", "Santoso", 60000)
    karyawan.give_raise()
    assert karyawan.annual_salary == 65000


def test_give_custom_raise():
    """Kenaikan khusus harus sesuai jumlah yang diberikan."""
    karyawan = Employee("Budi", "Santoso", 60000)
    karyawan.give_raise(10000)
    assert karyawan.annual_salary == 70000



import pytest
from employee import Employee


@pytest.fixture
def karyawan():
    """Karyawan yang bisa dipakai di semua fungsi tes."""
    return Employee("Budi", "Santoso", 60000)


def test_give_default_raise(karyawan):
    """Kenaikan bawaan harus 5000."""
    karyawan.give_raise()
    assert karyawan.annual_salary == 65000


def test_give_custom_raise(karyawan):
    """Kenaikan khusus harus sesuai jumlah yang diberikan."""
    karyawan.give_raise(10000)
    assert karyawan.annual_salary == 70000
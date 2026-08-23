from django.db import models


class Employee(models.Model):
    name       = models.CharField(max_length=200)
    phone      = models.CharField(max_length=15, blank=True)
    role       = models.CharField(max_length=100, blank=True)
    salary     = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    join_date  = models.DateField()
    is_active  = models.BooleanField(default=True)
    address    = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ("present",  "Present"),
        ("absent",   "Absent"),
        ("half_day", "Half Day"),
        ("leave",    "Leave"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date     = models.DateField()
    status   = models.CharField(max_length=10, choices=STATUS_CHOICES, default="present")
    note     = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.name} — {self.date} — {self.status}"


class SalaryPayment(models.Model):
    METHOD_CHOICES = [
        ("cash", "Cash"),
        ("bank", "Bank"),
        ("upi",  "UPI"),
    ]

    employee     = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="salary_payments")
    month        = models.CharField(max_length=7)   # format: 2025-06
    amount_paid  = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method       = models.CharField(max_length=10, choices=METHOD_CHOICES, default="cash")
    note         = models.CharField(max_length=200, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "month")

    def __str__(self):
        return f"{self.employee.name} — {self.month} — ₹{self.amount_paid}"
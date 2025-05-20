from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, blank=True)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    employee_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} to {self.member.name}"

class Fine(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine for {self.loan}"

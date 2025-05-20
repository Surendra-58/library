from django.contrib import admin
from .models import Book, Member, Librarian, Loan, Fine

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Librarian)
admin.site.register(Loan)
admin.site.register(Fine)


from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Author, Book, Borrowing
from faker import Faker
import random
from datetime import timedelta, datetime

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with fake users, authors, books, and borrowings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(0)

        # --- Clear old data ---
        Borrowing.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        self.stdout.write(self.style.WARNING("Old data deleted."))

        # --- Create Users ---
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="123456"
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS("✅ Users created."))

        # --- Create Authors ---
        authors = []
        for _ in range(5):
            author = Author.objects.create(
                full_name=fake.name(),
                Birth_Year=fake.date_of_birth(minimum_age=25, maximum_age=90)
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS("✅ Authors created."))

        # --- Create Books ---
        books = []
        for _ in range(10):
            book = Book.objects.create(
                Book_title=fake.sentence(nb_words=3),
                Author=random.choice(authors),
                posted_Date=fake.date_this_decade(),
                Number_of_Copies=random.randint(1, 10),
                Is_Alvalible=random.choice([True, False])
            )
            books.append(book)
        self.stdout.write(self.style.SUCCESS("✅ Books created."))

        # --- Create Borrowings ---
        for _ in range(10):
            book = random.choice(books)
            client = random.choice(users)
            borrow_date = fake.date_time_this_year()
            return_date = borrow_date + timedelta(days=random.randint(3, 14))
            Borrowing.objects.create(
                Book=book,
                Client=client,
                Borrow_Date=borrow_date,
                Return_Date=return_date,
                Returned=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("✅ Borrowings created."))
        self.stdout.write(self.style.SUCCESS("🎉 Database successfully seeded!"))

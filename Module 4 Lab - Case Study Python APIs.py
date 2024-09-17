import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Set up Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    ROOT_URLCONF='__main__',
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'library',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'books.db'),
        }
    },
    STATIC_URL='/static/',
)

# Define the models
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name

# Define the serializers
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'publisher']

# Define the views
from rest_framework import generics

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Define the URLs
from django.urls import path

urlpatterns = [
    path('api/books/', BookListCreate.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]

# Run migrations and start the server
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__main__')
    django.setup()
    execute_from_command_line([sys.argv[0], 'makemigrations'])
    execute_from_command_line([sys.argv[0], 'migrate'])
    execute_from_command_line([sys.argv[0], 'runserver'])

if __name__ == "__main__":
    main()
from django.db import models

# Create your models here.


class Category(models.Model):
    # Field to store the name of the category, with a maximum length of 150 characters.
    category = models.CharField(max_length=150)

    def __str__(self):
        # Returns a human-readable representation of the model instance, which is the category name in this case.
        return self.category


class Joke(models.Model):
    # Field to store the joke text. There is no limit on the length of the text.
    joke = models.TextField()

    # Foreign key relationship with the Category model. The on_delete=models.CASCADE parameter indicates that if a category
    # is deleted, all jokes associated with it will also be deleted.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        # Returns a human-readable representation of the model instance, which is the joke text in this case.
        return self.joke

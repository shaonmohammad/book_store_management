from django.contrib import admin
from .  models import BookModels
# Register your models here.


class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'catagory',
                    'first_pub', 'last_pub')


admin.site.register(BookModels, BookStoreModelAdmin)

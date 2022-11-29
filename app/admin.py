from django.contrib import admin
from app.models import *
# Register your models here.



class DataModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'phone_number', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'category',)


admin.site.register(DataModel,DataModelAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
from django.contrib import admin
from .models import Customer, Category, Course

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

#@admin.register(Age)
#class AgeAdmin(admin.ModelAdmin):
#    ...

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("category", "name", 'kid_age', 'price', 'date_price', 'image',)
    
    @admin.display()
    def category(self, obj):
        return obj
    category.short_description = 'Name'

#@admin.register(Price)
#class PriceAdmin(admin.ModelAdmin):
#    ...

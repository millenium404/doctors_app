from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)

# User = get_user_model()
#
# class RecipeIngredientInline(admin.StackedInline):
#     model = RecipeIngredient
#     readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
#     extra = 0
#     # fields = ['name', 'quantity', 'unit', 'directions']
#
#
# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [RecipeIngredientInline]
#     list_display = ['name', 'user']
#     readonly_fields = ['timestamp', 'updated']
#     raw_id_fields = ['user']
#
# admin.site.register(Recipe, RecipeAdmin)

from django.contrib import admin

from .models import Review, Hotel


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class Hotel(admin.ModelAdmin):
    pass

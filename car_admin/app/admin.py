from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "review_count")
    list_filter = ("brand", "model")
    search_fields = ("brand", "model")


class ReviewAdmin(admin.ModelAdmin):
    # pass
    form = ReviewAdminForm
    list_display = ("car", "title")
    search_fields = ("car__model", "title")
    list_filter = ("car__brand", "car__model")


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)

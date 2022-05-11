from django.contrib import admin
from .models import Snack


@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'purchaser', )
    list_filter = ('purchaser', 'name')
    search_fields = ('name',)

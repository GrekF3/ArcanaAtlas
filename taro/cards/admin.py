from django.contrib import admin
from .models import Card, CardsDesk
# Register your models here.


class AdminCard(admin.TabularInline):
    model = Card
    extra = 0

@admin.register(CardsDesk)
class AdminCarDesk(admin.ModelAdmin):
    inlines = (AdminCard,)
    prepopulated_fields = {"desk_slug": ("name",)}
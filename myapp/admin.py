from django.contrib import admin

# Register your models here.
from myapp.models import Faq

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display =["id", "question", "answer", "attachment"]
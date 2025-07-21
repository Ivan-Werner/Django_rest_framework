from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "city", "avatar")
    search_fields = ("email",)
    search_filter = ("email",)


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ("id", "user", "payment_date", "amount")

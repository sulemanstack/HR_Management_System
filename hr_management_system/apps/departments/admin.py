from django.contrib import admin

from .models import Department, Designation


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "manager",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "department",
        "is_active",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "department",
        "is_active",
    )
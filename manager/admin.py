from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Worker, Task, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", )}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": ("position",)
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("is_completed", )


admin.site.register(TaskType, Position)

from django.contrib import admin
from .models import level, subject, topic, sheet_name, questions, index, UserAnswers, flag
from import_export.admin import ImportExportModelAdmin
import nested_admin


@admin.register(questions)
class questionsupload(ImportExportModelAdmin):
    pass


@admin.register(index)
class indexupload(ImportExportModelAdmin):
    pass


class questionsInline(nested_admin.NestedTabularInline):
    model = questions
    extra = 1


class sheet_nameAdmin(nested_admin.NestedModelAdmin):
    inlines = [questionsInline]


admin.site.register(level)
admin.site.register(subject)
admin.site.register(UserAnswers)
admin.site.register(flag)


@admin.register(topic)
class topicupload(ImportExportModelAdmin):
    pass


admin.site.register(sheet_name, sheet_nameAdmin)

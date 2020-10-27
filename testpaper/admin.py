from django.contrib import admin
from .models import exam, TestPaper, questions, TestIndex, UserAnswers, UserResult, flag, timer
from import_export.admin import ImportExportModelAdmin
import nested_admin


@admin.register(questions)
class questionsupload(ImportExportModelAdmin):
    pass


@admin.register(TestIndex)
class TestIndexupload(ImportExportModelAdmin):
    pass


class questionsInline(nested_admin.NestedTabularInline):
    model = questions
    extra = 1


class TestPaperAdmin(nested_admin.NestedModelAdmin):
    inlines = [questionsInline]


admin.site.register(exam)
admin.site.register(TestPaper, TestPaperAdmin)
admin.site.register(UserAnswers)
admin.site.register(UserResult)
admin.site.register(flag)
admin.site.register(timer)

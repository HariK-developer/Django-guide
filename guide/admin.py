from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from guide.models import Foo

# Register your models here.


@admin.register(Foo)
class BookAdmin(ImportExportModelAdmin):
    pass
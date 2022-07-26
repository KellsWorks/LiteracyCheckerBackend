from django.contrib import admin

from Tests.models import Question
from Tests.models import Test

admin.site.register(Question)
admin.site.register(Test)

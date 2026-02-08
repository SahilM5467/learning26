from django.contrib import admin
from . models import User, Survey, SurveyTemplate, Question, Option, Response, Answer, Notification, Report

# Register your models here.

admin.site.register(User)
admin.site.register(Survey)
admin.site.register(SurveyTemplate)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Answer)
admin.site.register(Notification)
admin.site.register(Report)



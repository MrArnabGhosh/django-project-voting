from django.contrib import admin
from . models import Question,Choice
# Register your models here.
admin .site.site_header="The Poll Mall"
admin.site.site_title="Voting Admin Area"
admin.site.index_title="Welcome To our Voting Admin Area"



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra= 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None ,{'fields':['question_text']}),('Date Information',{'fields':['pub_date'],'classes':['collapes']}),]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)


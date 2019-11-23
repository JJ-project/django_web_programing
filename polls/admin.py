from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):  #TabularInline : 테이블 형식으로 보여줌
    model = Choice
    extra = 3 #새로 추가할 항목을 화면에 한번에 보여줄 개수 지정

class QuestionAdmin(admin.ModelAdmin):   
   # fields = ['question_text','pub_date'] #필드 UI순서를 바꿔줌
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date') #레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] #필터 사이드 바 추가
    search_fields = ['question_text'] #검색 박스 추가 


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

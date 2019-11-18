from django.shortcuts import render #장고의 단축 함수인 render()함수를 import
from django.shortcuts import get_object_or_404 #장고의 단축 함수인 get_object_or_404함수를 import하도록 함수명만 추가
from polls.models import Question, Choice   #Question 테이블에 액세스하기 위해 polls.Question클래스를 import
from django.http import HttpResponseRedirect, HttpResponse #리다이렉트 기능
from django.urls import reverse #url 처리를 위해 필요
def index(request): #뷰함수 정의. request객체는 뷰 함수의 필수 인자
    #latest_question_list는 Question테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 5개의 최근 Question객체를 가져옴
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] 
    #템플릿에 넘겨주는 방식은 파이썬 사전 타입으로, 템플릿에 사용될 변수명과 그 변수명에 해당하는 객체를 매핑하는 사전으로
    #context변수를 만들어서 이를 render()함수에 보내줌
    context = {'latest_question_list': latest_question_list}
    #render함수는 템플릿 파일인 polls/index.html에 context변수를 적용하여 사용자에게 보여줄 최종 HTML 텍스트를 만들고,
    #이를 담아소 HttpResponse 객체를 반환함
    #index() 뷰 함수는 최종적으로 클라이언트에게 응답할 데이터인 HttpResponse 객체를 반환함
    return render(request, 'polls/index.html', context)

def detail(request, question_id): #추가로 question_id 인자를 받음. 다음과 같이 정의한 URL 패턴에서 정규표현식으로
                                  #추출한 question_id 파라미터가 뷰 함수의 인자로 넘어오는 것.
    # get_object_or_404()함수는 첫 번째 인자는 모델 클래스이고, 두 번째 인자부터는 검색 조건을 여러 개 사용할 수 있음.
    # Question클래스로부터 pk=question_id 검색 조건에 맞는 객체를 조회함. 조건에 맞는 객체가 없으면 Http404 익셉션을 발생시킴.
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        #request.POST는 제출된 폼의 데이터를 담고 있는 객체로서, 파이썬 사전처럼 키로 그 값을 구할 수 있음.
        #request.POST['choice']는 폼 데이터에서 키가 'choice'에 해당하는 값인 'choice_id'를 String으로 리턴함
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): #폼의 POST데이터에서 'choice'라는 키가 없으면 KeyError 익셉션을 발생시킴.
                                            #또는 검색 조건에 맞는 객체가 없으면 Choice.DoesNotExist 익셉션이 발생함.
        #설문 투표 폼을 다시 보여줌
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else: #익셉션이 발생하지 않고 정상 처리하는 경우
        selected_choice.votes += 1 #Choice객체 .votes 속성, 즉 선택 카운터를 1 증가시킴.
        selected_choice.save() #변경 사항을 해당 Choice 테이블에 저장함.
        #POST 데이터를 정상적으로 처리하였으면, 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        #HttpResponseRedirect 객체의 생성자는 리다이렉트할 타겟 URL을 인자로 받음.
        #타겟 URL은 reverse() 함수로 만듦.
        #최종적으로 vote() 뷰 함수는 리다이렉트할 타겟 URL을 담은 HttpResponseRedirect 객체를 반환함.
        #이처럼 웹 프로그램에서 POST방식의 폼 데이터를 처리하는 경우, 그 결과를 보여줄 수 있는 페이지로 이동시키기 위해
        #HttpResponseRedirect 객체를 리턴하는 것이 일반적임.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question':question})
    

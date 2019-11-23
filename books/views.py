from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# Create your views here.

class BooksModelView(TemplateView):
    template_name = "books/index.html"

    #템플릿 시스템으로 넘겨줄 컨텍스트 변수가 있는 경우 get_context_data()메소드를 오버라이딩 해주면 됨
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #get_context_data() 메소드를 정의할 때는 반드시 첫 줄에 super()메소드를 호출해야 함
        context['model_list'] = ['Book', 'Author', 'Publisher'] #첫 화면에 테이블 리스트를 보여주기 위해 컨텍스트 변수 'model_list'에 담아 템플릿에다가 넘겨줌
        return context

#ListView는 객체가 들어있는 리스트를 구성하여 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 됨. 만일 이런 리스트를 테이블에 들어있는 모든 레코드를 가져와 구성하는 경우에는 테이블명
#즉 모델 클래스명만 지정해주면 됨
#그리고 명시하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2가지 있는데, 하나는 컨텍스트 변수로 object_list를 사용하고, 또 하나는 템플릿 파일을 "모델명 소문자_list.html" 형식의
#이름으로 지정해 줌
class BookList(ListView):
    model = Book
    #books/book_list.html

class AuthorList(ListView):
    model = Author
    #books/author_list.html
class PublisherList(ListView):
    model = Publisher
    #books/publisher_list.html

#DetailView는 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 됨. 만일 테이블에서 PK로 조회해서 특정 객체를 가져오는 경우에는 테이블명, 즉 모델 클래스명만 지정해주면 됨.
#조회 시 사용할 PK 값은 URLconf에서 추출하여 뷰로 넘어온 파라미터를 사용
#여기서도 컨텍스트 변수로 object_list를 사용하고, 또 하나는 템플릿 파일을 "모델명 소문자_detail.html" 형식의 이름으로 지정해 줌
class BookDetail(DetailView):
    model = Book
    #books/book_detail.html

class AuthorDetail(DetailView):
    model = Author
    #books/author_detail.html

class PublisherDetail(DetailView):
    model = Publisher
    #books/publisher_detail.html

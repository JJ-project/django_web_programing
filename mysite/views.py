from django.views.generic.base import TemplateView
from django.apps import apps

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['app_list'] = ['polls', 'books']
        dictVerBose = {}
        #장고에서 제공하는 apps객체의 get_app_configs() 메소드를 호출하면 settings.py 파일의 INSTALLED_APP에 등록된 각 앱의 
        #설정 클래스들을 담은 리스트를 반환함
        for app in apps.get_app_configs():
            print(app)
            print(app.path)    
            if 'site-packages' not in app.path: #물리적 경로에 'site-packages'라는 디렉토리가 포함되어 있다면 제외시킴
                dictVerBose[app.label] = app.verbose_name
                                                            #app.label:books
                                                            #app.verbose_name:Book-Author-Publisher App
                print("app.verbose_name:"+app.verbose_name)
        context['verbose_dict'] = dictVerBose
        return context

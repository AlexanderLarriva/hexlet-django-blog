from django.shortcuts import render
from django.views import View


# def index(request):
#     app_name = "Hexlet django blog"  # Название приложения
#     return render(request, "articles/index.html", {"app_name": app_name})


class ArticleIndexView(View):
    template_name = 'articles/index.html'
    def get(self, request, *args, **kwargs):
        app_name = "Hexlet django blog"
        context = {
            'app_name': app_name,
        }
        return render(request, self.template_name, context)
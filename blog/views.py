from django.shortcuts import render
from blog.models import Article
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.

# class Article_List(ListView):
#     model = Article
#     context_object_name = 'articles'
#     extra_context = {
#         'title': "yangiliklar"
#     }
#     template_name = 'blog/index.html'
#
#     def get_queryset(self):
#         return Article.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(Article_List, self).get_context_data()
#         context['news'] = Paginator('articles', 1)
#         page = context['news'].page(1)

def article_list(request):
    articles = Article.objects.all()
    news = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
    objects = news.get_page(page_number)
    context = {
        'articles': objects,
    }
    print(objects)
    return render(request, 'blog/index.html', context=context)








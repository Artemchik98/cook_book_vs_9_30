from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post,PostPoint
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'


def post_list(request):
    object_list=Post.objects.all()
    paginator=Paginator(object_list,1) #10 постов = 10 страниц
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)# пост №5
    except PageNotAnInteger: # Если постов на страницу по 10 а всего их 5
        posts=paginator.page(1)
    except EmptyPage:#если номер страницы которой нет
        posts=paginator.page(paginator.num_pages)

    return render(request,'blog/post/list.html',{'page':page,
                                                'posts':posts})








def post_detail(request,year,month,day,slug):
    post_object=get_object_or_404(Post, status='published',
                                        slug=slug,
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day)

    post_points=PostPoint.objects.filter(post=post_object)
    return render(request,'blog/post/detail.html',{'post':post_object,
                                                   'post_points':post_points})
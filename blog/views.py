from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
# Create your views here.
from .models import Post, PostPoint


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 1)  # 10 постов = 10 страниц
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)  # пост №5
    except PageNotAnInteger:  # Если постов на страницу по 10 а всего их 5
        posts = paginator.page(1)
    except EmptyPage:  # если номер страницы которой нет
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})


def post_detail(request, year, month, day, slug):
    post_object = get_object_or_404(Post,
                                    status='published',
                                    slug=slug,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    post_points = PostPoint.objects.filter(
        post=post_object)

    comments = post_object.comments.filter(
        active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(
            data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(
                commit=False)
            new_comment.post = post_object
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post_object,
                   'post_points': post_points,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id,
                             status='published')
    sent = False
    if request.method == "POST":
        print(request.POST)
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} {cd['email']} рекомендует " \
                      f"вам прочитать {post.title}"
            message = f'Прочтите "{post.title}" по cсылке ' \
                      f' {post_url}\n' \
                      f'{cd["name"]} прокоментировал ' \
                      f'{cd["comment"]}'
            send_mail(subject, message, "admin@cook_book.com",
                      [cd['to'], ])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent})

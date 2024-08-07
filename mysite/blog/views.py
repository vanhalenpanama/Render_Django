from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# 홈화면 -> 최근 게시물 5개가 있는 구조
def home(request):
    recent_posts = Post.objects.order_by('-created_date')[:5]
    return render(request, 'blog/home.html', {'recent_posts': recent_posts})


# post_list -> 모델에서 게시글을 가져오는 함수
def post_list(request):
    post_list = Post.objects.all().order_by('-created_date')
    paginator = Paginator(post_list, 1) # 한 페이지에 1개의 게시글을 보여줌
    
    page = request.GET.get('page') # 페이지 번호를 가져오는 함수
    posts = paginator.get_page(page) # 해당 페이지의 게시글을 가져오는 함수
    
    return render(request, 'blog/post_list.html', {'posts': posts})


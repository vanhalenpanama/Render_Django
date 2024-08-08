# 페이징 처리 -> 한 페이지에 보여줄 게시글의 수를 지정하고, 페이지 번호를 클릭하면 해당 페이지로 이동
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post
from django.contrib.auth import logout
from .forms import PostForm
from django.contrib.auth.decorators import login_required
''' # def post_create()
from django.shortcuts import render, redirect #템플릿 렌더링 / URL 리디렉션
from .forms import PostForm
'''

# 홈페이지 뷰 함수 작성
def home(request):
    # 최근에 작성된 5개의 게시글을 가져오는 함수
    recent_post = Post.objects.all().order_by('-created_date')[:5] 
    # request 요청하는 객체, blog/home.html 템플릿 파일, recent_post 모델에서 가져온 데이터
    return render(request, 'blog/home.html',{'recent_post': recent_post})


def logout_view(request):
    logout(request)
    return redirect('/')


# post_list -> 모델에서 게시글을 가져오는 함수
def post_list(request):
    post_list = Post.objects.all().order_by('-created_date')
    paginator = Paginator(post_list, 1) # 한 페이지에 1개의 게시글을 보여줌
    
    page = request.GET.get('page') # 페이지 번호를 가져오는 함수
    posts = paginator.get_page(page)  # 현재 페이지의 게시글을 가져오는 함수
    # 페이지 번호를 URL의 쿼리스트링에서 가져오는 함수 예를 들어 ?page=2 두번째 페이지를 가져오게 함
    # 객체에서 현재 페이지의 게시글을 가져오는 함수 
    # -> 유효하지 않은 페이지 번호를 입력하면 기본적으로 첫번째 게시글을 가져오도록 수행 
    return render(request, 'blog/post_list.html', {'posts': posts})


# 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # pk값이 일치하는 포스트를 가져오는 함수 오류에 검증!
    return render(request, 'blog/post_detail.html', {'post': post})


#
@login_required
def post_create(request):
    if request.method == "POST": # Post요청 확인
        form = PostForm(request.POST) # PostFrom 인스턴스 생성 인자 전달
        if form.is_valid(): # 폼의 유효성
            post = form.save(commit=False) # Post객체 생성
            post.author = request.user  # 현재는 로그인 기능이 없으므로 나중에 구현
            post.save() #객체 저장
            return redirect('post_detail', pk=post.pk) # 새로 생성된 게시물의 상세 페이지로 리 디렉션 / post_detail URL 패턴에 새 게시물의 기본 키('pk')를 전달
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

#
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # if post.author != request.user:
    #     return redirect('post_detail', pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 이미 데이터베이스에 저장된 게시물을 수정 instance = post 기존 Post객체를 폼에 제공
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재는 로그인 기능이 없으므로 나중에 구현
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

#
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# home 뷰는 요청이 들어오면 최근에 작성된 5개의 포스트를 홈페이지에서 보여줌
# recnet_post -> 모델에서 가장 최근에 작성된 5개의 게시글을 가져오는
# render 템플릿을 활용해 응답을 생성 -> request 요청하는 객체, blog/home.html 템플릿 파일, 
# recent_post 모델에서 가져온 데이터

# Create your views here.





# def category_posts(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     posts = Post.objects.filter(category=category).order_by('-created_date')
#     return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})





#---------------0807코드--------------------------

# from django.shortcuts import render
# from django.core.paginator import Paginator
# from .models import Post

# # 홈화면 -> 최근 게시물 5개가 있는 구조
# def home(request):
#     recent_posts = Post.objects.order_by('-created_date')[:5]
#     return render(request, 'blog/home.html', {'recent_posts': recent_posts})


# # post_list -> 모델에서 게시글을 가져오는 함수
# def post_list(request):
#     post_list = Post.objects.all().order_by('-created_date')
#     paginator = Paginator(post_list, 1) # 한 페이지에 1개의 게시글을 보여줌
    
#     page = request.GET.get('page') # 페이지 번호를 가져오는 함수
#     posts = paginator.get_page(page) # 해당 페이지의 게시글을 가져오는 함수
    
#     return render(request, 'blog/post_list.html', {'posts': posts})


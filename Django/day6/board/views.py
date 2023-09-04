from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# 소셜 로그인
def social_login_view(request):
    return render(request, 'board/social_login.html')

# 전체 게시물 조회
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/article_list.html', {'articles':articles})

# 게시물 작성 (생성)
def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request,'board/article_create.html')

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = UserCreationForm()
        return render(request, 'board/register.html',{'form':form})
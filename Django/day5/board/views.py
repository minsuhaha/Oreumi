from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# 한 함수당 하나의 html 페이지로 잡아주면 좋음!
def article_list(request):
    articles = Article.objects.all().order_by('-created_at') # 오랜된 글부터 나오도록
    return render(request, 'board/article_list.html', {'articles' : articles})

def article_create(request):
    if request.method == 'POST': # 폼에서 글작성 버튼으로부터 요청이 들어왔다.
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('article_list')

    return render(request, 'board/article_create.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')

    else:
        form = UserCreationForm()
        return render(request, 'board/register.html', {'form':form})
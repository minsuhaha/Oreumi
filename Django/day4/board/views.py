from django.shortcuts import render, redirect
from .models import Post
# from datetime import date, datetime

def read_Post_data(request):
    # start_date = datetime.strptime('2023-08-16 11:00:00', '%Y-%m-%d %H:%M:%S')
    # posts = Post.objects.filter(title__contains = '오르미 2')
    posts = Post.objects.all()
    return render(request, 'board/index.html', { "posts" : posts })

def add_Post_data(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        published_date = request.POST['published_date']
        recommend_count = request.POST['recommend_count']

        post = Post(title=title, content=content, published_date=published_date, recommend_count=recommend_count)
        post.save()
        
        # url name='index'로 redirect 해주기
        return redirect('index')
    
    return render(request, 'board/add_page.html')


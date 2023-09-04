from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

# 소셜 로그인
def social_login_view(request):
    return render(request, 'users/social_login.html')

# 로그인 성공 시
def login_success(request):
    username = request.user # 현재 로그인 된 사용자의 이름 가져오기
    return render(request, 'users/main.html', {'username':username})
    # return redirect('main', username=username)
# 로그아웃
def logout_view(request):
    logout(request) # 사용자를 로그아웃 시킵니다.
    return redirect('social_login')
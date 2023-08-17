from django.shortcuts import render

from django.shortcuts import render

def index(request):
    message = "Django 템플릿 예제"
    number = 2023
    my_list = ['Python', 'Django', 'HTML', 'CSS']
    my_dict = {
        'name': '오르미',
        'age': 10,
        'city': '서울'
    }
    
    context = {
        'message': message,
        'number': number,
        'my_list': my_list,
        'my_dict': my_dict,
    }
    
    return render(request, 'main/index.html', context)


def new_page(request):
    return render(request, 'main/oreumi_page.html')

def new_page2(request):
    return render(request, 'main/oreumi_page2.html')

def new_page3(request):
    return render(request, 'main/oreumi_page3.html')




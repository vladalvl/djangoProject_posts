from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # print(request)
    return render(request, 'base.html')


def post(request):
    post_content = request.headers
    return render(request, 'posts.html', {'content': post_content})


def about(request):
    return render(request, 'about.html', {'content': '<h1>About</h1>'})

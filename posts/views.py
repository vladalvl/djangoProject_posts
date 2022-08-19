from django.shortcuts import render, HttpResponse


def home(request):
    print(request)
    return render(request, 'posts/base.html')


def post(request, post_id: int):
    print(post_id)
    post_content = request.headers
    return render(request, 'posts/posts.html', {'content': post_content})


def about(request):
    return render(request, 'posts/about.html', {'content': '<h1>About</h1>'})

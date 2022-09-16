from django.shortcuts import render, redirect, HttpResponse
# from posts.forms import CreateForm


def home(request):
    print(request)
    return render(request, 'posts/base.html')


def post(request, post_id: int):
    print(type(post_id), post_id)
    if request.method == 'GET':
        print('Параметры', request.GET)

        query_to_bd = (request.GET.get('price_min'), request.GET.get('price_max'))
        print('query_to_bd', query_to_bd)
    return render(request, 'posts/posts.html', {'content': request.GET})


def post_str(request, post_id: str):
    print('ID в виде строки', post_id)
    post_content = request.headers
    return render(request, 'posts/posts.html', {'content': post_content})


def about(request):
    return render(request, 'posts/about.html', {'content': '<h1>About</h1>'})


# def create_post(request):
#
#     user_form = CreateForm()
#
#     if request.method == 'POST':
#         user_form = CreateForm(request.POST)
#         if user_form.is_valid():
#             print('VALID', request.POST)
#             print({**user_form.cleaned_data})
#             return redirect('home')
#
#         else:
#             print('ERROR', request.POST)
#
#     return render(request, 'posts/create.html', {'form': user_form})

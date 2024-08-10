from django.shortcuts import render
from django.http import Http404

# Create your views here.

blog_dict={
    "flask": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
    'django': "Flask provides configuration and conventions, with sensible defaults, to get started. This section of the documentation explains the different parts of the Flask framework and how they can be used, customized, and extended. Beyond Flask itself, look for community-maintained extensions to add even more functionality.",
    "laravel" : "Laravel values beauty. We love clean code just as much as you do. Simple, elegant syntax puts amazing functionality at your fingertips. Every feature has been thoughtfully considered to provide a wonderful developer experience.",
}

def welcome(request):
    title_data="Welcome!"
    content_data="Welcome to my blog page"
    return render(request, "blog/welcome.html",{
        'title_data': title_data,
        'content_data':content_data,
    })


def index(request):
    title_data="Index"
    content_data="Here are all the lists of blog posts"
    return render(request, "blog/index.html",{
        'title_data': title_data,
        'content_data': blog_dict,
    })


def post (request,slug):
    title_data="Post"
    content_data="Post-Data"
    try:
        content_data=blog_dict[slug]
    except KeyError:
        raise Http404()
    return render(request, "blog/post.html",{
        'title_data': title_data,
        'content_data':content_data,
    })

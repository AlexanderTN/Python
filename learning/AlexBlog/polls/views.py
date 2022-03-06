# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def index(request):
#     print('nothing')
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.views import generic
from .models import Post
from django.shortcuts import render

class PostList(generic.ListView):      
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-created_on')  #.filter(status=1)
    template_name = 'index.html'
    #return render()

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post


# Create your views here.

def post_list(request):

	post_list = Post.objects.all()

	query = request.GET.get('query')

	if query:

		post_list = post_list.filter(text__icontains=query)

	return render_to_response('blog/post_list.html', {'post_list': post_list,
													'query': query})


def post_detail(request, pk):

	post = Post.objects.get(id=pk)

	return render_to_response('blog/post_detail.html', {'post': post})
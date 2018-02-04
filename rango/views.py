from django.shortcuts import render

from django.http import HttpResponse

# Import the Category model
from rango.models import Category
from rango.models import Page

def index(request):
# Query the database for a list of ALL categories currently stored.
# Order the categories by no. likes in descending order.
# Retrieve the top 5 only - or all if less than 5.
# Place the list in our context_dict dictionary
# that will be passed to the template engine.

	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages':page_list}

# Return a rendered response to send to the client. We make use of the shortcut function to make our lives easier.Note that the first parameter is the template we wish to use.

	return render(request, 'rango/index.html', context_dict)


def about(request):

	context_dict = {'boldmessage':"This tutorial has been put together by Malgorzata Kurkiewicz."}

	return render(request, 'rango/about.html', context = context_dict)

def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass
	# to the template rendering engine.
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)


		context_dict['pages'] = pages
		context_dict['category'] = category

	except Category.DoesNotExist:

		context_dict['category'] = None
		context_dict['pages'] = None

	# Go render the response and return it to the client.
	return render(request, 'rango/category.html', context_dict)

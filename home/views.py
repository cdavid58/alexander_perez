from django.shortcuts import render

def Index(request):
	return render(request,'index.html')

def Category(request):
	return render(request,'category.html')

def About(request):
	return render(request,'about.html')

def Blog(request):
	return render(request,'blog.html')

def Blog_Details(request):
	return render(request,'blog_details.html')

def Contact(request):
	return render(request,'contact.html')
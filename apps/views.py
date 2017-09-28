from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD</h1> 
    <a href="/books_fbv_user/">Click here to login</a><br>    
    """
    return HttpResponse(html)
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"code.html")
def counter(request):
    words=request.POST['text']
    words_count=len(words.split())
    return render(request,"counter.html",{"words":words_count})

                            
                        

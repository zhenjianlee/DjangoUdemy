from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ReviewForm, ReviewModelForm
from .models import ReviewModel
from django.views import View

# Create your views here.

# View as a Class
class ReviewView(View):
    form= ReviewModelForm()
    def GET(self,request):
        return render(request,"reviews/review.html",{
        'form': form,
    })
        
        
    def POST(self,request):
        form= ReviewModelForm(request.POST)
        if form.is_valid():
            newReview=ReviewModel(**form.cleaned_data)
            newReview.save()
            return HttpResponseRedirect("thank-you")
        
    def thank_you(self,request):
        return render(request,"reviews/thank_you.html")


# View as a Function
# def review(request):
#     if request.method == 'POST':
#         #form = ReviewForm(request.POST)
#         form= ReviewModelForm(request.POST)
#         if form.is_valid():
#             newReview=ReviewModel(**form.cleaned_data)
#             newReview.save()
#             return HttpResponseRedirect("thank-you")
#     else:
#         #form = ReviewForm()
#         form= ReviewModelForm()
#     return render(request,"reviews/review.html",{
#         'form': form,
#     })
    

# def thank_you(request):
#     return render(request,"reviews/thank_you.html")
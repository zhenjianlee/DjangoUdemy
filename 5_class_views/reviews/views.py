from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ReviewForm, ReviewModelForm
from .models import ReviewModel
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView ,CreateView

# Create your views here.
def thank_you(request):
    return render(request,"reviews/thank_you.html")

# View as a Class - Base View
class ReviewView(View):
    def get(self,request):
        form= ReviewModelForm()
        return render(request,"reviews/reviews.html",{
        'form': form,
    })
        
    def post(self,request):
        form= ReviewModelForm(request.POST)
        if form.is_valid():
            newReview=ReviewModel(**form.cleaned_data)
            newReview.save()
            return HttpResponseRedirect("thank-you")
        
# View as a Class - FormView
class ReviewFormView(FormView):
    #MUST USE MODEL FORM TO SAVE TO DB - MODEL WILL NOT WORK!
    form_class=ReviewModelForm
    template_name="reviews/reviews_form.html"
    success_url="thank-you"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
# View as a Class - CreateView
class ReviewCreateView(CreateView):
    model=ReviewModel
    fields="__all__"
    template_name="reviews/reviews.html"
    success_url="thank-you"
        
        
# Using Base View
# class ListView(View):
#     def get(self,request):
#         reviews = ReviewModel.objects.all()
#         return render(request,"reviews/list.html",{
#             'reviews': reviews,
#         })

# Using TemplateView       
class NormalListView(TemplateView):
    template_name="reviews/list_normal.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        reviews = ReviewModel.objects.all()
        context['reviews']=reviews
        return context

# Using ListView
class ListView(ListView):
    model=ReviewModel
    template_name="reviews/list_view.html"

# Template View - Single Detail
class ReviewTemplateView(TemplateView):
    template_name="reviews/review_template.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        review_id=kwargs['id']
        review=ReviewModel.objects.get(pk=review_id)
        context['review']=review
        return context
    
# Detail View - Single Detail
class ReviewDetailView(DetailView):
    model=ReviewModel
    template_name="reviews/review_detail.html"

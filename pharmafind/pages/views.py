from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SearchForm
from pharmacydatabase.models import Drug, DrugSet, DrugType, Brand, Pharmacy

home = 'http://127.0.0.1:8000'

# Create your views here.
def home_view(request):
    query = request.GET.get('query', -1)
    weight = request.GET.get('weight', False)
    area = request.GET.get('area', False)
    if query != -1:
        form = SearchForm(request.GET)
        if form.is_valid():
            redirectto = '/search/?query=' + query
            if weight:
                redirectto += '&weight=' + weight
            if area:
                redirectto += '&area=' + area
            return redirect(redirectto)
    else:
        form = SearchForm()
    return render(request, "home.html", {'form':form})

def tohome(request):
    return redirect(home)

def search(request):
    query = request.GET.get('query', -1)
    weight = request.GET.get('weight', False)
    area = request.GET.get('area', False)
    form = SearchForm()
    if query == -1:
        return redirect(home)
    drugsets = DrugSet.objects.filter(drug__drugtype__name__contains=query)
    drugsets2 = DrugSet.objects.filter(drug__brand__name__contains=query)
    if weight:
        drugsets = drugsets.filter(drug__milligrams__contains=weight)
        drugsets2 = drugsets2.filter(drug__milligrams__contains=weight)
    if area:
        drugsets = drugsets.filter(pharmacy__area__contains=area)
        drugsets2 = drugsets2.filter(pharmacy__area__contains=area)
    drugsets = drugsets.union(drugsets2)
    drugsets = drugsets.order_by('-count', 'id')
    hasresults = drugsets.exists()
    return render(request, "search.html", {'query':query, 'weight':weight, 'form':form, 'results':drugsets, 'hasresults':hasresults, 'area':area})

def drugview(request):
    id = request.GET.get('id', False)
    if id:
        try:
            drugset = DrugSet.objects.get(pk=id)
        except:
            return render(request, "medicineviewerror.html")
        return render(request, "medicineview.html", {'drugset':drugset})
    else:
        return redirect(home)

def pharmamanage(request):
    currentuser = request.user
    if currentuser.is_authenticated:
        return render(request, "pharmamanage.html")
    else:
        return redirect(home + '/login/')

@login_required
def account_redirect(request):
    return redirect(home)
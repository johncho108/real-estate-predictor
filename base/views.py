from django.shortcuts import render, redirect
from . import regression as r
from . forms import RequiredFeaturesForm, OptionalFeaturesForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import csv

def home(request):
    prediction_display = None
    
    if request.method == 'POST':
        form1 = RequiredFeaturesForm(request.POST)
        form2 = OptionalFeaturesForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            bedrooms = form1.cleaned_data['bedrooms']
            sqft_living = form1.cleaned_data['sqft_living']
            grade = form1.cleaned_data['grade']

            optional_features = []
            bathrooms = form2.cleaned_data['bathrooms']
            if bathrooms:
                optional_features.append(('bathrooms', bathrooms))
            sqft_lot = form2.cleaned_data['sqft_lot']
            if sqft_lot:
                optional_features.append(('sqft_lot', sqft_lot))
            floors = form2.cleaned_data['floors']
            if floors:
                optional_features.append(('floors', floors))
            waterfront = form2.cleaned_data['waterfront']
            waterfront_val = None
            if waterfront == 'yes':
                waterfront_val = 1
            elif waterfront == 'no':
                waterfront_val = 0
            if waterfront_val != None:
                optional_features.append(('waterfront', waterfront_val))
            view = form2.cleaned_data['view']
            if view != None:
                optional_features.append(('view', view))
            condition = form2.cleaned_data['condition']
            if condition != None:
                optional_features.append(('condition', condition))

            optional_variables = []
            optional_vals = []
            for i, j in optional_features:
                optional_variables.append(i)
                optional_vals.append(j)
            regression = r.fit_regression(*optional_variables)
            prediction = r.predict(regression, bedrooms, sqft_living, grade, *optional_vals)
            prediction_display = r.display(prediction)
            context = {'prediction_display': prediction_display, 'form1': form1, 'form2': form2}
            return render(request, 'home.html', context)
    
    form1 = RequiredFeaturesForm()
    form2 = OptionalFeaturesForm()
    context = {'prediction_display': prediction_display, 'form1': form1, 'form2': form2}
    return render(request, 'home.html', context)

def data(request):
    csv_rows = []
    with open('base/sample.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            csv_rows.append(row)
    context = {'csv_rows': csv_rows}
    return render(request, 'data.html', context)
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect. Please try again.')
        except:
            messages.error(request, 'Username or password is incorrect. Please try again.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


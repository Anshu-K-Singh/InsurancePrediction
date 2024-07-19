from django.shortcuts import render
from django.http import HttpResponse
import joblib

model = joblib.load('static/random_forest_regressor') 
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def predict(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        sex = bool(request.POST.get("sex"))
        bmi = float(request.POST.get('bmi'))
        children = int(request.POST.get("children"))
        smoker = bool(request.POST.get("smoker"))
        region = bool(request.POST.get("region"))
        
        pred = model.predict([[age, sex, bmi, region, children, smoker]])
        
        
        return render(request, 'predict.html', {'output': pred} )
    else:
        return render(request, "predict.html")
    
def contact(request):
    return render(request, 'contact.html')


from django.shortcuts import render
from fakeuserclassification.forms import InputForm
import pickle
import numpy as np
import os

def popularity_metric(friends_count: int, followers_count: int):
    return np.round(np.log(1+friends_count) * np.log(1+followers_count), 3)

def compute_popularity_metric(friends_count,followers_count):
    return popularity_metric(friends_count=friends_count,followers_count=followers_count)

def predict(request):

    print("in predict")

    if request.method == "POST":
        inputForm = InputForm(request.POST)

        if inputForm.is_valid():

            print("in if")
            rf_classifier = pickle.load(open(os.path.abspath(os.path.dirname(__name__))+'/model/randomforest_model.pickle', 'rb'))

            followers_count = inputForm.cleaned_data["followers_count"]
            friends_count = inputForm.cleaned_data["friends_count"]
            listed_count = inputForm.cleaned_data["listed_count"]
            favourites_count = inputForm.cleaned_data["favourites_count"]
            verified = inputForm.cleaned_data["verified"]
            statuses_count = inputForm.cleaned_data["statuses_count"]
            default_profile = inputForm.cleaned_data["default_profile"]
            default_profile_image = inputForm.cleaned_data["default_profile_image"]
            popularity = compute_popularity_metric(int(friends_count),int(followers_count))


            prediction = rf_classifier.predict([[followers_count,friends_count,listed_count,favourites_count,verified,statuses_count,default_profile,default_profile_image,popularity]])
            print("Test Prediction:",prediction)

            if prediction[0]==0:
                return render(request, "index.html", {"result":"Not a Bot"})
            elif prediction[0]==1:
                return render(request, "index.html", {"result":"Bot"})
        else:
            return render(request, 'index.html', {"message": "Please Fill Form Data"})
    else:
        return render(request, 'index.html', {"message": "Invalid Request"})
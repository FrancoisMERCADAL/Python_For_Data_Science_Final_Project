from django.http import HttpResponse
from django.shortcuts import render
from Datas.predict_trees import decision_tree_predict, random_forest_predict, xgboost_predict

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def accueil(request):
    return render(request, 'page/accueil.html')

def decision_tree(request):
    prediction = decision_tree_predict()
    string = ""
    for nb in prediction:
        string += str(nb) + ", "
    return render(request, 'page/decision_tree.html', {'decision_tree_result': string})

def random_forest(request):
    prediction = random_forest_predict()
    string = ""
    for nb in prediction:
        string += str(nb) + ", "
    return render(request, 'page/random_forest.html', {'random_forest_result': string})

def xgboost(request):
    prediction = xgboost_predict()
    string = ""
    for nb in prediction:
        string += str(nb) + ", "
    return render(request, 'page/xgboost.html', {'xgboost_result': string})
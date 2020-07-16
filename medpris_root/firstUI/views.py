from django.shortcuts import render
import pandas as pd

# Create your views here.
def indexPage(request):

    pris_contalgin = pd.read_excel ("/Users/johanankerallerup/dev/medpris_projekt/Data_medpriser/contalgin10_pris_19_20.xlsx", sheet_name=1)
    pris = pris_contalgin[pris_contalgin.columns[1]].tolist()
    varA = pris_contalgin[pris_contalgin.columns[0]].tolist()
    context = {"pris" :pris, "varA": varA}
    return(render(request, 'index.html', context))
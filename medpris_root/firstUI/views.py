from django.shortcuts import render
import pandas as pd
import datetime

# Create your views here.
def indexPage(request):

    pris_contalgin = pd.read_excel ("/Users/johanankerallerup/dev/medpris_projekt/Data_medpriser/contalgin10_pris_19_20.xlsx", sheet_name=1)
    pris = pris_contalgin[pris_contalgin.columns[1]].tolist()
    varA = pris_contalgin[pris_contalgin.columns[0]].tolist()


    list_datostr = []
    for i in range(len(varA)):
        DatoStr = varA[i].strftime("%d-%b-%Y")
        list_datostr.append(DatoStr)

    context = {"pris" :pris, "list_datostr": list_datostr}
    return(render(request, 'index.html', context))
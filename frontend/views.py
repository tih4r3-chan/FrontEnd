from django.shortcuts import render

# Create your views here.
# mostrar inicio
def registro(request):
    return render(request,'registro.html')
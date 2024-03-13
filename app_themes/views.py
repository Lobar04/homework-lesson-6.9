from django.shortcuts import render

# Create your views here.


def theme():
    with open(r'C:\Users\Nafisa\Desktop\LobarPython\m6-l9\app_themes\themes.txt', 'r') as theme:
        a = theme.read().split('\n')
        return a
def theme_table(request):

    return render(request,'theme_table.html',{'themes': theme()})


def main(request):
    return render(request,'main.html')
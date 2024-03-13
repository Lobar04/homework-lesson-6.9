from django.shortcuts import render

# Create your views here.
pupils_info = [['Nurbek Doniyorov',3,5,2,3,0,3,4,5,25],
               ['Boburmirzo Muhammadov',2,3,1,4,10,4,4,3,31],
               ['Fazliddin Asomov',3,5,2,4,10,4,4,3,35],
               ['Asadbek O\'ralov',2,5,1,2,10,3,4,3,30],
               ['Azizbek Aliyev',3,5,2,4,10,4,5,3,36],
               ['Murodjon Azimov',3,5,1,2,10,3,4,5,33]]

def pupils(request):
    return render(request,'pupils.html',{'pupils':pupils_info})


def pupil(request, pupil_id):
    pupil_id = int(pupil_id) - 1  # Adjust for zero-based indexing
    pupil_info = pupils_info[pupil_id]
    return render(request, 'pupil.html', {'pupil_info': pupil_info})
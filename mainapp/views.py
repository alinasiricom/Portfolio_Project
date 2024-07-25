from django.shortcuts import render

def index_view(request):
    context = {
        'full_name':'Ali Nasiri', 
        'job_title':'Back-end Developer',
        'email':'nasiri.ali.r@gmail.com',
        'Location':'Tehran',
        }
    return render(request, 'mainapp/index.html', context)

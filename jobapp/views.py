from django.shortcuts import render
import requests

def index(request):
    url = "https://indreed.herokuapp.com/api/jobs?q={}&l={}&country=ng&sort=date"
    params = request.GET
    
    job_title = params["title"] if params.get("title", None) else ''
    job_location = params["location"] if params.get("location", None) else ''
    if job_title or job_location:
        response = requests.get(url.format(job_title, job_location))
    else:
        url = "https://indreed.herokuapp.com/api/jobs?q={}&country=ng&sort=date"
        response = requests.get(url.format(job_title))
    job_list = response.json()


    context = {'job_list': job_list}
 
    
    return render(request,'index.html', context)
    
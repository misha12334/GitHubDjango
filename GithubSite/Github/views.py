from urllib.request import urlopen,Request

from django.shortcuts import render
from django.utils.baseconv import base64
import requests
from github import Github

def home(request):
    global user
    email=request.GET['email']
    password=request.GET['password']
    g = Github("mish.tchurkin@yandex.ru", "123123123123a")
    user = g.get_user()
    list_rep= user.get_repos()
    context = {
        'list_rep': list_rep,
        'user':user
    }

    #repo = user.get_repo("serPochta")
    #asddas = repo.get_archive_link("zipball")

    return render(request, 'Github/repo.html',context)

def download(request2):
    str_req = str(request2)
    name_repo =  request2.path[10:]
    name_repo=name_repo[:-2]
    repo = user.get_repo(name_repo)
    url_zip= repo.get_archive_link("zipball")
    r = requests.get(url_zip)
    req = Request(url_zip)

    webpage = urlopen(req)
    #f = open("C:/Users/Vladimir/Downloads/"+name_repo+".zip", 'wb')
    #f.write(r.content)
    #f.close()
    list_rep= user.get_repos()
    context = {
        'list_rep': list_rep,
        'user':user
    }
    return render(request2, 'Github/repo.html',context)

def auth(request):
    return render(request, 'Github/repo.html')

def git(request):
    return render(request, 'Github/git.html')



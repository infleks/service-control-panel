from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from theapp.models import Service


def index(req):
    return render(req, "index.html", {})

def servicedata(req):
    services = Service.objects.all()
    resj = {}

    if len(services)<1:
        resj["error"] = 1
        resj["message"] = "There is no service to show. Try to add one."
    else:
        servicesj = []
        for s in services:
            servicesj.append({
                'Id' : s.pk,
                'Name' : s.sname,
                'URL' : s.surl,
                'Database' : s.sdb,
                'Server' : s.ssrv,
                'Production' : s.sprod,
                'Status' : 'Unknown' # get service status
            })
        resj['services'] = servicesj
        resj['titles'] = ['Name', 'URL', 'Database', 'Server', 'Production', 'Status']
        resj['error'] = 0
        resj['message'] = "Successful."

    return JsonResponse(resj)

def saveservice(req):
    if req.method != "POST":
        return redirect("index")

    po = req.POST

    s = Service()
    s.sname = po['sname']
    s.surl = po['surl']
    s.suser = po['suser']
    s.spwd = po['spwd']
    s.sdb = po['sdb']
    s.ssrv = po['ssrv']
    s.sprod = po['sprod']

    s.save()

    return redirect("index")

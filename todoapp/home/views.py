from django.shortcuts import render

from todoapp.utils import http

def welcome(req):
    # context = {}
    # if req.user.is_authenticated():
    #     context["user"] = req.user

    return render(req, "home/index.html")
                  # context=context)

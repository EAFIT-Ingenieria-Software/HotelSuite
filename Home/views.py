from django.shortcuts import render

# Create your views here.


def index(request):
    template_data = {}
    template_data["title"] = "Home"

    return render(request, "index.html", {"template_data": template_data})

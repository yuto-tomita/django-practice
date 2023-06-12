from django.shortcuts import render

def index(request):
  context = {
    "property": "this is args"
  }

  return render(request, "todos/index.html", context)


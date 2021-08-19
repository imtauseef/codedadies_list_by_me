from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name="base.html")


def search(request):
    searched_things = request.POST.get('search')
    context = {
        'searched_things': searched_things,
    }

    return render(request, "home_app/search.html", context)
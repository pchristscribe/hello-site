from django.shortcuts import render
from django.views import View



# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(
            request,
            template_name = "hello_app.html",
        )
class HelloView(View):
    def get(self, request, name):
        return render(
            request,
            template_name='hello_name.html',
            context={'person': name},
        )

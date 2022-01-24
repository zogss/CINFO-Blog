from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



class RegisterView(TemplateView):
    def post(self, request):
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/blog')

        return render(request, 'cadastro.html', {'form_usuario': form_usuario})

    def get(self, request):
        form_usuario = UserCreationForm()

        return render(request, 'cadastro.html', {'form_usuario': form_usuario})
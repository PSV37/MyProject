from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render , redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Movie
from .forms import UserForms
from .login import LoginForms




class IndexView(generic.ListView):
	  template_name='App/index.html'
	  def get_queryset(self):
		  return Movie.objects.all()

class DetailView(generic.DetailView):
    model = Movie
    template_name = "App/detail.html"


class MovieAdd(CreateView):
    model = Movie
    fields = ['actor','movie_name','Praducer','Director','Catagory','movie_logo']
    



class MovieUpdate(UpdateView):
    model = Movie
    fields = ['actor','movie_name','Praducer','Director','Catagory','movie_logo']

 
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserFormView(View):
    form_class = UserForms
    template_name = 'App/Registration_form.html'

    def get(self,request):
	    form=self.form_class(None)
	    return render(request,self.template_name , {'form':form})

    def post(self,request):
       form = self.form_class(request.POST) 	

    
       if form.is_valid():
          user = form.save(commit=False)

          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user.set_password(password)
          user.save()
        

          #return user object if credentials are correct
          user = authenticate(username=username , password=password)

          if user is not None:
 
          	if user.is_active:
          		login(request,user)
          		return redirect('index')

       return render(request,self.template_name , {'form':form})

class UserLoginForm(View):
    form_class = LoginForms
    template_name = 'App/login.html'

    def get(self,request):
      form=self.form_class(None)
      return render(request,self.template_name , {'form':form})

    def post(self,request):
       form = self.form_class(request.POST)   

    
       if form.is_valid():
          user = form.save(commit=False)

          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user.set_password(password)
          user.save()
        

          #return user object if credentials are correct
          user = authenticate(username=username , password=password)

          if user is not None:
 
            if user.is_active:
              login(request,user)
              return redirect('index')

       return render(request,self.template_name , {'form':form})

       
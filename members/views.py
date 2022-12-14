#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#  template = loader.get_template('myfirst.html')
#  return HttpResponse(template.render())


#from django.http import HttpResponse
#from django.template import loader
#from .models import Members

#def index(request):
#  mymembers = Members.objects.all().values()
#  output = ""
#  for x in mymembers:
#    output += x["firstname"]
#  return HttpResponse(output)


from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members


def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('members/index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def add(request):
  template = loader.get_template('members/add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('members:index'))


def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('members:index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('members/update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('members:index'))


def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('members/info.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
from django.shortcuts import render, get_object_or_404
from .models import Position, Voters
from django.contrib.auth.decorators import login_required
#from django.db.models import Count
# Create your views here.

@login_required
def vote(request, position_id):
  message = ""
  total = 0
  

  position = get_object_or_404(Position, id=position_id)
  if request.user.voter.voted:
    message = "Sorry you cant vote more than once"
    
  else:
    position.votes += 1
    request.user.voter.voted = True
    request.user.voter.posit = position.name
    position.save()
    request.user.voter.save()
    message = "done"
    
    
  positions = Position.objects.all()
  #Getting total of all votes
  for pos in positions:
    total += pos.votes
    
    
  position.percentage = (position.votes/total) * 100
  position.save()
  positions = Position.objects.all()
  context = {
    'positions': positions,
    'message': message
   
  }
  return render(request, 'voting/index.html', context)

@login_required
def homepage(request):
  positions = Position.objects.all()
  context = {'positions': positions}
  return render(request, 'voting/index.html', context)
  
@login_required
def unvote(request):
  
  if not request.user.voter.voted:
    pass
  else:
    position = get_object_or_404(Position, name = request.user.voter.posit)
    position.votes -= 1 
    total = 0
  
    request.user.voter.voted = False
    position.save()
  
    positions = Position.objects.all()
  
    request.user.voter.save()
    for pos in positions:
      total += pos.votes
    
  
    position.percentage = (position.votes/total) * 100
    position.save()
  positions = Position.objects.all()
 
  context = {
    'positions': positions,
  
   
  }
  return render(request, 'voting/index.html', context)
  

#from django.db.models.signals import post_migrate
#from django.dispatch import receiver
#from .models import Team

#@receiver(post_migrate)
#def create_teams(sender, **kwargs):
 #   teams_to_create = ["MANAGEMENT", "SALES", "SUPPORT"]
  #  existing_teams = Team.objects.filter(name__in=teams_to_create).values_list("name", flat=True)
   # teams_to_create = [team for team in teams_to_create if team not in existing_teams]
    
   # for team_name in teams_to_create:
    #    team = Team(name=team_name)
     #   team.save()

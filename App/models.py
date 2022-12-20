from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
def is_mail_esprit(mail):
    if str(mail).endswith("@esprit.tn")==False:
        raise ValidationError("votre email est incorrect",params={'m':mail})
class User(models.Model):
    nom=models.CharField('Nom',max_length=255)
    prenom=models.CharField(max_length=255)
    email=models.EmailField(validators=[is_mail_esprit])
    def __str__(self):
        # return "Le nom est "+self.nom+"Le prénom est"+self.prenom
        return f"Le nom est {self.nom} le prenom est {self.prenom}"

class etudiant(User):
    groupe=models.CharField(max_length=255)
class coach(User):
    pass
class project(models.Model):
    nom_projet=models.CharField(max_length=255)
    duree_projet=models.IntegerField("Durée Estimée",default=0)
    etat=models.BooleanField(default=False)
    temps_alloue=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    membres=models.ManyToManyField(
        etudiant,
        related_name="les_projets",
        through='MembershipInProject'
    )
    createur=models.OneToOneField(
        etudiant,
        on_delete=models.SET_NULL,
        null=True
    )
    superviseur=models.ForeignKey(
        coach,
        on_delete=models.CASCADE
    )
class MembershipInProject(models.Model):
    projet=models.ForeignKey(project,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(etudiant,on_delete=models.CASCADE)
    time_allocated=models.IntegerField()




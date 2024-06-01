from django.db import models


class Hudud(models.Model):
    name = models.CharField(max_length=110, unique=True)


    def __str__(self) -> str:
        return self.name
    


class Qurilishtashkiloti(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    qachon_ttopgan = models.IntegerField()
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.name
    



class Qurilishbinosi(models.Model):
    qurilishtashkiloti = models.ForeignKey(Qurilishtashkiloti, on_delete=models.CASCADE)
    hudud_id = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, unique=True)
    maydoni_kv = models.IntegerField()
    qavat = models.IntegerField()
    parkovkasi = models.BooleanField(default=False)
    kindergarden = models.BooleanField(default=False)
    lift = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name
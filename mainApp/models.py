from django.db import models


class Davlat(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Club(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='clublar/', blank=True, null=True)
    prezident = models.CharField(max_length=255, blank=True)
    murabbiy = models.CharField(max_length=255, blank=True)
    t_sana = models.DateField(blank=True, null=True)
    top_transfer = models.TextField(blank=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True)
    kapital = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Player(models.Model):
    ism = models.CharField(max_length=255, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True)
    narx = models.PositiveSmallIntegerField(blank=True, null=True)
    t_yil = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ism


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    club_eski = models.ForeignKey(Club, on_delete=models.SET_NULL, related_name='eskilar', null=True)
    club_yangi = models.ForeignKey(Club, on_delete=models.SET_NULL, related_name='yangilar', null=True)
    narx = models.PositiveSmallIntegerField(blank=True, null=True)
    taxmin_narx = models.PositiveSmallIntegerField(blank=True, null=True)
    sana = models.DateField(blank=True, null=True)
    mavsum = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.player.ism}: ({self.club_eski.nom} - {self.club_yangi})"

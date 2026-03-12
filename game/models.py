from django.db import models


# Create your models here.
class Monster ( models.Model ) :
    TYPE_CHOICES = (
        (1, "炎属性"),
        (2, "水属性"),
        (3, "闇属性"),
    )
    
    name = models.CharField(
        max_length=100
    )
    hp = models.IntegerField(
        default=0
    )
    mp = models.IntegerField(
        default=0
    )
    type = models.IntegerField(
        choices=TYPE_CHOICES
    )

    def __str__(self):
        s = "<Monster " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "HP=" + str(self.hp) + " " + \
            "MP=" + str(self.mp) + " " + \
            "タイプ=" + self.get_type_display() + " " + \
            ">"
        return s
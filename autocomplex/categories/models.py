from django.db import models

class Details(models.Model):
    TYPES= (
        ('moscow_detail','москвич'),
        ('sliva_detail','слива'),
        ('volga_detail','волга'),
    )

    title= models.CharField(max_length=20,verbose_name='Название')
    image= models.ImageField(blank= True, verbose_name= 'Фото', upload_to= 'categories/')
    option= models.CharField(max_length=20, choices=TYPES, verbose_name="Категория")

    def __str__(self):
        return self.title



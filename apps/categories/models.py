from django.db import models

from apps.users.models import CustomUser as User 


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Макаланын категориясы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Макаланын категориясы'
        verbose_name_plural = 'Макаланын категориялары'
        
        
class SearchHistory(models.Model):
    query = models.CharField(max_length=350, verbose_name='Издоонун сурамы')
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history', verbose_name='Каттоочулар')
    
    def __str__(self) -> str:
        return self.query
    
    
    class Meta:
        verbose_name = 'Издоонун сурамы'
        verbose_name_plural = 'Издоонун сурамдары'

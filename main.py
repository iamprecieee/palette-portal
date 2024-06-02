from django.db.models import TextChoices, Choices


class Type(TextChoices):
        LIMITED = ('LT', 'limited')
        OPEN = ('OP', 'open edition')
        SINGULAR = ('SI', '1/1')
        
     
     
Choices = list(Type)   
print(Type.choices)
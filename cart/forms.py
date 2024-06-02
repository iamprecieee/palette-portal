from django.forms import Form, TypedChoiceField, BooleanField, HiddenInput


class CartUpdateForm(Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    quantity = TypedChoiceField(coerce=int, choices=QUANTITY_CHOICES)
    override = BooleanField(required=False, initial=False,
                            widget=HiddenInput)
from django.forms import ModelForm
from .models import Cart
#
# class CartAddForm(ModelForm):
#     class Meta:
#         model = Cart
#         fields = ['count', 'user', 'product']
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #
#     # def add_fields(self, **kwargs):
#     #     for key, value in kwargs.items():
#     #         self.fields[key] = value
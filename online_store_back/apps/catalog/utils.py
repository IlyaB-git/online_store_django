from .models import Category

class CategoriesList:
    def get_extra_context(self, **kwargs):
        context = kwargs
        context['catalog_categories'] = Category.objects.all()
        return context

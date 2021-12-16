from django.views.generic import TemplateView

class IndexView(TemplateView):
    def get_template_names(self):
        return 'index.html'
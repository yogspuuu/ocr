from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from utils.process import *
import base64

# Create your views here.
@require_http_methods(["POST"])
def predict_image(request):
    if request.method == "POST":
        imgB64 = request.POST["image"]
        filename = b64_to_image(imgB64)
        return HttpResponse(get_text(filename, remove=REMOVE_AFTER_PREDICTION))
        

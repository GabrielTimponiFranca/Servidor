from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def teste(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response("Ola mundo rest!")
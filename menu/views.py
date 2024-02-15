from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


# Create your views here.
# functional approach
# def item_list(request):
#     items = Item.objects.all() # QueryObj 
#     my_list = []
#     # QueryObj => Python List[dictionary]
#     for item in items:
#         my_list.append({
#             "name":item.name,
#             "price":item.price,
#             "description":item.description,

#         })
#     #return JsonResponse(my_list, safe=False)
#     return JsonResponse({'menu_items': my_list})

# Using REST framework Response
@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



# Serialization - change data types into other data types
def item_list_serialized(request):
    items = Item.objects.all() 
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

# we need api_view decorator
@api_view(['GET'])
def item_detail(request, itemId):
    item = Item.objects.get(id=itemId)
    serializer = ItemSerializer(item)
    # Django Rest framework comes with Response
    return Response(serializer.data)
    
# alternatively, we can use APIView 
class ItemDetailView(APIView):
    def get(self, request, itemId):
        item = Item.objects.get(id=itemId)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
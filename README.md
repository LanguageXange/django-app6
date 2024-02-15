# Django & REST framework

A nice and short introduction to how Django REST framework works!

https://www.django-rest-framework.org/
https://www.django-rest-framework.org/api-guide/responses/
https://www.django-rest-framework.org/api-guide/serializers/

## Return Data in JSON format with `JsonResponse`

```python
from django.http import JsonResponse

def item_list(request):
    items = Item.objects.all()
    return JsonResponse(items, safe=False)
```

**HOWEVER, we will see this error**
`Object of type QuerySet is not JSON serializable`

### Solution #1 - Transform QueryObj into a List of Dictionary

```python
def item_list(request):
    items = Item.objects.all() # QueryObj
    my_list = []
    for item in items:
        my_list.append({
            "name":item.name,
            "price":item.price,
            "description":item.description,

        })
    return JsonResponse(my_list, safe=False)

```

### Solution #2 - Django REST framework & `serializers`

- `pip install djangorestframework`
- Add `rest_framework` to `INSTALLED_APPS` in `settings.py`
- Create a `serializers.py` file

```python
from rest_framework import serializers
from .models import Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

```

- In our `views.py` file

```python
def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

```

## Single Item Detail View with REST framework `Response` & `api_view`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def item_detail(request, itemId):
    item = Item.objects.get(id=itemId)
    serializer = ItemSerializer(item)
    # Django Rest framework comes with Response
    return Response(serializer.data)

```

`python manage.py runserver`

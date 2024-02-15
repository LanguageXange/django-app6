from django.urls import path 


from .views import item_list,item_list_serialized,item_detail,ItemDetailView


urlpatterns = [
    path('', item_list, name="home"),
    path('drf/',item_list_serialized, name="drf"),
    path('<int:itemId>/',item_detail, name="detail"), #api_view
    path('item/<int:itemId>/',ItemDetailView.as_view(), name="detail-view"), # APIView
]

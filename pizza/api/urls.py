from django.urls import path
from api import views as v

urlpatterns = [
path('',v.apiOverview,name=''),
path('pizza-list/',v.pizzaList,name='pizza-list'),
path('pizza-detail/<str:pid>/',v.pizzaDetail,name='pizza-detail'),
path('pizza-create/',v.pizzaCreate,name='pizza-create'),
path('pizza-update/<str:pid>/',v.pizzaUpdate,name='pizza-update'),
path('pizza-delete/<str:pid>/',v.pizzaDelete,name='pizza-delete'),
path('pizza-filter/type/<str:ptype>',v.pizzaFilterbyType,name='pizza-filter'),
path('pizza-filter/size/<str:psize>',v.pizzaFilterbySize,name='pizza-filter'),
]
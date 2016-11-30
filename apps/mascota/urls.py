from django.conf.urls import url
from apps.mascota.views import index,mascota_view,mascota_list,mascota_edit,mascota_delete
from apps.mascota.views import MascotaList,MascotaCreate

urlpatterns = [
    url(r'^$', index,name='index'),
    #url(r'nuevo$',mascota_view,name='mascota_crear'),
    url(r'nuevo$',MascotaCreate.as_view(),name='mascota_crear'),
    #url(r'listar',mascota_list,name="mascota_listar"),
    url(r'listar$',MascotaList.as_view(),name="mascota_listar"),
    url(r'^editar/(?P<id_mascota>\d+)/$',mascota_edit,name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$',mascota_delete,name='mascota_eliminar')
]
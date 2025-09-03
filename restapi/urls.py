from django.urls import path

from restapi.views import PostComputerHardwareView, GetAllComputerHardwareView, DeleteByComputerHardwareIdView, \
    GetByComputerHardwareId, UpdateByComputerHardwareId, SearchFilterByIdOrNameView

urlpatterns = [
    path('create/', PostComputerHardwareView.as_view()),
    path('get/', GetAllComputerHardwareView.as_view()),
    path('delete/', DeleteByComputerHardwareIdView.as_view()),
    path('get_id/', GetByComputerHardwareId.as_view()),
    path('update/', UpdateByComputerHardwareId.as_view()),
    path('search/', SearchFilterByIdOrNameView.as_view())
]
from django.conf.urls import url,include
from Basic_app import views

# TEMPLATE TAGGING:

app_name='Basic_app'

urlpatterns =[
    url(r'^other/$',views.other, name='other'),
    url(r'^relative_url/$',views.relative_url,name='relative_url')
    
]

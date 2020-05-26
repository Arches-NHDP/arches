from django.urls import path

from . import views
from . import glossary_form

urlpatterns = [
	path('', views.index, name="index"),
	path('enter/', views.enterGLOSSARY),
	path('like_category/', views.like_category, name='like_category'),
	path('api/vocab/<str:word>/', views.getWordDefinition),
	path('api/vocablist/<str:word>/', views.returnVocList),
	path('vocablist/', views.showVoc),
	path('vocablist/<str:word>/', views.showDetail),
	path('glossary/test/', glossary_form.test),
	path('glossary/list/', glossary_form.list_terms),
	path('glossary/update/', glossary_form.update_terms),
	path('glossary/do_update/', glossary_form.do_update_terms),
	path('glossary/add/', glossary_form.add_terms),
	path('glossary/upload/', glossary_form.upload_terms),
	path('glossary/remove/', glossary_form.remove_terms),
	path('glossary/glossaries/', glossary_form.glossary_listing),
	path('glossary/img_picker/', glossary_form.easydb_imagepicker),
]
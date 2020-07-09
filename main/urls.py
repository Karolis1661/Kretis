from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, single_article, articles, websites, e_shop, design, contacts, calculator, projects, single_project


urlpatterns = [
    path('', home_page, name='home_page'),
    path('straipsniai/', articles, name='articles'),
    re_path(r'straipsniai/(?P<url>\w+)', single_article, name='single_article'),
    path('svetaines', websites, name='websites'),
    path('elektroninės_parduotuves', e_shop, name='e_shop'),
    path('dizainas', design, name='design'),
    path('kontaktai', contacts, name='contacts'),
    path('skaiciuokle', calculator, name='calculator'),
    path('projektai', projects, name='projects'),
    re_path(r'projektai/(?P<client>\w+)', single_project, name='single_project'),
]
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

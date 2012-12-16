from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^portfolio/', include('portfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portfolio.views.home'),
    url(r'^album', 'portfolio.views.render_album'),
    url(r'^getimage', 'portfolio.views.get_image'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# static serving
# comme c'est nginx qui sert le contenu static vue du web, en local
# ca marche pas car on passe directement par gunicorn qui lui ne peut pas
# servir de contenu static, on laisse donc django le faire lui meme :/



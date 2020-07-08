from django.contrib import admin

from main.models import Article, ArticleCategory, ClientRequest, WebRequest, EshopRequest, DesignRequest, Projects

admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(ClientRequest)
admin.site.register(WebRequest)
admin.site.register(EshopRequest)
admin.site.register(DesignRequest)
admin.site.register(Projects)

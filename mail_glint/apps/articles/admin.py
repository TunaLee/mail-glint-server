from django.contrib import admin

from mail_glint.apps.articles.models.index import Article, ArticleTag, ArticleCategory, HumanArticle, Episode
from mail_glint.bases.admin import Admin
from mail_glint.bases.inlines import StackedInline


class EpisodeInline(StackedInline):
    model = Episode
    fieldsets = (
        ("Episode", {"fields": ('number', 'name', 'thumbnail', 'subtitle', 'content')}),
    )
    extra = 0


@admin.register(ArticleCategory)
class ArticleCategoryView(Admin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        ("정보", {"fields": ('name',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name',)}),
    )


@admin.register(ArticleTag)
class ArticleTagView(Admin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        ("정보", {"fields": ('name',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name',)}),
    )


@admin.register(Article)
class ArticleView(Admin):
    list_display = ('category', 'author', 'title')
    search_fields = ('category', 'author', 'title')
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('category', 'author', 'title', 'subtitle', 'content', 'tags', 'thumbnail')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('category', 'author', 'title', 'subtitle', 'content', 'tags', 'thumbnail')}),
    )


@admin.register(HumanArticle)
class HumanArticleView(Admin):
    list_display = ('title', 'name')
    search_fields = ('title', 'name')
    readonly_fields = ('',)
    inlines = (EpisodeInline,)

    fieldsets = (
        ("정보", {"fields": ('title', 'subtitle', 'name', 'content', 'thumbnail')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('title', 'subtitle', 'name', 'content', 'thumbnail')}),
    )

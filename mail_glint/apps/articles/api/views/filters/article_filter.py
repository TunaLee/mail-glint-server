# Django
import django_filters
from django_filters import CharFilter, NumberFilter, RangeFilter


# Models
from mail_glint.apps.articles.models.index import Article, HumanArticle


class ArticlesFilter(django_filters.FilterSet):
    title = CharFilter(field_name='name', lookup_expr='icontains')
    category_id = NumberFilter(field_name='category_id')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    class Meta:
        model = Article
        fields = ['title', 'category_id', 'author', 'is_active']

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)


# class HumanArticlesFilter(django_filters.FilterSet):
#     number = CharFilter(field_name='episodes__number', method='number_filter')
#     class Meta:
#         model = HumanArticle
#         fields = ['number']
#
#     def number_filter(self, queryset, name, value):
#         return queryset.filter(article__number=value)


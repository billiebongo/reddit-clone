import logging

logger = logging.getLogger(__name__)
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 30


from rest_framework import pagination


class FivePaginationLimitOffset(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class TenPaginationLimitOffset(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class FivePaginationPageNumber(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'


class TenPaginationPageNumber(pagination.PageNumberPagination):
    page_size = 10

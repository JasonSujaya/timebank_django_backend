from rest_framework import pagination


class PostPaginationLimitOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    max_limit = 2


class PostPaginationPageNumber(pagination.PageNumberPagination):
    page_size = 3

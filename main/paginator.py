from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 100

    def get_page_size(self, request):
        if request.query_params.get("page") or request.query_params.get(
            self.page_size_query_param
        ):
            page_size = min(
                int(
                    request.query_params.get(self.page_size_query_param, self.page_size)
                ),
                self.max_page_size,
            )
            if page_size > 0:
                return page_size
            elif page_size == 0:
                return None
            else:
                pass
        else:
            return None
        return self.page_size

    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.page.paginator.count,
                "pages": self.page.paginator.num_pages,
                "data": data,
            }
        )

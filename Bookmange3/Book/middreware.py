class TestMiddreware():

    def __init__(self):
        pass

    def process_request(self, request):
        print('--------------request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('--------------view')

    def process_template_response(self, request, response):
        print('--------------template')
        return response

    def process_response(self, request, response):
        print('--------------response')
        return response
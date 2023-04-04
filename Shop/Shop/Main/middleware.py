import time


def simple_middleware(get_response):

    def middleware(request):
        t1 =time.time()
        request.hello = t1
        response = get_response(request)
        t2 = time.time()
        print(f'Time is {t2-t1}')
        return response

    return middleware
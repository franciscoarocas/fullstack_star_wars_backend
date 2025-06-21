
import httpx

def build_fake_response(response_data):

    def _factory(*args, **kwargs):
      url = args[0] if args else "" # Assuming the first argument is the URL
      req = httpx.Request("GET", url)
      return httpx.Response(200, json=response_data, request=req)

    return _factory


def build_fake_response_error(status_code=503):
    def _factory(url):
        req = httpx.Request("GET", url)
        return httpx.Response(status_code, request=req)

    return _factory
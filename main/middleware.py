class AllowCredentialsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求逻辑

        response = self.get_response(request)
        # 设置 Access-Control-Allow-Credentials 头部
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'

        return response

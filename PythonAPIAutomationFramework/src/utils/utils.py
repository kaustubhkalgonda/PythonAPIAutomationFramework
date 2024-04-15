class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_put_delete_basic_auth(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }
        return headers

    def common_headers_put_delete_cookie(token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
            "Accept":"application/json"
        }
        return headers
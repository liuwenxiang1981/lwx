# import urllib.request
# import urllib.parse
# # para = {"joker":"hahah","joker2":"huhu"}

# # data = bytes(urllib.parse.urlencode({(para),encoding='utf8'}))
# url ='http://www.17k.com/chaper/2933095/36699279.html'
# response =urllib.request.urlopen(url)
# # response = urllib.request.urlopen(url)
# print(response.read().decode())
import urllib.request
import urllib.parse
def main():
# data = urllib.parse.urlencode({parameters)
    request_ = urllib.request.Request(url='http://www.17k.com/chapter/2933095/36699279.html',method="GET")
    response = urllib.request.urlopen(request_)
# print(response.url)
    HTML=response.read().decode('utf8')
    with open("/home/weifang/Desktop/liuwenxiang/test.txt",mode='w') as f:
        f.write(HTML)
main()

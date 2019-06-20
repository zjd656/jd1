import urllib.request
headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
url='http://wwww.hao123.com/get'
w = {'http://114.230.30.238:808','http://183.185.25.152:9797 ','http://27.184.131.187:8888'}
for wl in w:
    try:
        proxy_handle = {'http':'w'}
        proxy = urllib.request.ProxyHandler(proxy_handle)
        print('%s 爬取成功'%wl)
    except:
        response !=200：
        print('%s 爬取失败'%wl)
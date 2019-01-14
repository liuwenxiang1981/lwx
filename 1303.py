import requests
# def get_imageNet_data(path):
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
response = requests.get('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808',headers=headers)

ImageUrls = response.text
split_urls = ImageUrls.split('\r\n') 
for url in split_urls:
    try:
        picture = requests.get(url,headers=headers,timeout=3,allow_redirects=False)
    except Exception as i:
        print(i)
    else:
        # picture = requests.get(url=url,headers=headers)
        imageName = url.split('/')[-1]
        with open('/home/weifang/Desktop/liuwenxiang/{}.jpg'.format(imageName),mode='wb') as f:
            f.write(picture.content)


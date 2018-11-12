# -*-coding:utf-8-*-
import requests
import json
from urllib.request import urlretrieve


def download_image(url):
    header = {
        'Referer': 'https://cn.bing.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    try:
        res = requests.get(url,headers=header)
        #print(res.text)
        #print(res.status_code)
        result = json.loads(res.text)['images']
        #print(result)
        for item in result:
            print(item)
        #print(result[0]['copyright'])
        #print(result[0]['url'])
        download_url = "https://cn.bing.com"+result[0]['url']
        #print(download_url)
        image = requests.get(download_url)
        image_name = result[0]['copyright']
        #print(image_name.split('，')[0].split('‘')[0])
        name = image_name.split('，')[0].split('‘')[0]
        #with open('%s.jpg'%name,'wb') as f:
        #    f.write(image.content)
        #    print("下载完成")
    except:
        print("获取数据失败")

if __name__ == "__main__":
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=3"
    download_image(url)    

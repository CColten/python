# -*-coding:utf-8-*-
############################################
# Program: 用于下载必应壁纸                   #
# History: 2017.11.12                      #
# author: CTS                              #
# version: Second release                  #
############################################
import requests
import json


def getImageUrl(url):
    header = {
        'Referer': 'https://cn.bing.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    try:
        image_dict={}
        res = requests.get(url,headers=header)
        result = json.loads(res.text)['images']
        #download_url = "https://cn.bing.com"+result[0]['url']
        for item in result:
            #print(item)
            image_name = item['copyright'].split('(')[0]
            image_url = "https://cn.bing.com"+item['url']
            print(image_url)
            image_dict[image_name] = image_url
        #print(image_dict)
        return image_dict
    except:
        print("获取数据失败")

def download_image(image_dict):
    try:
        for item in image_dict:
            downlaod_url = image_dict[item]
            image = requests.get(downlaod_url)
            image_name = item
            with open('%s.jpg'%image_name,'wb') as f:
                f.write(image.content)
                string = "下载完成    " + "%s"%image_name
                print(string)
    except:
        print("下载失败")

if __name__ == "__main__":
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=7"
    image_dict = getImageUrl(url)    
    download_image(image_dict)


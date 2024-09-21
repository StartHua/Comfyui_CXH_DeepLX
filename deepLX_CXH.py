
import os
import requests
import json

from PyDeepLX import PyDeepLX

current_folder = os.path.dirname(os.path.abspath(__file__))
key_json = os.path.join(current_folder, "key.txt")

class CXH_DeepLX_Free:
 
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""},),
                "source":   (["ZH","EN"],{"default":"ZH"} ),
                "target":   (["ZH","EN"],{"default":"EN"} ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH/DeepLX"

    def gen(self, text:str,source,target):
        try:
            outStr = PyDeepLX.translate(text, source, target) 
        except :
            outStr = PyDeepLX.translate(text, source, target)     
            
        return(outStr,)

class CXH_DeepLX_translate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""},),
                "source": (["auto", "ZH中文","EN英语","DE德语","JA日语"],{"default":"auto"}),
                "target":  (["ZH中文","EN英语","DE德语","JA日语"],{"default":"EN英语"}),
                "proxy":("STRING", {"multiline": False, "default": "https://deeplx.missuo.ru/translate?key="},),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH/DeepLX"

    def gen(self, text:str,source,target,proxy):
        result = ""
        with open(key_json, 'r', encoding='utf-8') as file:  
            # 读取文件内容  
            key = file.read()  
            # 打印文件内容  
            print(key)  
        
        if key == None or key =="":
            print("key == None")

        url = proxy + key
        if target !="auto":
            target = target[:2]

        try:
            payload = json.dumps({
            "text": text,
            "source_lang": source,
            "target_lang": target
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            # 检查请求是否成功  
            if response.status_code == 200:  
                # 将响应的JSON内容解析为Python字典  
                data = response.json()  
                # 从字典中获取alternatives  
                result = data.get('data', " ")  
            else:  
                print("请求失败，状态码：", response.status_code)
                result= response.status_code
        except :
            result="error"
                        
        return(result,)

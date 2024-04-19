
import os

from PyDeepLX import PyDeepLX

class deepLX_CXH:
 
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
    CATEGORY = "CXH"

    def gen(self, text:str,source,target):
        try:
            outStr = PyDeepLX.translate(text, source, target) 
        except :
            outStr = PyDeepLX.translate(text, source, target)     
            
        return(outStr,)

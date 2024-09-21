from .deepLX_CXH import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "CXH_DeepLX_Free":CXH_DeepLX_Free,
    "CXH_DeepLX_translate":CXH_DeepLX_translate
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CXH_DeepLX_Free":"CXH_DeepLX_Free",
    "CXH_DeepLX_translate":"CXH_DeepLX_translate"
}

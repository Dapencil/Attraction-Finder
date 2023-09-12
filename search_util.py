from serpapi import GoogleSearch
import numpy as np

class SearchUtil:
    def __init__(self,api_key):
        self.key = api_key
    
    def search_img(self,query):
        image_results = []
        check_list = []
        params ={
        "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
        "q": query,                       # search query
        "tbm": "isch",                    # image results
        "num": "50",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": self.key,  
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        print("Search Finished")
        if "error" not in results:
            for image in results["images_results"]:
                if image["original"] not in check_list:
                    image_results.append({
                        'src' :  image["original"],
                        'width' : image["original_width"],
                        'height' : image["original_height"]
                    })
                    check_list.append(image["original"])
        
        return image_results
    
    def get_image_of(self,query,width,height,ratio):
        print("Getting Image :",query)
        unfilter_imgs = self.search_img(query)
        filter_size = [image for image in unfilter_imgs if image['width'] > width and image['height'] > height and image['width'] > image['height']]
        filter_ratio = [image for image in filter_size if abs(image['width']/image['height'] - ratio) < 1]

        if len(filter_ratio) == 0 :
            return {
                "src" : "https://eagle-sensors.com/wp-content/uploads/unavailable-image.jpg"
            }
        else:
            flag = True
            while flag:
                index = np.random.randint(1,5)
                if index < len(filter_ratio):
                    flag = False
            
            image = filter_ratio[index]
            return image


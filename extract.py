import urllib2 
import json as js

def extract_labels():
    galax_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/local_groups')
    galax_info = galax_url.read()
    galax_params = js.loads(galax_info)
    label= []
    
    for i in galax_params:
         label.append(i['label'])
    
    return label


def extract_distly(c):
    galax_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/local_groups')
    galax_info = galax_url.read()
    galax_params = js.loads(galax_info)
    distance = []
    
    for i in galax_params:
        distance.append(i['distly'])
    
    return distance
    


#print extract_distly("M 32")
# def galax_dict():
#     label_list = extract.extract[0] 
#     dist_list = extract.extract[1]
    
    




import numpy as np
from pathlib import Path
import os
import yaml

#split 
#make data generator based on data, crate folder with data and 
#write test to check - read what items are expected on that day
#check what items expected and check if files with that data are fetched
#check if all columns are like in template
#check if are exist


def load_file()->dict:
    p = Path(os.getcwd())
    #print(p.parent)
    with open(os.path.join(p.parent,'incoming_data','const_config.yaml')) as stream:
        try:
            dict_for_config =yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dict_for_config

def process_config(dict_for_config):
    types_in_dict = dict_for_config['cfg_setup']

    


def check_if_file_exist():
    numer_of_data_generated = 10
    np.random.seed(8)
    expected_product_list = ['Pork','Beef','Wheat Products']        
    columns_from_client=['consumption','wh_stock']


d =load_file()
print(d)
process_config(d)
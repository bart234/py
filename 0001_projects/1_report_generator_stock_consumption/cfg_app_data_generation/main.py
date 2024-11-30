import numpy as np
import pandas as pd
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



class ProcessConfig:
    def __init__(self,dict_for_config) -> None:
        self.types_in_dict = dict_for_config['cfg_setup']
        self.types_in_dict = dict_for_config['products']
        self.wh_stock = None
        self.consumption = None

    class Product:
        def __init__(self, name, wh_stock,consumption) -> None:
            self.name =name
            self.wh_stock = wh_stock
            self.consumption=consumption
        #TODO: finish class and do preparing  functions
    def prepare_wh_stock_and_consumption():
        wh_stock =pd.DataFrame({self._consumption_data_cols[0]:[2,22,222],
                                                   self._consumption_data_cols[1]:[5,50,500]},index=self._product_list)


self._wh_stock_consumption = pd.DataFrame({self._consumption_data_cols[0]:[2,22,222],
                                                   self._consumption_data_cols[1]:[5,50,500]},index=self._product_list)

        
self._order_data_cols=['orders','days_to_stock']    #columns from order data 
self._client_data_ord_pork =pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=1,high=8,size=self._size_of_generated_arr),
                                            self._order_data_cols[1]:np.random.randint(low=2,high=8,size=self._size_of_generated_arr)})
self._client_data_ord_beef=pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=5,high=45,size=self._size_of_generated_arr),
                                            self._order_data_cols[1]:np.random.randint(low=2,high=18,size=self._size_of_generated_arr)})
self._client_data_ord_wheat =pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=45,high=745,size=self._size_of_generated_arr),
                                            self._order_data_cols[1]:np.random.randint(low=2,high=22,size=self._size_of_generated_arr)})

    


def check_if_file_exist():
    numer_of_data_generated = 10
    np.random.seed(8)
    expected_product_list = ['Pork','Beef','Wheat Products']        
    columns_from_client=['consumption','wh_stock']


d =load_file()
print(d)
p = ProcessConfig(d)
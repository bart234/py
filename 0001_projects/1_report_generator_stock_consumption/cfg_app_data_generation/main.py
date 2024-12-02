import numpy as np
import pandas as pd
from pathlib import Path
import os
import yaml
from dataclasses import dataclass

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


class Product:
    name: str
    consumption: int
    wh_stock: int
    gen_orders:list
    gen_consumption:list

class ProcessConfig:
    def __init__(self,dict_for_config) -> None:
        self.cfg_setup_in_dict = dict_for_config['cfg_setup']
        self.product_in_dict = dict_for_config['products']
        self.product_list = [k for k in self.product_in_dict.key()]
        self.product_list_and_cfg = []
        for k,v in self.product_in_dict.items():
            p =Product(k,
                        v['base_wh_consumption'],
                        v['base_wh_stock'],
                        v['base_boundry_for_generate_orders_down'],
                        v['base_boundry_for_generate_consumption_up'])
            self.product_list_cfg.append(p)

    def PrepareConsumptionAndStockTable(self)->pd.DataFrame:
        self.wh_stock =pd.DataFrame({self._consumption_data_cols[0]:[2,22,222],
                                self._consumption_data_cols[1]:[5,50,500]},index=self._product_list)

    def PrepareDataForEachProduct(self)->list:
        pass



  


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
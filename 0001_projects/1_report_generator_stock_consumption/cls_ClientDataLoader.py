import pandas as pd
import numpy as np
import datetime

class ClientDataLoader:
    def __init__(self):        
        self._size_of_generated_arr = 10
        np.random.seed(8)
        
        #data which will be loadad from files
        self._product_list = ['Pork','Beef','Wheat Products']
        self._wh_stock_consumption = pd.DataFrame({'consumption':[2,22,222],'wh_stock':[5,50,500]},index=self._product_list)
        self._client_data_ord_pork =pd.DataFrame({'orders':np.random.randint(low=1,high=8,size=self._size_of_generated_arr),'days_to_stock':np.random.randint(low=2,high=8,size=self._size_of_generated_arr)})
        self._client_data_ord_beef=pd.DataFrame({'orders':np.random.randint(low=5,high=45,size=self._size_of_generated_arr),'days_to_stock':np.random.randint(low=2,high=18,size=self._size_of_generated_arr)})
        self._client_data_ord_wheat =pd.DataFrame({'orders':np.random.randint(low=45,high=745,size=self._size_of_generated_arr),'days_to_stock':np.random.randint(low=2,high=22,size=self._size_of_generated_arr)})

        #columns strings 
        self._client_data_column__orders='orders'
        self._client_data_column__days_to_stock='days_to_stock'
        self._client_consumption_data_column__consumption='consumption'
        self._client_consumption_data_column__wh_stock='wh_stock'
        self._client_consumption_data_column__item='Item'

    #--------------------------------------- getters -------------------------------------
    def get_client_data_dict_item_data(self)->dict:
        return {self._product_list[0]:self._client_data_ord_pork ,self._product_list[1]:self._client_data_ord_beef ,self._product_list[2]:self._client_data_ord_wheat}  
    def get_client_product_list(self)->list:return self._product_list
    def get_client_column_from_raw_data__orders(self)->str:return self._client_data_column__orders  
    def get_client_column_from_raw_data__days_to_stock(self)->str:return self._client_data_column__days_to_stock  
    def get_client_column_from_consumption__consumption(self)->str:return self._client_consumption_data_column__consumption  
    def get_client_column_from_consumption__wh_stock(self)->str:return self._client_consumption_data_column__wh_stock  
    def get_client_column_from_consumption__item(self)->str:return self._client_consumption_data_column__item  
    def get_client_data_consumption(self)->pd.DataFrame:return self._wh_stock_consumption

import pandas as pd
import numpy as np
import datetime

class ClientDataLoader:
    def __init__(self):        
        self._size_of_generated_arr = 10
        np.random.seed(8)
        
        #data which will be loadad from files
        self._product_list = ['Pork','Beef','Wheat Products']        
        self._consumption_data_cols=['consumption','wh_stock']  #columns from consumption data 
        self._wh_stock_consumption = pd.DataFrame({self._consumption_data_cols[0]:[2,22,222],
                                                   self._consumption_data_cols[1]:[5,50,500]},index=self._product_list)

        
        self._order_data_cols=['orders','days_to_stock']    #columns from order data 
        self._client_data_ord_pork =pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=1,high=8,size=self._size_of_generated_arr),
                                                  self._order_data_cols[1]:np.random.randint(low=2,high=8,size=self._size_of_generated_arr)})
        self._client_data_ord_beef=pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=5,high=45,size=self._size_of_generated_arr),
                                                 self._order_data_cols[1]:np.random.randint(low=2,high=18,size=self._size_of_generated_arr)})
        self._client_data_ord_wheat =pd.DataFrame({self._order_data_cols[0]:np.random.randint(low=45,high=745,size=self._size_of_generated_arr),
                                                   self._order_data_cols[1]:np.random.randint(low=2,high=22,size=self._size_of_generated_arr)})

        #additional column used in futher process 
        self._client_consumption_data_column__item='Item'

    #--------------------------------------- getters -------------------------------------
    def get_client_product_list(self)->list:return self._product_list

    def get_client_data_dict_item_data(self)->dict:
        return {self._product_list[0]:self._client_data_ord_pork ,self._product_list[1]:self._client_data_ord_beef ,self._product_list[2]:self._client_data_ord_wheat}      

    def get_client_column_from_raw_data__orders(self)->str:return self._order_data_cols[0]  
    def get_client_column_from_raw_data__days_to_stock(self)->str:return self._order_data_cols[1]  

    def get_client_column_from_consumption__consumption(self)->str:return self._consumption_data_cols[0]  
    def get_client_column_from_consumption__wh_stock(self)->str:return self._consumption_data_cols[1]  

    def get_client_column_from_consumption__item(self)->str:return self._client_consumption_data_column__item  
    def get_client_data_consumption(self)->pd.DataFrame:return self._wh_stock_consumption

    #--------------------------------------- data loader ----------------------------------

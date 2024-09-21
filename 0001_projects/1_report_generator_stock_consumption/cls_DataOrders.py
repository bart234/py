import numpy as np
import pandas as pd
import datetime
import cls_ConfigAndData as ConfigAndData

class DataOrders:
    ''' it load data from sources item: df - concat all together, manipulate and keep as one tab
    to access use get_data_for_item(item)
    '''
    def __init__(self, cfg: ConfigAndData.ConfigAndData, dict_item_data:dict):
        #-------------------------- variables ------------------------------------
        self._column_name__delivery_date = cfg.get_column_name__delivery_date()
        self._column_name__item = cfg.get_column_name__item()
        self._column_name__days_to_stock = cfg.get_column_name__days_to_stock()

        #-------------------------- structs --------------------------------------
        self._item_list = list(dict_item_data.keys())
        self._orders_tab=pd.DataFrame
        self._grupped_by_day_item=pd.DataFrame
        
        #-------------------------- functions ------------------------------------
        self._create_order_df_with_all_items(dict_item_data)
        self._add_current_date_to_today_orders()        
        self._convert_number_into_date_plus_offset()
        self._sort_by_items_and_dates()
        self._group_sum_order_by_item_and_day()
        

        
    def print_report(self):
            print(self._orders_tab.to_string())

    def _create_order_df_with_all_items(self,dict_item_data:dict):
        for k,v in dict_item_data.items():
            v[self._column_name__item]=k
        self._orders_tab = pd.concat(list(dict_item_data.values()))
    
    def _add_current_date_to_today_orders(self):
        self._orders_tab[self._column_name__delivery_date]=datetime.datetime.today().date()
    
    def _add_diffrent_date_to_today_orders(self,year_:int,month_:int,day_:int):
        self._orders_tab[self._column_name__delivery_date]=datetime.date(year=year_,month=month_,day=day_)

    def _convert_number_into_date_plus_offset(self):
        self._orders_tab[self._column_name__delivery_date] = (self._orders_tab[self._column_name__delivery_date] + self._orders_tab[self._column_name__days_to_stock].apply(pd.offsets.Day)) #pd.to_timedelta(,unit='D')

    def _sort_by_items_and_dates(self):
        self._orders_tab = self._orders_tab.sort_values([self._column_name__item,self._column_name__delivery_date])

    def _group_sum_order_by_item_and_day(self):
        self._grupped_by_day_item= self._orders_tab.groupby([self._column_name__item,self._column_name__delivery_date]).sum()
        #convert group into df
        self._grupped_by_day_item = pd.DataFrame(self._grupped_by_day_item)
        #resetting multiindex which we ahve after groupby
        self._grupped_by_day_item.reset_index(inplace=True)

    #------------------------------------- getters ----------------------------------
    def get_data_grupped_by_item_day_sum_order(self)->pd.DataFrame: return self._grupped_by_day_item
    def get_data_for_item(self,item)->pd.DataFrame: return self._grupped_by_day_item[self._grupped_by_day_item[self._column_name__item==item]]
    def get_data_for_all_items(self)->pd.DataFrame: return self._grupped_by_day_item
    def get_item_list(self)->list:return self._item_list


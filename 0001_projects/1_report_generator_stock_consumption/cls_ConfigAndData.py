import numpy as np
import cls_ClientDataLoader as ClientDataLoader


class ConfigAndData:
    def __init__(self, cdl:ClientDataLoader.ClientDataLoader):
        #------------------------- init ----------------------------
        self._cdl =cdl
        self._columns_at_raw_resource_dict_name_value_type={}
        self._calendar_cfg_days=0
        self._calendar_cfg_dict_new_col_name_init_val={}
        self._column_data_orders_new_delivery_date=''

        #-------------------------- variables ----------------------
        self._calendar_cfg_days = 30
        self._new_columns_at_calendar__current_stock='current_stock'
        self._new_columns_at_calendar__stock_replenish='stock_replenish'
        self._new_columns_at_calendar__after_stock_replenish='after_stock_replenish'
        self._columns_data_orders_column__delivery_date='Delivery_date'
        self._columns_data_orders_column__day ='Day'

    #-------------------------- structures ----------------------
        self._columns_at_raw_resource_dict_name_value_type={cdl.get_client_column_from_consumption__item():int,
                                                            cdl.get_client_column_from_consumption__consumption():int}

        self._calendar_cfg_dict_new_col_name_init_val ={cdl.get_client_column_from_consumption__item():np.nan,
                                                        cdl.get_client_column_from_consumption__consumption():np.nan,
                                                        self._new_columns_at_calendar__stock_replenish:np.nan,
                                                        self._new_columns_at_calendar__after_stock_replenish:np.nan}

        self._report_column_replacement_dict={self._column_data_orders_new_delivery_date:self._columns_data_orders_column__day,
                                              cdl.get_client_column_from_raw_data__orders:self._new_columns_at_calendar__stock_replenish}

    #-------------------------- getters --------------------------
    def get_columns_from_raw_resource_list(self)->list:return [k for k in self._columns_at_raw_resource_dict_name_value_type.keys()]
    def get_calendar_max_days(self)->int:return self._calendar_cfg_days
    def get_calendar_new_columns_name_and_initial_values(self)->dict:return self._calendar_cfg_dict_new_col_name_init_val
    def get_column_name__delivery_date(self)->str:return self._columns_data_orders_column__delivery_date
    def get_column_name__item(self)->str:return self._cdl.get_client_column_from_consumption__item()
    def get_column_name__days_to_stock(self)->str:return self._cdl.get_client_column_from_raw_data__days_to_stock()

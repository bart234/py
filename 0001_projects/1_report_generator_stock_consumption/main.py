#variable at bash
'''
    create env:     python3 -m venv env_name
    env activate: source env_env/bin/activate
    global: source $HOME/Desktop/py_env/env_pd_np/bin/activate
    env deactivate: deactivate
'''

import pandas as pd
import numpy as np
import datetime

product_list =['Pork','Wheat Products','Beef']
size_of_generated_arr = 10
np.random.seed(8)

def datetime_test():
    d = {'A':'3444','B':'eeee','C':32}
    print(list(d))
    print(datetime.datetime.now().date()+datetime.timedelta(days=3))
    print((datetime.datetime.now()).strftime('%d-%b-%Y'))
    convert_int_int_date_with_offset = lambda x: (datetime.datetime.now().date()+datetime.timedelta(days=x))
    calendar_by_lambda = pd.DataFrame(data=[convert_int_int_date_with_offset(i) for i in range(1,40)])
    calendar_by_pd = pd.date_range(datetime.datetime.now().date(),periods=30)
    print(calendar_by_pd)
    '''
    print(datetime.datetime.date().str)
    '''

#fix that - remove unused def, extract const values into structures, create structures for client for easy update

#add structure which will be gather all config for reports

#describbe all process for data manipulation at client site

#add option when data from file containt info about two items - do not list them - process all, deliver both

#client require additional columns with serial number but only with beef and pork

#client would add wh and shelves space m3, each item will have some basic m3, by box, or crate, wh data will be added
#about wh space - show availible shelves
#result additional report about with shelves are full and with food quantity , and expectation if foo will be consumed
#enough fast to keep next order valid

#additional, add some dates into raw data which will not exactly true if we compare them to days to stock
#in that case just fix it with base of days_to_stock

#create folder tree and orders for few days ahead, with order ahead - bash and load it with today date

#additionaly generate for all items and save it withcurrent date

#additionaly add reading system to read yesterday file, open it, open today file, and add new orders to existing one, recalculate

#additionaly, add some mechanism to make consumption diffrent in some days like sat-sun

#additionaly, cut out additional calendar rows which are empty

class HowTo:
    pass
    #describe here everything what is done 
            #def offset_me(row,x): return row[self._column_name__delivery_date] +  pd.DateOffset(days=x)
        #self._orders_tab['c'] = self._orders_tab.apply(lambda row:offset_me(row0,2),axis=1)
        
        #self._orders_tab['c'] = self._orders_tab[self._column_name__delivery_date] +self._orders_tab[self._column_name__days_to_stock].apply(pd.offsets.Day)

class Calendar:
    '''main function:
    create base for report output table
    1. it generate calendar for n-days(calendar_get_days) ->[Item(item name), Day(yyyy-mm-dd, weak_day)]
    2. generate dict with item:calendar (based on items list delivered)
    3. each item_calendar is enriched by empty cols:    
    4. calendar_cfg_dict_new_col_name_init_value - it contain list of columns to add with initial value which will be set for each item
    5. enriching: it require client data wh_stock_consumption cols=[item,consumption,wh_stock], rows=[item1,item2,item3]
    6. consumption - set for all calendar, wh_stock - set for day 0 (today) - rest is set to 0
    7. calendars like that are availible on calendar_get_item_calendas(item)
    '''
    
    def __init__(self,days):
        self._days = days
        self._calendar=np.nan
        self._dict_for_calendars_item_calendar={}
        self._column_name__consumption='consumption'
        self._column_name__item='Item'
        self._column_name__current_stock='current_stock'
        self._column_name__wh_stock='wh_stock'

        self._generate_basic_calendar()

    #--------------------------------------------- public ------------------------------------------------
    def create_calendar_for_items_and_adjust_it(self,calendar_cfg_dict_new_col_name_init_value:dict,
                                                list_of_items:list,
                                                wh_stock_consumption:pd.DataFrame):
        self._add_new_columns_with_init_value(calendar_cfg_dict_new_col_name_init_value)

        for item in list_of_items:
            #create copy of absic calendar for Item 
            self._create_calendar_for_item(item)
            #adding current stock and consumption to calendar from additional data - wh_stock_consumption
            self._adjust_calendar_for_item(item,wh_stock_consumption)

    #--------------------------------------------- getters -----------------------------------------------
    def calendar_get_days(self)->int:return self._days
    def calendar_get_basic_calendar(self)->pd.DataFrame:return self._calendar
    def calendar_get_item_calendas(self,item:str)->pd.DataFrame: return self._dict_for_calendars_item_calendar[item]
    def calendar_print_item_calendas(self,item:str): print(self._dict_for_calendars_item_calendar[item].to_string())

    #------------------------------------------ inner functions ------------------------------------------
    def _generate_basic_calendar(self):
        self._calendar = pd.DataFrame(data=[(datetime.datetime.now().date()+pd.offsets.Day(a)) for a in range (0,self._days)])
        self._calendar.columns=['Day']
        self._calendar['week_day']=self._calendar['Day'].dt.day_name()
    
    def _add_new_columns_with_init_value(self,calendar_cfg_dict_new_col_name_init_value:dict):
        for k,v in calendar_cfg_dict_new_col_name_init_value.items():
            self._calendar[k]=v

    def _create_calendar_for_item(self,item:str):
        self._dict_for_calendars_item_calendar[item]=self._calendar.copy()

    def _adjust_calendar_for_item(self, item:str, consumption_data:pd.DataFrame):
        #add  data to item column in custom calendar
        self._dict_for_calendars_item_calendar[item][self._column_name__item]=item
        #add  data to consumption column in custom calendar
        self._dict_for_calendars_item_calendar[item][self._column_name__consumption]=(consumption_data.loc[[item]][self._column_name__consumption]).iloc[0]
        #add  data to item column in custom calendar
        self._dict_for_calendars_item_calendar[item].loc[0,[self._column_name__current_stock]]= (consumption_data.loc[[item]][self._column_name__wh_stock]).iloc[0]

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

class ConfigAndData:
    def __init__(self, cdl:ClientDataLoader):
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


class DataOrders:
    ''' it load data from sources item: df - concat all together, manipulate and keep as one tab
    to access use get_data_for_item(item)
    '''
    def __init__(self, cfg: ConfigAndData, dict_item_data:dict):
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


class Report:
    '''
    Every step have loop for all items from list. Items and their data are not combain together
    Also each stem is separated, main reason for that is make it easier to clontrol
    All config data and client_data are in struct ConfigAndData
    '''
    def __init__(self, cfg:ConfigAndData,
                 items_list:list,
                 item_calendar:Calendar,
                 data_orders:DataOrders):
    #-------------------------------- init -------------------------------
        self._items_output_calendars={}
    #-------------------------------- structures -------------------------
        self._items_list = items_list
        self._items_calendar_obj = item_calendar
        self._item_data=data_orders.get_data_for_all_items()
        self._cfg=cfg

    def replace_columns_on_item_data(self, dict_for_replacment_old_new:dict):
        self._item_data=self._item_data.rename(columns=dict_for_replacment_old_new)
    
    def merge_orders_data_with_calendar(self):
        for k in self._items_list:
            self._items_output_calendars[k]=self._items_calendar_obj.calendar_get_item_calendas(k).merge(self._item_data[self._item_data['Item']==k],on='Day',how='left')
      
    def merger_fix_drop_additional_columns(self,list_columns_to_drop:list):
        for k in self._items_list:
            self._items_output_calendars[k].drop(columns=list_columns_to_drop,inplace=True)
    
    def merger_fix_rename_columns_dict_old_new(self, dict_rename_old_new:dict):
        for k in self._items_list:
            self._items_output_calendars[k].rename(columns=dict_rename_old_new,inplace=True)
    
    def fill_nan_at_column(self,column_name:str):
        #we fill columns again because we join just existing dates, notexisted are nan
        for k in self._items_list:
            self._items_output_calendars[k][column_name]=self._items_output_calendars[k][column_name].fillna(value=0)

    def set_column_order(self,list_column_order:list):
        for k in self._items_list:
            self._items_output_calendars[k]=self._items_output_calendars[k].reindex(columns=list_column_order)
    
    def calculate_rows(self):        
        for k in self._items_list:
            for i in range(0,self._items_calendar_obj.calendar_get_days()):
                #recalculation in row: current_stock + stock_replenish = after_stock_replenish
                self._items_output_calendars[k].loc[i,['after_stock_replenish']]=self._items_output_calendars[k].loc[i,['current_stock']][0]+\
                                                                                self._items_output_calendars[k].loc[i,['stock_replenish']][0]
                #recalculation in row+1: after_stock_replenish(stock from prevois day) - consumption(today) = current_stock(today)
                self._items_output_calendars[k].loc[i+1,['current_stock']]=self._items_output_calendars[k].loc[i,['after_stock_replenish']][0]-\
                                                                                self._items_output_calendars[k].loc[i,['consumption']][0]
    def get_reports_dict(self,item_list_or_empty_for_all:list):
        if (len(item_list_or_empty_for_all))==0:
            return self._items_output_calendars
        else:
            dict_to_out={}
            for k in item_list_or_empty_for_all:
                dict_to_out[k]=self._items_calendar_obj[k]
            return dict_to_out
    
    def print_report(self):
        for k,v in self._items_output_calendars.items():
            print(k)
            print(v.to_string())
               
    def print_raw_data(self):
        print(self._item_data.to_string())

def prepare_report():
    cdl = ClientDataLoader()
    config=ConfigAndData(cdl)
    c = Calendar(config.get_calendar_max_days())
    #list_of_items=["Pork"]
    list_of_items=cdl.get_client_product_list()

    c.create_calendar_for_items_and_adjust_it(config.get_calendar_new_columns_name_and_initial_values(),
                                             list_of_items,
                                             cdl.get_client_data_consumption())
    
    do = DataOrders(config,cdl.get_client_data_dict_item_data())

    #report
    r = Report(config,list_of_items,c,do)
    r.replace_columns_on_item_data({'Delivery_date':'Day','orders':'stock_replenish'})
    r.merge_orders_data_with_calendar()
    r.merger_fix_drop_additional_columns(['stock_replenish_x','Item_y'])
    r.merger_fix_rename_columns_dict_old_new({'Item_x':'Item','stock_replenish_y':'stock_replenish'})
    r.fill_nan_at_column('stock_replenish')
    r.fill_nan_at_column('after_stock_replenish')
    r.fill_nan_at_column('days_to_stock')
    r.set_column_order(['Item','Day','week_day','consumption','current_stock','stock_replenish','after_stock_replenish'])
    r.calculate_rows()
    r.print_report()


#datetime_test()
prepare_report()
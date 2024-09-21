import numpy as np
import pandas as pd
import datetime

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

import cls_Calendar as Calendar
import cls_ConfigAndData as ConfigAndData
import cls_DataOrders as DataOrders

class Report:
    '''
    Every step have loop for all items from list. Items and their data are not combain together
    Also each stem is separated, main reason for that is make it easier to clontrol
    All config data and client_data are in struct ConfigAndData
    '''
    def __init__(self, cfg:ConfigAndData.ConfigAndData,
                 items_list:list,
                 item_calendar:Calendar.Calendar,
                 data_orders:DataOrders.DataOrders):
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
#variable at bash
'''
    create env:     python3 -m venv env_name
    env activate: source env_env/bin/activate
    global: source $HOME/Desktop/py_env/env_pd_np/bin/activate
    env deactivate: deactivate
'''
import cls_Calendar as Calendar
import cls_ClientDataLoader as ClientDataLoader
import cls_ConfigAndData as ConfigAndData
import cls_DataOrders as DataOrders
import cls_Report as Report


def prepare_report():
    cdl = ClientDataLoader.ClientDataLoader()
    config=ConfigAndData.ConfigAndData(cdl)
    c = Calendar.Calendar(config.get_calendar_max_days())
    #list_of_items=["Pork"]
    list_of_items=cdl.get_client_product_list()

    c.create_calendar_for_items_and_adjust_it(config.get_calendar_new_columns_name_and_initial_values(),
                                             list_of_items,
                                             cdl.get_client_data_consumption())
    
    do = DataOrders.DataOrders(config,cdl.get_client_data_dict_item_data())

    #report
    r = Report.Report(config,list_of_items,c,do)
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


prepare_report()
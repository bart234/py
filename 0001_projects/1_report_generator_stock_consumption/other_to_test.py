
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

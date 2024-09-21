
#fix that - remove unused def, extract const values into structures, create structures for client for easy update

#extract deprecated function from  row roll at report: calculate_rows

#finish test cls

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

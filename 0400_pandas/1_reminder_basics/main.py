import pandas as pd
import numpy as np
import os
import json
#https://github.com/tategallery/collection

fields_to_get_from_df =['id','artist','title','medium','year','acquisitionYear','height','width','units']
fields_to_get_from_json =['id','all_artists','title','medium','acquisitionYear','height','width','units']

def print_nicely_list(l:list):
    for i in l:
        print(i)

#-----------------------------------------------------------------------------------------------------------------
class UsfullFunctions:
    def getPathForUpperFolder(folder_to_find:str,path_is_splited_by:str,add_slesh_at_end:bool) -> str:
        list_of_folders_path = os.path.abspath(__file__).split(path_is_splited_by)
        index_of_folder = list_of_folders_path.index(folder_to_find)
        return (path_is_splited_by.join(list_of_folders_path[0:index_of_folder+1])+(path_is_splited_by if add_slesh_at_end else ''))
    
    def traverse_through_folder_tree(path_to_traverse:str,max_files_loaded:int =0)->list:
        list_to_return=[]
        current_loaded = 0
        for root,dirs,files in os.walk(path_to_traverse):
            for f in files:
                if f.endswith('json'):
                    list_to_return.append(os.path.join(root,f))                                     
                    if max_files_loaded !=0:
                        current_loaded +=1   
                    if current_loaded >max_files_loaded:
                        return list_to_return
                        #list_to_return.append(os.path.join(root,f))
        return list_to_return

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
class JsonActions:
    def get_record_from_json(path:str, fields_to_extract_from_json:list)->tuple:
        with open(path) as my_file:
            content = json.load(my_file)
        record =[]
        for field in fields_to_extract_from_json:
            record.append(content[field])
        return tuple(record)
    
    
class ExtractFromJsonAndTree:
    def getDfFromMultiFilesInTree(fields_to_get_from_json:list,list_with_paths:list)->list:
        list_of_tuples = []
        for path in list_with_paths:
            list_of_tuples.append(JsonActions.get_record_from_json(path,fields_to_get_from_json))
        return list_of_tuples

    def makeDfFromJsonAndSaveAs(data_from_files:list, fields:list,save_as:str)->pd.DataFrame:
        df =pd.DataFrame(data=data_from_files,columns=fields)
        df.to_pickle(save_as+'.pickle')
        print("DD saved as: "+save_as)

#--------------------------------------------------------------------------------------------------------
class BasicReminder:        
    def work_with_data_csv():
        #index_col='id'     -   in that way we reuse existing index which is on id column
        #usecols=[...]      -   we filter at start, what column we need
        
        path_to_upper_file = UsfullFunctions.getPathForUpperFolder()('git','/',True)
        folder_with_data = 'git_data_art_collection/'
        df = pd.read_csv(path_to_upper_file+folder_with_data+"artwork_data.csv",nrows=2555,index_col='id',
                usecols=['id','artist','title','medium','year','acquisitionYear','height','width','units'])
        df.to_pickle('save_df_for_me.pickle')
        print(df)

    def work_with_pathing():
        list_of_folders_path = os.path.abspath(__file__).split('/')
        folder_to_find='git'
        index_of_folder = list_of_folders_path.index(folder_to_find)
        #print(index_of_folder)
        #print('/'.join(list_of_folders_path[0:index_of_folder+1]))
        #print(os.path.dirname(os.path.abspath(__file__)).split())
        print(UsfullFunctions.getPathForUpperFolder()('git','/',True))
        print(UsfullFunctions.getPathForUpperFolder()('git','/',False))

    def box_array():
        arr_2d = np.random.rand(3,2)
        print(arr_2d)
        df = pd.DataFrame(arr_2d)
        print(df)
        print("Data access")
        print(arr_2d[1,1])
        df.columns=['Column 1','Colum 2']
        df.index=['r1','r2','r3']

    def basic_arr_generation():
        arr_with_rands = np.random.rand(3)
        df = pd.Series(arr_with_rands)
        df2=pd.DataFrame(arr_with_rands)
        df_with_index = pd.Series(data=arr_with_rands,
                                index=['1th','2nd','3th'])
        print(df_with_index)

if __name__=='__main__':
    #ExtractFromJsonAndTree.getDfFromMultiFilesInTree(fields_to_get_from_json,
    #                                                 UsfullFunctions.getPathForUpperFolder('git','/',True) + 'git_data_art_collection/artworks',
    #                                                 5)
    json_path_list =UsfullFunctions.traverse_through_folder_tree(UsfullFunctions.getPathForUpperFolder('git','/',True) + 'git_data_art_collection/artworks',5)
    data_from_jsons =ExtractFromJsonAndTree.getDfFromMultiFilesInTree(fields_to_get_from_json,json_path_list)
    ExtractFromJsonAndTree.makeDfFromJson(data_from_jsons,fields_to_get_from_json)
   
    #testing part
    #print_nicely_list(UsfullFunctions.traverse_through_folder_tree(UsfullFunctions.getPathForUpperFolder('git','/',True) + 'git_data_art_collection/artworks',5)) #like above but take all files
    #print(JsonActions.get_record_from_json(UsfullFunctions.getPathForUpperFolder('git','/',True) + 'git_data_art_collection/n00106-12388.json',fields_to_get_from_json))
    #------------------------------------------------------------------------------------
    #BasicReminder.work_with_data_csv()
    #BasicReminder.work_with_pathing()
    #BasicReminder.box_array()
    #BasicReminder.basic_arr_generation()
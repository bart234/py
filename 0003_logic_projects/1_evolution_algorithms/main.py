import os

def main():
    #bagpack problem
    #we haave one bagpack, and a lot of items, each item have diffrent weigth and value
    #bagpack can only carry 9kg
    #target: to maximize value in bagpack
    #result: expected will be one of best solutions, not best one, we will not use force method
    #metod: evolution algoritm will be created and use
    #additionaly: adjustment elements can be added
    data = data_creation()  #[0] is a dict, [1] iare id,value,weigth


def data_creation()->list:
    #dict: item:id
    #list[list[id,value,weigth]]
    d ={'sword':1,'shield':2,'pan':3,'cup':4,'fork':5,'coin':6,'gold_dagger':7,'bag_of_salt':8,'glass':9,'frame':10,'watch':11,'fan':12,'book':13,'plug':14,'pen':15}
    list_value_weigth=[[1,2,4],[2,1,3],[3,1,3],
                       [4,3,1],[5,1,1],[6,3,1],
                       [7,6,4],[8,3,7],[9,3,2],
                       [10,2,2],[11,5,1],[12,3,4],
                       [13,5,4],[14,1,1],[15,2,1]]
    return list(d,list_value_weigth)



main()

class TestResult():
    def __init__(self) -> None:
        #works only with np.random.seed(8)
        expected_values_from_report={"Pork":{-1:'    Item        Day   week_day  consumption  current_stock  stock_replenish  after_stock_replenish',
                                            0:'0   Pork 2024-09-21   Saturday          2.0            5.0              0.0                    5.0',
                                            3:'3   Pork 2024-09-24    Tuesday          2.0           -1.0              3.0                    2.0',
                                            4:'4   Pork 2024-09-25  Wednesday          2.0            0.0              3.0                    3.0',
                                            10:'10  Pork 2024-10-01    Tuesday          2.0           14.0              0.0                   14.0',
                                            29:'29  Pork 2024-10-20     Sunday          2.0          -24.0              0.0                  -24.0'},
                                    'Wheat Products':{-1:'    Item        Day   week_day  consumption  current_stock  stock_replenish  after_stock_replenish',
                                            0:'0   Wheat Products 2024-09-21   Saturday        222.0          500.0              0.0                  500.0',
                                            3:'3   Wheat Products 2024-09-24    Tuesday        222.0          370.0              0.0                  370.0',
                                            4:'4   Wheat Products 2024-09-25  Wednesday        222.0          148.0             76.0                  224.0',
                                            10:'10  Wheat Products 2024-10-01    Tuesday        222.0          885.0            126.0                 1011.0',
                                            29:'29  Wheat Products 2024-10-20     Sunday        222.0        -1651.0              0.0                -1651.0'},
                                    'Beef':{-1:'    Item        Day   week_day  consumption  current_stock  stock_replenish  after_stock_replenish',
                                            0:'0   Beef 2024-09-21   Saturday         22.0           50.0              0.0                   50.0',
                                            3:'3   Beef 2024-09-24    Tuesday         22.0          -16.0              0.0                  -16.0',
                                            4:'4   Beef 2024-09-25  Wednesday         22.0          -38.0             19.0                  -19.0',
                                            10:'10  Beef 2024-10-01    Tuesday         22.0          -94.0              0.0                  -94.0',
                                            29:'29  Beef 2024-10-20     Sunday         22.0         -341.0              0.0                 -341.0'}
                                    }

class Student:
    const_rate = 0.84

    def __init__(self,first,second,avg) -> None:
        self.first = first
        self.second = second
        self.avg = avg

    @property
    def email(self):
        return '{}.{}@uni.gov.com'.format(self.first,self.second)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.second)
    
    def decrease_avg(self):
        self.avg = float(self.avg*self.const_rate)
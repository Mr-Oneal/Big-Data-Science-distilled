"""Lab 1. Basic wordcount
"""
from mrjob.job import MRJob
import re
import time
import datetime

class Lab4(MRJob):

# this class will define two additional methods: the mapper method goes here
    def mapper(self, _, line):
        try:
            ds_row = line.split(",") #data set row
            if len(ds_row) == 9:
                stock_symbol = ds_row[1]
                date = ds_row[2]
                stock_price_close = ds_row[6]
                stock_volume = ds_row[7]
                amount_exchanged = float(stock_price_close)*float(stock_volume)
                yield(None,(date,stock_symbol,amount_exchanged))
        except:
            pass

    def combiner(self,_, values):
        sorted_values = sorted(values, reverse=True, key=lambda values: values[2])
        i = 0
        for value in sorted_values:
            yield("top",value)
            i+=1
            if i>=10:
                break


#and the reducer method goes after this line
    def reducer(self,_, values):
        print("run",1)
        sorted_values = sorted(values, reverse=True, key=lambda values: values[2])
        i = 0
        for value in sorted_values:
            yield("{} - {} - {}".format(value[0],value[1],value[2]),None)

            i+=1
            if i>=10:
                break

if __name__ == '__main__':
    Lab4.run()

"""Lab 3"""

from mrjob.job import MRJob
import re
import time
import datetime

#We will count how many tweets were sent during each day of the olympics

#This line declares the class Lab3, that extends the MRJob format.
class Lab3(MRJob):

# this class will define two additional methods: the mapper method goes here
   def mapper(self, _, line):
        fields = line.split(";")
        try:
            if (len(fields)==4):
                time_epoch = int(fields[0])/1000
                day = time.strftime("%d-%m-%Y",time.gmtime(time_epoch)) #returns day of the month
                yield(day,1)
        except:
            pass
            #no need to do anything

#and the reducer method goes after this line
   def reducer(self,day,tweetCounts):
       yield (day, sum(tweetCounts))

#this part of the python script tells to actually run the defined MapReduce job. Note that Lab2 is the name of the class
if __name__ == '__main__':
    Lab3.run()

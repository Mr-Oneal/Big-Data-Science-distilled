"""Lab 3"""

from mrjob.job import MRJob
import re
import time
import datetime
import statistics

class Lab3(MRJob):

# this class will define two additional methods: the mapper method goes here
   def mapper(self, _, line):
        fields = line.split(";")
        try:
            if (len(fields)==4):
                #tweetLength = len(fields[2])
                tweetHash = fields[2].count('#')
                yield("Hash",tweetHash)
        except:
            pass
            #no need to do anything

   def combiner(self,lengthString,tweetLength,):
       tweetLengthCount = sum(tweetLength)
       yield (lengthString,tweetLengthCount)


#and the reducer method goes after this line
   def reducer(self,lengthString,tweetLength):
       lenghtSum = sum(tweetLength)
       average = lenghtSum/25568614.0
       yield("Length",average)

if __name__ == '__main__':
    #Lab3.JOBCONF= { 'mapreduce.job.reduces': '5' }
    Lab3.run()

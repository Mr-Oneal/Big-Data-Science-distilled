"""Lab 2"""
from mrjob.job import MRJob
import re

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class Lab2, that extends the MRJob format.
class Lab2(MRJob):

# this class will define two additional methods: the mapper method goes here
   def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

#combiner 
   def combiner(self,word,counts):
       yield(word,sum(counts))

#and the reducer method goes after this line
   def reducer(self,word,counts):
       yield (word, sum(counts))

#this part of the python script tells to actually run the defined MapReduce job. Note that Lab2 is the name of the class
if __name__ == '__main__':
    #Lab2.JOBCONF= { 'mapreduce.job.reduces': '3' }
    Lab2.run()

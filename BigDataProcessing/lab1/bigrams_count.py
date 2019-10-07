""" You will need to load these libraries in your machine by loading the corresponding Python 
module. At the beginning of your lab session, in the terminal, write the following command:

module load python/3.7.0"""

"""Lab 1. Basic wordcount
"""
from mrjob.job import MRJob
import re

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class Lab1, that extends the MRJob format.
class Lab1(MRJob):

# this class will define two additional methods: the mapper method goes here
   def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for i in range(len(words)-1):
            bigram = (words[i].lower(),words[i+1].lower())
            yield (bigram, 1)
#and the reducer method goes after this line
   def reducer(self,bigram,counts):
       yield (bigram,sum(counts))

               
#this part of the python script tells to actually run the defined MapReduce job. Note that Lab1 is the name of the class
if __name__ == '__main__':
    Lab1.run()

"""Use this command to run the program
python bigrams_count.py input/sherlock.txt > out.txt"""
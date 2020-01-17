
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class Lab4(MRJob):

    sector_table={}
# this class will define two additional methods: the mapper method goes here
    def mapper_join_init(self):
        with open("companylist.tsv") as f:
            for line in f:
                fields = line.split("\t")
                key = fields [0]
                val = fields[3]
                self.sector_table[key] = val

    def mapper_repl_join(self, _, line):
        try:
            fields = line.split(",") #data set row
            company = fields[1]
            if company in self.sector_table:
                year = int(fields[2][:4])
                volume = int(fields[7])
                key = (self.sector_table[company],year)
                yield(key,volume)
        except:
            pass

    def mapper_length(self,key,volume):
        yield(key,volume)

    def reducer_sum(self,key,volumes):
        total = sum(volumes)
        yield(key,total)

    def steps(self):
        return [MRStep(mapper_init=self.mapper_join_init,
                        mapper=self.mapper_repl_join),
                MRStep(mapper = self.mapper_length,
                        reducer=self.reducer_sum)]

if __name__ == '__main__':
    Lab4.run()

from mrjob.job import MRJob
from mrjob.step import MRStep

class MostTripsTotalRevenue(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.final_reducer)
        ]
    
    def mapper(self, _, line):
        if not line.startswith('VendorID'):
            data = line.strip().split(',')
            vendor_id = data[0]
            revenue = float(data[16])
            yield vendor_id, revenue
    
    def reducer(self, key, values):
        total_revenue = sum(values)
        yield None, (total_revenue, key)
    
    def final_reducer(self, _, values):
        max_revenue, vendor_id = max(values)
        yield vendor_id, max_revenue


if __name__ == '__main__':
    MostTripsTotalRevenue.run()
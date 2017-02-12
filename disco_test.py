from disco.core import result_iterator
from disco.job import Job


def map(line, params):
    for char in line:
        yield char, 1

total = 0

def reduce(iter, params):
    global total
    from disco.util import kvgroup
    for word, counts in kvgroup(sorted(iter)):
        s = sum(counts)
        total += s
        yield word, s, float(s) / total

if __name__ == '__main__':
    input = ["http://discoproject.org/media/text/chekhov.txt"]
    job = Job().run(input=input, map=map, reduce=reduce)
    for word, count in result_iterator(job.wait()):
        print word, count
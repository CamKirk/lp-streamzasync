from streamz import Stream
import random


source = Stream()
source.map(lambda x : x**2 ).sink(print)

while True:
    source.emit(random.randint(1,100))
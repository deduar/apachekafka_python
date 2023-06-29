import sys
from .producer import Producer

if __name__ == '__main__':
    producer = Producer(sys.argv[1], sys.argv[2], sys.argv[3])
    producer.start_write()
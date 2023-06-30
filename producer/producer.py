from kafka import KafkaProducer
import time
import json
import requests

from .reader.data_reader import Reader

class Producer:
    def __init__(self, file_name, topic, freq):
        self.topic = topic
        self.freq = freq if isinstance(freq, int) else int(freq)
        self.producer = KafkaProducer(bootstrap_servers='myKafka:9092',
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        self.reader = Reader(file_name)

    def start_write(self):
        for index, value in self.reader.data.iterrows():
            dict_data = dict(value)
            # self.producer.send(self.topic, value=dict_data)
            headers = {'Accept-Encoding': 'UTF-8', 'Content-Type': 'application/json'}
            dict_data["amount"] = str(dict_data["amount"])
            r = requests.post('http://myServiceCO2:8080/CFPEstimate', headers=headers, data=json.dumps(dict_data))
            # print(f'Message {index + 1}: {r.json()}')
            self.producer.send(self.topic, value=r.json())
            time.sleep(self.freq)

if __name__ == '__main__':
    pass
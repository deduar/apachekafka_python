from kafka import KafkaProducer
# import time
import json
# import requests

from cfplib.cfp import CFP

from .reader.data_reader import Reader

class Producer:
    def __init__(self, topic):
        self.topic = topic
        # self.freq = freq if isinstance(freq, int) else int(freq)
        self.producer = KafkaProducer(bootstrap_servers='myKafka:9092',
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        # self.reader = Reader(file_name)

    def start_write(self):
        for index, value in self.reader.data.iterrows():
            dict_data = dict(value)
            # self.producer.send(self.topic, value=dict_data)
            # headers = {'Accept-Encoding': 'UTF-8', 'Content-Type': 'application/json'}
            # dict_data["amount"] = str(dict_data["amount"])
            # r = requests.post('http://myServiceCO2:8080/CFPEstimate', headers=headers, data=json.dumps(dict_data))
            # print(f'Message {index + 1}: {r.json()}')
            req_info = {"title":"COMP.TPV FISICO NACI -- CENTROCARY SIERR MP","amount":"-52.3","date":"2023-02-10","category":"automóvil y transporte","subcategory":"compra y alquiler"}
            # cfp = CFP(req_info)
            # cfp_estimate = cfp.estimateCFP()
            self.producer.send(self.topic, value=req_info.json())
            # time.sleep(self.freq)

if __name__ == '__main__':
    pass
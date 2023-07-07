from kafka import KafkaConsumer
import json

from cfplib.cfp import CFP

from producer.producer import Producer

class Consumer:
    def __init__(self, topic):
        self._consumer = KafkaConsumer(topic,
                                       bootstrap_servers='myKafka:9092',
                                       value_deserializer=lambda x: json.loads(x.decode('utf-8')))

        self.data = []

    @property
    def consumer(self):
        return self._consumer

    @consumer.setter
    def consumer(self, value):
        if isinstance(value, KafkaConsumer):
            self._consumer = value

    def star_read(self):
        self.receive_message()

    def receive_message(self):
        for message in self._consumer:
            message = message.value
            cfp = CFP(message)
            cfp_estimate = cfp.estimateCFP()
            prod = Producer(topic="aba_cfp_producer")
            prod.producer.send("aba_cfp_producer",value=cfp_estimate)
            print(f'{message}')


if __name__ == '__main__':
    pass
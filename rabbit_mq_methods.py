import pika
import config


def connection():
    # pika connect to remote host and port
    credentials = pika.PlainCredentials(config.MQ_USER, config.MQ_PASSWORD)
    parameters = pika.ConnectionParameters(config.MQ_HOST, config.MQ_PORT, config.MQ_VIRTUAL_HOST, credentials)
    mq_connection = pika.BlockingConnection(parameters)
    return mq_connection


class RabbitMqMethods:
    def __init__(self):
        self.mq_connection = connection()
        self.channel = self.mq_connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    def consume_message(self, queue_name):
        method_frame, header_frame, body = self.channel.basic_get(queue_name)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return body
        else:
            return "No message returned"

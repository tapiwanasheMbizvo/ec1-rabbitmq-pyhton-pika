from rabbit_mq_methods import RabbitMqMethods
import  time
mq = RabbitMqMethods()

# mq.declare_queue("test_queue")
#mq.publish_message("test_queue", "Another test message")

#msg_body = mq.consume_message("test_queue")

#print(msg_body)

while True:
    time.sleep(1)
    msg_body = mq.consume_message("test_queue")
    print(f"Received message {msg_body}")

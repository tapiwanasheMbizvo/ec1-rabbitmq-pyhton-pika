from rabbit_mq_methods import RabbitMqMethods
import time

mq = RabbitMqMethods()


x = 1
while True:
    mq.publish_message("test_queue", "Message #{}".format(x))
    time.sleep(1)
    x += 1
    print("Message #{} published".format(x))
    if x == 10:
        break

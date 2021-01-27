from collections import deque
import pika , json



class TaskShooter(object):
    """store and fire group of actions when needed"""

    def __init__(self):
        # self.tasks = deque()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')



    def CloseChannel():
        self.channel.close()

    #
    # def AddTask(self,task_name):
    #     self.tasks.append(task_name)
    #
    # def RemoveTask(self,task_name):
    #     self.tasks.remove(task_name)
    #
    # def Update_task(self,task_name):
    #     task_index=self.tasks.index(task_name)
    #     RemoveTask(task_name)
    #     self.tasks.insert(task_index,task_name)

    def Fire(self,tasks):

        self.channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(tasks),
                       properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ))
        print(" [x] Sent %r" % json.dumps(tasks))

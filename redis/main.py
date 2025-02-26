import read
import redis_client

redishost='172.18.0.2'
redis_port=6379
file= 'redis/input.csv'

t = redishost, redis_port

d = {'test3':'this is test3', 'test4':'this is test4'}


class main_cls:
    def __init__(self, file, *args):
        self.args = args
        self.file = file
        self.read= read.read_data(self.file)
        self.conn= redis_client.conn(self.file,*self.args)


    def set_val(self):
        data= self.read.read_file()
        for x in range(1,len(data)):
            print(f"sending data to server")
            self.conn.send_input(data[x][0], data[x][1])
    def get_val(self):
        data= self.read.read_file()
        for x in range(1,len(data)):
            print(f"key is: {str(data[x][0])}, value is: {self.conn.read_output(str(data[x][0]))}")

    def add_data_file(self, d: dict, file=file):
        file = self.file if file=={} else file
        self.read.add_data(d)


    


m = main_cls(file,*t)
# m.conn.send_input('test1', 'output1')
# print(m.conn.r.get("test1"))
# print(m.conn.read_output('test1'))
# m.set_val()
m.get_val()
# m.add_data_file(d)
# m.set_val()
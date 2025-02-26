import redis
import read


redishost='172.18.0.2'
redis_port=6379
file= 'redis/input.csv'
d = {'test3':'this is test3', 'test4':'this is test4'}

t = redishost, redis_port

class conn:
    def __new__(cls,*args):
        if not hasattr(cls, 'instance'):
            cls.instance=super(conn,cls).__new__(cls)
        return cls.instance
    def __init__(self, file,*args):
       self.args= args
       self.file= file
       self.r = redis.StrictRedis(*self.args,decode_responses=True)
    #    self.read= read.read_data(self.file)

    def send_input(self,key: str, value: str):
        
        self.r.set(key, value)
    def read_output(self,key: str):
        return self.r.get(key)



# class send_val_db(conn):

#     def __init__(self, *args):
#         super().__init__(*args)
#     def send_input(self,key: str, value: str):
#         self.r.set(key, value)
#     def read_output(self,key: str):
#         return self.r.get(key)


# v1 = send_val_db(file,*t)
# print(v1.read.read_file())
# v1.read.add_data(d)
# print(v1.read.read_file())
# v1.read.del_data(d)
# print(v1.read.read_file())

# print(v1.read)

# v1.send_input('test1', 'output')
# r = v1.read_output('test1')

# print(r)
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
logger = logging.getLogger()


def add(a,b):
    return a+b

a=add(2,3)
print(a)
logging.info(f"value of a is : {a}")
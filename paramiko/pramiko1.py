from paramiko import client

host= "localhost"

user = 'vikasdw'
password = 'Babita@17'

ssh_client = client.SSHClient()
ssh_client.connect(hostname=host, 
                   username=user, password=password,
                   look_for_keys=False, allow_agent= False)


print('connect sucessfull')


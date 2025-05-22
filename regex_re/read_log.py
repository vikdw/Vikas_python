import logging
import re

# Set up basic configuration
logging.basicConfig(
    filename='log.log',                # Log file name
    filemode='a',                      # 'a' for append, 'w' to overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG                # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
)



pattern= re.compile(r"(^\d{2}\/\d{2}\s\d{2}:\d{2}:\d{2})(?:\sTRACE\s*:\.+.*T1_expire:\s)(T1 expired)", re.MULTILINE)

with open("sample.log", 'r') as f:
    data= f.read()

    print(data)
    op= pattern.findall(data)
    
    for message  in op:
        logging.info(f"Date is: {message[0]}")
        logging.debug(f"messae is {message[1]}")


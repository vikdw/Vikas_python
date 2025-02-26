import numbers
from datetime import timedelta, datetime



class Timezone:
    def __init__(self, name, offset_hr, offset_min):
        if name is None or len(str(name))==0:
            raise ValueError('name can not be empty string.')       

        if not isinstance(offset_hr, numbers.Integral) or offset_hr not in [i for i in range(-12,15)]:
            raise ValueError('offset_hr is not interger or in -12 to +12')
        
        if not isinstance(offset_min, numbers.Integral) or offset_min not in [i for i in range(-59,60)]:
            raise ValueError('offset_min is not interger or in -59 to 59')
        
        offset = timedelta(hours=offset_hr, minutes=offset_min)
        if offset< timedelta(hours=-12, minutes=0) or offset> timedelta(hours=14, minutes=0):
            raise ValueError('offset should be between -12:00 to +14:00')

        self._name=name
        self._offset_hr = offset_hr
        self._offset_min = offset_min 
        self._offset = offset
  
        @property
        def offset(self):
            return self._offset
        @property
        def name(self):
            return self._name  

class Account:
    _interest_rate= 5  # in percentage
    def __init__(self, account_number, Fname, Lname, timezone=None,
                 initial_balance=0):
         
        _transaction_codes = {
            'deposit': 'D',
            'withdraw': 'W',
            'interest': 'I',
            'rejected': 'X'
             }
        self._startTxValue=100

        if not isinstance(account_number, int) or len(str(account_number).strip()) == 0:
            raise ValueError('account number can not be empty or non interger.')
        if not isinstance(Fname, str) or len(str(Fname).strip()) == 0:
            raise ValueError('First name can not be empty or non string.')
        if not isinstance(Lname, str) or len(str(Lname).strip()) == 0:
            raise ValueError('Last name can not be empty or non string.')
        
        self._account_number=account_number
        self.Fname = Fname
        self.Lname = Lname

        if timezone==None:
            timezone=Timezone('UTC', 0, 0)
        self._timezone=timezone
        self._balance= float(initial_balance)
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.real):
            raise ValueError('interest rate should be real number')
        if value < 0:
            raise ValueError('interest rate can not be -ve value.')
        cls._interest_rate = value

    @property
    def balance(self):
        return self._balance
    
    @property
    def First_name(self):
        return self.Fname
    
    @First_name.setter
    def First_name(self, Fname):
        self.Account.validate_name('Fname', Fname, 'First_Name')

    @property
    def Last_name(self):
        return self.Lname
    @Last_name.setter
    def Last_name(self, Lname):
        self.validate_name('Lname', Lname, 'Last_Name')
     
    def fullname(self):
        return f'{self.Fname} {self.Lname}'
    
    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, Timezone):
            raise ValueError('timezone should be a Timezone object.')
        self._timezone= value
         
    
    def validate_name(self, attr, value, field):
        if value is None or len(str(value).strip())==0:
            raise ValueError(f'{field} can  not be empty.')
        setattr(self, attr, value)
    
    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.now().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self._account_number}-{dt_str}-{self.make_tx_no()}'
    
    def make_tx_no(self):
        self._startTxValue = self._startTxValue + 1
        return self._startTxValue
    
    def make_transaction(self):
        return self.generate_confirmation_code('dummy')
 
a = Account(100, 'vikas', 'dwivedi', initial_balance=10001)
print(a.First_name)
print(a.balance)
print(a.make_transaction())
print(a.make_transaction())
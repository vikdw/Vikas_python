import numbers
from datetime import timedelta



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
    def __init__(self, account_number, Fname, Lname):
        self._startTxValue=100
        if not isinstance(account_number, int) or len(str(account_number).strip) == 0:
            raise ValueError('account number can not be empty or non interger.')
        if not isinstance(Fname, str) or len(str(Fname).strip) == 0:
            raise ValueError('First name can not be empty or non string.')
        if not isinstance(Lname, str) or len(str(Lname).strip) == 0:
            raise ValueError('Last name can not be empty or non string.')
        
        self._account_number=account_number
        self._Fname = Fname
        self._Lname = Lname
    
    @property
    def First_name(self):
        return self._Fname
    @First_name.setter
    def First_name(self, Fname):
        self._Fname = Fname

    @property
    def Last_name(self):
        return self._Lname
    @Last_name.setter
    def Last_name(self, Lname):
        self._Fname = Lname

    def make_tx_no(self):
        self._startTxValue = self._startTXValue + 1
        return self._startTxValue
    
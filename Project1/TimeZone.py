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
        


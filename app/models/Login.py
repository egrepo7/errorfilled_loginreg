from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()
   	
   	def reg_user(self, regdata):
   		errors = {}

   		if not regdata['reg_fname'] or len(regdata['reg_fname']) < 2:
   			errors.update({'fname':'First name must be at least 2 characters long'})
   		if not regdata['reg_lname'] or len (regdata['reg_lname']) < 2:
   			errors.update({'lname':'Last name must be at least 2 characters long'})

   		if len(errors) > 0:
   			return errors

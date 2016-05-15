from system.core.controller import *

class Logins(Controller):
    def __init__(self, action):
        super(Logins, self).__init__(action)
        self.load_model('Login')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('main.html')

    def register(self):
    	newuser = self.models['Login'].reg_user(request.form)


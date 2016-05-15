from system.core.router import routes

routes['default_controller'] = 'Logins'
routes['POST']['/reg'] = 'Logins#register'
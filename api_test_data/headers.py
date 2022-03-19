from .get_token import user_token

user_bearer_token = 'Bearer ' + str(user_token)
# admin_bearer_token = 'Bearer ' + str(admin_token)
headers_with_token = {'Authorization': user_bearer_token, 'Content-Type': 'application/json',
                           'Accept': 'application/json'}
# admin_headers_with_token = {'Authorization': admin_bearer_token, 'Content-Type': 'application/json',
#                             'Accept': 'application/json'}
headers = {'Content-Type': 'application/json'}

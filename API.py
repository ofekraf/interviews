from sanic_auth import Auth
from sanic import Sanic, response
import json

app = Sanic(__name__)
app.config.AUTH_LOGIN_ENDPOINT = 'login'


@app.middleware('request')
async def add_session_to_request(request):
    with open('user') as json_file:
        res = json.load(json_file)
        res['requests'] = request
        return res


auth = Auth(app)


def get_user():
    with open('user') as json_file:
        return json.load(json_file)


# extracting the required data
def get_res(input_data):
    res = {}
    for block in input_data:
        for key in block:
            if "Val" in key:
                res[block["name"]] = block[key]
    return res


@app.route('/login', methods=['GET', 'POST'])
async def login(request):
    if request.method == 'POST':
        # assuming these exist as well for authentication purposes
        username = request.form.get('username')
        password = request.form.get('password')

        # fetch user from local_file
        user = get_user().get(name=username)
        if user and user[username] == password:
            auth.login_user(request, user)
            return get_res(request.data)
    return response.redirect('/login')  # assuming there is a login page, just don't let the user log in
    # for lack of time,  i did not build this page myself
    # but notice this only supports post routing for logged in users

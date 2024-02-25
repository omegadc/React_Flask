from flask import Flask

app = Flask(__name__)

@app.route("/") #@app.route("/", methods=['GET','POST'])
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == __main__:
    app.run(debug=True)
'''
<variable name> = keyword argument
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


APIs with JSON
A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. If you return a dict or list from a view, it will be converted to a JSON response.

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
'''
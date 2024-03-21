from flask import Flask
from flask_cors import CORS
from user.infrastructure.routers.user_router import user_router
from task.infrastructure.routers.task_router import task_router

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.register_blueprint(user_router)
app.register_blueprint(task_router)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
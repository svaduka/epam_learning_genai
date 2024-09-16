from flask import Flask, request, jsonify, render_template
# import user_bot as ub
from chat import chat_logic as cl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def process_user_input(user_input):
    return cl.process_user_input(user_input)



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print(f"User Input {user_input}")
    response = process_user_input(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
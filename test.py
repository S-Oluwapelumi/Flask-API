from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    print(type(data['prompt']))
    # To check 'prompt' and 'user' parameters are strings
    if isinstance(data.get('prompt'), str) and isinstance(data.get('user'), str):

        return 'Status == 200', 200
    else:
        return 'Invalid request', 400
    
if __name__ == '__main__':
    app.run(debug=True)

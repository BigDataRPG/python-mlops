from flask import Flask, abort
from transformers import pipeline
from pydantic import BaseModel


generator = pipeline('text-generation', model='gpt2')

app = Flask(__name__)

class Body(BaseModel):
    test: str


@app.route('/')
def first_page():
    return '<h1>Hello World! This is the self-document API to interact with GPT2 model and generate text</h1>'


@app.route('/error')
def error():
    abort(500, "Oops! Something went wrong...")
    
    
@app.post('/generate')
def predict(body: Body):
    results = generator(body.test, max_length=35, num_return_sequence=1)[0]
    return results


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
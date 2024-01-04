from flask import Flask, abort, jsonify, request
from transformers import pipeline
from pydantic import BaseModel
import asyncio

MAX_USERS = 1300
semaphore = asyncio.Semaphore(MAX_USERS)

generator = pipeline('text-generation', model='gpt2')

app = Flask(__name__)

class Body(BaseModel):
    test: str


@app.route('/')
def first_page():
    return '<h1>Hello World! This is the self-document API to interact with GPT2 model and generate text</h1>'


@app.route('/error')
def error():
    abort(404, "Oops! Something went wrong...")
    
    
async def generate_text_async(input_text):
    async with semaphore:
        try:
            if not input_text:
                return {"input_text": "", "generated_text": "Input text is empty"}
            else:
                generated_text = generator(input_text, max_length=100, num_return_sequences=1)[0]['generated_text']
                return {"input_text": input_text, "generated_text": generated_text}
        except Exception as e:
            return {"input_text": input_text, "generated_text": str(e)}


@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        request_data = request.get_json()
        input_text = request_data.get('text', '')
        if not input_text:
            return jsonify({"error": "Please provide text input"}), 400

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        generated_text = loop.run_until_complete(generate_text_async(input_text))

        return jsonify({"input_text": input_text, "generated_text": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
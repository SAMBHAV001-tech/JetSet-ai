from flask import Flask, request, jsonify
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Initialize the tokenizer, retriever, and model
tokenizer = RagTokenizer.from_pretrained('facebook/rag-token-nq')
retriever = RagRetriever.from_pretrained('facebook/rag-token-nq')
model = RagSequenceForGeneration.from_pretrained('facebook/rag-token-nq')

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_rag():
    query = request.json.get('query')  # Get user query from the request
    inputs = tokenizer(query, return_tensors="pt")
    retrieved_docs = retriever.retrieve(inputs['input_ids'], inputs['attention_mask'])
    generated_output = model.generate(input_ids=inputs['input_ids'], 
                                      attention_mask=inputs['attention_mask'], 
                                      retrieved_doc_ids=retrieved_docs)
    answer = tokenizer.decode(generated_output[0], skip_special_tokens=True)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Running on localhost:5000

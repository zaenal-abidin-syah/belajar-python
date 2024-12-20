from flask import Flask, request, jsonify, render_template
import torch
import numpy as np
from torch import nn, optim
# 38,1.0,24.0,3.0,0.0,0.0,0.0,1.0,6.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0
app = Flask(__name__)

# Define your model architecture
model = nn.Sequential(
    nn.Linear(30,8),
    nn.ReLU(),
    nn.Dropout(.2),
    
    nn.Linear(8,8),
    nn.ReLU(),
    nn.Dropout(.1),
    
    # nn.Linear(16,8),
    # nn.ReLU(),
    # nn.Dropout(.2),
    
    nn.Linear(8,4),
    nn.Sigmoid()
)
optimizer = optim.AdamW(model.parameters(), lr=0.0005)
criterion = nn.BCELoss() # model diakhiri sigmoid -> binary clf, multilabel clf
# criterion = nn.NLLLoss() # model diakhiri logsoftmax -> multiclass clf
# callback = Callback(model, outdir="model")

# Load weights into the model

model.load_state_dict(torch.load('./model/weights_best.pth'))
model.eval()  # Set model to evaluation mode

@app.route('/')
def index():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Example: Assume input is a JSON array of features
        data = request.json
        # return jsonify(data)
        # input_data = torch.tensor(data['features'], dtype=torch.float32).unsqueeze(0)  # Adjust shape as needed
        input_data = torch.FloatTensor(data['features'])  # Adjust shape as needed
        
        # Make prediction
        with torch.no_grad():
            output = model(input_data)
            probabilities = output.squeeze().tolist()
            predictions = (output > 0.5).int().tolist()
        
        return jsonify({
            'status': 'success',
            'prediction': predictions,
            'probabilities': probabilities
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

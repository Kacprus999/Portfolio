import torch
import torchvision.transforms as transforms

from PIL import Image
from NeuralNetwork import NeuralNetwork

def getPrediction(img_path, network_name):
    
    # Inicjacja sieci neuronowej
    neural_net = NeuralNetwork.NeuralNetwork()
    PATH = './NeuralNetwork/trained_networks/'
    img = Image.open(img_path)
    transform_tensor = transforms.ToTensor()(img).unsqueeze_(0)
    classes = ['glass', 'metal', 'paper', 'plastic']
    neural_net.load_state_dict(torch.load(PATH + network_name, map_location='cpu'))
    neural_net.eval()
    outputs = neural_net(transform_tensor)

    # Wyciągnięcie największej wagi co przekłada się na rozpoznanie klasy, w tym przypadku rodzju odpadu
    return classes[torch.max(outputs, 1)[1]]
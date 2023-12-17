import torch

device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

class StockTrainerNN(torch.nn.Module):
    def __init__(self):
        super(StockTrainerNN, self).__init__()

        # input layer
        self.layer1 = torch.nn.Linear(15, 20)
        # hidden layer
        self.layer2 = torch.nn.Linear(20, 20)
        # output layer
        self.layer3 = torch.nn.Linear(20, 5)

        # activation
        self.activation = torch.nn.ReLU()

        # dtype
        self.double()
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.activation(x)
        x = self.layer2(x)
        x = self.activation(x)
        x = self.layer3(x)
        return x
    
    def predict(self, x):
        return self.forward(x)

from torch import nn, cuda, backends

device = "cuda" if cuda.is_available() else "mps" if backends.mps.is_available() else "cpu"

class StockTrainerNN(nn.Module):
    def __init__(self):
        super(StockTrainerNN, self).__init__()

        # input layer
        self.layer1 = nn.Linear(15, 45)
        # hidden layer
        self.layer2 = nn.Linear(45, 20)
        # output layer
        self.layer3 = nn.Linear(20, 5)

        # activation
        self.activation = nn.ReLU()

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

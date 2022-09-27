import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class FcnTorch(nn.Module):
    def __init__(self, in_features=80, h1=512, h2=256, h3 = 128, h4 = 64, h5 = 32, out_features=45):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)    # input layer
        self.fc2 = nn.Linear(h1, h2)
        self.fc3 = nn.Linear(h2, h3)     
        self.fc4 = nn.Linear(h3, h4)     
        self.fc5 = nn.Linear(h4, h5)     
        self.out = nn.Linear(h5, out_features)  # output layer
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = self.out(x)
        return x
    
    def count_parameters(self):
        params = [p.numel() for p in self.parameters() if p.requires_grad]
        for item in params:
            print(f'{item:>7}')
        print(f'_______\n{sum(params):>7}{" <- Total trainable parameters"}')
        
        
class customLSTM(nn.Module):
        def __init__(self, in_features=80, h1 = 50, h2 = 30, out_features=45):
            super().__init__()
            pass
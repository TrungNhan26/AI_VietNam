import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2) == 0.26
print(output)

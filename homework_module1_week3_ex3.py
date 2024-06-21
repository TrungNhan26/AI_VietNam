import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        max_val = torch.max(x)            # Find the maximum value in the input tensor
        exp_x = torch.exp(x - max_val)    # Subtract max_val from each element and compute the exponential
        sum_exp_x = torch.sum(exp_x)      # Compute the sum of exponentials
        return exp_x / sum_exp_x          # Normalize by the sum of exponentials

data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == 0.0
print(output)

import torch
from torch import nn

torch.manual_seed(7)
vocab_size = 12
d_model = 4

embedding = nn.Embedding(vocab_size, d_model)   # E: [12, 4]
input_ids = torch.tensor([[2, 5, 2, 9]])       # [B=1, n=4]
x = embedding(input_ids)                       # [1, 4, 4]

print("E:", embedding.weight.shape)
print("input_ids:", input_ids.shape)
print("x:", x.shape)
print("x[0] - jedna sekwencja:", x[0].shape)
print("x[0, 0] to E[2]:", torch.equal(x[0, 0], embedding.weight[2]))
print("powtórzone ID daje ten sam wektor:",
      torch.equal(x[0, 0], x[0, 2]))


# Korzystamy z input_ids, x, nn i d_model z poprzedniego fragmentu.
max_seq_len = 32
position_embedding = nn.Embedding(max_seq_len, d_model)

n = input_ids.shape[1]                         # w przykładzie n = 4
positions = torch.arange(n).unsqueeze(0)      # [[0, 1, 2, 3]]
position_vectors = position_embedding(positions)
x_with_position = x + position_vectors

print("cała tabela pozycji:", position_embedding.weight.shape)  # [32, 4]
print("wybrane pozycje:", positions)
print("P dla tej sekwencji:", position_vectors.shape)           # [1, 4, 4]
print("X:", x.shape)                                             # [1, 4, 4]
print("H = X + P:", x_with_position.shape)                       # [1, 4, 4]

print("przed dodaniem pozycji wektory ID 2 są identyczne:",
      torch.equal(x[0, 0], x[0, 2]))
print("po dodaniu pozycji reprezentacje się różnią:",
      not torch.allclose(x_with_position[0, 0], x_with_position[0, 2]))
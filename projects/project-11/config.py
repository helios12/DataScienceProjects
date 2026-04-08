import torch

is_debug_mode = False
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
img_size = 256 if is_debug_mode else 640
num_epochs = 10 if is_debug_mode else 20
batch_size = 4
model_path = "vangogh_style_net.pth"
import torch.nn as nn


class StyleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 9, padding=4),
            nn.ReLU(inplace=True),

            nn.Conv2d(32, 64, 3, stride=2, padding=1),      # downsample
            nn.ReLU(inplace=True),

            nn.Conv2d(64, 128, 3, stride=2, padding=1),     # downsample
            nn.ReLU(inplace=True),

            nn.Conv2d(128, 64, 3, padding=1),
            nn.ReLU(inplace=True),

            # Upsample back to original size
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(64, 32, 3, padding=1),
            nn.ReLU(inplace=True),

            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(32, 3, 9, padding=4),
            nn.Tanh()  # output in [-1, 1]
        )

    def forward(self, x):
        return self.net(x)
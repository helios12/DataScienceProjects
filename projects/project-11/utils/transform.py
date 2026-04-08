from torchvision import transforms


def get_transform(img_size):
    return transforms.Compose([
    transforms.Resize(img_size+20),
    transforms.CenterCrop(img_size),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
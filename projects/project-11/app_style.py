import argparse
import sys
import torch

from config import img_size, device
from models.style_net import StyleNet
from PIL import Image
from torchvision import transforms
from utils.transform import get_transform


def apply_style(model_path, image_path, result_image_path):
    model = StyleNet().to(device)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    transform = get_transform(img_size)
    img = Image.open(image_path).convert("RGB")
    img = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        out = model(img)

    def denorm(x):
        mean = torch.tensor([0.485,0.456,0.406]).view(1,3,1,1).to(device)
        std  = torch.tensor([0.229,0.224,0.225]).view(1,3,1,1).to(device)
        return (x * std + mean).clamp(0,1)

    out_img = denorm(out)[0].cpu()
    transforms.ToPILImage()(out_img).save(result_image_path)
    

def main():
    parser = argparse.ArgumentParser(
        description="Apply a trained style transfer model to an image."
    )

    parser.add_argument("--model_path", type=str, required=True, help="Path to the trained model")
    parser.add_argument("--image_path", type=str, required=True, help="Path to the input image")
    parser.add_argument("--result_image_path", type=str, required=True, help="Path to save the result image")

    args = parser.parse_args()

    # Validation (redundant with required=True, but explicit as requested)
    if not args.model_path or not args.image_path or not args.result_image_path:
        print("Error: All arguments (--model_path, --image_path, --result_image_path) must be provided.")
        sys.exit(1)

    print("Model path:", args.model_path)
    print("Image path:", args.image_path)
    print("Result image path:", args.result_image_path)

    apply_style(args.model_path, args.image_path, args.result_image_path)


if __name__ == "__main__":
    main()

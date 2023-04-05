import warnings
warnings.filterwarnings(
    "ignore", message="User provided device_type of \'cuda\', but CUDA is not available. Disabling")

from tqdm import tqdm
import glob
import os
import argparse
from RealESRGAN import RealESRGAN
import numpy as np
from PIL import Image
import torch
import sys

parser = argparse.ArgumentParser(description='Real-ESRGAN options')
parser.add_argument('--input', '-i', required=True,
                    help='Input file path (can be an image or a folder)')
parser.add_argument('--output', '-o', required=True,
                    help='Output file path (can be an image or a folder')
parser.add_argument('--scale', '-s', type=int,
                    default=4, help='Upscale factor')
args = parser.parse_args()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

images = []
is_image = False
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']

if os.path.isdir(args.input):
    print(f"> Info: reading folder {args.input}")
    for extension in tqdm(image_extensions):
        images.extend(glob.glob(f"{args.input}/{extension}"))
    print(f"> Info: found {len(images)} images")

elif os.path.isfile(args.input) and args.input.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
    images = [args.input]
    is_image = True
else:
    print('> Error: file not recognized or folder not found')
    sys.exit()

if is_image == False:
    if os.path.isdir(args.output) == False:
        print('> Error: the output should be an existing folder')
        sys.exit()

print(f"> Info: loading ESRGAN-model with scale {args.scale}")
model = RealESRGAN(device, scale=args.scale)
model.load_weights(f'weights/RealESRGAN_x{args.scale}.pth', download=True)
print("> Info: ESRGAN-model loaded")

for path_to_image in tqdm(images, desc='Upscaling images', leave=True):
    image = Image.open(path_to_image).convert('RGB')
    sr_image = model.predict(image)
    if is_image == False:
        sr_image.save(f'{args.output}/{os.path.basename(path_to_image)}')
    else:
        sr_image.save(f'{args.output}')
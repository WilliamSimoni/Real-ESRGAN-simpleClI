# Installation
1. Download Anaconda: Go to the Anaconda download page at  and download the appropriate version of Anaconda for your operating system.
2. Install Anaconda: Follow the installation instructions for your operating system to install Anaconda on your computer. (Check “Add Anaconda3 to my PATH environment variable“).
3. Create a folder for the project. The folder will contain the ESRGAN model. 
4. Open the terminal in the folder. To do it:
5. Run the following commands:
```python
conda create -n RealESRGAN python=3.9.16
```
```python
conda activate RealESRGAN
pip install git+https://github.com/sberbank-ai/Real-ESRGAN.git
```

# How to Use
1. Open the terminal in the project folder. To do it:
2. Click on the folder path in the address bar at the top of the window to select it.
3. Replace the current path with "cmd" (without quotes) and press Enter.
4. Run ```conda activate RealESRGAN```
5. Run ```python .\upscale.py --help``` to see how to use the upscale script.
```
usage: upscale.py [-h] --input INPUT --output OUTPUT [--scale SCALE]

Real-ESRGAN options

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input image file path
  --output OUTPUT, -o OUTPUT
                        Output image file path
  --scale SCALE, -s SCALE
                        Upscale factor
```

# Example
In the project folder, create images and a results folder. In the images folder, put the input images. Then run:
```
python upscale.py -i ./images -o ./results -s 4
```

# Documentation for Setting up Image Cropping Environment 

Introduction
This documentation provides step-by-step instructions for setting up an environment for cropping images using Python. The environment setup includes creating a virtual environment, installing required pip modules, and creating the necessary folders.

## Prerequisites
To follow these instructions, you will need to have Python 3 and pip installed on your computer.

#### Step 1: Create a Virtual Environment
To create a virtual environment for image cropping, open your command prompt or terminal and navigate to your project directory. Then, run the following command:
```bash
python -m venv env
```
This command creates a new virtual environment named "env" in your project directory.

#### Step 2: Install Required Pip Modules
After creating the virtual environment, activate it by running the following command:
```bash
source env/bin/activate
```
Then, install the required pip modules by running the following command:
```bash
pip install -r requirements.txt
```
This command installs all the required modules listed in the "requirements.txt" file.

#### Step 3: Create the Necessary Folders
To prepare for image cropping, create two folders named "img" and "crop" in your project directory. The "img" folder will contain the original images, and the "crop" folder will contain the cropped images.

You can create the folders manually or use the following commands:
```bash
mkdir img
mkdir crop
```
## Conclusion
After completing these steps, you are ready to start cropping images using Python in your virtual environment. To use the virtual environment in your Python scripts, make sure to activate it before running any commands or scripts. You can activate the environment by running the command:
```bash
source env/bin/activate
python image_crop.py
```

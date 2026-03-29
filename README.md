# 😷🛡️ MaskGuard AI — Face Mask Detector

A real-time face mask detection system built with MobileNetV2, OpenCV, and Streamlit.
Classifies masked vs. unmasked faces via live webcam or image upload — wrapped in a polished web UI.
<img width="1440" height="810" alt="Screenshot 2026-03-28 at 1 49 20 PM" src="https://github.com/user-attachments/assets/f22a1447-dfcf-418e-8b14-f414b79465c5" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 29 PM" src="https://github.com/user-attachments/assets/fb6d86d4-c7f9-4546-966c-d8326514ed40" />
<img width="1440" height="805" alt="Screenshot 2026-03-28 at 1 49 36 PM" src="https://github.com/user-attachments/assets/704926e5-4169-455a-8bb1-39ef26ddb77e" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 43 PM" src="https://github.com/user-attachments/assets/aec2f81e-f1c3-4c0f-a40d-ff0f59dddac7" />

---

📌 Table of Contents

Overview
Features
Tech Stack
Project Structure
Prerequisites
Setup & Installation
Downloading Required External Files
Running the App
Training the Model
Model Architecture & Results
Troubleshooting
Author
License


🔍 Overview
MaskGuard AI is a deep learning computer vision project that detects whether a person is wearing a face mask in real time. It uses transfer learning on top of MobileNetV2 (pretrained on ImageNet), fine-tuned on a dataset of 7,553 labelled face images.
The entire application is served through a Streamlit web interface with four pages:

A landing home page with project info and model stats
A live webcam detection page
An image upload detection page
An analytics dashboard showing training curves and dataset statistics

Face localisation before classification is handled by OpenCV's Haar Cascade face detector.

✨ Features

🎥 Live webcam detection — real-time bounding boxes with Mask / No Mask labels and confidence scores
🖼️ Image upload detection — upload any JPG or PNG and get instant results
📊 Analytics dashboard — training accuracy/loss curves, dataset distribution charts, and full model architecture breakdown
🧠 MobileNetV2 transfer learning — high accuracy with a lightweight, deployment-ready model (~2.4M parameters)
🌐 Streamlit web UI — fully browser-based, no GUI toolkit required
⚡ Command-line runnable — single command to launch the full app


<img width="600" height="460" alt="image" src="https://github.com/user-attachments/assets/8cefe600-0d5f-417d-aa13-cccbb46fe971" />

<img width="601" height="618" alt="image" src="https://github.com/user-attachments/assets/be305699-4937-4faa-b9a8-cdb46fa34a1a" />

Note: A face_detector/ folder with Caffe SSD model files is required for detect_mask_video.py.
The main Streamlit app (app.py) uses OpenCV's Haar Cascade which is bundled with opencv-python and requires no separate download.


dataset link - https://www.kaggle.com/datasets/omkargurav/face-mask-dataset

✅ Prerequisites
Ensure the following are installed on your machine before proceeding:

Python 3.7 or higher — Download
pip — comes bundled with Python
Git — Download
A webcam — only needed for the Live Webcam detection page

Check your Python version:
python --version
# Expected: Python 3.7.x or higher

🚀 Setup & Installation
Follow every step in order. Do not skip steps.
Step 1 — Clone the repository

git clone https://github.com/RANVEER12082005/FACE-MASK-DETECTOR-PROJECT.git
cd FACE-MASK-DETECTOR-PROJECT

Step 2 — Create a virtual environment
This keeps the project's dependencies isolated from your system Python.
# Create the environment
python -m venv venv

# Activate it
# macOS / Linux:
source venv/bin/activate

# Windows (Command Prompt):
venv\Scripts\activate.bat

# Windows (PowerShell):
venv\Scripts\Activate.ps1

You should see (venv) at the start of your terminal prompt. Keep this active for all remaining steps.

step 3 — Install dependencies
pip install tensorflow opencv-python streamlit numpy matplotlib scikit-learn imutils

If requirements.txt has been populated, you can alternatively run:
pip install -r requirements.txt

Installation takes 2–5 minutes depending on your internet speed (TensorFlow is ~500MB).

📥 Downloading Required External Files
Dataset (required to train the model)
Download the face mask image dataset from Kaggle:
👉 Face Mask Dataset — Kaggle
After downloading, extract the archive and place images into the correct folders:
dataset/
├── with_mask/        ← paste all masked-face images here
└── without_mask/     ← paste all unmasked-face images here

If you already have a pre-trained model saved in models/, you can skip the dataset download and go straight to running the app.

Face Detector Caffe Model (required for detect_mask_video.py CLI only)
The standalone CLI script detect_mask_video.py uses an OpenCV DNN-based SSD face detector. Download these two files and place them in a folder called face_detector/ at the project root:

mkdir face_detector

 Running the App
Make sure your virtual environment is activated ((venv) visible in terminal), then run:
streamlit run app.py

This will start the Streamlit server and automatically open the app in your browser at:
http://localhost:8501

Navigating the app
Use the sidebar to switch between pages:
PageWhat it does🏠 HomeProject overview, model stats, how-it-works pipeline📷 Live WebcamReal-time mask detection from your camera🖼️ Upload ImageUpload a photo and detect mask / no-mask📊 DashboardTraining curves, dataset distribution, architecture summary
Press Ctrl+C in the terminal to stop the server.

This will:

Load and preprocess images from dataset/with_mask/ and dataset/without_mask/
Apply data augmentation (rotation, zoom, horizontal flip, shear)
Fine-tune MobileNetV2 with a custom classification head
Save the trained model to the models/ directory
Generate a plot.png showing training accuracy and loss curves

Training takes approximately 5–15 minutes depending on your hardware. A GPU is recommended but not required.

🔬 Model Architecture & Results
Architecture
The model stacks a custom classification head on top of MobileNetV2 with its top layers removed:
Input (224 × 224 × 3)
    ↓
MobileNetV2 (frozen, ImageNet weights) — feature extraction
    ↓
AveragePooling2D (7 × 7)
    ↓
Flatten
    ↓
Dense(128, activation=ReLU)
    ↓
Dropout(0.5)
    ↓
Dense(2, activation=Softmax)   →   [With Mask, Without Mask]

<img width="632" height="721" alt="image" src="https://github.com/user-attachments/assets/31b8852b-16a9-4af0-b254-0b315dd9228a" />

Troubleshooting
ModuleNotFoundError: No module named 'streamlit' (or any other module)
→ Your virtual environment isn't activated, or you skipped the install step. Run:

source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install streamlit tensorflow opencv-python numpy matplotlib scikit-learn imutils

FileNotFoundError for deploy.prototxt or .caffemodel
→ These are only needed for detect_mask_video.py. Follow the Caffe Model download instructions above.
No model found / app crashes on startup
→ Either train the model first (python train_mask_detector.py --dataset dataset) or ensure a saved model exists in the models/ folder.
Webcam page shows a blank or error
→ Check that your webcam is connected and not in use by another application. On some systems you may need to grant browser camera permissions at http://localhost:8501.
TensorFlow installation fails on Apple Silicon (M1/M2/M3 Mac)
→ Use:
pip install tensorflow-macos

pip install tensorflow is very slow
→ This is normal — TensorFlow is a large package (~500MB). Wait it out or use a faster internet connection.

👨‍💻 Author
Ranveer — @RANVEER12082005

📄 License
This project is open-source and available under the MIT License.



---

## 👨‍💻 Author

**Ranveer** — [@RANVEER12082005](https://github.com/RANVEER12082005)

---

> ⭐ If you found this project helpful, please give it a star!

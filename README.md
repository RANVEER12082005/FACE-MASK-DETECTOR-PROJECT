# 😷 Face Mask Detector

Real-time face mask detection using MobileNetV2, OpenCV, and TensorFlow/Keras — classifies masked vs. unmasked faces from webcam feed or static images, with a built-in analytics dashboard.
<img width="1440" height="810" alt="Screenshot 2026-03-28 at 1 49 20 PM" src="https://github.com/user-attachments/assets/f22a1447-dfcf-418e-8b14-f414b79465c5" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 29 PM" src="https://github.com/user-attachments/assets/fb6d86d4-c7f9-4546-966c-d8326514ed40" />
<img width="1440" height="805" alt="Screenshot 2026-03-28 at 1 49 36 PM" src="https://github.com/user-attachments/assets/704926e5-4169-455a-8bb1-39ef26ddb77e" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 43 PM" src="https://github.com/user-attachments/assets/aec2f81e-f1c3-4c0f-a40d-ff0f59dddac7" />

---

📌 Table of Contents

About the Project
Features
Tech Stack
Project Structure
Prerequisites
Installation & Setup
Downloading Required Files
Usage
Model Training
Results
Known Issues & Troubleshooting
Author
License


📖 About the Project
The Face Mask Detector is a deep learning-powered computer vision system that automatically detects whether a person is wearing a face mask or not — in real time.
It uses Transfer Learning with MobileNetV2 as the base model (pre-trained on ImageNet), with custom classification layers added on top and fine-tuned on a labelled dataset of masked and unmasked faces. Face localization is handled by OpenCV's DNN module using a Caffe-based SSD model before passing detected faces to the mask classifier.
The project includes multiple interfaces — webcam-based live detection, static image upload detection, and an analytics dashboard.

✨ Features

🎥 Real-time webcam detection with bounding boxes and confidence scores
🖼️ Static image upload detection via image_upload.py
📊 Analytics dashboard (dashboard.py) for monitoring detection stats
🟢 Green bounding box → Mask detected
🔴 Red bounding box → No mask detected
🧠 MobileNetV2 transfer learning for high accuracy with a lightweight model
⚡ Command-line executable — no GUI setup required


🛠️ Tech Stack
LibraryVersionPurposePython3.7+Core languageTensorFlow / Keras2.xModel building & trainingMobileNetV2—Pre-trained backbone (transfer learning)OpenCV (opencv-python)4.xImage processing & face detectionNumPy—Numerical operationsMatplotlib—Training accuracy/loss plotsscikit-learn—Model evaluation metricsimutils—Image utility functions

📁 Project Structure
FACE-MASK-DETECTOR-PROJECT/
│
├── dataset/
│   ├── with_mask/              # Images of people wearing masks
│   └── without_mask/           # Images of people not wearing masks
│
├── face_detector/              # ⚠️ Must be downloaded separately (see below)
│   ├── deploy.prototxt         # Caffe model architecture config
│   └── res10_300x300_ssd_iter_140000.caffemodel  # Pre-trained face detector weights
│
├── models/                     # Saved trained mask detector models
│
├── train_mask_detector.py      # Train the MobileNetV2 mask classifier
├── detect_mask_video.py        # Real-time webcam mask detection
├── webcam_detection.py         # Alternate webcam detection script
├── image_upload.py             # Static image mask detection
├── app.py                      # Main application entry point
├── dashboard.py                # Analytics dashboard
├── model_utils.py              # Shared model loading utilities
├── requirements.txt            # Python dependencies
└── README.md

✅ Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.7 or higher — Download Python
pip (comes with Python)
Git — Download Git
A working webcam (only required for real-time detection scripts)

Verify your Python version:
bashpython --version
# or
python3 --version

🚀 Installation & Setup
Follow these steps exactly to set up and run the project from scratch.
Step 1 — Clone the Repository
bashgit clone https://github.com/RANVEER12082005/FACE-MASK-DETECTOR-PROJECT.git
cd FACE-MASK-DETECTOR-PROJECT
Step 2 — Create a Virtual Environment (Recommended)
Using a virtual environment keeps dependencies isolated and avoids version conflicts.
bash# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
You should now see (venv) in your terminal prompt.
Step 3 — Install Dependencies
bashpip install tensorflow opencv-python numpy matplotlib scikit-learn imutils

Note: If requirements.txt is populated in a future update, you can alternatively run:
bashpip install -r requirements.txt


📥 Downloading Required Files
The project needs two additional resources that are not stored in this repository due to file size:
1. Face Detector Model (Caffe SSD)
The OpenCV face detector requires two files. Download them and place them inside a folder named face_detector/ at the project root.
bashmkdir face_detector
Download the files:

deploy.prototxt
res10_300x300_ssd_iter_140000.caffemodel

Place both files inside face_detector/. Your structure should look like:
face_detector/
├── deploy.prototxt
└── res10_300x300_ssd_iter_140000.caffemodel
2. Training Dataset
Download the face mask dataset from Kaggle:
👉 Face Mask Dataset — Kaggle
After downloading, extract and place images into:
dataset/
├── with_mask/       ← paste masked face images here
└── without_mask/    ← paste unmasked face images here

🧪 Usage
All scripts are run from the terminal inside the project root directory. Make sure your virtual environment is activated.
1. Train the Mask Detector Model
Run this first if you don't have a pre-trained model saved in models/:
bashpython train_mask_detector.py --dataset dataset
This will train the MobileNetV2 model and save the output to the models/ directory. A training accuracy/loss graph (plot.png) will also be generated.

2. Real-Time Webcam Detection
bashpython detect_mask_video.py
or alternatively:
bashpython webcam_detection.py
A webcam window will open showing live detection with bounding boxes.
Press Q to quit.

3. Detect Mask in a Static Image
bashpython image_upload.py --image path/to/your/image.jpg
Replace path/to/your/image.jpg with the actual path to an image file on your system.

4. Run the Main App
bashpython app.py

5. Launch the Analytics Dashboard
bashpython dashboard.py

🔬 Model Training Details
The classifier is built on top of MobileNetV2 with its top classification head removed. Custom fully-connected layers are appended and trained for binary classification (mask / no mask).
ParameterValueBase ModelMobileNetV2 (ImageNet weights)OptimizerAdamLoss FunctionBinary Cross-EntropyEpochs20Batch Size32Input Size224 × 224 pxData AugmentationRotation, zoom, horizontal flip, shear
Face detection before classification is handled by OpenCV's DNN module using a Caffe-based Single Shot Detector (SSD) model.

📊 Results
MetricValueTraining Accuracy~99%Validation Accuracy~98%Model Parameters~2.4M
The training curves are saved to plot.png in the project root after training.

🐛 Known Issues & Troubleshooting
ModuleNotFoundError for any package
→ Make sure your virtual environment is activated and you've run the install step.
FileNotFoundError for deploy.prototxt or .caffemodel
→ You haven't downloaded the face detector files. Follow the Downloading Required Files section above.
Webcam not opening / black screen
→ Check that your webcam is connected and not being used by another application.
TensorFlow installation issues on Apple Silicon (M1/M2/M3)
→ Use pip install tensorflow-macos instead of tensorflow.
No module named 'cv2'
→ Run pip install opencv-python.

👨‍💻 Author
Ranveer — @RANVEER12082005

📄 License
This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Ranveer** — [@RANVEER12082005](https://github.com/RANVEER12082005)

---

> ⭐ If you found this project helpful, please give it a star!

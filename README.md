# 😷 Face Mask Detector

A real-time face mask detection system built with **Python**, **OpenCV**, **TensorFlow/Keras**, and **MobileNetV2**. The model classifies whether a person is wearing a face mask or not — using both static images and live webcam feeds.
preview of the project 
<img width="1440" height="810" alt="Screenshot 2026-03-28 at 1 49 20 PM" src="https://github.com/user-attachments/assets/f22a1447-dfcf-418e-8b14-f414b79465c5" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 29 PM" src="https://github.com/user-attachments/assets/fb6d86d4-c7f9-4546-966c-d8326514ed40" />
<img width="1440" height="805" alt="Screenshot 2026-03-28 at 1 49 36 PM" src="https://github.com/user-attachments/assets/704926e5-4169-455a-8bb1-39ef26ddb77e" />
<img width="1440" height="808" alt="Screenshot 2026-03-28 at 1 49 43 PM" src="https://github.com/user-attachments/assets/aec2f81e-f1c3-4c0f-a40d-ff0f59dddac7" />

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

The **Face Mask Detector** was developed to help promote public safety by automatically detecting whether individuals are wearing face masks. It leverages deep learning and computer vision techniques to perform real-time classification.

This project uses **transfer learning** with **MobileNetV2** as the base model, fine-tuned on a dataset of masked and unmasked faces. Detection is powered by **OpenCV's DNN face detector** (Caffe-based SSD model).

---

## ✨ Features

- 🔍 **Real-time detection** via webcam or video stream
- 🖼️ **Static image detection** from file
- 🎯 **High accuracy** using MobileNetV2 transfer learning
- 📦 **Lightweight model** suitable for deployment
- 🟢 Green bounding box for **"Mask"**, 🔴 Red for **"No Mask"**
- 📊 Confidence score displayed on each detection

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.7+ | Core programming language |
| TensorFlow / Keras | Model building and training |
| MobileNetV2 | Pre-trained backbone (transfer learning) |
| OpenCV | Image processing & face detection |
| NumPy | Numerical computations |
| Matplotlib | Plotting training graphs |
| scikit-learn | Evaluation metrics |
| imutils | Image utility functions |

---

## 📁 Project Structure

```
FACE-MASK-DETECTOR-PROJECT/
│
├── dataset/
│   ├── with_mask/          # Images of people wearing masks
│   └── without_mask/       # Images of people without masks
│
├── face_detector/
│   ├── deploy.prototxt      # Caffe model config
│   └── res10_300x300_ssd_iter_140000.caffemodel
│
├── train_mask_detector.py   # Script to train the model
├── detect_mask_image.py     # Detect mask in a static image
├── detect_mask_video.py     # Detect mask in real-time video
├── mask_detector.model      # Saved trained model
├── plot.png                 # Training accuracy/loss graph
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Webcam (for real-time detection)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/RANVEER12082005/FACE-MASK-DETECTOR-PROJECT.git
cd FACE-MASK-DETECTOR-PROJECT
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install required dependencies**

```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

### 🏋️ Train the Model

```bash
python train_mask_detector.py --dataset dataset
```

### 🖼️ Detect Mask in an Image

```bash
python detect_mask_image.py --image path/to/image.jpg
```

### 📹 Detect Mask in Real-Time Video

```bash
python detect_mask_video.py
```

> Press **`Q`** to quit the video stream.

---

## 🔬 Model Training

The model uses **MobileNetV2** as the base with the top layers removed. Custom classification layers are added and the model is trained using:

- **Optimizer:** Adam
- **Loss Function:** Binary Cross-Entropy
- **Epochs:** 20
- **Batch Size:** 32
- **Data Augmentation:** Rotation, zoom, flip, shear

The face detector uses a **Caffe-based SSD model** to locate faces in frames before passing them to the mask classifier.

---

## 📊 Results

| Metric | Value |
|--------|-------|
| Training Accuracy | ~99% |
| Validation Accuracy | ~98% |
| Model Parameters | ~2.4M |

The training loss and accuracy curves are saved as `plot.png` after training.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ranveer** — [@RANVEER12082005](https://github.com/RANVEER12082005)

---

> ⭐ If you found this project helpful, please give it a star!

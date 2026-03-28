import ssl
import certifi
import os

ssl._create_default_https_context = ssl.create_default_context

import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import AveragePooling2D, Dropout, Flatten, Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# ── Settings ──────────────────────────────────────────
DATASET_PATH  = "dataset"
MODEL_PATH    = "models/mask_detector.h5"
LEARNING_RATE = 1e-4
EPOCHS        = 20
BATCH_SIZE    = 32
IMAGE_SIZE    = 224

print("[INFO] Loading images...")

data   = []
labels = []

# ── Load images from both folders ─────────────────────
for category in ["with_mask", "without_mask"]:
    folder = os.path.join(DATASET_PATH, category)
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        try:
            image = cv2.imread(img_path)
            image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
            image = img_to_array(image)
            image = preprocess_input(image)
            data.append(image)
            labels.append(category)
        except Exception as e:
            print(f"Skipping {img_path}: {e}")

print(f"[INFO] Loaded {len(data)} images")

# ── Encode labels ──────────────────────────────────────
le     = LabelEncoder()
labels = le.fit_transform(labels)
labels = to_categorical(labels, num_classes=2)
labels = np.array(labels)
data   = np.array(data, dtype="float32")

# ── Split into train and test ──────────────────────────
(trainX, testX, trainY, testY) = train_test_split(
    data, labels, test_size=0.20, stratify=labels, random_state=42
)

# ── Build model using MobileNetV2 ─────────────────────
print("[INFO] Building model...")

baseModel = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_tensor=Input(shape=(IMAGE_SIZE, IMAGE_SIZE, 3))
)

headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(7, 7))(headModel)
headModel = Flatten()(headModel)
headModel = Dense(128, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(2, activation="softmax")(headModel)

model = Model(inputs=baseModel.input, outputs=headModel)

# Freeze base model layers
for layer in baseModel.layers:
    layer.trainable = False

# ── Compile ────────────────────────────────────────────
model.compile(
    loss="categorical_crossentropy",
    optimizer=Adam(learning_rate=LEARNING_RATE),
    metrics=["accuracy"]
)

# ── Train ──────────────────────────────────────────────
print("[INFO] Training model... (this may take a few minutes)")

history = model.fit(
    trainX, trainY,
    batch_size=BATCH_SIZE,
    validation_data=(testX, testY),
    epochs=EPOCHS
)

# ── Save model ─────────────────────────────────────────
print("[INFO] Saving model...")
model.save(MODEL_PATH)
print(f"[INFO] Model saved to {MODEL_PATH}")

# ── Plot accuracy & loss ───────────────────────────────
plt.style.use("ggplot")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(history.history["accuracy"],     label="Train Accuracy")
ax1.plot(history.history["val_accuracy"], label="Val Accuracy")
ax1.set_title("Accuracy")
ax1.set_xlabel("Epoch")
ax1.legend()

ax2.plot(history.history["loss"],     label="Train Loss")
ax2.plot(history.history["val_loss"], label="Val Loss")
ax2.set_title("Loss")
ax2.set_xlabel("Epoch")
ax2.legend()

plt.tight_layout()
plt.savefig("models/training_plot.png")
plt.show()
print("[INFO] Training plot saved to models/training_plot.png")
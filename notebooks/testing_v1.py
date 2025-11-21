import os
import json
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

ROOT = ".."
MODEL_PATH = f"{ROOT}/models/model_v2.keras"
DATA_DIR = f"{ROOT}/data/test_set"
RESULT_PATH = f"{ROOT}/results/test_v2_user1.json"

print("Loading model:", MODEL_PATH)

model = load_model(MODEL_PATH)
model.summary()

# ================================
# FIXED IMAGE SIZE (User-2 used 128x128)
# ================================
IMG_SIZE = 128
BATCH_SIZE = 32

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),   # ✔ CORRECTED
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)

# Make predictions
pred_probs = model.predict(test_generator)

# For 2-class softmax output, choose the index of max probability
pred_labels = np.argmax(pred_probs, axis=1)

true_labels = test_generator.classes

# Calculate metrics
accuracy  = accuracy_score(true_labels, pred_labels)
precision = precision_score(true_labels, pred_labels)
recall    = recall_score(true_labels, pred_labels)
f1        = f1_score(true_labels, pred_labels)

results = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1)
}

print("\n=== MODEL v2 RESULTS ON USER 1 DATASET ===")
print(json.dumps(results, indent=4))

os.makedirs("results", exist_ok=True)

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=4)

print(f"\nSaved results to {RESULT_PATH}")

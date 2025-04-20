import numpy as np  # NumPy
from PIL import Image, ImageOps  # Görüntü işlemleri
from tensorflow.keras.models import load_model  # Model yükleme 

def get_class(image_path, model_path, labels_path):
        # Modeli yükle
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()
    
    # Görüntü ön işleme
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Tahmin yap
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    return class_name, confidence_score


# **BlindSight: AI Scene Describer**  

🚀 **BlindSight** is an AI-powered application that provides **real-time scene descriptions for visually impaired users**. It captures frames from a live video feed, processes them using **Google Gemini Pro Vision**, and generates detailed textual descriptions of the surroundings.  

---

## 📌 **Features**  
✅ **Real-time scene descriptions** using AI 📝  
✅ **Webcam-based video processing** 📷  
✅ **Optimized API usage** to reduce quota consumption ⚡  
✅ **User-friendly Streamlit interface** 🎨  

---

## 🛠 **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/BlindSight-AI-Scene-Describer.git
cd BlindSight-AI-Scene-Describer
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Google Gemini API Key**  
Replace your API key inside `main.py`:  
```python
API_KEY = "your-google-api-key"
```

---

## ▶️ **Usage**  

Run the Streamlit app:  
```bash
streamlit run main.py
```

- Click **"Start Video Analysis"** to begin.  
- Click **"Stop"** to end the analysis.  
- The app captures frames and provides **real-time AI-generated descriptions**.  

---

## 📂 **Project Structure**  
```
📁 BlindSight-AI-Scene-Describer
 ┣ 📜 main.py             # Main application code
 ┣ 📜 requirements.txt    # Required dependencies
 ┣ 📜 README.md           # Project documentation
 ┗ 📜 .gitignore          # Git ignore file
```

---

## 🔧 **Requirements**  
- Python 3.8+  
- OpenCV (`cv2`)  
- Streamlit  
- Pillow (`PIL`)  
- Google Generative AI SDK  

---

## 📜 **License**  
This project is licensed under the **MIT License**.  

---

### 🚀 **Contributions & Support**  
- Feel free to open **issues** or submit **pull requests**.  
- Star ⭐ this repository if you find it helpful!  

---


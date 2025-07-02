# PlateformeML

**PlateformeML** is an intuitive web application for automated machine learning. It allows users to upload their own datasets, train various machine learning models, visualize results, and replay experiments—all from a simple browser interface. The project is built with a **Django backend** and a **HTML / Bootstrap / JavaScript frontend** *(React is not used yet but planned for a future version)*.

---

## 🚀 Features

- 📂 **CSV dataset upload**
- 📊 **Model selection (classification or regression: SVM, RandomForest, KNN, etc.)**
- 🧪 **Customizable hyperparameters**
- 📈 **Result visualization (confusion matrix, ROC curves, accuracy, etc.)**
- 💾 **Model and experiment saving**
- 👥 **User session management**

---

## 🛠️ Tech Stack

| Component        | Stack                              |
|------------------|-------------------------------------|
| Frontend         | **HTML**, **Bootstrap**, **JavaScript** |
| Backend          | **Django**, **Django REST Framework** |
| Machine Learning | **Scikit-learn**, **Pandas**, **Numpy**, **Matplotlib** |
| Database         | **PostgreSQL** *(or SQLite for local testing)* |
| Authentication   | Django Auth (session-based) or JWT (optional) |

---

## 📚 How to Use

1. **Upload a CSV dataset**
2. **Choose a model (e.g., SVM, RandomForest, KNN...)**
3. **Set hyperparameters**
4. **Train the model and view the results**
5. **Save the session and replay experiments later**

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/FlorianTSUALA/PlateformeML.git
cd PlateformeML

# Backend setup (Django)
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# The frontend (HTML/Bootstrap/JS) is served via Django templates

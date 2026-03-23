# 🎬 Movie Recommendation System (Hybrid - Production Ready)

## 📌 Overview

This project is a **Hybrid Movie Recommendation System** that suggests movies using:

* **Collaborative Filtering** (Cosine Similarity)
* **Content-Based Filtering** (Genre Similarity)

It combines both approaches to provide **more accurate and reliable recommendations**.

---

## 🚀 Features

* 🔍 Movie recommendations based on user selection
* 🧠 Hybrid recommendation engine (collaborative + content-based)
* ⚡ Fast similarity computation using cosine similarity
* 🧩 Modular code structure (production-style)
* 🎨 Interactive UI using Streamlit

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## 📊 Dataset

We use the **MovieLens (ml-latest-small)** dataset.

### Files used:

* `movies.csv`
* `ratings.csv`

---

## 📁 Project Structure

```bash
recommendation-system/
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── model.py
│   ├── recommend.py
│
├── models/
│   ├── cosine.pkl
│   ├── genre.pkl
│
├── notebook/
│   └── experimentation.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Collaborative Filtering

* Builds a **user-movie matrix**
* Uses **cosine similarity**
* Recommends movies liked by similar users

---

### 2️⃣ Content-Based Filtering

* Uses **movie genres**
* Finds movies with similar content

---

### 3️⃣ Hybrid Model

* Combines both methods:

```text
Hybrid Score = (0.7 × Collaborative) + (0.3 × Content)
```

* Produces better and more balanced recommendations

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd recommendation-system
```

---

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Train Models (IMPORTANT)

Run this once to generate similarity files:

```bash
python -c "from src.data_loader import load_data; from src.preprocess import create_matrix; from src.model import train_collaborative, train_content; movies, ratings = load_data(); import pandas as pd; data = pd.merge(ratings, movies, on='movieId'); matrix = create_matrix(data); train_collaborative(matrix); train_content(movies)"
```

This will create:

* `models/cosine.pkl`
* `models/genre.pkl`

---

### Step 5: Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Open the app in browser
2. Select a movie from dropdown
3. Click **Recommend**
4. Get top 10 similar movies 🎉

---

## 💼 Resume Highlight

Built a Hybrid Movie Recommendation System using Collaborative Filtering (Cosine Similarity) and Content-Based Filtering (Genre Similarity), deployed with an interactive Streamlit interface.

---

## 🔮 Future Improvements

* 🎬 Add movie posters using TMDB API
* ⭐ Include ratings/popularity weighting
* 🧠 Use tags for better content understanding
* ☁️ Deploy on Streamlit Cloud / AWS

---

## 👨‍💻 Author

Swapnil Salvi
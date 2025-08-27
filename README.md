# 🛡️ CommentGuard

A Streamlit-powered machine learning project for CS 250 that detects spam in YouTube comments.
This app lets you **train your own model**, **predict comment labels**, and **visualize performance** — all in an interactive interface.

---

## ✨ Features

* 🔮 **Prediction**: Classify new comments as spam or not spam.
* 🏗️ **Custom Training**: Build and save your own model with labeled data.
* 📊 **Visualization**: Explore trends and model performance with interactive charts.
* ⚡ Easy to use — everything runs inside a Streamlit app.

---

## 📂 Project Structure

```
├── Introduction.py             # App introduction / landing page
├── 1Predict Comment.py         # Predict spam/ham for new comments
├── 2Create Your Own Model.py   # Train a custom machine learning model
├── 3Visualization.py           # Visualize results and comment distributions
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/comment-guard.git
cd comment-guard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run Introduction.py
```

---

## 🧠 How It Works

* Preprocesses and vectorizes comment text.
* Trains a machine learning model (Logistic Regression / Naive Bayes, etc.).
* Saves the trained model for reuse.
* Provides interactive plots to understand predictions and dataset trends.

---

## 📸 Example

```text
Input:  "Click here to claim your free prize!!!"
Output: Spam ✅  

Input:  "I really enjoyed this video, thanks!"
Output: Not Spam 🎉
```

---

## 🛠️ Tech Stack

* Python 3.11+
* Streamlit
* pandas, numpy
* scikit-learn
* matplotlib, seaborn

---

## 📌 Future Improvements

* Add YouTube API integration for live comment fetching.
* Expand UI with advanced filters and dataset upload.

---

## 📄 License

MIT License. Free to use, modify, and share.

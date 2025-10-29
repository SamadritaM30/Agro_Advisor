# 🌾 AI-Powered Agro Advisory System

An AI-enabled advisory system designed to empower Indian farmers with timely and actionable insights on crops, soil, weather, pest control, and more — using state-of-the-art Natural Language Processing (NLP), Retrieval-Augmented Generation (RAG), and Machine Learning (ML).

---

## 📌 Overview

The Agro Advisory System is a multi-modal AI solution that helps farmers:
- Understand and categorize their queries 
- Retrieve relevant answers from structured data & documents (RAG)
- Get predictive insights (e.g., crop yield, soil fertility)
- Receive actionable, personalized recommendations

> This project addresses real-world challenges in Indian agriculture like low productivity, limited access to scientific knowledge, and low adoption of digital advisory systems.

---

## 🧠 Core Features

- 🔍 **Intent Classification**: Categorizes farmer queries into 20+ agriculture-related categories (e.g., crop health, irrigation, pest management).
- 📚 **Knowledge Layer with RAG**: Uses Retrieval-Augmented Generation to provide accurate answers using document embeddings and vector search.
- 📊 **ML-based Structured Models**: Predictive models using XGBoost and other algorithms for insights like expected yield, fertilizer need, etc.
- 🗣️ **Multi-modal Inputs**: Accepts queries via text, voice, and images.
- 🌐 **FastAPI Backend + Streamlit Frontend**: Robust backend API with an intuitive frontend for user interaction.
- 🔁 **Feedback Loop**: Learns and improves with user feedback over time.

---

## 🚀 Technologies Used

| Component | Tech Stack |
|----------|------------|
| **NLP Pipeline** | Tokenization, Cleaning, TF-IDF / BERT / DistilBERT |
| **Vector Search** | FAISS, Sentence Transformers |
| **ML Models** | XGBoost, Scikit-learn |
| **RAG** | HuggingFace Transformers |
| **Backend** | FastAPI |
| **Frontend** | Streamlit / React (optional) |

---

## ✅ Phases Completed

- [x] **Phase 1**: Dataset Preparation & Data Preprocessing 
- [x] **Phase 2**: Intent Classification  
- [x] **Phase 3**: NLP Pipelines (Text Preprocessing, Feature Extraction)  
- [x] **Phase 4**: RAG Component for Answer Generation  
- [x] **Phase 5**: ML-based Structured Prediction Models  
- [x] **Phase 6**: APIs + Model + RAG + LLM Integration 
- [ ] **Phase 7**: UI, Feedback Loop and Continuous Learning 

---

## 🧪 Sample Use Case

> **Input (Text)**: _"My tomato plants have white spots on leaves, what should I do?"_

- ✅ Intent: Crop Disease  
- 🔍 RAG Answer: “This symptom indicates powdery mildew. You can use sulfur-based fungicides...”  
- 📈 ML Insight: Predicted low yield if left untreated  
- 💡 Action: Spray fungicide X , suggested


---

## 📚 Datasets -

  https://www.kaggle.com/datasets/samadritam30/farmer-queries
  PPT OF DATASET HUNT : https://www.canva.com/design/DAGpSkbv4h8/_JbKRh31dfXYJ-3FnlrrdQ/edit?utm_content=DAGpSkbv4h8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

> **Input (Text)**: _"My tomato plants have white spots on leaves, what should I do?"_

- ✅ Intent: Crop Disease  
- 🔍 RAG Answer: “This symptom indicates powdery mildew. You can use sulfur-based fungicides...”  
- 📈 ML Insight: Predicted low yield if left untreated  
- 💡 Action: Spray fungicide X , suggested

---


## 💡 Vision

To revolutionize Indian agriculture by enabling **data-driven decision making** at the grassroots level and **bridging the gap** between scientific knowledge and rural practice - ultimately contributing to **food security**, **better crop yield**, and **farmer empowerment**.


#  Demographic & Behavioral Inference Without PII

##  Problem Statement

With the rising importance of user privacy and increasing regulatory pressures (GDPR, CCPA, etc.), traditional personalization approaches that rely on cookies or Personally Identifiable Information (PII) are becoming obsolete.  

**Hackathon Challenge (Problem Statement 4 - Synapses '25):**  
Create a machine learning model or inference engine that estimates demographics (age bracket, gender, affluence) and behavioral personas (browsing style, purchase intent) purely from anonymized on-site behavior like:
- Click patterns
- Scroll depth
- Dwell time
- Device/browser data  

The goal is to provide **actionable personalization** — without breaching privacy.

---

##  Why This Project Matters

- Enables **privacy-first personalization** strategies.
- Helps **e-commerce platforms** understand visitors using only anonymous behavioral data.
- Powers **real-time user segmentation** and dynamic content targeting.
- Facilitates **cookie-less marketing** for the post-privacy era.

---

##  Key Challenges

-  No access to real-world behavioral datasets due to privacy restrictions.
-  Simulating realistic behavior across devices, time zones, and usage patterns.
-  Building interpretable models that can infer abstract traits from noisy, synthetic data.
-  Creating a complete pipeline from simulation to visualization with minimal friction.

---

##  System Workflow

### Step 1: Simulating User Behavior
We created a **rule-based agent** that interacts with an open-source e-commerce platform to mimic real-world sessions. Each session logs:
- **Time zone**
- **Device** (mobile/desktop)
- **Actions**: `load_home`, `visit_page`, `scroll`, `click`, `hover`, `search`

### Step 2: Data Enrichment Using Distributions
To add realism:
- **CTGAN** was used to augment and generalize session data.
- Probabilistic modeling (using **Poisson** and **Binomial distributions**) added variance in:
  - Session duration
  - Scroll depth
  - Pages viewed
  - Item interactions

These features helped us model **affluence** and **consumer traits** more precisely.

### Step 3: Data Labeling
We labeled simulated sessions with:
- `affluence_level`: Low / Medium / High  
- `consumer_trait`: Deal Seeker / Brand Conscious / Window Shopper / etc.

---

##  Model & Backend

### Inference Engine
- Model: **Random Forest Classifier**
- Trained to infer:
  - **Affluence Level** (`Low`, `Medium`, `High`)
  - **Consumer Trait** (`Deal Seeker`, `Brand Conscious`, `Window Shopper`, etc.)

###  Real-Time Backend
- Built using **FastAPI**
- Accepts anonymized behavior features
- Returns persona predictions instantly

###  Visualization Dashboard
- Built using **Streamlit**
- Allows users to:
  - Upload or input features
  - View real-time model predictions
  - Explore sample sessions and trait mappings

---

##  Folder Structure
<pre><code> ## Folder Structure ``
├── app/                   # FastAPI backend
├── dashboard.py           # Streamlit dashboard
├── data_simulation/                  # Agent-based simulation and 
                                      notebooks Simulated & processed data
├── models/                 # Trained inference models
├── model_evaluation/        #evluation of model F1 score ,accuracy     
├── requirements.txt         #dependencies require to run model
└── README.md
---
''' </code></pre>
##  Inputs to the Model

The model accepts anonymized behavior-based inputs:

- `age_group`: string  
- `tech_savviness`: low / medium / high  
- `interests`: string  
- `device_type`: mobile / desktop  
- `actions`: list of action codes (`load_home`, `scroll`, `click`, etc.)  
- `items_added_to_cart`: integer  
- `affluence_score`: numeric (derived behaviorally)

---

##  Sample Output


{
  "affluence_level": "Medium",
  "consumer_trait": "Deal Seeker"
}


---


## How To Run Locally##
1.clone the repo and install Dependencies

git clone <repo-url>
cd <project-directory>
pip install -r requirements.txt

2. uvicorn app.main:app --reload
Open the Swagger UI docs at: http://127.0.0.1:8000/docs
3. launch the streamlit dashboard
streamlit run dashboard.py
Visit: http://localhost:8501
---

##  Highlights##

-  Simulated realistic user behavior using rule-based virtual agents
-  Augmented behavior sequences using CTGAN for generative realism
-  Injected behavioral noise and depth using Poisson & Binomial distributions
-  Trained a Random Forest inference engine for trait prediction
-  Built a real-time FastAPI backend for predictions
-  Streamlit dashboard for easy persona visualization
-  Zero use of PII — fully privacy-compliant behavior-based inference

---

##  Tools & Technologies Used ##

- **Python** – Core scripting and data processing
- **Pandas / NumPy** – Data manipulation
- **CTGAN** – Conditional Tabular GAN for data generation
- **Scikit-learn** – ML model training (Random Forest)
- **FastAPI** – Real-time backend API
- **Uvicorn** – ASGI server for FastAPI
- **Streamlit** – Interactive dashboard for persona visualization
- **Matplotlib / Seaborn** – Exploratory data analysis
- **Jupyter Notebook** – Simulation and development environment

---

##  Future Work ##

-  Integrate **SHAP** for model explainability
-  Enable **real-time session tracking** and online learning
-  Deploy the backend using **Docker** for scalability
-  Host the model via **Hugging Face Spaces** or **Render/Vercel**
-  Extend prediction classes using **unsupervised clustering**
-  Add more behavior layers (e.g., rage clicks, abandonment paths)

---

##  Team & Credits ##

This project was developed as part of the **Synapses '25 Hackathon** under Problem Statement 4: *Demographic & Behavioral Inference Without PII*.

**Team Name:** *[_noobs]*  
**Members:** *[Shah Mokshat(23123036),Swaroop Itkikar(23118077)]*  
**Affiliation:** *[IIT Roorkee]*  
**Year:** *2025*

---

##  Extras##

-  Notebook for synthetic session simulation using virtual agents is included
-  Persona predictions mapped to marketing-friendly labels
-  Swagger UI available for API testing at `/docs`
-  Sample predictions and test inputs bundled with the repo
-  Modular file structure for easy reproducibility and scalability
- **Demo video uploaded** showcasing end-to-end workflow and predictions
---

>  **Note:** This project uses **only synthetic data** generated using simulation and generative models. No Personally Identifiable Information (PII) or real user data has been used at any stage. This ensures compliance with privacy-first development principles.

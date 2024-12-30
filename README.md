
---

# 🚀 **Student Management CRUD API**  

Welcome to the **Student Management CRUD API**, a simple backend built with **FastAPI**, designed to manage student data effortlessly.  

## 🛠️ **How to Set Up the Project**  

### 1️⃣ **Clone the Repository**  
Start by cloning the project repository to your local machine:  

```bash
git clone https://github.com/mtbaloch/daytwo.git
cd  daytwo
```  

---

### 2️⃣ **Create and Activate a Virtual Environment**  
To manage dependencies, create a virtual environment:  

```bash
# Create a virtual environment on windows
# Create environment - here last env is the virtual environment name
python -m venv env
# Activate environment - here last env is the virtual environment name
env\Scripts\activate

# Create a virtual environment on macOS/Linux
# Create environment - here last env is the virtual environment name
python3 -m venv env
# Activate environment - here last env is the virtual environment name
source env\bin\activate
```  

---

### 3️⃣ **Install Dependencies**  
Install all the required dependencies using the `requirements.txt` file:  

```bash
pip install -r requirements.txt
```  

---

### 4️⃣ **Set Up Environment Variables**  
Copy the example `.env` file and create your own `.env` file:  

```bash
cp .env.example .env
```  

Edit the `.env` file to configure your environment variables with your own secret values but don't change keys.  

---

### 5️⃣ **Run the Server**  
Start the FastAPI server using:  

```bash
fatapi dev app/
```  

This will start the server, and you can access the API locally.  

---

### 🔗 **URLs for Testing**  
Here are the endpoints for testing the API:  

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

### 📢 **Follow Me**  
Follow for updates, tips, and more:  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/mtbaloch/) 
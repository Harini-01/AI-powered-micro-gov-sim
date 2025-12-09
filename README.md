# AI-Powered Micro-Government Simulator

## Implementation Steps

---

### 1️⃣ Clone the Repository

```bash
# Using Git Bash / WSL
git clone <YOUR-REPO-URL>
cd micro_gov_simulator
2️⃣ Create & Activate Virtual Environment
Git Bash / WSL:

bash
Copy code
python -m venv .venv
source .venv/Scripts/activate
CMD:

cmd
Copy code
.venv\Scripts\activate.bat
PowerShell:

powershell
Copy code
.venv\Scripts\Activate.ps1
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ (Optional) Set up Ollama AI Backend
Install Ollama CLI and download a model (e.g., mistral).

Update utils.py with the correct path to Ollama:

python
Copy code
OLLAMA_PATH = r"C:\Users\<YourUser>\AppData\Local\Ollama\Ollama.exe"
If Ollama is not available, the app will use mock responses.

5️⃣ Run the Streamlit App
bash
Copy code
streamlit run app.py
Enter a city policy scenario (e.g., 5% tax increase).

Click Simulate Scenario.

View the city-wide summary.

6️⃣ Quick Start (One-Liner for Git Bash)
bash
Copy code
git clone <YOUR-REPO-URL> && cd micro_gov_simulator && python -m venv .venv && source .venv/Scripts/activate && pip install -r requirements.txt && streamlit run app.py
pgsql
Copy code

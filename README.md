AI-Powered Micro-Government Simulator
Implementation Steps
1. Clone the Repository
git clone <YOUR-REPO-URL>
cd micro_gov_simulator

2. Create & Activate Virtual Environment
# Git Bash / WSL
python -m venv .venv
source .venv/Scripts/activate

# CMD
.venv\Scripts\activate.bat

# PowerShell
.venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. (Optional) Set up Ollama AI Backend

Ensure Ollama CLI is installed and a model (e.g., mistral) is downloaded.

In utils.py, set the correct path to Ollama:

OLLAMA_PATH = r"C:\Users\<YourUser>\AppData\Local\Ollama\Ollama.exe"


If Ollama is not available, the app will automatically use mock responses.

5. Run the Streamlit App
streamlit run app.py


Enter a city policy scenario (e.g., 5% tax increase) in the text box.

Click Simulate Scenario to view the city-wide summary.

6. Notes

The simulation uses modular AI agents: Finance, Health, Transport, Disaster.

The Mayor Agent combines their outputs into a structured summary.

The app works fully with mock responses if Ollama is not set up.
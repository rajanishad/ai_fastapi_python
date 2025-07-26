# Py venv related commands
python -m venv venv
# On Windowsw
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Important commands
create .env file at root

pip freeze > requirements.txt

uvicorn app.main:app --reload
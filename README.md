# Functionality
### *Celeb browser*. Application designed for searching date of birth of celebrity person.
![second_image](static\assets\pudzian.png)

# Setup

> ### Upgrade pip to the latest version:
```python
python -m pip install --user --upgrade pip
```

> ### Install virtual environment:
```python
python -m pip install --user virtualenv
python -m venv %venv_name% #creates folder in your current directory
```

> ### Activate virtual environment:
<br>

**bash**
```bash
source %venv_name%/bin/activate
```
**powershell**
```powershell
.\%venv_name%\Scripts\Activate.ps1
```

> ### Install dependencies:
```python
pip install -r requirements.txt
```

> ### Set environment variable:

**bash**:
```bash
export FLASK_APP=app.py
```
**powershell**:
```powershell
set FLASK_APP=app.py
```

> ### Run flask server:
```python
flask run
```
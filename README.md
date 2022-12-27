# Setup

* ### Upgrade pip to the latest version:
```python
python -m pip install --user --upgrade pip
```
<br>

* ### Install virtual environment:
```python
python -m pip install --user virtualenv
python -m venv %venv_name% #creates folder in your current directory
```
<br>

* ### Activate virtual environment:

**bash**
```bash
source %venv_name%/bin/activate
```
**powershell**
```powershell
.\%venv_name%\Scripts\Activate.ps1
```
<br>

* ### Install dependencies:
```python
pip install -r requirements.txt
```
<br>

* ### Set environment variable:

**bash**:
```bash
export FLASK_APP=app.py
```
**powershell**:
```powershell
set FLASK_APP=app.py
```
<br>

* ### Run flask server:
```python
flask run
```
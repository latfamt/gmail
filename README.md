## To execute

### 1. Start the Docker containter
```
docker run -d -P -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug:3.141.59-bismuth
```
### 2. Сreate a virtual environment
```
python -m venv gm_venv
```
### 3. Activate the virtual environment
```
source gm_venv/bin/activate
```
### 4. Install requirements
```
pip install -r requirements.txt
```
### 5. Start the test
```
pytest tests/test_gmail.py
```
### 6. Inspect visually what the browser is doing
In VNC viewer connect: ```127.0.0.1:5900```
(password: secret)

echo "[!] Installing Package...."
sleep 1
apt-get install python -y
pip install pyquery urllib3 requests 
python run.py
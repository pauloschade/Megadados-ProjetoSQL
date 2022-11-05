## How to run
1. Install all packages
"""
pip3 install requirements.txt
"""

2. Create a database  
3. Create a .env file with the following content

""".env
USER_NAME= {YOUR_DB_USER}
PASSWD={YOUR_DB_PASSWORD}
DBNAME={YOUR_DB_NAME}
IP={LOCAL_IP}
"""

4. Run the migrations script

"""
python3 migrate.py
"""

5. Start the app

"""
uvicorn main:app --reload
"""
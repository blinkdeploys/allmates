import os
from app import server
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    server.run(host=os.environ.get('HOST', '0.0.0.0'),
               port=int(os.environ.get('PORT')),
               debug=True)

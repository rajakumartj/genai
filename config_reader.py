import os
from configparser import ConfigParser
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.ini')
print(initfile)

config = ConfigParser()
res = config.read(initfile)

data = config.get("API_KEYS", "OPENAI_API_KEY")
print(data)
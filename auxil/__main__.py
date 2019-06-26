from . import Auxil

with open('config.py') as f:
	Auxil(config=eval(f.read(), {})).run()

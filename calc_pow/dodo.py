from config import (wanted_base, wanted_exp)

DOIT_CONFIG = dict(verbosity=2)

def task_power():
	return dict(file_dep=["calc_power.py"],
		    actions=[f"python calc_power.py -b {wanted_base} -e {wanted_exp}"])
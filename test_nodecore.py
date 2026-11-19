#Automated QA Suite(first project)

import pytest
from nodecore import calc_utilization, get_thermal_state

def test_valid_math():
	assert calc_utilization("a100", 48) == 50.0

	assert calc_utilization("RTX4090", 6) == 25.0


def test_thermal_state():
	assert get_thermal_state(90.0) == "THROTTLING"

	assert get_thermal_state(50.0) == "OPTIMAL"

	assert get_thermal_state(15.0) == "UNDERUTILIZED"


def test_hardware_faults():
		#if hardware doesnt exist
	with pytest.raises(KeyError):
		calc_utilization("GTX1080Ti",8)

		#corrupted/negative Telementry
	with pytest.raises(ValueError):
		calc_utilization("RTX5080", -10)

		# OOM Prevention (requesting more vram than available)
	with pytest.raises(MemoryError):
		calc_utilization("RTX4090", 40)

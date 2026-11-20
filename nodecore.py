#first project starting


def calc_utilization(node_name, vram_req):
	nodes = {"A100":96,
		"RTX5090":32,
		"RTX4090":24,
		"RTX5080":16,
		"RTX5070Ti":12,
		"RTX5060":8
	}

	node_name = node_name.strip().upper()
	if node_name not in nodes :
		raise KeyError(f"Unknown hardware node: {node_name}")

	if vram_req <= 0 :
		raise ValueError("VRAM request must be positive.")

	if vram_req > nodes[node_name] :
		raise MemoryError("ÖOM Crash prevented: Request exceeds node capacity.")

	
	util = round((vram_req / nodes[node_name])*100 , 2)
	return util


def get_thermal_state(util):
	if util >= 85.0 :
		return "THROTTLING"

	elif util >= 40.0 :
		return "OPTIMAL"

	else :
		return "UNDERUTILIZED"



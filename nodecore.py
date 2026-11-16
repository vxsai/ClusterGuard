#


def calc_utilization(node_name, vram_req):
	nodes = {"A100":96,
		"RTX5090":32,
		"RTX4090":24,
		"RTX5080":16,
		"RTX5070Ti":12,
		"RTX5060":8
	}

	node_name = node_name.strip().upper()
	if node_name not in node :
		raise KeyError("Unknown hardware node")

	if 

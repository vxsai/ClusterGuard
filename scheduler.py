#Command-line batch runner for clusterguard (the automation CLI)

import sys
import statistics
import cowsay
import nodecore

def main():
	if len(sys.argv) < 3:
		sys.exit("Usage: python scheduler.py [node_name] [job1_gb] [job2_gb] ...")

	target_node = sys.argv[1]
	raw_jobs = sys.argv[2:]
	valid_loads = []

	for job in raw_jobs :
		try:
			req_gb  = float(job.strip())
			util = nodecore.calc_utilization(target_node , req_gb)

		except KeyError :
			sys.exit(f"CRITICAL: Node '{target_node}' not found in cluster")

		except ValueError :
			print("SKIPPED: Corrupted Telemetry or Negative number.")
			continue

		except MemoryError:
			print("OOM Quarantined alert: Job exceeds node capacity.")
			continue

		state = nodecore.get_thermal_state(util)
		valid_loads.append(util)
		print(f"[PASS] Job: {req_gb}GB -> Load: {util}% [{state}]")


	if len(valid_loads) > 0:
		avg_load = round(statistics.mean(valid_loads), 2)
		cowsay.tux(f"{target_node.upper()} Batch Complete | Mean Load: {avg_load}%")

if __name__ == "__main__":
	main()

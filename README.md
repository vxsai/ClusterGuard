

# ClusterGuard: Compute Node & Telemetry Sanitizer

**ClusterGuard** is a lightweight, fault-tolerant pre-flight validation engine written in Python. It prevents Out-Of-Memory (OOM) hardware crashes and pipeline failures by sanitizing batch job queues and hardware telemetry before execution on shared GPU clusters (e.g., NVIDIA A100, RTX 4090) or industrial automation nodes.

## Core Architecture (v1.0)
* **`nodecore.py` (Deterministic Validation Engine):** Enforces hardware capacity limits, sanitizes malformed inputs, calculates utilization loads, and classifies thermal states (`UNDERUTILIZED`, `OPTIMAL`, `THROTTLING`).
* **`scheduler.py` (CLI Batch Processor):** Ingests multi-job queues via command-line arguments, isolates corrupted telemetry packets (`ValueError`) and capacity overflows (`MemoryError`) without halting valid jobs, and outputs statistical load summaries.
* **`test_nodecore.py` (Automated QA Suite):** Full unit test coverage using `pytest` to verify mathematical accuracy and hardware fault interlocks (`KeyError`, `ValueError`, `MemoryError`).

## Quick Start

### 1. Run Automated Unit Tests
```bash
pytest test_nodecore.py


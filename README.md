<div align="center">

# NIDSFuzz

A fuzzing framework for rule-driven Network Intrusion Detection Systems

[![Paper](https://img.shields.io/badge/NSDI'26-Paper-blue)](https://www.usenix.org/conference/nsdi26)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.11-yellow.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Required-blue.svg)](https://www.docker.com/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

</div>

## Introduction

NIDSFuzz provides an automated environment for discovering rule enforcement inconsistencies across **Snort2**, **Snort3**, and **Suricata**. It generates test traffic, feeds it through multiple NIDS simultaneously, and reports discrepancies in their alert outputs.

### Network Topology

```text
+----------------+        +------------------+        +-------------------+
| NIDS Initiator | <----> | Gateway & Mirror | <----> | Tunable Responder |
+----------------+        +------------------+        +-------------------+
                             /     |      \
                            +      +       +
                   +--------+  +--------+  +----------+
                   | Snort3 |  | Snort2 |  | Suricata |
                   +--------+  +--------+  +----------+
                           (Promiscuous Mode)
```

## Prerequisites

- **Docker** & Docker Compose
- **Python** >= 3.11
- [**uv**](https://docs.astral.sh/uv/) (Python package manager)

## Installation

> **Note:** This section is for **local development and debugging only**. If you just want to quickly test NIDS with NIDSFuzz, you can skip this section and go directly to [Usage](#usage) — everything runs via Docker Compose with no local installation required.

```bash
uv sync
```

## Usage

> **Quick Start:** No prior installation is needed — you can launch NIDSFuzz directly using the provided `docker-compose` configuration. Just make sure Docker and Docker Compose are installed.

### 1. Prepare Rules

Place your rules in:

```bash
./benchmark/rules/
```

Update rule configuration in `docker-compose/variables.env`:

```text
SNORT2_RULE_FILE=...
SNORT3_RULE_FILE=...
```

### 2. Start Fuzzing

```bash
bash ./benchmark/start.sh --fuzzing
```

> **Note:** The biggest bottleneck during setup may be your network speed.

### 3. Stop & Clean Up

```bash
bash ./benchmark/clean.sh --fuzzing
```

This saves all generated logs (alerts, packets, discrepancies, etc.) and cleans up all containers, networks, and volumes.

### 4. Replay Abnormal Cases

```bash
bash ./benchmark/start.sh --replay -packets fuzzing-results/initiator/log
bash ./benchmark/clean.sh --replay
```

## Output Structure

After running `clean.sh`, results are organized as follows:

```text
fuzzing-results/
├── initiator/
│   └── log/
│       ├── fuzzing.log
│       ├── discrepancies.txt
│       └── packets.bin
├── responder/
│   └── log/
│       └── server.log
├── snort2/
│   └── log/
│       └── snort2.log
├── snort3/
│   └── log/
│       └── snort3.log
└── suricata/
    └── log/
        ├── eve.json
        ├── fast.log
        ├── stats.log
        └── suricata.log
```

## Citation

If you use NIDSFuzz in your research, please cite our paper:

```bibtex
@inproceedings{nidsfuzz,
  title     = {From Intention to Practice: Towards Systematic Validation of NIDS Rule Enforcement},
  booktitle = {Proceeding of the 23rd USENIX Symposium on Networked Systems Design and Implementation},
  year      = {2026}
}
```

## License

This project is licensed under the [MIT License](LICENSE).

# 🧰 DevOps Engineering Workstation Setup (AWS EC2)

## 📌 Overview

This document describes the setup of a **cloud-based DevOps engineering workstation** hosted on AWS EC2.

Instead of performing DevOps operations from a local machine, all development and infrastructure activities are executed from a centralized EC2 instance — following real-world enterprise DevOps practices.

This workstation acts as a:

* DevOps Jump Host
* Engineering Bastion
* Infrastructure Automation Node
* Container Build Environment

---

## 🏗 Architecture Approach

```
Local Machine
     ↓ SSH
AWS EC2 DevOps Workstation
     ↓
Docker / GitHub / Automation / Deployment
```

This approach ensures:

* Environment consistency
* Secure infrastructure access
* Reproducible deployments
* Production-like workflow

---

## ☁️ EC2 Instance Details

| Configuration  | Value            |
| -------------- | ---------------- |
| Cloud Provider | AWS              |
| OS             | Ubuntu 22.04 LTS |
| Instance Type  | t3.medium        |
| Access Method  | SSH              |
| User           | ubuntu           |

---

## 🔄 System Update

Update system packages before installing DevOps tools:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🔧 Git Installation

Git is required for source control and GitHub integration.

```bash
sudo apt install git -y
git --version
```

Example Output:

```
git version 2.43.0
```

---

## 🐍 Python Environment Standardization

Python is used for automation, scripting, and AI-assisted DevOps tooling.

### Install Python 3.11

```bash
sudo apt update && sudo apt upgrade
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
sudo apt install python3.11-dev python3.11-venv python3.11-distutils python3.11-gdbm python3.11-tk libbz2-dev libffi-dev libssl-dev libreadline-dev libsqlite3-dev zlib1g-dev
```

Verify installation:

```bash
python3.11 --version
```

---

## 🧪 Virtual Environment Creation

To avoid dependency conflicts, all automation tools run inside an isolated Python environment.

Create virtual environment directory:

```bash
mkdir -p ~/.venvs
```

Create DevOps environment:

```bash
python3.11 -m venv ~/.venvs/devops
```

Activate environment:

```bash
source ~/.venvs/devops/bin/activate
```

Expected shell prefix:

```
(devops) ubuntu@ip-xxx
```

---

## 🐳 Docker Installation (Official Repository Method)

Docker is installed using the official Docker repository instead of Ubuntu defaults to ensure production compatibility.

### Install prerequisites

```bash
sudo apt install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
```

### Add Docker GPG key

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Add Docker repository

```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker Engine

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

## 🔐 Docker Non-Root Access

Allow Docker execution without sudo:

```bash
sudo usermod -aG docker $USER
exit
```

Reconnect via SSH after this step.

---

## ✅ Verification Commands

```bash
git --version
python3.11 --version
docker --version
docker compose version
whoami
```

Example Output:

```
git version 2.43.0
Python 3.11.x
Docker version 29.x
Docker Compose version v2+
ubuntu
```

---

## ✅ Result

The EC2 instance now functions as a **production-ready DevOps engineering workstation**, capable of:

* Containerized application development
* Infrastructure automation
* CI/CD execution
* Monitoring integration
* AI-assisted DevOps workflows

---

## 🧠 Industry Best Practices Applied

* Cloud-based engineering environment
* Python dependency isolation
* Official Docker installation
* Non-root container execution
* Reproducible setup documentation

---

## 🚀 Next Step

Design and implement a production-grade containerized application platform with reverse proxy architecture.


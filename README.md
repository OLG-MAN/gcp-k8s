# Task k8s-gcp

## Task 1 

## Minikube

* Create a kubernetes deployment and service with the 'fortune' program 
* Docker image: https://hub.docker.com/r/perarneng/fortune/ 
* Make this deployment accessible as a service from within the cluster
* A different fortune should show every time the service is called. 
* Use local Minikube

--------------------------------------

## Solution

### 0. Prepare working environment. Create vm with docker and minikube in GCP.

```
# Set default zone
gcloud config set compute/zone us-central1-c

# Create default VM.
gcloud compute instances create minikube1 --machine-type=n2-standard-2

# Install Docker on minikube1 VM
sudo apt-get update

sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

# Post-install
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo apt install kubectl -y

# Start Minikube
minikube start
```

### 1. Make Docker image with nginx and python-cgi

```
# Dockerfile in ./Dockerfile
# After push to my docker hub account olegan/fotune-app:tagname
```

### 2. Deploy to minikube (GKE)

```
# Use my gcp free-tier gke cluster instead minikube, create default cluster
gcloud container clusters create cluster k1
gcloud container clusters get-credentials k1

# Deploy and expose fortune-app
# Make deployment and service in ./k8s/*.yaml files
kubectl apply -f ./k8s/deploy.yaml
kubectl apply -f ./k8s/svc.yaml
```

--------------------------------------------------

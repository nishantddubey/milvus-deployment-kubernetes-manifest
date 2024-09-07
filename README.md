# Milvus Deployment and Connection Guide

## Overview

This guide covers the deployment of Milvus, etcd, MinIO, and Attu on Kubernetes using manifests. It also provides instructions on connecting to Milvus using PyMilvus.

## Prerequisites

- **Kubernetes Cluster**: Ensure you have a running Kubernetes cluster.
- **kubectl**: CLI tool to interact with Kubernetes.
- **Python**: Ensure Python is installed.
- **PyMilvus**: Python client for Milvus.

## Setup Commands

### 1. Clone the Repository

Clone this repository or create a directory for your manifests.

```bash
git clone https://github.com/nishantddubey/milvus-deployment-kubernetes-manifest.git
cd milvus-deployment-kubernetes-manifest
```

### 2. Create the Namespace

Create a namespace for the deployment:

```bash
kubectl create namespace milvus
```

###  3. Apply Kubernetes Manifests

Apply the manifests to deploy etcd, MinIO, Milvus, and Attu:

```bash
kubectl apply -f etcd-deployment.yaml -n milvus
kubectl apply -f minio-deployment.yaml -n milvus
kubectl apply -f milvus-deployment.yaml -n milvus
kubectl apply -f attu-deployment.yaml -n milvus
```

### 4. Verify Deployments

Check the status of the deployments and services:

```bash
kubectl get deployments -n milvus
kubectl get services -n milvus
```

## Connecting to Milvus Using PyMilvus

### 1. Install PyMilvus

Install PyMilvus using pip:

```bash
pip install pymilvus

```

### 2. Connect to Milvus and Create a Collection

Use the following Python script to connect to Milvus and create a collection. Save the script to a file, for example connect_milvus.py. Available in the repo

Run the script:

```bash
python connect_milvus.py

```






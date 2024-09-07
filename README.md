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

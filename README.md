# Building a Secure and Robust DevOps Pipeline for Training and Deploying Neural Networks

## Overview
This project demonstrates how to set up a secure and robust DevOps pipeline for training and deploying neural networks using Terraform, Jenkins, and Docker.

## Project Structure
- `infrastructure/`: Terraform scripts for infrastructure setup.
- `ci-cd/`: Jenkins pipeline scripts for continuous integration and deployment.
- `src/`: Source code for training the model and making predictions.
- `tests/`: Unit tests for the model.
- `Dockerfile`: Docker configuration for the application.

## Getting Started
1. Clone the repository.
2. Configure GCP credentials and SSH keys.
3. Navigate to the `infrastructure` folder and run Terraform commands to set up the environment.
4. Set up Jenkins and point it to the `ci-cd` directory for CI/CD.

## Running the Project
1. Build the Docker image with `docker build -t neural-net-image .`
2. Run the Docker container with `docker run -d --name neural-net-container neural-net-image`

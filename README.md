# python3-lambda-layers
This repository treats about how to automate AWS Lambda Layers deployment with Docker and Terraform

## Requirements
- A docker or docker-ce installed,
- Terraform ~> 0.11.12 to use filebase64hash256 for Terraform to detect code changes, it can also work with base64sha256(file()) for Terraform earlier versions.

## Installation and Deployment

run
```
chmod +x lambda/build.sh 
chmod +x lambda/layer-pandas/build_layer.sh
cd lambda/
./build.sh
cd ..
terraform init
terraform apply
```
and type _yes_

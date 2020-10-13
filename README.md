# -ECE444-F2020-Lab3
Marinette
This repo is a clone of https://github.com/miguelgrinberg/flasky

## How to run this lab

### Building Docker
To build the files, run the command:
`docker build -t lab4:latest .`
The dockerfile are located in the base directory with the filename Dockerfile.

### Running Docker
To run the built image, run the command:
`docker run -p 5000:5000 lab4`

This will allow you to access the browser at the address:
`http://0.0.0.0:5000`

## Screenshot of the docker image running
![Activity 1 Screenshot](/images/image1.PNG)

## Screenshot of the website running
![Activity 2 Screenshot](/images/image2.PNG)

## Docker images
![Activity 2 Screenshot](/images/image3.PNG)

## Docker vs Virtual Machine
Docker runs on containers, which are like a virtual machine in a sense that they both take "images" (snapshot of your current computer environment) and upload it so that it can be shared with other people. The difference is that VMs take a snapshot of your entire OS and its resources, whereas containers are take just enough information from the OS to run the process. As such, containers are much smaller and faster than virtual machines.



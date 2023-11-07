# NSA-Client-Server
A simple client-server application where the client makes a request to the server, the server processes the request, and sends back the response.

# Simple Python Client-Server Application Guide

This guide will walk you through setting up a simple client-server application in Python on an Ubuntu system. You will learn how to send requests, receive responses, trace packets, view firewall rules, and evaluate server response time.

## Contributors
- Teresiah Njeri
- Richard Karanu

## Prerequisites
- Python 3.x installed on Ubuntu
- Basic understanding of Python programming
- Terminal access with sufficient privileges (you may need `sudo` for some commands)

## Installation and Setup

After confirming the installation of Python and `pip`, you'll need to create two Python scripts: one for the server and one for the client.

## Running the Application

To execute your scripts, open two separate terminal windows:

- In the first terminal, navigate to the location of your server script and run:

``` python3 server.py

This will start the server, which will listen for incoming connections.

- In the second terminal, navigate to the location of your client script and execute:

``` python3 client.py

This action will send a request to the server, which the server will process and respond to.

## Packet Tracing

To observe the packet flow between the client and server, you can use `tcpdump`. Run the following command in a separate terminal before starting your server and client:

```sudo tcpdump -i lo -n port 12345

This will display the packets that are being sent and received on the loopback interface on port 12345.

## Firewall Configuration

Your Ubuntu system uses `ufw` (Uncomplicated Firewall) to manage network traffic rules. To allow traffic on the port that the server listens to:

- To set the rule:

```sudo ufw allow 12345/tcp

- To enable the firewall, if it's not already active:

``` sudo ufw enable

- To check the status of your firewall rules:


## Measuring Server Response Time

The server response time is the duration from when the client sends a request until it receives a response. The client script should be modified to measure and output this time, providing insights into the performance of the server.

After setting up the application, tracing the packets, and configuring the firewall, you should have a better understanding of how a basic client-server system operates on a network.

By following this guide, you will have taken your first steps into network programming with Python on Ubuntu.

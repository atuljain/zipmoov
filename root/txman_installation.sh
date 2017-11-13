#!/bin/bash
################################################################################
# Script for installing txman working branch on Ubuntu (could be used for other branch/version too)
# Author: Atul Jain     
#-------------------------------------------------------------------------------
# This script will install txman on your Ubuntu server. It can install multiple txman instances
# in one Ubuntu because of the different ports
#-------------------------------------------------------------------------------
# Make a new file:
# sudo nano txman_installation_script.sh
# Place this content in it and then make the file executable:
# sudo chmod +x txman_installation_script.sh
# Execute the script to install txman:
# ./txman_installation_script
################################################################################
 
##fixed parameters
PORT="8000"
HOST="127.0.0.1"
#Choose the txman version which you want to install. For example: txman_v_1.1, txman_v_1.2, txman_v_1.3 etc.
BRANCH="txman_v_1.1"
#--------------------------------------------------
# Update Server
#--------------------------------------------------
echo -e "\n---- Update Server ----"
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip
#--------------------------------------------------
# Create Virtual Environment
#--------------------------------------------------
echo -e "\n---- Create Virtual Environment----"

sudo pip install virtualenv

virtualenv DjangoMongodb

source DjangoMongodb/bin/activate
#--------------------------------------------------
# Install Dependencies intp VirtualENV
#--------------------------------------------------
echo -e "\n---- Install python packages ----"
pip install -r ./txman/dx_man/requirements/requirement.txt


# echo -e "\n---- Clone txman   ----"
# git clone --branch $BRANCH http://gitlab.tradeboox.in/atul/txman.git

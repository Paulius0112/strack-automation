import string    
import random  
import os
import sys
import subprocess

def deployAnsible(nodeType):
    if(nodeType == 0):
        # Bitcoin
        S = 10  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  
        
        file_name = "main.yml"
        save_path = "./ansible/bitcoin/vars"

        completeName = os.path.join(save_path, file_name)

        f = open(completeName, "a")
        f.write("SYNTROPY_API_KEY:\""+ os.environ.get('SYNTROPY_API_KEY') +"\"\n")
        f.write("SYNTROPY_CONTROLLER_URL:\""+ os.environ.get('SYNTROPY_CONTROLLER_URL') +"\"\n")
        f.write("SYNTROPY_USERNAME:\""+ os.environ.get('SYNTROPY_USERNAME') +"\"\n")
        f.write("SYNTROPY_PASSWORD:\""+ os.environ.get('SYNTROPY_PASSWORD') +"\"\n")
        f.write("GRAFANA_USERNAME:\""+ username +"\"\n")
        f.write("GRAFANA_PASSWORD:\""+ password +"\"\n")
        f.close()

        bashCommand = "cd ansible/bitcoin/ansible && ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -i ../inventory.yml main.yaml"

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    elif(nodeType == 1):
        # Elrond
        S = 10  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  
        secret = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  

        file_name = "main.yml"
        save_path = "./ansible/elrond/vars"

        completeName = os.path.join(save_path, file_name)

        f = open(completeName, "a")
        f.write("SYNTROPY_API_KEY:\""+ os.environ.get('SYNTROPY_API_KEY') +"\"\n")
        f.write("SYNTROPY_CONTROLLER_URL:\""+ os.environ.get('SYNTROPY_CONTROLLER_URL') +"\"\n")
        f.write("SYNTROPY_USERNAME:\""+ os.environ.get('SYNTROPY_USERNAME') +"\"\n")
        f.write("SYNTROPY_PASSWORD:\""+ os.environ.get('SYNTROPY_PASSWORD') +"\"\n")
        f.write("GRAFANA_USERNAME:\""+ username +"\"\n")
        f.write("GRAFANA_PASSWORD:\""+ password +"\"\n")
        f.write("ELROND_VERSION:\""+ os.environ.get('ELROND_VERSION') +"\"\n")
        f.write("ELROND_CONFIG_VERSION:\""+ os.environ.get('ELROND_CONFIG_VERSION') +"\"\n")
        f.write("ELROND_NETWORK_TYPE:\""+ os.environ.get('ELROND_NETWORK_TYPE') +"\"\n")
        f.write("NODE_DISPLAY_NAME:\""+ os.environ.get('NODE_DISPLAY_NAME') +"\"\n")
        f.close()

        bashCommand = "cd ansible/elrond/ansible && ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -i ../inventory.yml main.yaml"

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    elif(nodeType == 2):
        # Ethereum

        S = 10  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  
        secret = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  

        #nodeName = "syntropy" # this is the node name that will show up in eth-netstats
        #gethSyncMode = "light" # choose sync mode depending on your machine and data needs
        #gethApiFlags = "eth,web3,personal,net" # do not change this unless you need more access in the HTTP API
        #gethExtraFlags = "" # add any additional Geth flags here

        file_name = "main.yml"
        save_path = "./ansible/bitcoin/vars"

        completeName = os.path.join(save_path, file_name)

        f = open(completeName, "a")
        f.write("SYNTROPY_API_KEY:\""+ os.environ.get('SYNTROPY_API_KEY') +"\"\n")
        f.write("SYNTROPY_CONTROLLER_URL:\""+ os.environ.get('SYNTROPY_CONTROLLER_URL') +"\"\n")
        f.write("SYNTROPY_USERNAME:\""+ os.environ.get('SYNTROPY_USERNAME') +"\"\n")
        f.write("SYNTROPY_PASSWORD:\""+ os.environ.get('SYNTROPY_PASSWORD') +"\"\n")
        f.write("GRAFANA_USERNAME:\""+ username +"\"\n")
        f.write("GRAFANA_PASSWORD:\""+ password +"\"\n")
        f.write("NODE_NAME:\""+ os.environ.get('NODE_NAME') +"\"\n")
        f.write("GETH_SYNC_MODE:\""+ os.environ.get('GETH_SYNC_MODE') +"\"\n")
        f.write("GETH_API_FLAGS:\""+ os.environ.get('GETH_API_FLAGS') +"\"\n")
        f.write("GETH_EXTRA_FLAGS:\""+ os.environ.get('GETH_EXTRA_FLAGS') +"\"\n")
        f.close()

        bashCommand = "cd ansible/ethereum/ansible && ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook -i ../inventory.yml main.yaml"

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    else:
        print("Error")

def deployInfra(storageType):
    if(storageType == 0):
        # AWS
        print("Primas")
    elif(storageType == 1):
        # GCP
        ssh_public_key_file  = "~/.ssh/id_rsa.pub"
        gcp_project_id       = "<YOUR_GCP_PROJECT_ID>"
        gcp_credentials_file = "../service-key.json"
        gcp_region           = "europe-west3"
        gcp_zone             = "europe-west3-b"

        file_name = "terraform.tfvars"
        save_path = "./infra/gcp"

        completeName = os.path.join(save_path, file_name)


        f = open(completeName, "a")
        f.write("ssh_public_key_file=\""+ ssh_public_key_file +"\"\n")
        f.write("gcp_project_id=\""+ gcp_project_id +"\"\n")
        f.write("gcp_credentials_file=\""+ gcp_credentials_file +"\"\n")
        f.write("gcp_region=\""+ gcp_region +"\"\n")
        f.write("gcp_zone=\""+ gcp_zone +"\"\n")
        f.close()

        print("File create")

        bashCommand = "cd infra/gcp && terraform init && terraform apply -auto-approve"

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print("Command executed")
        
    elif(storageType == 2):
        # Azure
        print("2")
    else:
        print("Error")


def main():
    deployInfra(1)
    deployAnsible(0)

if __name__ == "__main__":
    main()
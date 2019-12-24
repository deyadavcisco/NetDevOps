# NetDevOps
LTRDCN-1074 Cisco Live 2019 Barcelona

WARNING:
"These scripts are meant for educational/proof of concept purposes only - as demonstrated at Cisco Live. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and I am not responsible for any damage or data loss incurred as a result of their use."

Bringing the lab exercises prepared for clients during Cisco Live 2019 Barcelona Instructor Led lab.
1. Inventory-Environment: Contains the environment settings to run Ansible Playbooks and inventory file (hosts).
2. Lab-Exercises: Contains Day 1, Day 2 and Day N exercises
  - Day 1 - Automate Configuration
  - Day 2 - Automate Monitoring
  - Day N - Automate Maintenance


Section 1: Day 1 - Automate Configuration

Objective 
•	Explore the Ansible Control Machine. Ansible version 2.7.2 is pre-installed.
o	Inventory file (path = /etc/ansible/hosts)
o	Group Variables (path = /etc/ansible/group_vars)
o	Config file (path = /etc/ansible/ansible.cfg) 
o	Playbooks (path = /home/ansible/lab-files/Day1-Automate-Configuration/tasks)
o	Ansible Documentation (ansible-doc [-l|-s] [options] [-t <plugin type] [plugin]) 
•	Use Ansible NX-OS network modules to configure Nexus 9000v instances in a VPC domain and related topology using NX-API and SSH based connection plugins.
•	At the end of this session, the servers should be able to communicate with each other over Eth1 interface.
•	The files under this section are located in the following folders in designated path:
o	tasks - lab exercises: /home/ansible/lab-files/Day1-Automate-Configuration/tasks
o	final - completed lab exercises: /home/ansible/lab-files/Day1-Automate-Configuration/final
o	challenges - solved challenges: /home/ansible/lab-files/Day1-Automate-Configuration/challenges
•	The playbook in some tasks is left incomplete denoted by <INCOMPLETE> for completion or have to be replaced with an appropriate value indicated by keyword FIXIT.


Step 1: Explore Ansible Control Machine
[Task 1] Browse Inventory file
[Task 2] Add a new group name [N9000v-Leaf] to inventory file	
[Task 3] Create group variables to split out host and group specific data	
[Task 4] Review ansible configuration file ansible.cfg	
[Task 5] Using ansible configuration settings to disable Deprecated warnings	
[Task 6] Review a playbook using NXOS module ‘nxos_nxapi’	
[Task 7] Use Ansible Documentation	
[Task 8] Run Ansible ‘ping’ module for hosts group ‘N9000v-All’	
Step 2: Create/modify playbooks to configure N9000v’s in given topology	
[Task 1] Enable NX-API for all Nexus 9000v switches	
[Task 2] Enable certain features on all Nexus 9000v switches	
[Challenge 1]	
[Task 3] Provision VLAN’s on all Nexus 9000v switches	
[Challenge 2]	
[Task 4] Idempotency	
[Task 5] Build VPC Domain between nx-osv9000-1 & nx-osv9000-2	
[Task 6] Configure Layer 2 interfaces on all Nexus 9000v switches in the environment	
[Challenge 3]	
[Task 7] Bundle (link aggregation) L2 interfaces in respective port-channel on all Nexus 9000v switches in the environment	
[Task 8] Configure SVI and HSRP on nx-osv9000-1 & nx-osv9000-2 switches using Ansible for inter-VLAN routing	
[Task 9] Access Server1 and Server2 and run ping between them over Eth1 interface (Optional)	
[Challenge 4]

Section 2: NX-API CLI/REST	
[Task 1] Access NX-API Developer Sandbox	31
[Task 2] Use “json-rpc” to update port description	33
[Task 3] Use “json” to update port description	34
[Task 4] Access Visore the build-in Object Store browser	35
[Task 5] Access Postman client to make REST query to the switch	37


Section 3: Day 2 - Automate Monitoring
Introduction 
Cisco NX-OS provides several different mechanisms like SNMP, CLI, XML for collecting data from a network. These mechanisms have limitations which restrict automation and scalability. One of them is the use of the pull model, where the initial request for data from network elements originates from the client. To initiate such requests, continual intervention or the presence of a Network Management System (NMS) is required. Another scalability problem arises when there is more than one NMS in the network.  It is only just a few common barriers which Networking engineers come through.  
A push model, on the other hand, continuously streams data of interest out of the network, which ultimately provides real or near real-time access to monitoring data. 
The Cisco Streaming Telemetry service provides a mechanism for selecting data of interest from Nexus devices and pushing it off the box periodically to remote management stations. Without going into details, we would like to mention that nowadays Nexus devices may provide you with hardware and software-based telemetry. Streaming Telemetry Principles: 
•	Performance: Push, not Pull 
•	Consumption: Analytics ready 
•	Granularity: Data-Model Driven 

Objective
•	Explore ELK stack and its integration as monitoring tool.
•	Use pre-build docker containers to deploy telemetry. 
•	At the end of this session, the Nexus 9000v instances should be able to send telemetry data which visualized with Kibana.

Section 3: Day 2 - Automate Monitoring

Step 1: Explore built-in NX-OS telemetry	
[Task 1] Enable Telemetry on all Nexus 9000v switches
Step 2: Deploy telemetry and ELK dockers on single host	
[Task 1] Check Docker daemon run on host
[Task 2] Run Docker Bridge network	
[Task 3] Deploy ELK container connected elknet bridge	
[Task 4] Deploy dockercisco/telemetryreceiver container	
Step 3. Explore Kibana configuration and visualization options	
[Task 1] Exploring Kibana GUI and basic configuration	
[Task 2] Create Data Table in Kibana	
[Challenge 5]	
[Task 3] Create Scripted fields to show Memory usage in percentage	
[Task 4] Create Memory Utilization Gauge	
[Task 5] Putting all together under Dashboard	
[Task 6] Adding supervisor’s Mgmt0 info to the Dashboard (Optional)	


Section 4: Day N - Automate Maintenance

Objective 
After completing this section, you will have an understanding of the followings:
•	Graceful Insertion and Removal (GIR) feature of NX-OS, also known as “maintenance mode”.
•	Leverage NX-OS patching capability to fix a software bug without upgrading the OS version.
•	Use Ansible modules to automate tasks, such as:
o	Creating Snapshots
o	Running validations
o	Backup Configuration
o	Copying file/path from Ansible controller to the switch.
o	Placing switch in maintenance mode
o	Install patch/SMU (Software maintenance upgrade)
o	Bringing switch back in normal mode
•	The files under this section are located in the following folders in designated path:
o	tasks - lab exercises: /home/ansible/lab-files/DayN-Automate-Maintenance/tasks
o	final - completed lab exercises: /home/ansible/lab-files/DayN-Automate-Maintenance/final
o	challenges - solved challenges: /home/ansible/lab-files/DayN-Automate-Maintenance/challenges
•	The playbook in some tasks is left incomplete denoted by <INCOMPLETE> for completion or have to be replaced with an appropriate value indicated by keyword FIXIT.
References:
For more details about GIR check: 
https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-737899.html

Section 4: Day N - Automate Maintenance	

[Task 1] Create Snapshots, run validations and backup configuration	
This task we will prepare the switch nx-osv9000-2 for maintenance mode, kindly explore the followings
[Challenge 6]	
[Task 2] Place the switch in maintenance mode
[Task 3] Install Patch/SMU on the switch in maintenance mode
[Challenge 7]	
[Task 4] Bring switch back to normal mode and compare snapshots
[Challenge 8]	

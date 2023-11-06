# Phoenix

## EVPN Notes

### Background


* VPWS - extended lan accross EVPN  
* EVPN can do multi-homing  
* Per EVI eth seg route RT 1  
* A/A multi homing - new Layer2 extended community  - control flag pbit 1 for A/A  
---
#### 3 tier, LEGACY requirements  
* Application Bandwidth  
* load balancing  
* vLAN segmentation  
* l2 domain quite large  
* limited scalability due to hierarchical design  
* STP blocking ports  
---
#### Modern DC requirements
* 70% of traffic moves east west , server to server.
* Addressing the Scaling issues
* CLOS topology, non-blocking, non interfering.
* needs ECMP in the data plane and control plane
* increase redundancy
* scalability , multiple links that carry traffic
* Problems to over come
⋅⋅⋅host mobility
⋅⋅⋅l3 communication
⋅⋅⋅vxLAN uses underlay IP and extends layer 2

* MP-BGP EVPN is the control place for vxLAN
* ARP suppression
* Multi-homing , limit flooding of traffic , DF BUM traffic
* MAC mobility,  rt-2 with seq numbers.
* New NLRI - AFI – 25 (Layer-2 VPN), SAFI 70 (EVPN)

---

#### EVPN RT-1

Ethernet Auto Discovery route
Active Active muliti homing

EVPN Instance = EVI
	Assign import/export  route target
	VNI in the DC
ES = Ethernet segment.
	One or more PE devices with ethernet link, referred to as an Ethernet Segment
ESI = Ethernet segmment Identifier
	represents EACH segment uniquely
	10 oct id

load-balance towards multiple leafs.
	Aliasing – remote leaf knows that the mac is reachable via the leafs who has advertised the ESI
	Per EVI

	
Fast convergence in failure event
	BGP Withdraw messages are to slow,  EthernetA-D per ES route triggering the remote PE to update the nexhop to the still active unit. For MAC addr associated with the ESI.
	Per ESI

prevent BUM traffic echoing back to multi homed segment.
	Split horizon, dont accept a RT-1 from you mulit-homed partner leaf.#
	vxLAN, looks at the src tunnel IP (loopback-1)
	Per ESI


---

#### EVPN RT-4
What happens to Bum traffic in multi-homed networks?

No need for peer links, standards based.

RT-1 eth auto discovery (AD route)
RT-4 Eth segment route

leafs connected to the same ES can automatically discover each other.  
BGP advertisement, carrys the ES route and ES import route type.  
BGP extended community for RT import.  
PE has a timer to allow all participating leafs to adv the RT-4  
Once the time has expired the leafs build the order list!!  
	DF is chosen per dot1q tag per ESI, they forward Bum onto the ESI  

---
#### EVPN RT-2

Flood and learn process,  
learn via src mac in frames/packet, src vLAN, src port  
floodlist, leafs that are interested in the VNI  
RT-2 , message say from leaf locally learnt mac-x is reachable using VNI x, only the leafs that have the VNI install the route. Next hop is the vTEP address.  
ARP Suppression, RT-2  has mac and IP  

---	

#### EVPN RT-3
inclusive Multicast Route – imet  
Build the floodlist for ingress replication, join, leave per VNI  
you could use L3 multicast as an alternative.  





# ANTA Demo step by step

## Network Ready for Use

### Initial steps

* Alter the bash display width for docker container

```bash
stty cols 120 rows 60
```

* Review ANTA parameters available in [`anta.env`](../anta.env)

```bash
cat anta.env
```

* Load anta parameters

```bash
source anta.env
```

* Run anta testing, esure you're in the correct directory.

```bash
anta nrfu -c test_leafs.yml table --tags leaf
```

> Analyzed first results.

* Update NRFU tests to with
    * Under test `VerifyBGPPeerCount` update `num_peers: 3`

* Run anta testing

```bash
anta nrfu -c test_leafs.yml table --tags leaf
```

## Focusing on Leaf devices

* Run testing only on leaf devices

```bash
anta nrfu -c test_leafs.yml table --tags leaf
```

## Focusing on Spine devices

```bash
anta nrfu -c test_spines.yml table --tags spine
```

## Collect Data from network

* Edit list of command to capture, use VScode as its faster.

```bash
vim network-tests/snapshot.yml
```

* Capture commmands

```bash
anta exec snapshot -c snapshot.yml
anta exec snapshot -c snapshot-evpn.yml
```


## AVD playbooks 

```bash
cd /home/avd/avd-demo/EMEA-AS-Lab/ansible-avd
➜  ansible-avd git:(master) ✗ ansible-playbook playbook.fabric-build.yml
➜  ansible-avd git:(master) ✗ ansible-playbook playbook.fabric-deploy.yml
```
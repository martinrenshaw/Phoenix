# DC1_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | l3leaf | Leaf1 | 172.17.100.3/16 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l3leaf | Leaf2 | 172.17.100.4/16 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l3leaf | Leaf3 | 172.17.100.5/16 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l3leaf | Leaf4 | 172.17.100.6/16 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | spine | Spine1 | 172.17.100.1/16 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | spine | Spine2 | 172.17.100.2/16 | cEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | Leaf1 | Ethernet1 | spine | Spine1 | Ethernet1 |
| l3leaf | Leaf1 | Ethernet2 | spine | Spine2 | Ethernet1 |
| l3leaf | Leaf1 | Ethernet10 | mlag_peer | Leaf2 | Ethernet10 |
| l3leaf | Leaf1 | Ethernet11 | mlag_peer | Leaf2 | Ethernet11 |
| l3leaf | Leaf2 | Ethernet1 | spine | Spine1 | Ethernet2 |
| l3leaf | Leaf2 | Ethernet2 | spine | Spine2 | Ethernet2 |
| l3leaf | Leaf3 | Ethernet1 | spine | Spine1 | Ethernet3 |
| l3leaf | Leaf3 | Ethernet2 | spine | Spine2 | Ethernet3 |
| l3leaf | Leaf4 | Ethernet1 | spine | Spine1 | Ethernet4 |
| l3leaf | Leaf4 | Ethernet2 | spine | Spine2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/24 | 256 | 16 | 6.25 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| Leaf1 | Ethernet1 | 10.255.0.1/31 | Spine1 | Ethernet1 | 10.255.0.0/31 |
| Leaf1 | Ethernet2 | 10.255.0.3/31 | Spine2 | Ethernet1 | 10.255.0.2/31 |
| Leaf2 | Ethernet1 | 10.255.0.5/31 | Spine1 | Ethernet2 | 10.255.0.4/31 |
| Leaf2 | Ethernet2 | 10.255.0.7/31 | Spine2 | Ethernet2 | 10.255.0.6/31 |
| Leaf3 | Ethernet1 | 10.255.0.9/31 | Spine1 | Ethernet3 | 10.255.0.8/31 |
| Leaf3 | Ethernet2 | 10.255.0.11/31 | Spine2 | Ethernet3 | 10.255.0.10/31 |
| Leaf4 | Ethernet1 | 10.255.0.13/31 | Spine1 | Ethernet4 | 10.255.0.12/31 |
| Leaf4 | Ethernet2 | 10.255.0.15/31 | Spine2 | Ethernet4 | 10.255.0.14/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.252.0.0/24 | 256 | 2 | 0.79 % |
| 10.254.0.0/24 | 256 | 4 | 1.57 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | Leaf1 | 10.254.0.1/32 |
| DC1_FABRIC | Leaf2 | 10.254.0.2/32 |
| DC1_FABRIC | Leaf3 | 10.254.0.3/32 |
| DC1_FABRIC | Leaf4 | 10.254.0.4/32 |
| DC1_FABRIC | Spine1 | 10.252.0.1/32 |
| DC1_FABRIC | Spine2 | 10.252.0.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.254.1.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | Leaf1 | 10.254.1.1/32 |
| DC1_FABRIC | Leaf2 | 10.254.1.1/32 |
| DC1_FABRIC | Leaf3 | 10.254.1.3/32 |
| DC1_FABRIC | Leaf4 | 10.254.1.4/32 |

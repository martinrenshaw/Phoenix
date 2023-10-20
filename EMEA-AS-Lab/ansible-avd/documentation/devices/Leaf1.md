# Leaf1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router OSPF](#router-ospf)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 172.17.100.3/16 | 172.17.0.1 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 172.17.100.3/16
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.2.1 | mgmt | - |
| 8.8.8.8 | mgmt | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf mgmt 8.8.8.8
ip name-server vrf mgmt 192.168.2.1
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| ansible | 15 | network-admin | False | - |
| arista | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username ansible privilege 15 role network-admin secret sha512 <removed>
username arista privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_LEAF1-2 | Vlan4094 | 10.253.2.1 | Port-Channel10 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_LEAF1-2
   local-interface Vlan4094
   peer-address 10.253.2.1
   peer-link Port-Channel10
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | Tenant_A_client_l2_only | - |
| 12 | Old_Gold_Ops_Zone_Test | - |
| 110 | Old_Gold_Ops_Zone_1 | - |
| 3009 | MLAG_iBGP_Old_Gold_Ops | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 10
   name Tenant_A_client_l2_only
!
vlan 12
   name Old_Gold_Ops_Zone_Test
!
vlan 110
   name Old_Gold_Ops_Zone_1
!
vlan 3009
   name MLAG_iBGP_Old_Gold_Ops
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet10 | MLAG_PEER_Leaf2_Ethernet10 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 10 |
| Ethernet11 | MLAG_PEER_Leaf2_Ethernet11 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 10 |
| Ethernet19 | host1_Eth1 | *trunk | *10,12,110,160 | *- | *- | 19 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_SPINE1_Ethernet1 | routed | - | 10.255.0.1/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_SPINE2_Ethernet1 | routed | - | 10.255.0.3/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_SPINE1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.0.1/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet2
   description P2P_LINK_TO_SPINE2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.0.3/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet10
   description MLAG_PEER_Leaf2_Ethernet10
   no shutdown
   channel-group 10 mode active
!
interface Ethernet11
   description MLAG_PEER_Leaf2_Ethernet11
   no shutdown
   channel-group 10 mode active
!
interface Ethernet19
   description host1_Eth1
   no shutdown
   channel-group 19 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel10 | MLAG_PEER_Leaf2_Po10 | switched | trunk | - | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel19 | host1_PortChannel3 | switched | trunk | 10,12,110,160 | - | - | - | - | 19 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel10
   description MLAG_PEER_Leaf2_Po10
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel19
   description host1_PortChannel3
   no shutdown
   switchport
   switchport trunk allowed vlan 10,12,110,160
   switchport mode trunk
   mlag 19
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.254.0.1/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.254.1.1/32 |
| Loopback100 | Old_Gold_Ops_VTEP_DIAGNOSTICS | Old_Gold_Ops | 10.255.1.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Old_Gold_Ops_VTEP_DIAGNOSTICS | Old_Gold_Ops | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.254.0.1/32
   ip ospf area 0.0.0.0
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.254.1.1/32
   ip ospf area 0.0.0.0
!
interface Loopback100
   description Old_Gold_Ops_VTEP_DIAGNOSTICS
   no shutdown
   vrf Old_Gold_Ops
   ip address 10.255.1.1/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan12 | Old_Gold_Ops_Zone_Test | Old_Gold_Ops | - | False |
| Vlan110 | Old_Gold_Ops_Zone_1 | Old_Gold_Ops | - | False |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf Old_Gold_Ops | Old_Gold_Ops | 1500 | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | False |
| Vlan4094 | MLAG_PEER | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan12 |  Old_Gold_Ops  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan110 |  Old_Gold_Ops  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3009 |  Old_Gold_Ops  |  10.253.0.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.253.0.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.253.2.0/31  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan12
   description Old_Gold_Ops_Zone_Test
   no shutdown
   vrf Old_Gold_Ops
!
interface Vlan110
   description Old_Gold_Ops_Zone_1
   no shutdown
   vrf Old_Gold_Ops
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf Old_Gold_Ops
   no shutdown
   mtu 1500
   vrf Old_Gold_Ops
   ip address 10.253.0.0/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 10.253.0.0/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 10.253.2.0/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 10010 | - | - |
| 12 | 10012 | - | - |
| 110 | 10110 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Old_Gold_Ops | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description Leaf1_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 12 vni 10012
   vxlan vlan 110 vni 10110
   vxlan vrf Old_Gold_Ops vni 10
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

##### Virtual Router MAC Address: 00:1c:73:00:dc:01

#### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| mgmt | False |
| Old_Gold_Ops | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
ip routing vrf Old_Gold_Ops
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| mgmt | false |
| Old_Gold_Ops | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt | 0.0.0.0/0 | 172.17.0.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 172.17.0.1
```

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | 10.254.0.1 | enabled | Ethernet1 <br> Ethernet2 <br> Vlan4093 <br> | disabled | 12000 | disabled | disabled | - | - | - | - |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.0 | - | True |
| Ethernet2 | 0.0.0.0 | - | True |
| Vlan4093 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |
| Loopback1 | 0.0.0.0 | - | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 10.254.0.1
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Vlan4093
   max-lsa 12000
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 10.254.0.1 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 10.252.0.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 10.252.0.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 10.253.0.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Old_Gold_Ops | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Old_Gold_Ops | 10.254.0.1:10 | 10:10 | - | - | learned | 12,110 |
| Tenant_A_client_l2_only | 10.254.0.1:10010 | 10010:10010 | - | - | learned | 10 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Old_Gold_Ops | 10.254.0.1:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 10.254.0.1
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description Leaf2
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 10.252.0.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.0.1 remote-as 65001
   neighbor 10.252.0.1 description Spine1
   neighbor 10.252.0.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.0.2 remote-as 65001
   neighbor 10.252.0.2 description Spine2
   !
   vlan-aware-bundle Old_Gold_Ops
      rd 10.254.0.1:10
      route-target both 10:10
      redistribute learned
      vlan 12,110
   !
   vlan-aware-bundle Tenant_A_client_l2_only
      rd 10.254.0.1:10010
      route-target both 10010:10010
      redistribute learned
      vlan 10
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Old_Gold_Ops
      rd 10.254.0.1:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.254.0.1
      update wait-install
      neighbor 10.253.0.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Route-maps

#### Route-maps Summary

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |
| Old_Gold_Ops | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance mgmt
!
vrf instance Old_Gold_Ops
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Old_Gold_Ops | 10.255.1.1 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Old_Gold_Ops address 10.255.1.1
```

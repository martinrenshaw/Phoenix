# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 183 | 183 | 0 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| Leaf1 |  41 | 41 | 0 | - |
| Leaf2 |  40 | 40 | 0 | - |
| Leaf3 |  32 | 32 | 0 | - |
| Leaf4 |  32 | 32 | 0 | - |
| Spine1 |  19 | 19 | 0 | - |
| Spine2 |  19 | 19 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  6 | 6 | 0 |
| Interface State |  57 | 57 | 0 |
| LLDP Topology |  20 | 20 | 0 |
| MLAG |  2 | 2 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  22 | 22 | 0 |
| Routing Table |  36 | 36 | 0 |
| Loopback0 Reachability |  24 | 24 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | Leaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | Leaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | Leaf3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | Leaf4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | Spine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | Spine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - MLAG_PEER_Leaf2_Ethernet10 | PASS | - |
| 8 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet11 - MLAG_PEER_Leaf2_Ethernet11 | PASS | - |
| 9 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet1 | PASS | - |
| 10 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet1 | PASS | - |
| 11 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet19 - host01_Eth1 | PASS | - |
| 12 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet15 - PC-2_Eth1 | PASS | - |
| 13 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - MLAG_PEER_Leaf1_Ethernet10 | PASS | - |
| 14 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet11 - MLAG_PEER_Leaf1_Ethernet11 | PASS | - |
| 15 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet2 | PASS | - |
| 16 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet2 | PASS | - |
| 17 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet20 - host01_Eth2 | PASS | - |
| 18 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 19 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 20 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet19 - host02_Eth1 | PASS | - |
| 21 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - PC-3_Eth1 | PASS | - |
| 22 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 23 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 24 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet20 - host02_Eth2 | PASS | - |
| 25 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - PC-1_Eth1 | PASS | - |
| 26 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet1 | PASS | - |
| 27 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet1 | PASS | - |
| 28 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet1 | PASS | - |
| 29 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet1 | PASS | - |
| 30 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet2 | PASS | - |
| 31 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet2 | PASS | - |
| 32 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet2 | PASS | - |
| 33 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet2 | PASS | - |
| 34 | Leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel10 - MLAG_PEER_Leaf2_Po10 | PASS | - |
| 35 | Leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host01_PortChannel to Host1 | PASS | - |
| 36 | Leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel10 - MLAG_PEER_Leaf1_Po10 | PASS | - |
| 37 | Leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host01_PortChannel to Host1 | PASS | - |
| 38 | Leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host02_PortChannel to Host2 | PASS | - |
| 39 | Leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host02_PortChannel to Host2 | PASS | - |
| 40 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 41 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 42 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Gold_data | PASS | - |
| 43 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3998 - MLAG_PEER_L3_iBGP: vrf GOLD | PASS | - |
| 44 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 45 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 46 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Gold_data | PASS | - |
| 47 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3998 - MLAG_PEER_L3_iBGP: vrf GOLD | PASS | - |
| 48 | Leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan34 - Gold_data | PASS | - |
| 49 | Leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan34 - Gold_data | PASS | - |
| 50 | Leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 51 | Leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 52 | Leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 53 | Leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 54 | Leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 55 | Leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 56 | Leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 57 | Leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 58 | Leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 59 | Leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 60 | Leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 61 | Leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 62 | Spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 63 | Spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 64 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet10 - remote: Leaf2_Ethernet10 | PASS | - |
| 65 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet11 - remote: Leaf2_Ethernet11 | PASS | - |
| 66 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet1 | PASS | - |
| 67 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet1 | PASS | - |
| 68 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet10 - remote: Leaf1_Ethernet10 | PASS | - |
| 69 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet11 - remote: Leaf1_Ethernet11 | PASS | - |
| 70 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet2 | PASS | - |
| 71 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet2 | PASS | - |
| 72 | Leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet3 | PASS | - |
| 73 | Leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet3 | PASS | - |
| 74 | Leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet4 | PASS | - |
| 75 | Leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet4 | PASS | - |
| 76 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Leaf1_Ethernet1 | PASS | - |
| 77 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Leaf2_Ethernet1 | PASS | - |
| 78 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: Leaf3_Ethernet1 | PASS | - |
| 79 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: Leaf4_Ethernet1 | PASS | - |
| 80 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Leaf1_Ethernet2 | PASS | - |
| 81 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Leaf2_Ethernet2 | PASS | - |
| 82 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: Leaf3_Ethernet2 | PASS | - |
| 83 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: Leaf4_Ethernet2 | PASS | - |
| 84 | Leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 85 | Leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 86 | Leaf1 | IP Reachability | ip reachability test p2p links | Source: Leaf1_Ethernet1 - Destination: Spine1_Ethernet1 | PASS | - |
| 87 | Leaf1 | IP Reachability | ip reachability test p2p links | Source: Leaf1_Ethernet2 - Destination: Spine2_Ethernet1 | PASS | - |
| 88 | Leaf2 | IP Reachability | ip reachability test p2p links | Source: Leaf2_Ethernet1 - Destination: Spine1_Ethernet2 | PASS | - |
| 89 | Leaf2 | IP Reachability | ip reachability test p2p links | Source: Leaf2_Ethernet2 - Destination: Spine2_Ethernet2 | PASS | - |
| 90 | Leaf3 | IP Reachability | ip reachability test p2p links | Source: Leaf3_Ethernet1 - Destination: Spine1_Ethernet3 | PASS | - |
| 91 | Leaf3 | IP Reachability | ip reachability test p2p links | Source: Leaf3_Ethernet2 - Destination: Spine2_Ethernet3 | PASS | - |
| 92 | Leaf4 | IP Reachability | ip reachability test p2p links | Source: Leaf4_Ethernet1 - Destination: Spine1_Ethernet4 | PASS | - |
| 93 | Leaf4 | IP Reachability | ip reachability test p2p links | Source: Leaf4_Ethernet2 - Destination: Spine2_Ethernet4 | PASS | - |
| 94 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet1 - Destination: Leaf1_Ethernet1 | PASS | - |
| 95 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet2 - Destination: Leaf2_Ethernet1 | PASS | - |
| 96 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet3 - Destination: Leaf3_Ethernet1 | PASS | - |
| 97 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet4 - Destination: Leaf4_Ethernet1 | PASS | - |
| 98 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet1 - Destination: Leaf1_Ethernet2 | PASS | - |
| 99 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet2 - Destination: Leaf2_Ethernet2 | PASS | - |
| 100 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet3 - Destination: Leaf3_Ethernet2 | PASS | - |
| 101 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet4 - Destination: Leaf4_Ethernet2 | PASS | - |
| 102 | Leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 103 | Leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 104 | Leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 105 | Leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 106 | Spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 107 | Spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 108 | Leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 109 | Leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 110 | Leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 111 | Leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 112 | Leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 113 | Leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 114 | Leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 115 | Leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 116 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.1 | PASS | - |
| 117 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.2 | PASS | - |
| 118 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.3 | PASS | - |
| 119 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.4 | PASS | - |
| 120 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.1 | PASS | - |
| 121 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.2 | PASS | - |
| 122 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.3 | PASS | - |
| 123 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.4 | PASS | - |
| 124 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 125 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 126 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 127 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 128 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 129 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 130 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 131 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 132 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 133 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 134 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 135 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 136 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 137 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 138 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 139 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 140 | Leaf1 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 141 | Leaf1 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 142 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 143 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 144 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 145 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 146 | Leaf2 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 147 | Leaf2 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 148 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 149 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 150 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 151 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 152 | Leaf3 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 153 | Leaf3 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 154 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 155 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 156 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 157 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 158 | Leaf4 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 159 | Leaf4 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 160 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.1 | PASS | - |
| 161 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.2 | PASS | - |
| 162 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.3 | PASS | - |
| 163 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.4 | PASS | - |
| 164 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.252.0.1 | PASS | - |
| 165 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.252.0.2 | PASS | - |
| 166 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.1 | PASS | - |
| 167 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.2 | PASS | - |
| 168 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.3 | PASS | - |
| 169 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.4 | PASS | - |
| 170 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.252.0.1 | PASS | - |
| 171 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.252.0.2 | PASS | - |
| 172 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.1 | PASS | - |
| 173 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.2 | PASS | - |
| 174 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.3 | PASS | - |
| 175 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.4 | PASS | - |
| 176 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.252.0.1 | PASS | - |
| 177 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.252.0.2 | PASS | - |
| 178 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.1 | PASS | - |
| 179 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.2 | PASS | - |
| 180 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.3 | PASS | - |
| 181 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.4 | PASS | - |
| 182 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.252.0.1 | PASS | - |
| 183 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.252.0.2 | PASS | - |

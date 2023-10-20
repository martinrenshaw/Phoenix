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
| 188 | 182 | 6 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| Leaf1 |  42 | 41 | 1 | NTP |
| Leaf2 |  42 | 41 | 1 | NTP |
| Leaf3 |  33 | 32 | 1 | NTP |
| Leaf4 |  33 | 32 | 1 | NTP |
| Spine1 |  19 | 18 | 1 | NTP |
| Spine2 |  19 | 18 | 1 | NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  6 | 0 | 6 |
| Interface State |  62 | 62 | 0 |
| LLDP Topology |  20 | 20 | 0 |
| MLAG |  2 | 2 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  22 | 22 | 0 |
| Routing Table |  36 | 36 | 0 |
| Loopback0 Reachability |  24 | 24 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | Leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | Leaf2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | Leaf3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | Leaf4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | Spine1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | Spine2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | Leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | Leaf2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | Leaf3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | Leaf4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | Spine1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | Spine2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 7 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - MLAG_PEER_Leaf2_Ethernet10 | PASS | - |
| 8 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet11 - MLAG_PEER_Leaf2_Ethernet11 | PASS | - |
| 9 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet1 | PASS | - |
| 10 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet1 | PASS | - |
| 11 | Leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet19 - host1_Eth1 | PASS | - |
| 12 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet10 - MLAG_PEER_Leaf1_Ethernet10 | PASS | - |
| 13 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet11 - MLAG_PEER_Leaf1_Ethernet11 | PASS | - |
| 14 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet2 | PASS | - |
| 15 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet2 | PASS | - |
| 16 | Leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet20 - host1_Eth2 | PASS | - |
| 17 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 18 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 19 | Leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet19 - host2_Eth1 | PASS | - |
| 20 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 21 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 22 | Leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet20 - host2_Eth2 | PASS | - |
| 23 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet1 | PASS | - |
| 24 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet1 | PASS | - |
| 25 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet1 | PASS | - |
| 26 | Spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet1 | PASS | - |
| 27 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF1_Ethernet2 | PASS | - |
| 28 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF2_Ethernet2 | PASS | - |
| 29 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF3_Ethernet2 | PASS | - |
| 30 | Spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF4_Ethernet2 | PASS | - |
| 31 | Leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel10 - MLAG_PEER_Leaf2_Po10 | PASS | - |
| 32 | Leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host1_PortChannel3 | PASS | - |
| 33 | Leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel10 - MLAG_PEER_Leaf1_Po10 | PASS | - |
| 34 | Leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host1_PortChannel3 | PASS | - |
| 35 | Leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host2 | PASS | - |
| 36 | Leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel19 - host2 | PASS | - |
| 37 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 38 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 39 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Old_Gold_Ops_Zone_Test | PASS | - |
| 40 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan110 - Old_Gold_Ops_Zone_1 | PASS | - |
| 41 | Leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Old_Gold_Ops | PASS | - |
| 42 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 43 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 44 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Old_Gold_Ops_Zone_Test | PASS | - |
| 45 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan110 - Old_Gold_Ops_Zone_1 | PASS | - |
| 46 | Leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Old_Gold_Ops | PASS | - |
| 47 | Leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Old_Gold_Ops_Zone_Test | PASS | - |
| 48 | Leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan110 - Old_Gold_Ops_Zone_1 | PASS | - |
| 49 | Leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan12 - Old_Gold_Ops_Zone_Test | PASS | - |
| 50 | Leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan110 - Old_Gold_Ops_Zone_1 | PASS | - |
| 51 | Leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 52 | Leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 53 | Leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 54 | Leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 55 | Leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 56 | Leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 57 | Leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Old_Gold_Ops_VTEP_DIAGNOSTICS | PASS | - |
| 58 | Leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 59 | Leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 60 | Leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Old_Gold_Ops_VTEP_DIAGNOSTICS | PASS | - |
| 61 | Leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 62 | Leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 63 | Leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Old_Gold_Ops_VTEP_DIAGNOSTICS | PASS | - |
| 64 | Leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 65 | Leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 66 | Leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Old_Gold_Ops_VTEP_DIAGNOSTICS | PASS | - |
| 67 | Spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 68 | Spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 69 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet10 - remote: Leaf2_Ethernet10 | PASS | - |
| 70 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet11 - remote: Leaf2_Ethernet11 | PASS | - |
| 71 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet1 | PASS | - |
| 72 | Leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet1 | PASS | - |
| 73 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet10 - remote: Leaf1_Ethernet10 | PASS | - |
| 74 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet11 - remote: Leaf1_Ethernet11 | PASS | - |
| 75 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet2 | PASS | - |
| 76 | Leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet2 | PASS | - |
| 77 | Leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet3 | PASS | - |
| 78 | Leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet3 | PASS | - |
| 79 | Leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Spine1_Ethernet4 | PASS | - |
| 80 | Leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Spine2_Ethernet4 | PASS | - |
| 81 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Leaf1_Ethernet1 | PASS | - |
| 82 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Leaf2_Ethernet1 | PASS | - |
| 83 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: Leaf3_Ethernet1 | PASS | - |
| 84 | Spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: Leaf4_Ethernet1 | PASS | - |
| 85 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: Leaf1_Ethernet2 | PASS | - |
| 86 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: Leaf2_Ethernet2 | PASS | - |
| 87 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: Leaf3_Ethernet2 | PASS | - |
| 88 | Spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: Leaf4_Ethernet2 | PASS | - |
| 89 | Leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 90 | Leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 91 | Leaf1 | IP Reachability | ip reachability test p2p links | Source: Leaf1_Ethernet1 - Destination: Spine1_Ethernet1 | PASS | - |
| 92 | Leaf1 | IP Reachability | ip reachability test p2p links | Source: Leaf1_Ethernet2 - Destination: Spine2_Ethernet1 | PASS | - |
| 93 | Leaf2 | IP Reachability | ip reachability test p2p links | Source: Leaf2_Ethernet1 - Destination: Spine1_Ethernet2 | PASS | - |
| 94 | Leaf2 | IP Reachability | ip reachability test p2p links | Source: Leaf2_Ethernet2 - Destination: Spine2_Ethernet2 | PASS | - |
| 95 | Leaf3 | IP Reachability | ip reachability test p2p links | Source: Leaf3_Ethernet1 - Destination: Spine1_Ethernet3 | PASS | - |
| 96 | Leaf3 | IP Reachability | ip reachability test p2p links | Source: Leaf3_Ethernet2 - Destination: Spine2_Ethernet3 | PASS | - |
| 97 | Leaf4 | IP Reachability | ip reachability test p2p links | Source: Leaf4_Ethernet1 - Destination: Spine1_Ethernet4 | PASS | - |
| 98 | Leaf4 | IP Reachability | ip reachability test p2p links | Source: Leaf4_Ethernet2 - Destination: Spine2_Ethernet4 | PASS | - |
| 99 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet1 - Destination: Leaf1_Ethernet1 | PASS | - |
| 100 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet2 - Destination: Leaf2_Ethernet1 | PASS | - |
| 101 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet3 - Destination: Leaf3_Ethernet1 | PASS | - |
| 102 | Spine1 | IP Reachability | ip reachability test p2p links | Source: Spine1_Ethernet4 - Destination: Leaf4_Ethernet1 | PASS | - |
| 103 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet1 - Destination: Leaf1_Ethernet2 | PASS | - |
| 104 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet2 - Destination: Leaf2_Ethernet2 | PASS | - |
| 105 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet3 - Destination: Leaf3_Ethernet2 | PASS | - |
| 106 | Spine2 | IP Reachability | ip reachability test p2p links | Source: Spine2_Ethernet4 - Destination: Leaf4_Ethernet2 | PASS | - |
| 107 | Leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 108 | Leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 109 | Leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 110 | Leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 111 | Spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 112 | Spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 113 | Leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 114 | Leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 115 | Leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 116 | Leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 117 | Leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 118 | Leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 119 | Leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.1 | PASS | - |
| 120 | Leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.252.0.2 | PASS | - |
| 121 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.1 | PASS | - |
| 122 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.2 | PASS | - |
| 123 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.3 | PASS | - |
| 124 | Spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.4 | PASS | - |
| 125 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.1 | PASS | - |
| 126 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.2 | PASS | - |
| 127 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.3 | PASS | - |
| 128 | Spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.254.0.4 | PASS | - |
| 129 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 130 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 131 | Leaf1 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 132 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 133 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 134 | Leaf2 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 135 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 136 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 137 | Leaf3 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 138 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.1 | PASS | - |
| 139 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.3 | PASS | - |
| 140 | Leaf4 | Routing Table | Remote VTEP address | 10.254.1.4 | PASS | - |
| 141 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 142 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 143 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 144 | Leaf1 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 145 | Leaf1 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 146 | Leaf1 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 147 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 148 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 149 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 150 | Leaf2 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 151 | Leaf2 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 152 | Leaf2 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 153 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 154 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 155 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 156 | Leaf3 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 157 | Leaf3 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 158 | Leaf3 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 159 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.1 | PASS | - |
| 160 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.2 | PASS | - |
| 161 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.3 | PASS | - |
| 162 | Leaf4 | Routing Table | Remote Lo0 address | 10.254.0.4 | PASS | - |
| 163 | Leaf4 | Routing Table | Remote Lo0 address | 10.252.0.1 | PASS | - |
| 164 | Leaf4 | Routing Table | Remote Lo0 address | 10.252.0.2 | PASS | - |
| 165 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.1 | PASS | - |
| 166 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.2 | PASS | - |
| 167 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.3 | PASS | - |
| 168 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.254.0.4 | PASS | - |
| 169 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.252.0.1 | PASS | - |
| 170 | Leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf1 - 10.254.0.1 Destination: 10.252.0.2 | PASS | - |
| 171 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.1 | PASS | - |
| 172 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.2 | PASS | - |
| 173 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.3 | PASS | - |
| 174 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.254.0.4 | PASS | - |
| 175 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.252.0.1 | PASS | - |
| 176 | Leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf2 - 10.254.0.2 Destination: 10.252.0.2 | PASS | - |
| 177 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.1 | PASS | - |
| 178 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.2 | PASS | - |
| 179 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.3 | PASS | - |
| 180 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.254.0.4 | PASS | - |
| 181 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.252.0.1 | PASS | - |
| 182 | Leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf3 - 10.254.0.3 Destination: 10.252.0.2 | PASS | - |
| 183 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.1 | PASS | - |
| 184 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.2 | PASS | - |
| 185 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.3 | PASS | - |
| 186 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.254.0.4 | PASS | - |
| 187 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.252.0.1 | PASS | - |
| 188 | Leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: Leaf4 - 10.254.0.4 Destination: 10.252.0.2 | PASS | - |

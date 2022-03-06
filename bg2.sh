# for h4 to h29

ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:29,actions=output:8
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:29,actions=output:6
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:29,actions=output:6

ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:04,actions=output:9
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:04,actions=output:4
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:04,actions=output:4

ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.29,actions=output:8
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.29,actions=output:6
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.29,actions=output:6

ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.4,actions=output:9
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.4,actions=output:4
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.4,actions=output:4

# for h5 to h30

ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:30,actions=output:9
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:30,actions=output:12
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:05,actions=output:8
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:05,actions=output:7

ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.30,actions=output:9
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.30,actions=output:12
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.5,actions=output:8
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.5,actions=output:7

# for h6 to h31

ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:31,actions=output:10
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:31,actions=output:6
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:31,actions=output:6

ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:06,actions=output:10
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:06,actions=output:5
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:06,actions=output:4

ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.31,actions=output:10
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.31,actions=output:6
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.31,actions=output:6

ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.6,actions=output:10
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.6,actions=output:5
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.6,actions=output:4

# for s1

ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:01,actions=output:1
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:03,actions=output:3
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:04,actions=output:4
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:05,actions=output:5
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:06,actions=output:6
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:07,actions=output:7

ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:08,actions=output:8
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:12,actions=output:9
ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:17,actions=output:10

# for s2

ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:08,actions=output:1
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:09,actions=output:2
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:10,actions=output:3

ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:01,actions=output:4
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:11,actions=output:5
ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:20,actions=output:6


# for s3
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:11,actions=output:1
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:12,actions=output:2
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:13,actions=output:3
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:14,actions=output:4
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:15,actions=output:5
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:16,actions=output:6

ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:02,actions=output:7
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:09,actions=output:8
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:18,actions=output:9
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:21,actions=output:10
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:24,actions=output:11
ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:27,actions=output:12

# for s4

ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:17,actions=output:1
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:18,actions=output:2
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:19,actions=output:3

ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:07,actions=output:4
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:13,actions=output:5
ovs-ofctl add-flow s4 dl_dst=00:00:00:00:00:23,actions=output:6

# for s5

ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:20,actions=output:1
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:21,actions=output:2
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:22,actions=output:3

ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:10,actions=output:4
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:16,actions=output:5
ovs-ofctl add-flow s5 dl_dst=00:00:00:00:00:26,actions=output:6

# for s6

ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:23,actions=output:1
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:24,actions=output:2
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:25,actions=output:3

ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:14,actions=output:4
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:19,actions=output:5
ovs-ofctl add-flow s6 dl_dst=00:00:00:00:00:32,actions=output:6

# for s7

ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:26,actions=output:1
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:27,actions=output:2
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:28,actions=output:3
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:29,actions=output:4
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:30,actions=output:5
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:31,actions=output:6
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:32,actions=output:7

ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:15,actions=output:8
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:22,actions=output:9
ovs-ofctl add-flow s7 dl_dst=00:00:00:00:00:25,actions=output:10

# arp for s1

ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.1,actions=output:1
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.2,actions=output:2
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.3,actions=output:3
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.4,actions=output:4
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.5,actions=output:5
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.6,actions=output:6
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.7,actions=output:7

ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.8,actions=output:8
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.12,actions=output:9
ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.17,actions=output:10

# arp for s2

ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.8,actions=output:1
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.9,actions=output:2
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.10,actions=output:3

ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.1,actions=output:4
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.11,actions=output:5
ovs-ofctl add-flow s2 arp,nw_dst=10.0.0.20,actions=output:6

# arp for s3

ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.11,actions=output:1
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.12,actions=output:2
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.13,actions=output:3
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.14,actions=output:4
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.15,actions=output:5
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.16,actions=output:6

ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.2,actions=output:7
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.9,actions=output:8
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.18,actions=output:9
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.21,actions=output:10
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.24,actions=output:11
ovs-ofctl add-flow s3 arp,nw_dst=10.0.0.27,actions=output:12

# arp for s4

ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.17,actions=output:1
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.18,actions=output:2
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.19,actions=output:3

ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.7,actions=output:4
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.13,actions=output:5
ovs-ofctl add-flow s4 arp,nw_dst=10.0.0.23,actions=output:6

# arp for s5

ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.20,actions=output:1
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.21,actions=output:2
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.22,actions=output:3

ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.10,actions=output:4
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.16,actions=output:5
ovs-ofctl add-flow s5 arp,nw_dst=10.0.0.26,actions=output:6

# arp for s6

ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.23,actions=output:1
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.24,actions=output:2
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.25,actions=output:3

ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.14,actions=output:4
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.19,actions=output:5
ovs-ofctl add-flow s6 arp,nw_dst=10.0.0.32,actions=output:6

# arp for s7

ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.26,actions=output:1
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.27,actions=output:2
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.28,actions=output:3
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.29,actions=output:4
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.30,actions=output:5
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.31,actions=output:6
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.32,actions=output:7

ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.15,actions=output:8
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.22,actions=output:9
ovs-ofctl add-flow s7 arp,nw_dst=10.0.0.25,actions=output:10
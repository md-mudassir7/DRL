import os

"""
    Adding flow entries
"""


# ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:01,actions=output:1
def add_flow_dl_dst(dpid, dl_dst, out_port, nw_dst=None, add_arp=False):
    command = 'ovs-ofctl add-flow {0} dl_dst={1},actions=output:{2}'.format(dpid, dl_dst, out_port)
    os.system(command)

    if add_arp:
        if nw_dst is None:
            print("ARP flow not added because nw_dst not specified")
        else:
            add_flow_arp(dpid, nw_dst, out_port)


"""
    Deleting flow entries
"""


# ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.1,actions=output:1
def add_flow_arp(dpid, nw_dst, out_port):
    command = 'ovs-ofctl add-flow {0} arp,nw_dst={1},actions=output:{2}'.format(dpid, nw_dst, out_port)
    os.system(command)


# sh ovs-ofctl del-flows s1 dl_dst=00:00:00:00:00:01
def del_flows(dpid, dl_dst, nw_dst=None, del_arp=False):
    command = 'ovs-ofctl del-flow {0} dl_dst={1}'.format(dpid, dl_dst)
    os.system(command)

    if del_arp:
        if nw_dst is None:
            print("ARP flow not deleted because nw_dst not specified")
        else:
            del_flow_arp(dpid, nw_dst)


# sh ovs-ofctl del-flows s1 arp,nw_dst=10.0.0.1
def del_flow_arp(dpid, nw_dst):
    command = 'ovs-ofctl del-flow {0} arp,nw_dst={1}'.format(dpid, nw_dst)
    os.system(command)

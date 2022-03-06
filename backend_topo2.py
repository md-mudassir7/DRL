import subprocess
import time
import os
import random

from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import lg

from flow_api import *
from flow_api import *

class MininetBackend(object):
    def __init__(self):
        self.net = Mininet(topo=None, build=False, listenPort=6633, ipBase='10.0.0.0/8')
        # for preventing net.pingFull() log outputs
        # lg.setLogLevel("warning")

        self.LINK_BW = 10
        self.res = []
        self.current_throughput = 0.0
        # info('*** Adding controller\n')
        self.c0 = self.net.addController(name='c0',
                                         controller=RemoteController,
                                         ip='127.0.0.1',
                                         protocol='tcp',
                                         port=6633)

        self.h1 = self.net.addHost('h1', ip='10.0.0.1', mac="00:00:00:00:00:01")
        self.h2 = self.net.addHost('h2', ip='10.0.0.2', mac="00:00:00:00:00:02")
        self.h3 = self.net.addHost('h3', ip='10.0.0.3', mac="00:00:00:00:00:03")
        self.h4 = self.net.addHost('h4', ip='10.0.0.4', mac="00:00:00:00:00:04")
        self.h5 = self.net.addHost('h5', ip='10.0.0.5', mac="00:00:00:00:00:05")
        self.h6 = self.net.addHost('h6', ip='10.0.0.6', mac="00:00:00:00:00:06")
        self.h7 = self.net.addHost('h7', ip='10.0.0.7', mac="00:00:00:00:00:07")
        self.h8 = self.net.addHost('h8', ip='10.0.0.8', mac="00:00:00:00:00:08")
        self.h9 = self.net.addHost('h9', ip='10.0.0.9', mac="00:00:00:00:00:09")
        self.h10 = self.net.addHost('h10', ip='10.0.0.10', mac="00:00:00:00:00:10")
        self.h11 = self.net.addHost('h11', ip='10.0.0.11', mac="00:00:00:00:00:11")
        self.h12 = self.net.addHost('h12', ip='10.0.0.12', mac="00:00:00:00:00:12")
        self.h13 = self.net.addHost('h13', ip='10.0.0.13', mac="00:00:00:00:00:13")
        self.h14 = self.net.addHost('h14', ip='10.0.0.14', mac="00:00:00:00:00:14")
        self.h15 = self.net.addHost('h15', ip='10.0.0.15', mac="00:00:00:00:00:15")
        self.h16 = self.net.addHost('h16', ip='10.0.0.16', mac="00:00:00:00:00:16")
        self.h17 = self.net.addHost('h17', ip='10.0.0.17', mac="00:00:00:00:00:17")
        self.h18 = self.net.addHost('h18', ip='10.0.0.18', mac="00:00:00:00:00:18")
        self.h19 = self.net.addHost('h19', ip='10.0.0.19', mac="00:00:00:00:00:19")
        self.h20 = self.net.addHost('h20', ip='10.0.0.20', mac="00:00:00:00:00:20")
        self.h21 = self.net.addHost('h21', ip='10.0.0.21', mac="00:00:00:00:00:21")
        self.h22 = self.net.addHost('h22', ip='10.0.0.22', mac="00:00:00:00:00:22")
        self.h23 = self.net.addHost('h23', ip='10.0.0.23', mac="00:00:00:00:00:23")
        self.h24 = self.net.addHost('h24', ip='10.0.0.24', mac="00:00:00:00:00:24")
        self.h25 = self.net.addHost('h25', ip='10.0.0.25', mac="00:00:00:00:00:25")
        self.h26 = self.net.addHost('h26', ip='10.0.0.26', mac="00:00:00:00:00:26")
        self.h27 = self.net.addHost('h27', ip='10.0.0.27', mac="00:00:00:00:00:27")
        self.h28 = self.net.addHost('h28', ip='10.0.0.28', mac="00:00:00:00:00:28")
        self.h29 = self.net.addHost('h29', ip='10.0.0.29', mac="00:00:00:00:00:29")
        self.h30 = self.net.addHost('h30', ip='10.0.0.30', mac="00:00:00:00:00:30")
        self.h31 = self.net.addHost('h31', ip='10.0.0.31', mac="00:00:00:00:00:31")
        self.h32 = self.net.addHost('h32', ip='10.0.0.32', mac="00:00:00:00:00:32")

        self.s1 = self.net.addSwitch('s1')
        self.s2 = self.net.addSwitch('s2')
        self.s3 = self.net.addSwitch('s3')
        self.s4 = self.net.addSwitch('s4')
        self.s5 = self.net.addSwitch('s5')
        self.s6 = self.net.addSwitch('s6')
        self.s7 = self.net.addSwitch('s7')
        # Add links

        self.net.addLink(self.h1, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h2, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h3, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h4, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h5, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h6, self.s1, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h7, self.s1, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h8, self.s2, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h9, self.s2, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h10, self.s2, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h11, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h12, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h13, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h14, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h15, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h16, self.s3, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h17, self.s4, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h18, self.s4, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h19, self.s4, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h20, self.s5, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h21, self.s5, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h22, self.s5, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h23, self.s6, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h24, self.s6, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h25, self.s6, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.h26, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h27, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h28, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h29, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h30, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h31, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.h32, self.s7, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.s1, self.s2, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s1, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s1, self.s4, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.s2, self.s3, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s2, self.s5, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.s3, self.s4, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s3, self.s5, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s3, self.s6, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s3, self.s7, cls=TCLink, bw=self.LINK_BW)

        self.net.addLink(self.s4, self.s6, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s5, self.s7, cls=TCLink, bw=self.LINK_BW)
        self.net.addLink(self.s6, self.s7, cls=TCLink, bw=self.LINK_BW)

        # run 'net' command in "mininet>" CLI to obtain all the ports mapped to each link

        # Adjacency matrix where map[i][j] gives link's port number for i-th switch connected to j-th switch.
        # 0 if switches i and j aren't connected in the topology
        # represents:   s_i:map[i][j] <===link===> map[j][i]:s_j
        # example:      S1:p8 <===link===> p4:S2
        self.port_map = [[0, 8, 9, 10, 0, 0, 0],
                         [4, 0, 5, 0, 6, 0, 0],
                         [7, 8, 0, 9, 10, 11, 12],
                         [4, 0, 5, 0, 0, 6, 0],
                         [0, 4, 5, 0, 0, 0, 6],
                         [0, 0, 4, 5, 0, 0, 6],
                         [0, 0, 8, 0, 9, 10, 0]]

        for controller in self.net.controllers:
            controller.start()

        self.net.get('s1').start([self.c0])
        self.net.get('s2').start([self.c0])
        self.net.get('s3').start([self.c0])
        self.net.get('s4').start([self.c0])
        self.net.get('s5').start([self.c0])
        self.net.get('s6').start([self.c0])
        self.net.get('s7').start([self.c0])

        self.net.build()
        time.sleep(2)

        #os.system('sudo ./flow_management/constant2.sh')
        #os.system('sudo ./flow_management/bg2.sh')
        os.system('sudo ./constant2.sh')
        os.system('sudo ./bg2.sh')

        # link traffic
        self.h8.cmd('iperf -s -p 6655 -i 1 &> ./logs/h8.log &')
        self.h12.cmd('iperf -s -p 6655 -i 1 &> ./logs/h12.log &')
        self.h17.cmd('iperf -s -p 6655 -i 1 &> ./logs/h17.log &')
        self.h11.cmd('iperf -s -p 6655 -i 1 &> ./logs/h11.log &')
        self.h18.cmd('iperf -s -p 6655 -i 1 &> ./logs/h18.log &')
        self.h20.cmd('iperf -s -p 6655 -i 1 &> ./logs/h20.log &')
        self.h21.cmd('iperf -s -p 6655 -i 1 &> ./logs/h21.log &')
        self.h27.cmd('iperf -s -p 6655 -i 1 &> ./logs/h27.log &')
        self.h24.cmd('iperf -s -p 6655 -i 1 &> ./logs/h24.log &')
        self.h23.cmd('iperf -s -p 6655 -i 1 &> ./logs/h23.log &')
        self.h26.cmd('iperf -s -p 6655 -i 1 &> ./logs/h26.log &')
        self.h32.cmd('iperf -s -p 6655 -i 1 &> ./logs/h32.log &')

        self.start_traffic()
        time.sleep(2)
        # start listening
        self.h28.cmd('iperf -s -p 6655 -i 1 &> ./logs/h28.log &')

        # CLI(self.net)
        # self.net.stop()

    def killProcess(self, host_num):

        # check if any background traffic process is running
        # stop the process if found
        # for background process associated with server 10.0.0.host_num
        command_str = "ps -ef | grep 10.0.0.{} | grep iperf".format(host_num)
        temp = subprocess.getoutput(command_str)
        temp = temp.split('\n')
        # print(temp)
        # temp=temp[0].split()
        # print(temp)
        # if temp[1] != '':
        #     subprocess.getoutput('kill '+temp[1])

        # do a while loop
        for i in range(0, len(temp)):
            temp2 = temp[i].split()
            if temp2[1] != '':
                subprocess.getoutput('kill ' + temp2[1])

    def start_traffic(self):

        # link traffic

        # self.h8.cmd('iperf -s -p 6655 -i 1 &> ./logs/h8.log &')
        self.h1.cmd('iperf -c 10.0.0.8 -p 6655 -b 5M -t 1800 &> ./logs/h1.log &')

        # self.h12.cmd('iperf -s -p 6655 -i 1 &> ./logs/h12.log &')
        self.h2.cmd('iperf -c 10.0.0.12 -p 6655 -b 5M -t 1800 &> ./logs/h2.log &')

        # self.h17.cmd('iperf -s -p 6655 -i 1 &> ./logs/h17.log &')
        self.h7.cmd('iperf -c 10.0.0.17 -p 6655 -b 5M -t 1800 &> ./logs/h7.log &')

        # self.h11.cmd('iperf -s -p 6655 -i 1 &> ./logs/h11.log &')
        self.h9.cmd('iperf -c 10.0.0.11 -p 6655 -b 5M -t 1800 &> ./logs/h9.log &')

        # self.h18.cmd('iperf -s -p 6655 -i 1 &> ./logs/h18.log &')
        self.h13.cmd('iperf -c 10.0.0.18 -p 6655 -b 5M -t 1800 &> ./logs/h13.log &')

        # self.h20.cmd('iperf -s -p 6655 -i 1 &> ./logs/h20.log &')
        self.h10.cmd('iperf -c 10.0.0.20 -p 6655 -b 5M -t 1800 &> ./logs/h10.log &')

        # self.h21.cmd('iperf -s -p 6655 -i 1 &> ./logs/h21.log &')
        self.h16.cmd('iperf -c 10.0.0.21 -p 6655 -b 5M -t 1800 &> ./logs/h16.log &')

        # self.h27.cmd('iperf -s -p 6655 -i 1 &> ./logs/h27.log &')
        self.h15.cmd('iperf -c 10.0.0.27 -p 6655 -b 5M -t 1800 &> ./logs/h15.log &')

        # self.h24.cmd('iperf -s -p 6655 -i 1 &> ./logs/h24.log &')
        self.h14.cmd('iperf -c 10.0.0.24 -p 6655 -b 5M -t 1800 &> ./logs/h14.log &')

        # self.h23.cmd('iperf -s -p 6655 -i 1 &> ./logs/h23.log &')
        self.h19.cmd('iperf -c 10.0.0.23 -p 6655 -b 5M -t 1800 &> ./logs/h19.log &')

        # self.h26.cmd('iperf -s -p 6655 -i 1 &> ./logs/h26.log &')
        self.h22.cmd('iperf -c 10.0.0.26 -p 6655 -b 5M -t 1800 &> ./logs/h22.log &')

        # self.h32.cmd('iperf -s -p 6655 -i 1 &> ./logs/h32.log &')
        self.h25.cmd('iperf -c 10.0.0.32 -p 6655 -b 5M -t 1800 &> ./logs/h25.log &')

        random_path = random.randint(0, 2)

        print("Less bg traffic in path", random_path)
        if random_path == 0:
            self.h30.cmd('iperf -s -p 6655 -i 1 &> ./logs/h30.log &')
            self.h5.cmd('iperf -c 10.0.0.30 -p 6655 -t 1800 &> ./logs/h5.log &')
            self.h31.cmd('iperf -s -p 6655 -i 1 &> ./logs/h31.log &')
            self.h6.cmd('iperf -c 10.0.0.31 -p 6655 -t 1800 &> ./logs/h6.log &')
        elif random_path == 1:
            self.h29.cmd('iperf -s -p 6655 -i 1 &> ./logs/h29.log &')
            self.h4.cmd('iperf -c 10.0.0.29 -p 6655 -t 1800 &> ./logs/h4.log &')
            self.h31.cmd('iperf -s -p 6655 -i 1 &> ./logs/h31.log &')
            self.h6.cmd('iperf -c 10.0.0.31 -p 6655 -t 1800 &> ./logs/h6.log &')
        else:
            self.h29.cmd('iperf -s -p 6655 -i 1 &> ./logs/h29.log &')
            self.h4.cmd('iperf -c 10.0.0.29 -p 6655 -t 1800 &> ./logs/h4.log &')
            self.h30.cmd('iperf -s -p 6655 -i 1 &> ./logs/h30.log &')
            self.h5.cmd('iperf -c 10.0.0.30 -p 6655 -t 1800 &> ./logs/h5.log &')

    def switch(self, s, p):
        # cmd="sudo ovs-ofctl dump-ports "+s
        # output=subprocess.check_output(cmd.split())
        output = subprocess.getoutput("sudo ovs-ofctl dump-ports " + s)
        port_details = {}
        n = int(output[28:30])
        for i in range(1, n):
            port_details[str(i)] = {}
        temp = output.split('\n')
        i = 1
        while i < 2 * n + 1:
            st = temp[i]
            # print("st = ", st)
            port = 0
            try:
                port = str(int(st[7:9]))
            except:
                i += 2
                continue
            # for odd one , rx
            new = st[11:]
            new = new.split(' ')
            rxpkts = new[1].replace('pkts=', '')
            rxpkts = rxpkts.replace(',', '')
            rxbytes = new[2].replace('bytes=', '')
            rxbytes = rxbytes.replace(',', '')

            port_details[port]['rxpkts'] = rxpkts
            port_details[port]['rxbytes'] = rxbytes

            # for even one, tx
            i += 1
            st = temp[i]
            new = st[11:]
            new = new.split(' ')
            txpkts = new[1].replace('pkts=', '')
            txpkts = txpkts.replace(',', '')
            txbytes = new[2].replace('bytes=', '')
            txbytes = txbytes.replace(',', '')

            port_details[port]['txpkts'] = txpkts
            port_details[port]['txbytes'] = txbytes
            i += 1
            # print("Ports for s-", s, port)
            # print(port_details[port])

        return port_details[p]

    # port packet loss for a link between s_a & s_b
    def link_port_pkt_loss(self, s_a, s_b):
        loss = 0

        # print("Calculating loss for ", "s" + str(s_a), self.port_map[s_a - 1][s_b - 1])
        l1 = self.switch('s' + str(s_a), str(self.port_map[s_a - 1][s_b - 1]))
        l = (float(l1['txpkts']) - float(l1['rxpkts'])) / float(l1['txpkts'])
        loss += abs(l)

        # print("Calculating loss for ", "s" + str(s_b), self.port_map[s_b - 1][s_a - 1])
        l2 = self.switch('s' + str(s_b), str(self.port_map[s_b - 1][s_a - 1]))
        l = (float(l2['txpkts']) - float(l2['rxpkts'])) / float(l2['txpkts'])
        loss += abs(l)

        return loss

    def link_throughput(self, h):
        with open('./logs/h{}.log'.format(h), 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
        a = 0
        try:
            # temp = last_line.split()[-1]
            # print('temp=', temp)
            unit = last_line.split()[-1]
            bw = last_line.split()[-2]
            # print('h=', h, 'Thrpt = ', bw, unit)

            a = float(bw)
        except:
            print("WARN: Couldn't fetch BW from h{}.log".format(h))
            print("h{}.log : {} \n".format(h, last_line))
            return a
        if unit == 'Mbits/sec':
            return a / self.LINK_BW
        else:
            return a / (self.LINK_BW * 1000)

    def link_latency(self, h_a, h_b):
        # range 0 - 5s
        # lat = self.net.pingFull(hosts=[self.net.hosts[h_a - 1], self.net.hosts[h_b - 1]])[0][2][3]
        # print("h{} ping h{}: {}".format(h_a, h_b, lat))
        return self.net.pingFull(hosts=[self.net.hosts[h_a - 1], self.net.hosts[h_b - 1]])[0][2][3] / 100.0

    def add_main_flows(self, path):
        print(path)
        for i in range(len(path) - 1):
            add_flow_dl_dst("s" + str(path[i]), "00:00:00:00:00:28", self.port_map[path[i] - 1][path[i + 1] - 1],
                            "10.0.0.28", add_arp=True)

        path.reverse()
        for i in range(len(path) - 1):
            add_flow_dl_dst("s" + str(path[i]), "00:00:00:00:00:03", self.port_map[path[i] - 1][path[i + 1] - 1],
                            "10.0.0.3", add_arp=True)

    def route_iperf(self):
        time.sleep(2)
        bw = self.net.iperf([self.h28, self.h3])[0].split()
        unit = bw[1]
        bw = bw[0]
        self.current_throughput = 0.0
        print('current_bw=', bw)
        try:
            self.current_throughput = float(bw)
        except:
            print("WARN: Couldn't calculate current BW")
            return self.current_throughput
        # print("Throughput: ", self.current_throughput)
        # del flows here if routing multiple times in the same episode
        # self.res.append(out.split('\n')[6])
        if unit == 'Mbits/sec':
            return self.current_throughput
        else:
            return self.current_throughput / 1000

    def route_main(self):
        # CLI(self.net)
        time.sleep(2)
        out = self.h3.cmd('iperf -c 10.0.0.28 -p 6655 -n 1M')
        print(out)
        self.current_throughput = 0.0
        out = (out.split('\n')[6]).split()
        bw = out[-2]
        unit = out[-1]
        # print('current_bw=', bw)
        try:
            self.current_throughput = float(bw)
        except:
            print("WARN: Couldn't calculate current BW", out)
            return self.current_throughput
        # print("Throughput: ", self.current_throughput)
        # del flows here if routing multiple times in the same episode
        # self.res.append(out.split('\n')[6])
        if unit == 'Mbits/sec':
            return self.current_throughput
        else:
            return self.current_throughput / 1000

    def clean(self):
        for i in range(32):
            self.killProcess(i + 1)

        os.system('sudo ./flow_management/clear2.sh')
        self.net.stop()
        os.system('sudo mn -c > /dev/null 2>&1')

# only for testing the topology
if __name__ == '__main__':
    mn = MininetBackend()
    x = 1
    p = []
    while x != 0:
        CLI(mn.net)
        # simulate an agent's task (Enter path)
        print("Enter Path length: ", end="")
        for _ in range(int(input())):
            p.append(int(input()))
        mn.add_main_flows(p)
        print("CurrentBW: ", mn.route_main())
        # mn.route_iperf()
        print("Enter 1.Add path, 0.Exit")
        x = int(input())
        p = []
    mn.clean()

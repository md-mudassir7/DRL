#!/usr/bin/env python
import gym
import numpy as np
from gym import spaces
import time
from backend_topo2 import MininetBackend


class TestEnv(gym.Env):

    def __init__(self, max_ticks=8):
        self.__version__ = "0.1.0"
        print("Initialising Test_MN_env - Version {}".format(self.__version__))

        # General variables defining the environment
        self.MAX_TICKS = max_ticks
        self.LINK_BW = 10

        self.SOURCE = 1
        self.DEST = 7
        self.current_switch = self.SOURCE
        # graph
        self.switch_map = np.array([
            [0, 1, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 0],
        ], dtype=np.int32)
        self.current_switch = 1
        # Mapping actions to switches
        self.link_action_dict = {
            1: [2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [1, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0],
            3: [0, 1, 0, 2, 4, 0, 5, 7, 6, 0, 0, 0],
            4: [0, 0, 1, 0, 3, 0, 0, 0, 0, 6, 0, 0],
            5: [0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 7, 0],
            6: [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 7],
            7: [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 5, 6]
        }
        # Mapping links to monitored hosts
        self.link_host_map = [[1, 8], [2, 12], [7, 17], [9, 11],
                              [13, 18], [10, 20], [16, 21], [15, 27],
                              [14, 24], [19, 23], [22, 26], [25, 32]]
        self.visited_node = [False for _ in range(7)]
        self.visited_node[0] = True
        self.routing_path = [self.SOURCE]
        # Reward matrix
        self.reward_mat = np.zeros((3, 12))

        self.backend = MininetBackend()
        self.action_space = spaces.Discrete(12)
        self.QOS_n = 3

        # Observation space
        low = np.zeros((self.QOS_n, 12), dtype=np.float32)

        high = np.ones((self.QOS_n, 12), dtype=np.float32)

        self.observation_space = spaces.Box(low=low.flatten(), high=high.flatten(), dtype=np.float32)
        self.current_ep = 0
        # episode over
        self.episode_over = False
        self.info = {'exit_status': 'FAILED', 'bw': 0.0}

    def step(self, action):
        """
        Agents takes a step in the environment with an action
        :param action : action_index (int)
        :return: obs, reward, episode_over (tuple)
            obs: observation tuple specific to the environment (object)
            reward: reward gained from the previous action
            episode_over: flag to indicate the end of an episode
        :info (dict) :
            diagnostic information useful for debugging. It can sometimes
            be useful for learning (for example, it might contain the raw
            probabilities behind the environment's last state change).
            However, official evaluations of your agent are not allowed to
            use this for learning.
        """

        reward = self.take_action(action)
        ob = self.get_state()

        return ob, reward, self.episode_over, self.info

    def take_action(self, action):
        # self.episode_over = self.backend.switch_action(action)
        reward = 0

        if self.ticks==self.MAX_TICKS || self.current_switch==self.destination:
            if self.current_switch==self.destination:
                print("\n--------Destination reached after %d ticks--------", %self.ticks)
                self.backend.add_main_flows(self.routing_path)
                start_time = time.time()
                BW = self.backend.route_main()
                end_time = time.time()
                self.episode_over = True
                self.info['exit_status'] = 'NORMAL'
                self.info['bw'] = 'BW'
                reward += 2
                print("Throughput = ", bw)
                print("Delay(s) = ", (end_time-start_time))
                if bw >= 0.5*self.LINK_BW
                    reward += 5
                elif 0.3*self.LINK_BW <= bw <= 0.5*self.LINK_BW
                    reward +=2
                else:
                    reward -= 3
            else:
                print("MAX_TICKS over ending episode")
                self.episode_over = True
                self.info['exit_status'] = 'FAILED'
                self.info['bw'] = 0.0
                reward -= 10
        else:
            self.ticks += 1
            dest_switch = self.link_action_dict[self.current_switch][action]
            if dest_switch != 0:
                if not self.visited_node[dest_switch - 1]:
                    reward = 0
                    self.visited_node[dest_switch - 1] = True
                    self.current_switch = dest_switch
                    self.routing_path.append(self.current_switch)
                else:
                    reward -= 1
            else:
                reward -= 2


        # if self.ticks == self.MAX_TICKS or self.current_switch == self.DEST:
        # call reward function
        return reward

    def get_reward(self):
        # write your reward function here
        return

    def reset(self):
        """
        Reset the state of the environment and returns an initial observation.

        Returns
        -------
        observation (object): the initial observation of the space.
        """
        self.current_ep += 1
        #self.ticks = 0
        self.episode_over = False
        for i in range(7):
            zself.visited_node[i] = False
        self.visited_node[0] = True
        self.routing_path = [self.SOURCE]
        self.current_switch = self.SOURCE
        self.backend.clean()
        self.backend = MininetBackend()
        return self.get_state()

    def render(self, mode='human', close=False):
        return

    def get_state(self):
        pkt_loss = np.ones(12, dtype=np.float32)
        bw = np.zeros(12,dtype=np.float32)
        lat = np.ones(12,dtype=np.float32)
        for i in range(len(self.link_action_dict[self.current_switch])):
            # packet loss
            if self.link_action_dict[self.current_switch][i] != 0:
                pkt_loss[i] = self.backend.link_port_pkt_loss(self.current_switch, self.link_action_dict[self.current_switch][i])
                bw[i] = self.backend.link_throughput(self.link_host_map[i][1])
                lat[i] = self.backend.link_latency(self.link_host_map[i][0] , self.link_host_map[i][1])

        return np.concatenate((pkt_loss,bw,lat), axis=None).tolist()

    def cleanup(self):
        self.backend.clean()

    def finalResult(self):
        print(self.backend.res)
        self.backend.res = []
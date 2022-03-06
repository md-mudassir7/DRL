import gym
import sys
import numpy as np
import os
import time

# import logging
# registers env with the init script
import env

from env.test_env import TestEnv
# from Agents.Dueling_DeepQN import Agent as DuelingAgent
from agents.DRLAgent import Agent
#import utils

if __name__ == '__main__':

    env = gym.make('mn-env-v2')
    score = 0
    n_episodes = 20
    load_chkpt = True
    MAX_TICKS = 10

    # logging.basicConfig(filename='dqn_ep_100.log', level=logging.DEBUG)

    # keeping track of score
    scores_history, eps_history = [], []
    input_dims = env.observation_space.shape[0]
    print("n_actions ", env.action_space.n)
    # Dueling DQN agent

    # dueling_dql_agent = DuelingAgent(gamma=0.99, epsilon=1.0, alpha=0.003,n_actions=env.action_space.n,
    #               input_dims=[input_dims], mem_size=100000,batch_size=64, eps_min=0.1,
    #               eps_dec=3e-3, replace=100)

    # DQN agent
    #agent = Agent(gamma=0.99,learn_rate=0.0001, epsilon=1.0, batch_size=64,input_dims=[env.observation_space.shape[0]],
                  #n_actions=env.action_space.n,layer1_size=64,layer2_size=96)
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4, epsn_end=0.01, input_dims=[8], learn_rate=0.003)
    observation = []
    avg_time = []

    if load_chkpt:
        agent.load_models()

    for i in range(n_episodes):
        print("\n=========================")
        print("\tEpisode", i)
        print("=========================")
        done = False
        score = 0
        observation = env.reset()
        info = {'exit_status': 'FAILED', 'bw': 0.0}
        while not done:
            # print("Ob:", observation)
            start_time = time.time()
            action = agent.choose_action(observation)
            end_time = time.time()
            observation_, reward, done, info = env.step(action)
            agent.learn()
            observation = observation_
            score += reward
            log_str = 'Ticks: %d ' % (env.ticks + 1) + 'Action: %d ' % action + \
                      'R: %d ' % reward + 'Total Reward: %s ' % score
            #print(log_str)
            avg_time.append(end_time - start_time)

        scores_history.append(score)
        avg_score = float(np.mean(scores_history[-20:]))
        print('episode: %d score: %.2f avg score: %.2f' % (i, score, avg_score))
        row = [i, score , avg_score , info['bw'], info['exit_status']]

        #if (i + 1) % 20 == 0:
        #    print('Score: ', score, avg_score)
        #    exit()

        if (i+1) % 20 == 0:
            agent.save_models()

    env.cleanup()

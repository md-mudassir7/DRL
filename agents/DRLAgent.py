import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim.adam as optim
import numpy as np
import os


class DeepQNet(nn.Module):
    def __init__(self, learn_rate, input_dims, fc1_dims, fc2_dims, n_actions, chkpt_dir='./DQNModels'):
        super(DeepQNet, self).__init__()
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.n_actions = n_actions

        self.fc1 = nn.Linear(*self.input_dims, self.fc1_dims)
        self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
        self.fc3 = nn.Linear(self.fc2_dims, self.n_actions)
        self.optimiser = optim.Adam(self.parameters(), lr=learn_rate)
        self.loss = nn.MSELoss()

        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)
        print("Device: ", self.device)

        self.chkpt_dir = chkpt_dir
        self.chkpt_file = os.path.join(self.chkpt_dir, 'dqn_chkpt_v3_0_host')

    def forward(self, state):
        x = F.relu(self.fc1(state.float()))
        x = F.relu(self.fc2(x))
        actions = self.fc3(x)

        return actions

    def save_checkpoint(self):
        print("~~~~~~ Checkpoint: Saving Model ~~~~~~")
        T.save(self.state_dict(), self.chkpt_file)

    def load_checkpoint(self):
        print("~~~~~~ Loading Checkpoint ~~~~~~")
        self.load_state_dict(T.load(self.chkpt_file))


class Agent():
    def __init__(self, gamma, epsilon, learn_rate, input_dims, batch_size, n_actions,
                 max_mem_size=100000, epsn_end=0.01, epsn_dec=3e-3):
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsn_min = epsn_end
        self.epsn_dec = epsn_dec
        self.learn_rate = learn_rate
        # self.action_space = np.arange(n_actions)
        self.action_space = [i for i in range(n_actions)]
        self.mem_size = max_mem_size
        self.batch_size = batch_size
        self.mem_ctr = 0

        self.neuralNet = DeepQNet(self.learn_rate, input_dims, fc1_dims=64, fc2_dims=32, n_actions=n_actions)

        self.state_memory = np.zeros((self.mem_size, *input_dims), dtype=np.float32)
        self.new_state_memory = np.zeros((self.mem_size, *input_dims), dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int32)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.bool)

    def store_transition(self, state, action, reward, new_state, done):
        index = self.mem_ctr % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.reward_memory[index] = reward
        self.action_memory[index] = action
        self.terminal_memory[index] = done

        # indicate step is over
        self.mem_ctr += 1

    def choose_action(self, observation):
        # state = T.tensor([observation]).to(self.neuralNet.device)
        # actions = self.neuralNet.forward(state)
        # # print("Actions layer: %s" % str(actions))
        # action = T.argmax(actions).item()

        if np.random.random() > self.epsilon:
            state = T.tensor([observation]).to(self.neuralNet.device)
            actions = self.neuralNet.forward(state)
            action = T.argmax(actions).item()
        else:
            action = np.random.choice(self.action_space)

        return action

    def learn(self):
        if self.mem_ctr < self.batch_size:
            return
        # print("\nINFO: Learning batch")
        self.neuralNet.optimiser.zero_grad()
        max_mem = min(self.mem_ctr, self.mem_size)

        batch = np.random.choice(max_mem, self.batch_size, replace=False)
        batch_index = np.arange(self.batch_size, dtype=np.int32)

        state_batch = T.tensor(self.state_memory[batch]).to(self.neuralNet.device)
        new_state_batch = T.tensor(self.new_state_memory[batch]).to(self.neuralNet.device)
        reward_batch = T.tensor(self.reward_memory[batch]).to(self.neuralNet.device)
        terminal_batch = T.tensor(self.terminal_memory[batch]).to(self.neuralNet.device)
        action_batch = self.action_memory[batch]

        q_eval = self.neuralNet.forward(state_batch)[batch_index, action_batch]
        q_next = self.neuralNet.forward(new_state_batch)
        # print("terminal_batch type = ", terminal_batch)
        q_next[terminal_batch] = 0.0

        q_target = reward_batch + self.gamma * T.max(q_next, dim=1)[0]

        loss = self.neuralNet.loss(q_target, q_eval).to(self.neuralNet.device)
        loss.backward()
        self.neuralNet.optimiser.step()

        self.epsilon = self.epsilon - self.epsn_dec if (self.epsilon > self.epsn_min) \
            else self.epsn_min

    def save_models(self):
        self.neuralNet.save_checkpoint()

    def load_models(self):
        self.neuralNet.load_checkpoint()

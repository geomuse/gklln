import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
import cv2  # 用于图像缩放
from collections import deque
import pygame
from gym_snake import SnakeEnv  
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Q网络
class DQNNet(nn.Module):
    def __init__(self, input_shape, action_size):
        super(DQNNet, self).__init__()
        c, h, w = input_shape
        self.conv = nn.Sequential(
            nn.Conv2d(c, 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU()
        )
        conv_out_size = self._get_conv_out(input_shape)
        self.fc = nn.Sequential(
            nn.Linear(conv_out_size, 512),
            nn.ReLU(),
            nn.Linear(512, action_size)
        )

    def _get_conv_out(self, shape):
        o = self.conv(torch.zeros(1, *shape))
        return int(np.prod(o.size()))

    def forward(self, x):
        x = x.float() / 255.0  # 归一化
        conv_out = self.conv(x)
        return self.fc(conv_out.view(x.size()[0], -1))

# 经验回放
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = zip(*batch)
        return np.array(state), action, reward, np.array(next_state), done
    def __len__(self):
        return len(self.buffer)

# 预处理：灰度 + 缩小
def preprocess(obs):
    obs_gray = cv2.cvtColor(obs, cv2.COLOR_RGB2GRAY)
    obs_resize = cv2.resize(obs_gray, (84, 84), interpolation=cv2.INTER_AREA)
    return np.expand_dims(obs_resize, axis=0)  # (1,84,84)

# DQN训练
def train_dqn(env, episodes=500):
    action_size = env.action_space.n
    state_shape = (1, 84, 84)  # 灰度图
    online_net = DQNNet(state_shape, action_size)
    target_net = DQNNet(state_shape, action_size)
    target_net.load_state_dict(online_net.state_dict())

    optimizer = optim.Adam(online_net.parameters(), lr=1e-4)
    buffer = ReplayBuffer(10000)

    gamma = 0.99
    batch_size = 32
    epsilon = 1.0
    epsilon_min = 0.1
    epsilon_decay = 0.995
    target_update_freq = 10

    for ep in range(episodes):
        obs = env.reset()
        obs = preprocess(obs)
        total_reward = 0
        done = False

        while not done:
            pygame.event.pump()  # 处理pygame事件，防止阻塞

            # ε-greedy
            if random.random() < epsilon:
                action = env.action_space.sample()
            else:
                with torch.no_grad():
                    q_values = online_net(torch.tensor(obs).unsqueeze(0))
                    action = q_values.argmax().item()

            next_obs, reward, done, _ = env.step(action)
            reward -= 0.01  # 惩罚拖延
            next_obs = preprocess(next_obs)

            buffer.push(obs, action, reward, next_obs, done)
            obs = next_obs
            total_reward += reward

            # 训练
            if len(buffer) >= batch_size:
                s, a, r, s_next, d = buffer.sample(batch_size)
                s = torch.tensor(s)
                a = torch.tensor(a)
                r = torch.tensor(r, dtype=torch.float32)
                s_next = torch.tensor(s_next)
                d = torch.tensor(d, dtype=torch.float32)

                q_values = online_net(s).gather(1, a.unsqueeze(1)).squeeze(1)
                with torch.no_grad():
                    max_next_q = target_net(s_next).max(1)[0]
                    target_q = r + gamma * max_next_q * (1 - d)

                loss = nn.MSELoss()(q_values, target_q)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        # 更新epsilon
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

        # 更新target网络
        if ep % target_update_freq == 0:
            target_net.load_state_dict(online_net.state_dict())

        print(f"Episode {ep}, Reward: {total_reward:.2f}, Epsilon: {epsilon:.2f}")

if __name__ == "__main__":

    env = SnakeEnv()
    train_dqn(env, episodes=500)
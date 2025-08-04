import gym

env = gym.make("CartPole-v1")
obs = env.reset()

for episode in range(5):  # 训练5局
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        env.render()  # 可视化（有些系统需要额外设置）
        action = env.action_space.sample()  # 随机动作
        obs, reward, done, info = env.step(action)
        total_reward += reward

    print(f"第 {episode+1} 局总奖励: {total_reward}")
env.close()
import gym

# 创建游戏环境
env = gym.make("FrozenLake-v1", render_mode="human")

# 初始化环境
env.reset()

# 运行游戏 500 步（自动玩）
for _ in range(500):
    action = env.action_space.sample()  # 随机动作
    obs, reward, done, truncated, info = env.step(action)
    if done or truncated:
        print(reward)
        env.reset()

env.close()

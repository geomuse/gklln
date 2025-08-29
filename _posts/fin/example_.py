import numpy as np
import matplotlib.pyplot as plt

# 模拟股票收益（非系统性风险 + 系统性风险）
np.random.seed(42)
n_assets = 100
n_obs = 1000
market_return = np.random.normal(0, 0.02, n_obs)

# 每只股票收益 = beta * market + 特定风险
betas = np.random.uniform(0.8, 1.2, n_assets)
specific_risk = np.random.normal(0, 0.03, (n_obs, n_assets))
returns = market_return.reshape(-1,1) * betas + specific_risk

portfolio_risks = []
for n in range(1, n_assets+1):
    weights = np.ones(n) / n
    sub_returns = returns[:, :n] @ weights
    portfolio_risks.append(np.std(sub_returns))

plt.plot(range(1, n_assets+1), portfolio_risks, label="Portfolio Risk")
plt.axhline(np.std(market_return), color="red", linestyle="--", label="Systematic Risk")
plt.xlabel("Number of Stocks in Portfolio")
plt.ylabel("Portfolio Risk (Std Dev)")
plt.title("Diversification Effect on Risk")
plt.legend()
plt.show()
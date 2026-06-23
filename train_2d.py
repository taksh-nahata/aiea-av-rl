import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CarRacing-v2", continuous=True)

model = PPO("CnnPolicy", env, verbose=1, tensorboard_log="./tensorboard_logs/")

print("The 2D self-driving car training is starting...")

model.learn(total_timesteps=10000, tb_log_name="PPO_2D_Racing")
print("The 2D self-driving car training has finished!")

env.close()
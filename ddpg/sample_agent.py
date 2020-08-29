import gym
import gym_grand_prix

# env = gym.make('Pendulum-v0')
env = gym.make('GrandPrix-v0')

observation = env.reset()
done = False
for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)
    print(observation, reward, info)
    if done:
        observation = env.reset()
env.close()


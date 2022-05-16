import numpy as np
from social_dilemmas.envs.pettingzoo_env import MAX_CYCLES
from social_dilemmas.envs.pettingzoo_env import env as aec_env

from random import seed
from random import randint

import matplotlib.pyplot as plt

seed(666)

def main():
    env = aec_env(env = "harvest", num_agents = 2)
    env.seed()
    env.reset()
    n_act = env.action_space("agent-0").n

    counter = 0
    for agent in env.agent_iter():
        counter += 1
        obs, reward, done, info = env.last()        
        action = randint(0,n_act-1) if not done else None
        env.step(action)
        img = env.render('rgb_array')
        plt.imshow(img)
        plt.show(block=False)
        plt.pause(1)
        plt.close("all")
        if counter%100 == 0:
            # r = env.observation_spaces
            # y = env.food_spaces
            # x = env.possible_missing_agents
            for agent in env.agents:
                print(agent, env.observation_space(agent))
            # print(x)
            # print(len(y))
            # print(y)
            # print(r)
            # break
        if counter == 10000:
            break


if __name__ == "__main__":
    main()
import numpy as np
from numpy.random import rand
from gym.spaces import Discrete

from math import floor
from social_dilemmas.envs.agent import HarvestAppleAgent, HarvestOrangeAgent
from social_dilemmas.envs.map_env import MapEnv
from social_dilemmas.maps import HARVEST_MAP
from social_dilemmas.envs.generate_map import create_map
from social_dilemmas.maps import BATTLE_MAP

APPLE_RADIUS = 2

# Add custom actions to the agent
# _HARVEST_ACTIONS = {"FIRE": 5}  # length of firing range

# SPAWN_PROB = [0, 0.005, 0.02, 0.05]

SPAWN_PROB = [1, 1, 1, 1]

HARVEST_VIEW_SIZE = 4


class HarvestEnv(MapEnv):
    def __init__(
        self,
        ascii_map=HARVEST_MAP,
        num_agents=1,
        return_agent_actions=False,
        use_collective_reward=False,
        inequity_averse_reward=False,
        proportion = 0.5,
        alpha=0.0,
        poc = True,
        beta=0.0,
    ):
        super().__init__(
            ascii_map,
            {},
            HARVEST_VIEW_SIZE,
            num_agents,
            return_agent_actions=return_agent_actions,
            use_collective_reward=use_collective_reward,
            inequity_averse_reward=inequity_averse_reward,
            alpha=alpha,
            beta=beta,
            poc = poc,
            proportion=proportion
        )
        self.apple_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"A":
                    self.apple_points.append([row, col])

        self.orange_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"O":
                    self.orange_points.append([row, col])
        self.proportion = proportion

    @property
    def action_space(self):
        return Discrete(7)

    def setup_agents(self):
        map_with_agents = self.get_map_with_agents()

        self.num_apple_agents = floor(self.proportion*self.num_agents)
        self.num_orange_agents = self.num_agents - self.num_apple_agents

        for i in range(self.num_apple_agents):
            agent_id = "agent-apple-" + str(i)
            spawn_point = self.spawn_point_apple()
            rotation = self.spawn_rotation()
            grid = map_with_agents
            agent = HarvestAppleAgent(agent_id, spawn_point, rotation, grid, view_len=HARVEST_VIEW_SIZE)
            self.agents[agent_id] = agent

        for i in range(self.num_orange_agents):
            agent_id = "agent-orange-" + str(i)
            spawn_point = self.spawn_point_orange()
            rotation = self.spawn_rotation()
            grid = map_with_agents
            agent = HarvestOrangeAgent(agent_id, spawn_point, rotation, grid, view_len=HARVEST_VIEW_SIZE)
            self.agents[agent_id] = agent

    def custom_reset(self):
        """Initialize the walls and the apples"""
        for apple_point in self.apple_points:
            self.single_update_map(apple_point[0], apple_point[1], b"A")
        for orange_point in self.orange_points:
            self.single_update_map(orange_point[0], orange_point[1], b"O")


    def custom_action(self, agent, action):
        agent.fire_beam(b"F")
        updates = self.update_map_fire(
            agent.pos.tolist(),
            agent.get_orientation(),
            self.all_actions["FIRE"],
            fire_char=b"F",
        )
        return updates

    def regenerate_map(self):
        # TODO: edit create map para solo llamarlo aqui
        self.world_map = self.ascii_to_numpy(create_map(existing_map = self.world_map, distance=9))
        # self.world_map = self.ascii_to_numpy(BATTLE_MAP)
        self.apple_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"A":
                    self.apple_points.append([row, col])

        self.orange_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"O":
                    self.orange_points.append([row, col])
        # return temporal_map


    def custom_map_update(self):
        """See parent class"""
        # spawn the apples
        # new_apples = self.spawn_apples()
        # new_oranges = self.spawn_oranges()
        # self.update_map(new_apples)
        # self.update_map(new_oranges)

        self.base_map = self.ascii_to_numpy(create_map(distance=9))
        # self.base_map = self.ascii_to_numpy(BATTLE_MAP)
        self.apple_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"A":
                    self.apple_points.append([row, col])

        self.orange_points = []
        for row in range(self.base_map.shape[0]):
            for col in range(self.base_map.shape[1]):
                if self.base_map[row, col] == b"O":
                    self.orange_points.append([row, col])




    def spawn_apples(self):
        """Construct the apples spawned in this step.

        Returns
        -------
        new_apple_points: list of 2-d lists
            a list containing lists indicating the spawn positions of new apples
        """

        new_apple_points = []
        agent_positions = self.agent_pos
        random_numbers = rand(len(self.apple_points))
        r = 0
        for i in range(len(self.apple_points)):
            row, col = self.apple_points[i]
            # apples can't spawn where agents are standing or where an apple already is
            if [row, col] not in agent_positions and (self.world_map[row, col] != b"A") and (self.world_map[row, col] != b"O"):
                num_apples = 0
                for j in range(-APPLE_RADIUS, APPLE_RADIUS + 1):
                    for k in range(-APPLE_RADIUS, APPLE_RADIUS + 1):
                        if j ** 2 + k ** 2 <= APPLE_RADIUS:
                            x, y = self.apple_points[i]
                            if (
                                0 <= x + j < self.world_map.shape[0]
                                and self.world_map.shape[1] > y + k >= 0
                            ):
                                if self.world_map[x + j, y + k] == b"A":
                                    num_apples += 1

                spawn_prob = SPAWN_PROB[min(num_apples, 3)]
                rand_num = random_numbers[r]
                r += 1
                if rand_num < spawn_prob:
                    new_apple_points.append((row, col, b"A"))
        return new_apple_points

    def spawn_oranges(self):
        """Construct the apples spawned in this step.

        Returns
        -------
        new_orange_points: list of 2-d lists
            a list containing lists indicating the spawn positions of new orange
        """

        new_orange_points = []
        agent_positions = self.agent_pos
        random_numbers = rand(len(self.apple_points))
        r = 0
        for i in range(len(self.apple_points)):
            row, col = self.apple_points[i]
            # apples can't spawn where agents are standing or where an apple already is
            if [row, col] not in agent_positions and (self.world_map[row, col] != b"A") and (self.world_map[row, col] != b"O"):
                num_oranges = 0
                for j in range(-APPLE_RADIUS, APPLE_RADIUS + 1):
                    for k in range(-APPLE_RADIUS, APPLE_RADIUS + 1):
                        if j ** 2 + k ** 2 <= APPLE_RADIUS:
                            x, y = self.apple_points[i]
                            if (
                                0 <= x + j < self.world_map.shape[0]
                                and self.world_map.shape[1] > y + k >= 0
                            ):
                                if (self.world_map[x + j, y + k] == b"O") or (self.world_map[x + j, y + k] == b"A"):
                                    num_oranges += 1

                spawn_prob = SPAWN_PROB[min(num_oranges, 3)]
                rand_num = random_numbers[r]
                r += 1
                if rand_num < spawn_prob:
                    new_orange_points.append((row, col, b"O"))
        return new_orange_points

    def count_apples(self, window):
        # compute how many apples are in window
        unique, counts = np.unique(window, return_counts=True)
        counts_dict = dict(zip(unique, counts))
        num_apples = counts_dict.get(b"A", 0)
        return num_apples

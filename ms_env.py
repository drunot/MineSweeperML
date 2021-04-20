# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:02:49 2021

@author: au615804
"""
# %%

import os, sys
sys.path.append(os.path.dirname(__file__))

from minesweeper.minesweeper import Minesweeper
import abc
import tensorflow as tf
import numpy as np
import math

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

# %%

class MinesweeperEnv(py_environment.PyEnvironment):
    
    def __init__(self):
        self._game = Minesweeper()
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(),
            dtype=np.int32,
            minimum=0,
            maximum=99,
            name='action'
            )
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(100,),
            dtype=np.int32,
            minimum=0,
            name='observation'
            )
        self._episode_ended = False
        
    def action_spec(self):
        return self._action_spec
    
    def observation_spec(self):
        return self._observation_spec
    
    def _reset(self):
        self._episode_ended = False
        self._game = Minesweeper()
        return self._game.board
    
    def _step(self, action):
        y = math.floor(action / self._game.width)
        x = round(action % self._game.width)
        random_guess = True
        for i in range(y-1, y+1):
            for j in range(x-1, x+1):
                if i < 0 or self._game.height < i or j < 0 or self._game.width < j:
                    pass
                if self._game.board[i][j] != 9:
                    random_guess = False
        if not self._game.board[y][x] == 9 or random_guess:
            reward = -0.5
        else:
            reward = 0.5
        if not self._game.open_square(y, x):
            self._episode_ended = True
            reward = -2
        elif self._game.is_game_won():
            self._episode_ended = True
            reward = 2
        
        return self._game.board, reward, self._episode_ended
            
        
# %%
env = MinesweeperEnv()
utils.validate_py_environment(env, episodes=5)

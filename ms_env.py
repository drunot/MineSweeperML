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

# %%

class MinesweeperEnv():
    
    def __init__(self):
        self._game = Minesweeper()
        self._episode_ended = False
        self._first_action = True
        
    def action_spec(self):
        return self._action_spec
    
    def observation_spec(self):
        return self._observation_spec
    
    def reset(self):
        self._episode_ended = False
        self._game = Minesweeper()
        self._first_action = True
        return self._game.board
    
    def step(self, action):
        y = math.floor(action / self._game.width)
        x = round(action % self._game.width)
        random_guess = True
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if i < 0 or self._game.height <= i or j < 0 or self._game.width <= j:
                    continue
                if self._game.board[i][j] != -1:
                    random_guess = False
        if not self._game.board[y][x] == -1 or random_guess and not self._first_action:
            reward = -0.5
        else:
            reward = 0.5
        if not self._game.open_square(y, x):
            self._episode_ended = True
            reward = -2
        elif self._game.is_game_won():
            self._episode_ended = True
            reward = 2
        
        self._first_action = False
        obs = np.divide(self._game.board, 10)
        return obs, reward, self._episode_ended
            
        
# %%
env = MinesweeperEnv()


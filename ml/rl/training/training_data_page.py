#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class TrainingDataPage(object):
    __slots__ = [
        'states', 'actions', 'rewards', 'next_states', 'next_actions',
        'possible_next_actions', 'reward_timelines', 'not_terminals'
    ]

    def __init__(
        self,
        states,
        actions,
        rewards,
        next_states,
        next_actions,
        possible_next_actions,
        reward_timelines,
        not_terminals=None,
    ) -> None:
        """
        Creates a TrainingDataPage object.

        In the case where `not_terminals` can be determined by next_actions or
        possible_next_actions, feel free to omit it.
        """
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.next_states = next_states
        self.next_actions = next_actions
        self.possible_next_actions = possible_next_actions
        self.reward_timelines = reward_timelines
        self.not_terminals = not_terminals

    def size(self) -> int:
        return len(self.states)

    def get_sub_page(self, start, end):
        return TrainingDataPage(
            self.states[start:end],
            self.actions[start:end],
            self.rewards[start:end],
            self.next_states[start:end],
            self.next_actions[start:end],
            self.possible_next_actions[start:end],
            self.reward_timelines[start:end],
            None
            if self.not_terminals is None else self.not_terminals[start:end],
        )

from __future__ import annotations

import itertools
from typing import NamedTuple

from aoc import utils


def parse_data(data):
    boss_hp = int(data[0].split()[2])
    boss_dp = int(data[1].split()[1])
    boss_ap = int(data[2].split()[1])
    return boss_hp, boss_dp, boss_ap


class Item(NamedTuple):
    name: str
    cost: int
    damage: int
    armour: int


WEAPONS = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

ARMOUR = [
    Item("<no armour>", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

RINGS = [
    Item("<no ring>", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defence +1", 20, 0, 1),
    Item("Defence +2", 40, 0, 2),
    Item("Defence +3", 80, 0, 3),
]


class Player:
    def __init__(self, name: str, hp: int, dp: int, ap: int):
        self.name = name
        self._hp = hp
        self._damage = dp
        self._armour = ap

    def attack(self, other: Player) -> bool:
        # When a player attacks, the other player defends.
        utils.log(f"Player {self.name} attacks {other.name} with dam:{self._damage}")
        other_hp = other._defend(self._damage)
        return other_hp <= 0

    def _defend(self, damage: int) -> int:
        utils.log(f"Player {self.name} defends with {self._armour}")
        damage_taken = max(1, damage - self._armour)
        self._hp -= damage_taken
        utils.log(
            f"Player {self.name} takes {damage_taken} damage and has {self._hp} hp remaining"
        )
        return self._hp


def play_one(player1: Player, player2: Player) -> Player:
    while True:
        if player1.attack(player2):
            utils.log(f"Player {player1.name} wins")
            return player1
        if player2.attack(player1):
            utils.log(f"Player {player2.name} wins")
            return player2


def choose_items(maximise_cost=False) -> list[tuple[tuple[int, int], int]]:
    # exactly one weapon
    # zero or one armour
    # zero, one, or two rings
    all_combinations = list(
        set(items) for items in itertools.product(WEAPONS, ARMOUR, RINGS, RINGS)
    )
    cost_by_effect: dict[tuple[int, int], int] = {}
    for comb in all_combinations:
        dam = 0
        arm = 0
        cost = 0
        for item in comb:
            dam += item.damage
            arm += item.armour
            cost += item.cost

        effect = dam, arm

        if maximise_cost:
            if cost_by_effect.get(effect, -1) < cost:
                cost_by_effect[effect] = cost
        else:
            if cost_by_effect.get(effect, 10000) > cost:
                cost_by_effect[effect] = cost

    by_price = sorted(cost_by_effect.items(), key=lambda x: x[1], reverse=maximise_cost)
    return by_price


def play_many(boss_stats, my_items, winner_is_me) -> int:
    for (dam, arm), price in my_items:
        me = Player("meee", 100, dam, arm)
        boss = Player("boss", *boss_stats)

        wanted_winner = me if winner_is_me else boss

        if play_one(me, boss) is wanted_winner:
            return price

    raise Exception("No winner")


def part1(data) -> int:
    return play_many(data, choose_items(), winner_is_me=True)


def part2(data) -> int:
    return play_many(data, choose_items(maximise_cost=True), winner_is_me=False)

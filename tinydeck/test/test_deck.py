# -*- coding: utf-8 -*-

import random
import unittest
import tinydeck
import tinydeck.deck as dk


class TestDeck(unittest.TestCase):

    def testDkSuits(self):
        model = '♠ ♥ ♦ ♣'.split()
        for s in dk.suits:
            model.remove(s)
        self.assertEquals(len(model), 0)

    def testDkRanks(self):
        model = 'A 2 3 4 5 6 7 8 9 J Q K 10'.split()
        for r in dk.ranks:
            model.remove(r)
        self.assertEquals(len(model), 0)

    def testDkDeck(self):
        model = ['♠A', '♥A', '♦A', '♣A',
                 '♠2', '♥2', '♦2', '♣2',
                 '♠3', '♥3', '♦3', '♣3',
                 '♠4', '♥4', '♦4', '♣4',
                 '♠5', '♥5', '♦5', '♣5',
                 '♠6', '♥6', '♦6', '♣6',
                 '♠7', '♥7', '♦7', '♣7',
                 '♠8', '♥8', '♦8', '♣8',
                 '♠9', '♥9', '♦9', '♣9',
                 '♠J', '♥J', '♦J', '♣J',
                 '♠Q', '♥Q', '♦Q', '♣Q',
                 '♠K', '♥K', '♦K', '♣K',
                 '♠10', '♥10', '♦10', '♣10']
        for c in dk.deck:
            model.remove(c)
        self.assertEqual(len(model), 0)

    def testDealDefault(self):
        deck = tinydeck.deal()
        model = list(dk.deck)
        for c in deck:
            model.remove(c)
        self.assertEqual(len(model), 0)

    def testDealSource(self):
        source = [1, 2, 3, 4, 5]
        model = list(source)
        deck = tinydeck.deal(source)
        for c in deck:
            model.remove(c)
        self.assertEqual(len(model), 0)

    def testDealLimit(self):
        deck = tinydeck.deal(limit=10)
        model = list(dk.deck)
        for c in deck:
            model.remove(c)
        self.assertEqual(len(model), 42)

    def testDealRand(self):
        rand = random.Random(1337)
        deck = tinydeck.deal(rand=rand)
        model = ['♣J', '♦9', '♣K', '♣6',
                 '♦J', '♥Q', '♦3', '♦6',
                 '♣7', '♥10', '♦7', '♠6',
                 '♣8', '♦4', '♦8', '♦2',
                 '♠Q', '♠J', '♠2', '♣10',
                 '♥9', '♦K', '♠5', '♥5',
                 '♥K', '♣Q', '♦10', '♠d4',
                 '♦Q', '♠A', '♣5', '♠K',
                 '♥2', '♥8', '♥4', '♥3',
                 '♥7', '♠8', '♣9', '♠7',
                 '♦5', '♥J', '♠3', '♣2',
                 '♦A', '♠9', '♥6', '♠10',
                 '♥A', '♣A', '♣4', '♣3']
        self.assertListEqual(list(deck), model)

    def testExpectSuitsIsTuple(self):
        self.assertIsInstance(dk.suits, tuple)

    def testExpectRanksIsTuple(self):
        self.assertIsInstance(dk.ranks, tuple)

    def testExpectDeckIsTuple(self):
        self.assertIsInstance(dk.deck, tuple)


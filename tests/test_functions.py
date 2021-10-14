import deltae
import unittest


class TestDeltaE2000(unittest.TestCase):

    def test_pair_1(self):
        """ Tests Pair 1 """
        # Pair 1
        Lab1 = {'L': 50.0, 'a': 2.6772, 'b': -79.7751}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 2.6774)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 79.82)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 271.9222)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 270.9611)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.6907)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.6578)
        self.assertEqual(sH, 1.8421)
        self.assertEqual(rT, -1.7042)
        self.assertEqual(de2000, 2.0425)

    def test_pair_2(self):
        """ Tests Pair 2 """
        # Pair 2
        Lab1 = {'L': 50.0, 'a': 3.1571, 'b': -77.2803}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.1573)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 77.3448)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 272.3395)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 271.1698)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.6843)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.6021)
        self.assertEqual(sH, 1.8216)
        self.assertEqual(rT, -1.707)
        self.assertEqual(de2000, 2.8615)

    def test_pair_3(self):
        """ Tests Pair 3 """
        # Pair 3
        Lab1 = {'L': 50.0, 'a': 2.8361, 'b': -74.02}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 2.8363)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 74.0743)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 272.1944)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 271.0972)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.6865)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.5285)
        self.assertEqual(sH, 1.8074)
        self.assertEqual(rT, -1.706)
        self.assertEqual(de2000, 3.4412)

    def test_pair_4(self):
        """ Tests Pair 4 """
        # Pair 4
        Lab1 = {'L': 50.0, 'a': -1.3802, 'b': -84.2814}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -1.3803)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 84.2927)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 269.0618)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 269.5309)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.7357)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.7584)
        self.assertEqual(sH, 1.9217)
        self.assertEqual(rT, -1.6809)
        self.assertEqual(de2000, 1.0)

    def test_pair_5(self):
        """ Tests Pair 5 """
        # Pair 5
        Lab1 = {'L': 50.0, 'a': -1.1848, 'b': -84.8006}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -1.1849)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 84.8089)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 269.1995)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 269.5997)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.7335)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.77)
        self.assertEqual(sH, 1.9218)
        self.assertEqual(rT, -1.6822)
        self.assertEqual(de2000, 1.0)

    def test_pair_6(self):
        """ Tests Pair 6 """
        # Pair 6
        Lab1 = {'L': 50.0, 'a': -0.9009, 'b': -85.5211}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -82.7485}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.9009)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 85.5258)
        self.assertEqual(c2Prime, 82.7485)
        self.assertEqual(h1Prime, 269.3964)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 269.6982)
        self.assertEqual(g, 0.0001)
        self.assertEqual(t, 0.7303)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 4.7862)
        self.assertEqual(sH, 1.9217)
        self.assertEqual(rT, -1.684)
        self.assertEqual(de2000, 1.0)

    def test_pair_7(self):
        """ Tests Pair 7 """
        # Pair 7
        Lab1 = {'L': 50.0, 'a': 0.0, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': -1.0, 'b': 2.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 0.0)
        self.assertEqual(a2Prime, -1.5)
        self.assertEqual(c1Prime, 0.0)
        self.assertEqual(c2Prime, 2.5)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 126.8697)
        self.assertEqual(hBarPrime, 126.8697)
        self.assertEqual(g, 0.5)
        self.assertEqual(t, 1.22)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.0562)
        self.assertEqual(sH, 1.0229)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 2.3669)

    def test_pair_8(self):
        """ Tests Pair 8 """
        # Pair 8
        Lab1 = {'L': 50.0, 'a': -1.0, 'b': 2.0}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': 0.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -1.5)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 2.5)
        self.assertEqual(c2Prime, 0.0)
        self.assertEqual(h1Prime, 126.8697)
        self.assertEqual(h2Prime, 0.0)
        self.assertEqual(hBarPrime, 126.8697)
        self.assertEqual(g, 0.5)
        self.assertEqual(t, 1.22)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.0562)
        self.assertEqual(sH, 1.0229)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 2.3669)

    def test_pair_9(self):
        """ Tests Pair 9 """
        # Pair 9
        Lab1 = {'L': 50.0, 'a': 2.49, 'b': -0.001}
        Lab2 = {'L': 50.0, 'a': -2.49, 'b': 0.0009}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7346)
        self.assertEqual(a2Prime, -3.7346)
        self.assertEqual(c1Prime, 3.7346)
        self.assertEqual(c2Prime, 3.7346)
        self.assertEqual(h1Prime, 359.9847)
        self.assertEqual(h2Prime, 179.9862)
        self.assertEqual(hBarPrime, 269.9854)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.7212)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1681)
        self.assertEqual(sH, 1.0404)
        self.assertEqual(rT, -0.0022)
        self.assertEqual(de2000, 7.1792)

    def test_pair_10(self):
        """ Tests Pair 10 """
        # Pair 10
        Lab1 = {'L': 50.0, 'a': 2.49, 'b': -0.001}
        Lab2 = {'L': 50.0, 'a': -2.49, 'b': 0.001}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7346)
        self.assertEqual(a2Prime, -3.7346)
        self.assertEqual(c1Prime, 3.7346)
        self.assertEqual(c2Prime, 3.7346)
        self.assertEqual(h1Prime, 359.9847)
        self.assertEqual(h2Prime, 179.9847)
        self.assertEqual(hBarPrime, 269.9847)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.7212)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1681)
        self.assertEqual(sH, 1.0404)
        self.assertEqual(rT, -0.0022)
        self.assertEqual(de2000, 7.1792)

    def test_pair_11(self):
        """ Tests Pair 11 """
        # Pair 11
        Lab1 = {'L': 50.0, 'a': 2.49, 'b': -0.001}
        Lab2 = {'L': 50.0, 'a': -2.49, 'b': 0.0011}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7346)
        self.assertEqual(a2Prime, -3.7346)
        self.assertEqual(c1Prime, 3.7346)
        self.assertEqual(c2Prime, 3.7346)
        self.assertEqual(h1Prime, 359.9847)
        self.assertEqual(h2Prime, 179.9831)
        self.assertEqual(hBarPrime, 89.9839)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.6175)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1681)
        self.assertEqual(sH, 1.0346)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 7.2195)

    def test_pair_12(self):
        """ Tests Pair 12 """
        # Pair 12
        Lab1 = {'L': 50.0, 'a': 2.49, 'b': -0.001}
        Lab2 = {'L': 50.0, 'a': -2.49, 'b': 0.0012}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7346)
        self.assertEqual(a2Prime, -3.7346)
        self.assertEqual(c1Prime, 3.7346)
        self.assertEqual(c2Prime, 3.7346)
        self.assertEqual(h1Prime, 359.9847)
        self.assertEqual(h2Prime, 179.9816)
        self.assertEqual(hBarPrime, 89.9831)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.6175)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1681)
        self.assertEqual(sH, 1.0346)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 7.2195)

    def test_pair_13(self):
        """ Tests Pair 13 """
        # Pair 13
        Lab1 = {'L': 50.0, 'a': -0.001, 'b': 2.49}
        Lab2 = {'L': 50.0, 'a': 0.0009, 'b': -2.49}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.0015)
        self.assertEqual(a2Prime, 0.0013)
        self.assertEqual(c1Prime, 2.49)
        self.assertEqual(c2Prime, 2.49)
        self.assertEqual(h1Prime, 90.0345)
        self.assertEqual(h2Prime, 270.0311)
        self.assertEqual(hBarPrime, 180.0328)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.9779)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1121)
        self.assertEqual(sH, 1.0365)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 4.8045)

    def test_pair_14(self):
        """ Tests Pair 14 """
        # Pair 14
        Lab1 = {'L': 50.0, 'a': -0.001, 'b': 2.49}
        Lab2 = {'L': 50.0, 'a': 0.001, 'b': -2.49}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.0015)
        self.assertEqual(a2Prime, 0.0015)
        self.assertEqual(c1Prime, 2.49)
        self.assertEqual(c2Prime, 2.49)
        self.assertEqual(h1Prime, 90.0345)
        self.assertEqual(h2Prime, 270.0345)
        self.assertEqual(hBarPrime, 180.0345)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.9779)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1121)
        self.assertEqual(sH, 1.0365)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 4.8045)

    def test_pair_15(self):
        """ Tests Pair 15 """
        # Pair 15
        Lab1 = {'L': 50.0, 'a': -0.001, 'b': 2.49}
        Lab2 = {'L': 50.0, 'a': 0.0011, 'b': -2.49}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.0015)
        self.assertEqual(a2Prime, 0.0016)
        self.assertEqual(c1Prime, 2.49)
        self.assertEqual(c2Prime, 2.49)
        self.assertEqual(h1Prime, 90.0345)
        self.assertEqual(h2Prime, 270.038)
        self.assertEqual(hBarPrime, 0.0362)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 1.3197)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1121)
        self.assertEqual(sH, 1.0493)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 4.7461)

    def test_pair_16(self):
        """ Tests Pair 16 """
        # Pair 16
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': 0.0, 'b': -2.5}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7496)
        self.assertEqual(a2Prime, 0.0)
        self.assertEqual(c1Prime, 3.7496)
        self.assertEqual(c2Prime, 2.5)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 270.0)
        self.assertEqual(hBarPrime, 315.0)
        self.assertEqual(g, 0.4998)
        self.assertEqual(t, 0.8454)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1406)
        self.assertEqual(sH, 1.0396)
        self.assertEqual(rT, -0.0001)
        self.assertEqual(de2000, 4.3065)

    def test_pair_17(self):
        """ Tests Pair 17 """
        # Pair 17
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 73.0, 'a': 25.0, 'b': -18.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.4569)
        self.assertEqual(a2Prime, 34.5687)
        self.assertEqual(c1Prime, 3.4569)
        self.assertEqual(c2Prime, 38.9743)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 332.4939)
        self.assertEqual(hBarPrime, 346.247)
        self.assertEqual(g, 0.3827)
        self.assertEqual(t, 1.4453)
        self.assertEqual(sL, 1.1608)
        self.assertEqual(sC, 1.9547)
        self.assertEqual(sH, 1.4599)
        self.assertEqual(rT, -0.0003)
        self.assertEqual(de2000, 27.1492)

    def test_pair_18(self):
        """ Tests Pair 18 """
        # Pair 18
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 61.0, 'a': -5.0, 'b': 29.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.4954)
        self.assertEqual(a2Prime, -6.9907)
        self.assertEqual(c1Prime, 3.4954)
        self.assertEqual(c2Prime, 29.8307)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 103.5532)
        self.assertEqual(hBarPrime, 51.7766)
        self.assertEqual(g, 0.3981)
        self.assertEqual(t, 0.6447)
        self.assertEqual(sL, 1.064)
        self.assertEqual(sC, 1.7498)
        self.assertEqual(sH, 1.1612)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 22.8977)

    def test_pair_19(self):
        """ Tests Pair 19 """
        # Pair 19
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 56.0, 'a': -27.0, 'b': -3.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.5514)
        self.assertEqual(a2Prime, -38.3556)
        self.assertEqual(c1Prime, 3.5514)
        self.assertEqual(c2Prime, 38.4728)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 184.4723)
        self.assertEqual(hBarPrime, 272.2362)
        self.assertEqual(g, 0.4206)
        self.assertEqual(t, 0.6521)
        self.assertEqual(sL, 1.0251)
        self.assertEqual(sC, 1.9455)
        self.assertEqual(sH, 1.2055)
        self.assertEqual(rT, -0.8219)
        self.assertEqual(de2000, 31.903)

    def test_pair_20(self):
        """ Tests Pair 20 """
        # Pair 20
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 58.0, 'a': 24.0, 'b': 15.0}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.5244)
        self.assertEqual(a2Prime, 33.8342)
        self.assertEqual(c1Prime, 3.5244)
        self.assertEqual(c2Prime, 37.0102)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 23.9095)
        self.assertEqual(hBarPrime, 11.9548)
        self.assertEqual(g, 0.4098)
        self.assertEqual(t, 1.1031)
        self.assertEqual(sL, 1.04)
        self.assertEqual(sC, 1.912)
        self.assertEqual(sH, 1.3353)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 19.4535)

    def test_pair_21(self):
        """ Tests Pair 21 """
        # Pair 21
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': 3.17359627958174, 'b': 0.585353074312861}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7494)
        self.assertEqual(a2Prime, 4.7596)
        self.assertEqual(c1Prime, 3.7494)
        self.assertEqual(c2Prime, 4.7954)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 7.0113)
        self.assertEqual(hBarPrime, 3.5056)
        self.assertEqual(g, 0.4997)
        self.assertEqual(t, 1.2616)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1923)
        self.assertEqual(sH, 1.0808)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.0)

    def test_pair_22(self):
        """ Tests Pair 22 """
        # Pair 22
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': 3.29722210201375, 'b': 7.94802472674044e-09}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7493)
        self.assertEqual(a2Prime, 4.945)
        self.assertEqual(c1Prime, 3.7493)
        self.assertEqual(c2Prime, 4.945)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 0.0)
        self.assertEqual(hBarPrime, 0.0)
        self.assertEqual(g, 0.4997)
        self.assertEqual(t, 1.3202)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1956)
        self.assertEqual(sH, 1.0861)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.0)

    def test_pair_23(self):
        """ Tests Pair 23 """
        # Pair 23
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': 1.86342083563163, 'b': 0.575651399700511}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7497)
        self.assertEqual(a2Prime, 2.7949)
        self.assertEqual(c1Prime, 3.7497)
        self.assertEqual(c2Prime, 2.8536)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 11.638)
        self.assertEqual(hBarPrime, 5.819)
        self.assertEqual(g, 0.4999)
        self.assertEqual(t, 1.2197)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1486)
        self.assertEqual(sH, 1.0604)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.0)

    def test_pair_24(self):
        """ Tests Pair 24 """
        # Pair 24
        Lab1 = {'L': 50.0, 'a': 2.5, 'b': 0.0}
        Lab2 = {'L': 50.0, 'a': 3.25917204763466, 'b': 0.334992094209014}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 3.7493)
        self.assertEqual(a2Prime, 4.8879)
        self.assertEqual(c1Prime, 3.7493)
        self.assertEqual(c2Prime, 4.8994)
        self.assertEqual(h1Prime, 0.0)
        self.assertEqual(h2Prime, 3.9206)
        self.assertEqual(hBarPrime, 1.9603)
        self.assertEqual(g, 0.4997)
        self.assertEqual(t, 1.2883)
        self.assertEqual(sL, 1.0)
        self.assertEqual(sC, 1.1946)
        self.assertEqual(sH, 1.0836)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.0)

    def test_pair_25(self):
        """ Tests Pair 25 """
        # Pair 25
        Lab1 = {'L': 60.2574, 'a': -34.0099, 'b': 36.2677}
        Lab2 = {'L': 60.4626, 'a': -34.1751, 'b': 39.4387}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -34.0678)
        self.assertEqual(a2Prime, -34.2333)
        self.assertEqual(c1Prime, 49.759)
        self.assertEqual(c2Prime, 52.2238)
        self.assertEqual(h1Prime, 133.2085)
        self.assertEqual(h2Prime, 130.9584)
        self.assertEqual(hBarPrime, 132.0835)
        self.assertEqual(g, 0.0017)
        self.assertEqual(t, 1.301)
        self.assertEqual(sL, 1.1427)
        self.assertEqual(sC, 3.2946)
        self.assertEqual(sH, 1.9951)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.2644)

    def test_pair_26(self):
        """ Tests Pair 26 """
        # Pair 26
        Lab1 = {'L': 63.0109, 'a': -31.0961, 'b': -5.8663}
        Lab2 = {'L': 62.8187, 'a': -29.7946, 'b': -4.0864}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -32.6194)
        self.assertEqual(a2Prime, -31.2542)
        self.assertEqual(c1Prime, 33.1427)
        self.assertEqual(c2Prime, 31.5202)
        self.assertEqual(h1Prime, 190.1951)
        self.assertEqual(h2Prime, 187.449)
        self.assertEqual(hBarPrime, 188.8221)
        self.assertEqual(g, 0.049)
        self.assertEqual(t, 0.9402)
        self.assertEqual(sL, 1.1831)
        self.assertEqual(sC, 2.4549)
        self.assertEqual(sH, 1.456)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.263)

    def test_pair_27(self):
        """ Tests Pair 27 """
        # Pair 27
        Lab1 = {'L': 61.2901, 'a': 3.7196, 'b': -5.3901}
        Lab2 = {'L': 61.4292, 'a': 2.248, 'b': -4.962}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 5.5668)
        self.assertEqual(a2Prime, 3.3644)
        self.assertEqual(c1Prime, 7.7487)
        self.assertEqual(c2Prime, 5.995)
        self.assertEqual(h1Prime, 315.924)
        self.assertEqual(h2Prime, 304.1385)
        self.assertEqual(hBarPrime, 310.0313)
        self.assertEqual(g, 0.4966)
        self.assertEqual(t, 0.6952)
        self.assertEqual(sL, 1.1586)
        self.assertEqual(sC, 1.3092)
        self.assertEqual(sH, 1.0717)
        self.assertEqual(rT, -0.0032)
        self.assertEqual(de2000, 1.8731)

    def test_pair_28(self):
        """ Tests Pair 28 """
        # Pair 28
        Lab1 = {'L': 35.0831, 'a': -44.1164, 'b': 3.7933}
        Lab2 = {'L': 35.0232, 'a': -40.0716, 'b': 1.5901}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -44.3939)
        self.assertEqual(a2Prime, -40.3237)
        self.assertEqual(c1Prime, 44.5557)
        self.assertEqual(c2Prime, 40.355)
        self.assertEqual(h1Prime, 175.1161)
        self.assertEqual(h2Prime, 177.7418)
        self.assertEqual(hBarPrime, 176.429)
        self.assertEqual(g, 0.0063)
        self.assertEqual(t, 1.0168)
        self.assertEqual(sL, 1.2148)
        self.assertEqual(sC, 2.9105)
        self.assertEqual(sH, 1.6476)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.8645)

    def test_pair_29(self):
        """ Tests Pair 29 """
        # Pair 29
        Lab1 = {'L': 22.7233, 'a': 20.0904, 'b': -46.694}
        Lab2 = {'L': 23.0331, 'a': 14.973, 'b': -42.5619}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 20.1424)
        self.assertEqual(a2Prime, 15.0118)
        self.assertEqual(c1Prime, 50.8532)
        self.assertEqual(c2Prime, 45.1317)
        self.assertEqual(h1Prime, 293.3339)
        self.assertEqual(h2Prime, 289.4279)
        self.assertEqual(hBarPrime, 291.3809)
        self.assertEqual(g, 0.0026)
        self.assertEqual(t, 0.3636)
        self.assertEqual(sL, 1.4014)
        self.assertEqual(sC, 3.1597)
        self.assertEqual(sH, 1.2617)
        self.assertEqual(rT, -1.2537)
        self.assertEqual(de2000, 2.0373)

    def test_pair_30(self):
        """ Tests Pair 30 """
        # Pair 30
        Lab1 = {'L': 36.4612, 'a': 47.858, 'b': 18.3852}
        Lab2 = {'L': 36.2715, 'a': 50.5065, 'b': 21.2231}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 47.9197)
        self.assertEqual(a2Prime, 50.5716)
        self.assertEqual(c1Prime, 51.3256)
        self.assertEqual(c2Prime, 54.8444)
        self.assertEqual(h1Prime, 20.9901)
        self.assertEqual(h2Prime, 22.766)
        self.assertEqual(hBarPrime, 21.8781)
        self.assertEqual(g, 0.0013)
        self.assertEqual(t, 0.9239)
        self.assertEqual(sL, 1.1943)
        self.assertEqual(sC, 3.3888)
        self.assertEqual(sH, 1.7357)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.4146)

    def test_pair_31(self):
        """ Tests Pair 31 """
        # Pair 31
        Lab1 = {'L': 90.8027, 'a': -2.0831, 'b': 1.441}
        Lab2 = {'L': 91.1528, 'a': -1.6435, 'b': 0.0447}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -3.1245)
        self.assertEqual(a2Prime, -2.4651)
        self.assertEqual(c1Prime, 3.4408)
        self.assertEqual(c2Prime, 2.4655)
        self.assertEqual(h1Prime, 155.241)
        self.assertEqual(h2Prime, 178.9612)
        self.assertEqual(hBarPrime, 167.1011)
        self.assertEqual(g, 0.4999)
        self.assertEqual(t, 1.1546)
        self.assertEqual(sL, 1.611)
        self.assertEqual(sC, 1.1329)
        self.assertEqual(sH, 1.0511)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.4441)

    def test_pair_32(self):
        """ Tests Pair 32 """
        # Pair 32
        Lab1 = {'L': 90.9257, 'a': -0.5406, 'b': -0.9208}
        Lab2 = {'L': 88.6381, 'a': -0.8985, 'b': -0.7239}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.8109)
        self.assertEqual(a2Prime, -1.3477)
        self.assertEqual(c1Prime, 1.227)
        self.assertEqual(c2Prime, 1.5298)
        self.assertEqual(h1Prime, 228.6315)
        self.assertEqual(h2Prime, 208.2412)
        self.assertEqual(hBarPrime, 218.4363)
        self.assertEqual(g, 0.5)
        self.assertEqual(t, 1.3916)
        self.assertEqual(sL, 1.593)
        self.assertEqual(sC, 1.062)
        self.assertEqual(sH, 1.0288)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 1.5381)

    def test_pair_33(self):
        """ Tests Pair 33 """
        # Pair 33
        Lab1 = {'L': 6.7747, 'a': -0.2908, 'b': -2.4247}
        Lab2 = {'L': 5.8714, 'a': -0.0985, 'b': -2.2286}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, -0.4362)
        self.assertEqual(a2Prime, -0.1477)
        self.assertEqual(c1Prime, 2.4636)
        self.assertEqual(c2Prime, 2.2335)
        self.assertEqual(h1Prime, 259.8025)
        self.assertEqual(h2Prime, 266.2073)
        self.assertEqual(hBarPrime, 263.0049)
        self.assertEqual(g, 0.4999)
        self.assertEqual(t, 0.9556)
        self.assertEqual(sL, 1.6517)
        self.assertEqual(sC, 1.1057)
        self.assertEqual(sH, 1.0337)
        self.assertEqual(rT, -0.0004)
        self.assertEqual(de2000, 0.6377)

    def test_pair_34(self):
        """ Tests Pair 34 """
        # Pair 34
        Lab1 = {'L': 2.0776, 'a': 0.0795, 'b': -1.135}
        Lab2 = {'L': 0.9033, 'a': -0.0636, 'b': -0.5514}

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000 = deltae.delta_e_2000(
            Lab1, Lab2, test=True, formula='Rochester')

        self.assertEqual(a1Prime, 0.1192)
        self.assertEqual(a2Prime, -0.0954)
        self.assertEqual(c1Prime, 1.1412)
        self.assertEqual(c2Prime, 0.5596)
        self.assertEqual(h1Prime, 275.9978)
        self.assertEqual(h2Prime, 260.1842)
        self.assertEqual(hBarPrime, 268.091)
        self.assertEqual(g, 0.5)
        self.assertEqual(t, 0.7826)
        self.assertEqual(sL, 1.7246)
        self.assertEqual(sC, 1.0383)
        self.assertEqual(sH, 1.01)
        self.assertEqual(rT, 0.0)
        self.assertEqual(de2000, 0.9082)


if __name__ == '__main__':
    unittest.main()

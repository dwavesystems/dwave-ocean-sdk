# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# ================================================================================================
import unittest

from dwave.system import DWaveSampler

try:
    DWaveSampler()
    _sampler = True
except Exception:
    _sampler = False


class TestSmokeIndividually(unittest.TestCase):
    """Use each package individually. Mostly we use the simple scripts from the READMEs."""
    def test_dwavebinarycsp(self):
        import dimod
        import dwavebinarycsp

        csp = dwavebinarycsp.factories.random_2in4sat(8, 4)  # 8 variables, 4 clauses

        bqm = dwavebinarycsp.stitch(csp)

        resp = dimod.ExactSolver().sample(bqm)

        for sample, energy in resp.data(['sample', 'energy']):
            csp.check(sample)

    def test_dnx(self):
        import dimod
        import dwave_networkx as dnx

        G = dnx.chimera_graph(1)

        cut = dnx.maximum_cut(G, dimod.ExactSolver())

    @unittest.skipUnless(_sampler, "No credentials found")
    def test_dwave_system(self):
        from dwave.system import DWaveSampler, EmbeddingComposite

        sampler = EmbeddingComposite(DWaveSampler())

        h = {'a': -1, 'b': +1}
        J = {('a', 'b'): -1}

        resp = sampler.sample_ising(h, J)

    def test_qbsolv(self):
        import dwave_qbsolv as qbsolv

        h = {'a': -1, 'b': +1}
        J = {('a', 'b'): -1}

        resp = qbsolv.QBSolv().sample_ising(h, J)

    def test_neal(self):
        import neal

        h = {'a': -1, 'b': +1}
        J = {('a', 'b'): -1}

        resp = neal.SimulatedAnnealingSampler().sample_ising(h, J)

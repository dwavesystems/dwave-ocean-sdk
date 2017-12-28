import unittest

import dwave_micro_client
import dwave_micro_client_dimod as micro
import dwave_networkx as dnx


try:
    dwave_micro_client.Connection()
    _sapi_connection = True
except (OSError, IOError):
    # no sapi credentials are stored on the path
    _sapi_connection = False


@unittest.skipUnless(_sapi_connection, "no connection to sapi web services")
class TestNetworkxDWaveSampler(unittest.TestCase):
    def test_max_cut(self):
        G = dnx.chimera_graph(2, 2, 4)

        sampler = micro.EmbeddingComposite(micro.DWaveSampler())

        cut = dnx.maximum_cut(G, sampler)

        for u, v in G.edges:
            self.assertTrue(u in cut or v in cut)
            self.assertFalse(u in cut and v in cut)

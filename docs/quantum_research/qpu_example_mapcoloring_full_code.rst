.. _qpu_example_mapcoloring_full_code:

=======================
Map Coloring: Full Code
=======================

See :ref:`map_coloring` for a description of the following code.

.. code-block:: python

    import networkx as nx
    import matplotlib.pyplot as plt
    from dimod.generators import combinations
    from dimod import BinaryQuadraticModel, ExactSolver
    from dwave.system import DWaveSampler, EmbeddingComposite

    # Represent the map as the nodes and edges of a graph
    provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    neighbors = [('AB', 'BC'), ('AB', 'NT'), ('AB', 'SK'), ('BC', 'NT'), ('BC', 'YT'), ('MB', 'NU'),
                 ('MB', 'ON'), ('MB', 'SK'), ('NB', 'NS'), ('NB', 'QC'), ('NL', 'QC'), ('NT', 'NU'),
                 ('NT', 'SK'), ('NT', 'YT'), ('ON', 'QC')]

    colors = ['y', 'g', 'r', 'b']

    # Add constraint that each node (province) select a single color
    bqm_one_color = BinaryQuadraticModel('BINARY')
    for province in provinces:
      variables = [province + "_" + c for c in colors]
      bqm_one_color.update(combinations(variables, 1))

    # Add constraint that each pair of nodes with a shared edge not both select one color
    bqm_neighbors  = BinaryQuadraticModel('BINARY')
    for neighbor in neighbors:
      v, u = neighbor
      interactions = [(v + "_" + c, u + "_" + c) for c in colors]
      for interaction in interactions:
        bqm_neighbors.add_quadratic(interaction[0], interaction[1], 1)

    bqm = bqm_one_color + bqm_neighbors

    # Set up a solver and sample 1000 times
    sampler = EmbeddingComposite(DWaveSampler())
    sampleset = sampler.sample(bqm, num_reads=1000, label='SDK Examples - Map Coloring BQM')

    best = sampleset.first

    def plot_map(sample):
      G = nx.Graph()
      G.add_nodes_from(provinces)
      G.add_edges_from(neighbors)
      # Create a {province: selected color} dict
      color_map = {}
      for province in provinces:
        for c in colors:
         if sample[province + '_' + c]:
             color_map[province] = c
      # Plot with the selected colors
      node_colors = [color_map.get(node) for node in G.nodes()]
      nx.draw_circular(G, with_labels=True, node_color=node_colors, node_size=3000, cmap=plt.cm.rainbow)
      plt.show()

    # Plot the lowest-energy sample if it meets the constraints
    sample = sampleset.first.sample
    if best.energy > 0:
        print("Failed to color map")
    else:
        plot_map(best.sample)

"""
All dimod samplers that can be applied without ordering
"""

# Import all universal samplers into the namespace. This lets tests do things
# like
# >>> for composite in dwave_sdk.universal_composites:
# ...     pass  # use the sampler in a test

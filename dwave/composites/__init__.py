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
"""
A unified namespace for :class:`dimod.Composite`s.

This namespace is populated by entry points. To contribute a composite, you
must identify it in your setup.py file like so.

.. code-block:: python

    entry_points = {'dwave.composites': ['YourComposite = import.path.to.composite:YourComposite']}

    setup(
        entry_points=entry_points,
        ...
    )

"""
from pkg_resources import iter_entry_points

# add the composites to the module from entrypoints, name conflicts override
globals().update((ep.name, ep.load()) for ep in iter_entry_points('dwave.composites'))
del iter_entry_points  # remove from namespace

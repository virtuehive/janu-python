..
.. Copyright (c) 2017, 2020 ADLINK Technology Inc.
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ADLINK janu team, <janu@adlink-labs.tech>
..

Janu-net API Reference
=======================

.. automodule:: janu
    :members: open, scout

Hello
-----
.. autoclass:: janu.Hello
    :members:

Session
-------
.. autoclass:: janu.Session
    :members:

Subscriber
----------
.. autoclass:: janu.Subscriber
    :members:

KeyExpr
------
.. autoclass:: janu.KeyExpr
    :members:

PeerId
------
.. autoclass:: janu.PeerId
    :members:

Timestamp
---------
.. autoclass:: janu.Timestamp
    :members:

SourceInfo
--------
.. autoclass:: janu.SourceInfo
    :members:

Sample
------
.. autoclass:: janu.Sample
    :members:

Reliability
-----------
.. autoclass:: janu.Reliability
    :members:

    .. autoattribute:: BestEffort
            :annotation:
    .. autoattribute:: Reliable
            :annotation:

SubMode
-------
.. autoclass:: janu.SubMode
    :members:

    .. autoattribute:: Push
            :annotation:
    .. autoattribute:: Pull
            :annotation:

Period
------
.. autoclass:: janu.Period
    :members:

SubInfo
-------
.. autoclass:: janu.SubInfo
    :members:

Publisher
---------
.. autoclass:: janu.Publisher
    :members:

CongestionControl
-----------------
.. autoclass:: janu.CongestionControl
    :members:

    .. autoattribute:: Drop
            :annotation:
    .. autoattribute:: Block
            :annotation:

Query
-----
.. autoclass:: janu.Query
    :members:

Queryable
---------
.. autoclass:: janu.Queryable
    :members:

Target
------
.. autoclass:: janu.Target
    :members:

    .. autoattribute:: BestMatching
            :annotation:
    .. autoattribute:: Complete
            :annotation:
    .. autoattribute:: All
            :annotation:
    .. autoattribute:: No
            :annotation:

QueryTarget
-----------
.. autoclass:: janu.QueryTarget
    :members:

ConsolidationMode
-----------------
.. autoclass:: janu.ConsolidationMode
    :members:

    .. autoattribute:: No
            :annotation:
    .. autoattribute:: Lazy
            :annotation:
    .. autoattribute:: Full
            :annotation:

QueryConsolidation
------------------
.. autoclass:: janu.QueryConsolidation
    :members:

Reply
-----
.. autoclass:: janu.Reply
    :members:

module janu.config
-----------------------
.. automodule:: janu.config
    :members:
    :undoc-members:

module janu.info
---------------------
.. automodule:: janu.info
    :members:
    :undoc-members:

module janu.whatami
------------------------
.. automodule:: janu.whatami
    :members:
    :undoc-members:

module janu.queryable
--------------------------
.. automodule:: janu.queryable
    :members:
    :undoc-members:

module janu.resource_name
------------------------------
.. automodule:: janu.resource_name
    :members:

module janu.encoding
-------------------------
.. automodule:: janu.encoding
    :members:
    :undoc-members:

module janu.sample_kind
--------------------------
.. automodule:: janu.sample_kind
    :members:
    :undoc-members:


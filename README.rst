Flix CLI
========

Introduction
------------

Get movie and theater information (powered (unofficially) by Flixster)
without having to leave the command line!

Installation
------------

``pip install flix``

Usage
-----

-  ``-n`` or ``--name`` to filter by a specific movie name
-  ``-t`` or ``--tomorrow`` to filter by movies playing tomorrow
-  ``-m`` or ``--month`` to select a month
-  ``-d`` or ``--day`` to select a day
-  There are weekday (e.g. ``mon``, ``tue``, etc.) choices, which will
   return results for the next given weekday
-  For any valid month & day combination, results will be returned for
   the *next* month & day combination.

   -  For example, if today is March 3rd, 2017 and you select March 2nd
      - results will be returned for March 2nd, 2018 (so probably not
      **that** many results).

-  There are also day of month values (e.g. ``1``, ``2``, ``3``, etc.)
-  ``-l`` or ``--limit`` to select the number of theaters to return
   movie options for.
-  Defaults to ``2``
-  Selection must be a positive integer, less than or equal to ``5``.

Time Hierarchy
~~~~~~~~~~~~~~

1. The ``--tomorrow`` flag is set
2. A weekday (``mon``, ``tue``, etc.) is chosen
3. Month & day combination
4. If no time element is defined, the default behavior is to use today
   as the date.

Examples
~~~~~~~~

Movies playing today
^^^^^^^^^^^^^^^^^^^^

``flix``

Movies that contain a particular substring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -n "foo bar"``

Movies that are playing tomorrow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -t``

Movies that are playing next Friday
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -d fri``

Movies that will be playing on the next 4th of July
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -m jul -d 4`` ``flix -m 6 -d 4``

Movies that will be playing on the 7th day of the current month
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -d 7``

Movies across three theaters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``flix -l 3``


=====================================
Python in QGIS
=====================================

When we use the term\  **PyQGIS** \we are refering to the QGIS Python bindings. Specifically, we are referring to a Python application programming interface (API) that wraps the QGIS C++ library. Here is the\   `C++ QGIS API documentation <http://doc.qgis.org/api>`_ \.

.. image:: ../_static/pyqgis_tools.png
    :scale: 80%
    :align: center

We'll be using the C++ QGIS API documentation as a roadmap to understanding PyQGIS because the PyQGIS API documentation is nonexistent. This can be a little confusing at times. But for the most part the Python bindings are a mirror of the C++ library.

We will become very familiar with parts of the above documentation as we build plugins. For now it's good to note that there's a number of ways to interact with QGIS using Python. Here are the most common ways:

    1. \  **Plugins** \: creating/extending editing tools that interact with data inside the QGIS environment 

    2. \  **Python Console** \: a command-line terminal inside QGIS to test ideas and do one-off quick jobs

    3. \  **Python Scripts/Applications** \: writing Python applications from scratch that are built off QGIS and Qt libraries. These applications would process spatial data outside the QGIS application but use core functionality under the hood. One example would be building a stripped down QGIS viewer with a very limited toolset for a specific workflow

We'll be focusing on using the installing plugins as well as using the Python console during this next hour. Everything we're learning will be directly applicable to our plugin development through the rest of the workshop.

------------------------------------------------------

QGIS Plugins
------------------------------

From within QGIS one can install contributed plugins from many sources, both public and provate.

The tutorial #1 that follows walks through the basics of adding plugin repositories and plugins themselves to QGIS.

------------------------------------------------------

Python Console
------------------

This is perhaps the easiest way to test out your plugin ideas.

From the Python Console we can access vector and raster layers that are already loaded into QGIS. Once accessed, we can start interacting with their attributes and geometry. Since a lot of plugin work is dealing with layer attributes and geometry then let's begin here.

The tutorial #2 that follows walks through the following building-block examples.



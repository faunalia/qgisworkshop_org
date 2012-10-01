=============================
Exercises
=============================

1) GOAL: On-the-Fly Raster Value Emitter
--------------------------------------------------------

In this exercise you build a plugin from start to finish using Plugin Builder . The goal will be to create a simple (maybe even crude) raster value display tool. The purpose is for you to figure out the programmatic steps based on a few clues. This exercise has a\  **starter** \and a\  **advanced** \component

Starter Exercise
----------------------

If you don't feel comfortable using Plugin Builder to create a tool from start to finish, then you modify a plugin that is already built and try to make it look like the solution.

1. Open Qgis and load the shaded relief raster layer\  ``/home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif``
2. Click on the plugin tool called\  ``foss4g2011_example2_solution``\or\  ``E#2SOL`` 
3. Hover the mouse cursor over the map and watch as the RGB values change dynamically. This is the end result that you will want to shoot for
4. Navigate to\  ``/home/qgis/.qgis/python/plugins/foss4g2011_example2_starter/``
5. Open the files\  ``foss4g2011_example2_starter.py`` \and\  ``foss4g2011_example2_starterdialog.py`` \and find the ares with commented code. You will want to uncomment code from these two files to make the tool work like the solution tool

Advanced Exercise
-----------------------

The Tool Requirements
*************************

* Display every band value for a raster on mouse hover. That sounds confusing, but the idea is that your tool should work with a single grayscale raster or an RGBA raster without blowing up. There will be no mouse clicks, we'll just be responding to the normal mouse cursor movement over the map canvas

* Feedback of raster values will be output to a GUI (your choice on how to implement this on the GUI)

Hints
***************

* You will want to connect a custom function to the map canvas signal\  `xyCoordinates <http://doc.qgis.org/api/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \

* You can get raster values for each band like this::

    rLayer = self.iface.mapCanvas().currentLayer()
    success, data = rLayer.identify(QgsPoint(-122, 47))
    for band, value in data.items():
        print str(band) + " = " + str(value)

Solution
************

If you want to peek at one possible solution (though a very ugly one) then check out these modules:

    * The main Python module\  `here <../_static/rastervaluedisplay.py>`_

    * The dialog module\  `there <../_static/rastervaluedisplaydialog.py>`_

    * The compiled ui module\  `over here <../_static/ui_rastervaluedisplay.py>`_

To get a visual idea about how simple my tool was, here's a picture:

.. image:: ../_static/raster_value_final.png
    :scale: 100%
    :align: center


2) GOAL: Chainage distance nodes plugin
--------------------------------------------------------

In this exercise you build a plugin that uses the\  `QgsGeometry <http://qgis.org/api/classQgsGeometry.html>`_ \functions. The goal will be to create a simple plugin that generates points along a line at supplied distance, then store them in a temporary layer.
The plugin has to work on the selected lines of the active vector layer.

.. note:: You need QGis > 1.8 as it defines the\  ``QgsGeometry.interpolate()`` \function, otherwise you need to create a function that returns a point along a line at a given distance.

Hints
*************************

* To create a temporary layer you can use the so called\  **memory provider** \.

The following example shows as to create and populate a\  `memory layer` \:
::
    # create a temporary point layer and load it into QGis
    layer = QgsVectorLayer("Point", "layer_name", "memory")
    QgsMapLayerRegistry.instance().addMapLayer(layer)

    # start editing the layer
    layer.startEditing()

    # add an attribute
    layer.addAttribute( QgsField("foo", QVariant.Int) )

    # create a feature and populate it with a point geometry and a value for the foo attribute
    f = QgsFeature()
    f.setGeometry(QgsGeometry.fromPoint(QgsPoint(0,0)))
    f.setAttributeMap( { 0 : 2 } )
    # add the feature to the layer
    layer.addFeature( f )

    # finish editing
    layer.commitChanges()


* In the QGis > 1.8 there's a new method on\  ``QgsGeometry`` \class called\  `interpolate <http://qgis.org/api/classQgsGeometry.html#a8c3bb1b01d941219f2321e6c6c3db7e1>`_ \. This method takes as argument a\  `distance` \and returns a point along the line (the geometry you're calling the function on) at that distance.

Solution
************

One possible solution can be found\  `here <../_static/chainage_dist_nodes_example4_solution.py>`_ \.


=====================================
Draw items on top of the canvas
=====================================

In this chapter we'll learn how to draw items on top of the canvas using the so called\  **map canvas items** \. 

There are two useful canvas item classes already available for convenience (though it's possible to create custom canvas item classes):
    - \  `QgsRubberBand <http://qgis.org/api/classQgsRubberBand.html>`_ \ for drawing polylines or polygons, 
    - \  `QgsVertexMarker <http://qgis.org/api/classQgsVertexMarker.html>`_ \ for drawing points.


They both work with map coordinates, so the shape is moved/scaled automatically when the canvas is being panned or zoomed. 

-------------------------------------------

QgsRubberBand and QgsVertedMarker
------------------------------------

Here's a simple example of how to use the\  ``QgsRubberBand`` \ class::

    r = QgsRubberBand(canvas, False)  # False = not a polygon, True = draw a polygon
    points = [ QgsPoint(-1,-1), QgsPoint(0,1), QgsPoint(1,-1) ]
    r.setToGeometry(QgsGeometry.fromPolyline(points), None)

\  **1.** \The first step is to create the\  ``QgsRubberBand`` \ object. 

The\  **QgsRubberBand constructor** \takes as first argument the\  **canvas** \, the second argument is a flag to choose the rubber band drawing mode, \  ``True`` \to draw a polygon (a closed and filled shape) or\  ``False`` \ for a polyline (a line with one or more segments).

In the above code a line will be drawn.

\  **2.** \The\  `setGeometry <http://www.qgis.org/api/classQgsRubberBand.html#a223d1a1e225911b33a5876add9d1c5aa>`_ \ method allows to set up the shape of the rubberband from an existent geometry. The first argument is the geometry (in the example the geometry is constructed from a list of points), the second argument is the\  ``QgsVectorLayer`` \containing the feature and its used for coordinate transformation from layer to map CRS.

In addition to the\  `setGeometry()` \method, we can build a geometry step by step using the\  ``addPoint()`` \method. We can also move a point using one of the 2 overloaded\  ``movePoint()`` \methods (one of them move the last point, the other one a point identified by its index) or remove the last point calling\  ``removeLastPoint()`` \.

To get the geometry from a rubber band we can use the\  `asGeometry() <http://www.qgis.org/api/classQgsRubberBand.html#aecb438a7c6e7c284d6a601d88985b66a>`_ \method. 

To clear a rubber band removing all the points we use the\  `reset() <http://www.qgis.org/api/classQgsRubberBand.html#ab3ae2a399091cc0af4f2617d89d1ec29>`_ \ method which takes as argument the drawing mode to use (see\  **QgsRubberBand constructor** \above).

.. note:: Calling\ ``addPoint()`` \method on an empty rubberband will insert the minimum amount of points needed for that kind of geometry, thus\  **the first call to addPoint() adds 2 points for lines and 3 points for polygons** \.

Rubber bands allow some customization, namely to change their color and line width::

    r.setColor(QColor(0,0,255))
    r.setWidth(3)

Rubber bands can be also used for drawing points, however\  ``QgsVertexMarker`` \class is better suited for this (as the\  `QgsRubberBand` \would only draw a rectangle around the desired point). 
How to use the vertex marker::

    m = QgsVertexMarker(canvas)
    m.setCenter(QgsPoint(0,0))

This will draw a red cross on position\  *(0,0)* \.
It is possible to customize the icon type, size, color and pen width::

    m.setColor(QColor(0,255,0))
    m.setIconSize(5)
    m.setIconType(QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
    m.setPenWidth(3)

Canvas items can be temporarily hidden and shown again using their\  ``hide()`` \ and\  ``show()`` \functions. Each canvas item is owned by the canvas, so to completely remove it you have call::

    canvas.scene().removeItem( item )

-------------------------------------------

Custom map canvas items
------------------------------

We could also create our custom map canvas items by subclassing the\  `QgsMapCanvasItem <http://www.qgis.org/api/classQgsMapCanvasItem.html>`_ \ class, so we can display whatever we need above all the loaded layers.

\ `Click here <../_static/mapcanvasitem_1.py>`_ \ to see an example of how to implement a custom marker which displays an image.


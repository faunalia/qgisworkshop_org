=============================================================
Tutorial -- Create a map tool to draw a line
=============================================================

We've already seen how to use the class\  `QgsMapToolEmitPoint <http://qgis.org/api/classQgsMapToolEmitPoint.html>`_ \to get the user does click on the canvas. Now we are going to use it together with\  `QgsRubberBand <http://qgis.org/api/classQgsRubberBand.html>`_ \to draw a line from user clicks.

The tool we're going to build will be do a few things:

    1. The tool will draw a line
    2. The tool will create a new vertices for every left click
    3. The tool will end to draw when the user performs a right click.

.. note:: The following code can be easily changed to make the tool able to draw a polygon instead of a line.

-------------------------------------------

Implement a custom map tool
------------------------------------

\  **1.** \Create a file\  ``maptools.py`` \, then copy and paste the following code.::

    from PyQt4 import QtCore, QtGui
    from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand
    # create the map tool to draw a line
    class LineDrawer(QgsMapToolEmitPoint):

        def __init__(self, canvas):
            # call the parent constructor
            QgsMapToolEmitPoint.__init__(self, canvas)
            # store the passed canvas
            self.canvas = canvas

            # flag to know whether the tool is performing a drawing operation 
            self.isDrawing = False

            # create and setup the rubber band to display the line
            self.rubberBand = QgsRubberBand( self.canvas, False )    # False = not a polygon = a line
            self.rubberBand.setColor( QtCore.Qt.red )
            self.rubberBand.setWidth( 1 )

The code above defines new class\  ``LineDrawer`` \by subclassing the\  ``QgsMapToolEmitPoint`` \class, this allows to easily re-implement the methods that handle mouse events on the canvas, namely:
    * \  `canvasMoveEvent() <http://www.qgis.org/api/classQgsMapToolEmitPoint.html#a67978acc75d5815075cbc1f27fbfc91d>`_ \ to get the mouse movement,
    * \  `canvasPressEvent() <http://www.qgis.org/api/classQgsMapToolEmitPoint.html#af2f2c7a0fc434c5087ec74fbf1aa0ae7>`_ \ to catch the mouse press event,
    * \  `canvasReleaseEvent() <http://www.qgis.org/api/classQgsMapToolEmitPoint.html#ab0f51aa7eff1bab6326400318600af05>`_ \ to get the mouse release event.

The\  ``isDrawing`` \flag is added to know if the tool is drawing the line, this will be set when the users start drawing the line and reset when he ends, i.e. after the right mouse button is pressed.

Then the code creates the\  ``QgsRubberBand`` \object that will be used to display the line while the user draw it.

\  **2.** \Next step is to handle user clicks on the canvas.

To accomplish this task we will re-implement the\  ``canvasPressEvent()`` \method::

        def canvasPressEvent(self, e):
            # which the mouse button?
            if e.button() == Qt.LeftButton:
                # left click

                # if it's the first left click, clear the rubberband 
                if not self.isDrawing:
                    self.rubberBand.reset( False )    # False = not a polygon = a line

                # we are drawing now
                self.isDrawing = True

                # convert the clicked position to map coordinates
                point = self.toMapCoordinates( e.pos() )
                # add a new point to the rubber band
                self.rubberBand.addPoint( point, True )    # True = display updates on the canvas
                # and finally show the rubber band
                self.rubberBand.show()

            elif e.button() == Qt.RightButton:
                # right click, stop drawing
                self.isDrawing = False

The\  ``canvasPressEvent`` \method gets a\  ``QMouseEvent`` \object which contains some information on the event, namely the mouse position (through the\  ``pos()`` \method) and the pressed button (using the\  ``button()`` \method).

Since the tool must react in a different way according to the pressed button, we check the\  ``e.button()`` \result.
    * If the pressed button is the left one:
        1) if it's the first click of this drawing operation (i.e.\  ``self.isDrawing == False`` \), clear the rubberband so the old line is removed
        2) Set the\  ``isDrawing`` \flag to\  ``True`` \to know we are drawing
        3) Add the point to the rubber band. To get the point, we need to convert the mouse position to the map coordinates using the\  `toMapCoordinate() <http://www.qgis.org/api/classQgsMapTool.html#a3340999b5da5020491201f590e4d7ce4>`_ \method. This method can be called everywhere within a map tool class since it's a QgsMapTool method, i.e. the base class of every QGis map tool. 
        4) Finally we can make the rubber band visible by calling\  ``show()`` \.

    * If the user pressed the right button, we just set the\  ``isDrawing`` \flag to\  ``False`` \to know the last drawing operation ended.

.. note:: A line containing\  `N` \segments has\  `N+1` \points. Though the\  ``addPoint()`` \method is called\  `N` \times only (the user does\  `N+1` \clicks but the last one is a right click) the rubberband has\  `N+1` \points because\  **the first addPoint() call adds 2 points** \.

\  **3.** \Update the line while the mouse is moving

Up on now the displayed rubberband is updated at every new point i.e. when the user clicks on the canvas. 
To make the tool working in a more interactively way, the end point of the last segment (the one the user is drawing) should follow the mouse until the user do click.

To do it we need to re-implement the\  ``canvasPressEvent()`` \method::

        def canvasMoveEvent(self, e):
            # check if it's already drawing
            if not self.isDrawing:
                return

            # convert the mouse position to map coordinates
            point = self.toMapCoordinates( e.pos() )
            # move the last point to the new coordinates
            self.rubberBand.movePoint( point )

Like the\  ``canvasPressEvent()`` \, the\  ``canvasMoveEvent()`` \method gets a \  ``QMouseEvent`` \object as argument.

First thing to do is to check if the tool is drawing and exit if it isn't.

Next step is to move the last point. The tool converts the mouse position to map coordinates using the\  ``toMapCoordinates`` \(more info above), then pass the result to\  ``movePoint()`` \.

\  **4.** \The last step: a way to get the line

We need a way to get the result, i.e. the line the user has drawn.
Let's add a new\  ``geometry()`` \method to our map tool that returns a\  ``QgsGeometry`` \.
::
        def geometry(self):
            return self.rubberBand.asGeometry()

The complete code of the\  ``LineDrawer`` \class can be found\  `here <../_static/maptool_linedrawer.py>`_ \.


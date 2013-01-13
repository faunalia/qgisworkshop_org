from PyQt4.QtCore import *
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
        self.rubberBand.setColor( Qt.red )
        self.rubberBand.setWidth( 1 )


    def clear(self):
        self.rubberBand.reset( False )    # False = not a polygon = a line

    def delete(self):
        self.canvas.scene().removeItem( self.rubberBand )

    def canvasPressEvent(self, e):
        # which the mouse button?
        if e.button() == Qt.LeftButton:
            # left click

            # if it's the first left click, clear the rubberband 
            if not self.isDrawing:
                self.clear()

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
            # emit a signal
            self.emit( SIGNAL("editingFinished()") )

    def canvasMoveEvent(self, e):
        # check if it's already drawing
        if not self.isDrawing:
            return

        # convert the mouse position to map coordinates
        point = self.toMapCoordinates( e.pos() )
        # move the last point to the new coordinates
        self.rubberBand.movePoint( point )

    def geometry(self):
        return self.rubberBand.asGeometry()


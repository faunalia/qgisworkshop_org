# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class ImageMarker(QgsMapCanvasItem):

    def __init__(self, canvas):
        QgsMapCanvasItem.__init__(self, canvas)

        self.canvas = canvas

        # hold the marker position
        self.center = QgsPoint()
        # default size in pixels
        self.size = 10

        # hold the image selected by the user
        self.img = None
        # hold a temporary scaled copy of the image
        self.tmp_img = None

    def setSize(self, size):
        # set the new image size
        self.size = size
        # remove the temporary scaled image, so it can be re-created
        self.tmp_img = None

    def setImagePath(self, path):
        # load the image by path
        pixmap = QPixmap( path )
        if pixmap.isNull():
            # image not found?
            self.img = None
        else:
            self.img = pixmap

        # remove the temporary scaled image, so it can be re-created
        self.tmp_img = None

    def setCenter(self, point):
        # set the new marker position
        self.center = point
        pt = self.toCanvasCoordinates( self.center )
        self.setPos( pt )

    def createTempScaledImage(self):
        if not self.img:
            # no image to draw
            return

        if self.tmp_img:
            # temporary image already created
            return

        # create a temporary scaled image
        self.tmp_img = self.img.scaled( self.size, self.size, Qt.KeepAspectRatio ).toImage()

    def paint(self, *args):
        if not self.img:
            # no image to draw
            return

        # create a temporary scaled image if not already done to avoid 
        # to recreate it at every re-paint
        if not self.tmp_img:
            self.createTempScaledImage()

        # get the painter
        painter = args[0]
        # draw the image now!
        painter.drawImage( -self.tmp_img.width() / 2.0, -self.tmp_img.height() / 2.0, self.tmp_img )

    def boundingRect(self):
        if not self.img:
            return QRectF()

        # create the temporary scaled image (if not already done)
        if not self.tmp_img:
            self.createTempScaledImage()

        w = self.tmp_img.width() / 2.0 # half image width
        h = self.tmp_img.height() / 2.0 # half image height

        # return the bounding box of the image
        return QRectF( -w, -h, 2.0*w, 2.0*h )

    def updatePosition(self):
        # update the marker position
        self.setCenter( self.center )

    def delete(self):
        # remove the marker from the canvas
        self.canvas.scene().removeItem( self )


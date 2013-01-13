"""
/***************************************************************************
 split_features_example5_solution
                                 A QGIS plugin
 Split features for QGis Workshop
                              -------------------
        begin                : 2012-09-20
        copyright            : (C) 2012 by Giuseppe Sucameli (Faunalia)
        email                : sucameli@faunalia.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources

# import the class of the line drawer map tool
from maptool_linedrawer import LineDrawer

class split_features_example5_solution:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # create the map tool to draw a line
        self.lineDrawer = LineDrawer( self.iface.mapCanvas() )
        QObject.connect( self.lineDrawer, SIGNAL("editingFinished()"), self.splitSelectedFeatures )

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/split_features_example5_solution/icon.png"), \
            "Split features", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("QGis Workshop", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("QGis Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)

        self.lineDrawer.delete()
        del self.lineDrawer


    def splitSelectedFeatures(self):
        # check to make sure we have a selected vector layer containing lines
        layer = self.iface.activeLayer()
        if layer and layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QGis.Polygon:

            import pdb
            pyqtRemoveInputHook()
            pdb.set_trace()

            line = self.lineDrawer.geometry().asPolyline()
            if len(line) == 0:
                # empty line
                return

            # Create a temporary layer and put it in edit mode
            vl = QgsVectorLayer("Polygon", "splitted features", "memory")
            vl.startEditing()

            # add a distance attribute
            vl.addAttribute( QgsField("parend id", QVariant.Int) )

            # Loop through all the selected features
            for feature in layer.selectedFeatures():
                geom = feature.geometry()

                (retval, newGeometries, topologyTestPoints) = geom.splitGeometry( line, False )
                if retval == 1:    # nessuna spezzatura
                    continue

                changedGeometries = newGeometries + [geom]
                for g in changedGeometries:
                    # Create a new QgsFeature, assign it the new geometry
                    # and put the distance into the distance field
                    fet = QgsFeature()
                    fet.setAttributeMap( { 0 : feature.id() } )
                    fet.setGeometry( g )

                    # store the feature into the temporary layer
                    vl.addFeature( fet )

            # save the changes
            vl.commitChanges()

            # finally load the layer in canvas
            QgsMapLayerRegistry.instance().addMapLayer( vl )

        else:
            QMessageBox.information(self.iface.mainWindow(), "Split features", "The tool works on the selected polygons of the active vector layer")

    # run method that performs all the real work
    def run(self):
        # set the line drawer tool as active tool in canvas
        self.iface.mapCanvas().setMapTool( self.lineDrawer )

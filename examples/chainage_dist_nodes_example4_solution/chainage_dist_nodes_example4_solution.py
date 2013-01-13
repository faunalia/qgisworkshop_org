"""
/***************************************************************************
 chainage_dist_nodes_example4_solution
                                 A QGIS plugin
 Chainage distance nodes for QGis Workshop
                              -------------------
        begin                : 2012-09-20
        copyright            : (C) 2012 by Giuseppe Sucameli (Faunalia)
        email                : sucameli@faunalia.it
 ***************************************************************************/

Based on "Generating chainage (distance) nodes in QGIS" by Nathan Woodrow
(see http://woostuff.wordpress.com/2012/08/05/generating-chainage-distance-nodes-in-qgis/)

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

class chainage_dist_nodes_example4_solution:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/chainage_dist_nodes_example4_solution/icon.png"), \
            "Chainage distance nodes", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("QGis Workshop", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("QGis Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)

    def pointsAt(self, dist, geom):
        points = []

        # ############ EDITS GO HERE ####################  
        ''' write code that will return ALL the points along the line at supplied distance''' 
        ''' Use the QgsGeometry.interpolate( distance ) function available in QGis > 1.8 to get a point along the line at given distance '''

        length = geom.length()
        currentdistance = dist

        while currentdistance < length:
            # Get a point along the line at the current distance
            point = geom.interpolate(currentdistance)
            points.append( point )

            # Increase the distance
            currentdistance = currentdistance + dist

        return points


    def pointsAlongSelectedLines(self, layer, distance):
        # Create a temporary layer and put it in edit mode
        vl = QgsVectorLayer("Point", "distance nodes", "memory")
        vl.startEditing()

        # add a distance attribute
        vl.addAttribute( QgsField("distance", QVariant.Int) )

        # Loop through all the selected features
        for feature in layer.selectedFeatures():
            geom = feature.geometry()

            # get the points along geom at given distance 
            points = self.pointsAt(distance, geom)

            # loop through points
            for i, point in enumerate(points):
                # Create a new QgsFeature, assign it the new geometry
                # and put the distance into the distance field
                fet = QgsFeature()
                fet.setAttributeMap( { 0 : i * distance } )
                fet.setGeometry( point )

                # store the feature into the temporary layer
                vl.addFeature( fet )

		# save the changes
        vl.commitChanges()

        # finally load the layer in canvas
        QgsMapLayerRegistry.instance().addMapLayer( vl )


    # run method that performs all the real work
    def run(self):
        # check to make sure we have a selected vector layer containing lines
        layer = self.iface.activeLayer()
        if layer and layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QGis.Line and len(layer.selectedFeatures()) > 0:

            # ask the distance value to the user (default value is 100)
            (dist, ok) = QInputDialog.getDouble(self.iface.mainWindow(), "Chainage distance nodes", "Enter the distance between points", 100)
            if not ok or dist <= 0:
                return

            # create a layer containing points along the selected lines of 
            # the current layer, then load it
            self.pointsAlongSelectedLines( layer, dist )

        else:
            QMessageBox.information(self.iface.mainWindow(), "Chainage distance nodes", "The tool works on the selected lines of the active vector layer")

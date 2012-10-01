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

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "chainage_dist_nodes_example4_solution"
def description():
    return "Chainage distance nodes - QGis Workshop"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load chainage_dist_nodes_example4_solution class from file chainage_dist_nodes_example4_solution
    from chainage_dist_nodes_example4_solution import chainage_dist_nodes_example4_solution
    return chainage_dist_nodes_example4_solution(iface)

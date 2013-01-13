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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "split_features_example5_solution"
def description():
    return "Split features - QGis Workshop"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load split_features_example5_solution class from file split_features_example5_solution
    from split_features_example5_solution import split_features_example5_solution
    return split_features_example5_solution(iface)

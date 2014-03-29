# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoValleCVC
                                 A QGIS plugin
 PlugIn para QGIS - Modelo Geoidal CVC del Valle del Cauca
                             -------------------
        begin                : 2014-03-27
        copyright            : (C) 2014 by Andres Herrera
        email                : fandresherrera@hotmail.com
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

def classFactory(iface):
    # load GeoValleCVC class from file GeoValleCVC
    from geovallecvc import geovallecvc
    return geovallecvc(iface)

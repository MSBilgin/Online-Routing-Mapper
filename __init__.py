# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OnlineRoutingMapper
                                 A QGIS plugin
 Generate routes by using online services (Openrouteservice, GraphHopper , TomTom, Here)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-10-23
        copyright            : (C) 2024 by Mehmet Selim BILGIN, Yunus Emre ONDER
        email                : mselimbilgin@yahoo.com, emre.ondr@hotmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OnlineRoutingMapper class from file OnlineRoutingMapper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .onlineroutingmapper import OnlineRoutingMapper
    return OnlineRoutingMapper(iface)

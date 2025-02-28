# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OnlineRoutingMapperDialog
                                 A QGIS plugin
 Generate routes by using online services (Google Directions, Here, MapBox, YourNavigation, OSRM etc.)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-10-01
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Mehmet Selim BILGIN
        email                : mselimbilgin@yahoo.com
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

import os

from qgis.PyQt.QtCore import Qt
from qgis.PyQt import uic, QtGui
from qgis.PyQt import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base.ui'))


class OnlineRoutingMapperDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if not event.key() == Qt.Key_Escape:
            super().keyPressEvent(event)



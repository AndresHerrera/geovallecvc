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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *

############################################
from qgis.core import *
from qgis.gui import *
############################################

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from geovallecvcdialog import geovallecvcdialog
import os.path


class geovallecvc:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
		
		############################################
		
		# reference to map canvas
        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
		
	
	
		
		############################################3
		
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'geovallecvc_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = geovallecvcdialog()

    def initGui(self):
        # Create action that will start plugin configuration
        #self.action = QAction(QIcon(":/plugins/geovallecvc/icon.png"),u"Calculo Ondulación Geoidal", self.iface.mainWindow())
        self.action = QAction(QIcon(os.path.join(self.plugin_dir,"icon.png")),u"Calculo Ondulación Geoidal", self.iface.mainWindow())
		# connect the action to the run method
        self.action.triggered.connect(self.run)
		
		#QObject.connect(self.action, SIGNAL("triggered()"), self.run)
		
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&geovallecvc", self.action)
		
		
		#self.action.clickTool.canvasClicked.connect(self.handleMouseDown)
		
		############################################
		# connect our custom function to a clickTool signal that the canvas was clicked
		#result = self.action.connect(canvasClicked(const QgsPoint &, Qt::MouseButton), self.handleMouseDown)
		#result=self.clickTool.canvasClicked.connect(self.handleMouseDown)
		#result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
		############################################
		
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&geovallecvc", self.action)
        self.iface.removeToolBarIcon(self.action)
	
	def handleMouseDown(self, point, button):
		QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )
    
	def cplanas_calcular(self):
		QMessageBox.information( self.iface.mainWindow(),"sdsdsd", "Gracias por usar el plugin !" )
	
	# run method that performs all the real work
    def run(self):
		# make our clickTool the tool that we'll use for now
        self.canvas.setMapTool(self.clickTool)
		# show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
			QMessageBox.information( self.iface.mainWindow(),"Mensaje", "Gracias por usar el plugin !" )
            #pass
		#result = self.dlg.exec_()
        # See if OK was pressed
		#if result == 1:
		#	QMessageBox.information( self.iface.mainWindow(),"Mensaje", "Gracias por usar el plugin !" )
            # substitute with your code)
            #pass
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoValleCVCDialog
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

import os
import urllib
from string import Template
from string import capwords
import datetime
import codecs
import struct

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *

from qgis.gui import *

import ogr, osr


from osgeo.gdal import *  
from osgeo.gdalnumeric import *  
from osgeo.gdalconst import * 
from numpy import *

from PyQt4 import QtCore, QtGui
from ui_geovallecvc import Ui_geovallecvc
# create the dialog for zoom to point
import os.path

class geovallecvcdialog(QtGui.QDialog, Ui_geovallecvc):
	def __init__(self):
		QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
		self.setupUi(self)
		
		self.plugin_dir = os.path.dirname(__file__)
		self.label_19.setPixmap(QPixmap(os.path.join(self.plugin_dir,"logo_g.png")));
		self.label_20.setPixmap(QPixmap(os.path.join(self.plugin_dir,"logo_g.png")));
		self.label_21.setPixmap(QPixmap(os.path.join(self.plugin_dir,"logo_g.png")));
		self.label_22.setPixmap(QPixmap(os.path.join(self.plugin_dir,"logo_g.png")));
	
	
	def trunc(f, n):
		return ('%.*f' % (n + 1, f))[:-1]
		
	def readRaster_GeograficasDecimales(self):
		self.plugin_dir = os.path.dirname(__file__)
		fileName=os.path.join(self.plugin_dir, 'geoid','geoide_1mm_w.tif')
		#fileName = ":/plugins/geovallecvc/geoid/geoide_1mm_w.tif" 
		ds = gdal.Open(fileName, GA_ReadOnly ) 
		if ds is None:
			QMessageBox.information( self,"Error", "No se pudo abrir el Geoide !")
		
		#print 'point (real-world coords): ',x,',',y
		
		self.cgd_w.setValidator(QDoubleValidator())
		self.cgd_n.setValidator(QDoubleValidator())
		
		x=float(self.cgd_w.text())
		y=float(self.cgd_n.text())
		
		
			
		transf = ds.GetGeoTransform()
		cols = ds.RasterXSize
		rows = ds.RasterYSize
		bands = ds.RasterCount #1
		band = ds.GetRasterBand(1)
		bandtype = gdal.GetDataTypeName(band.DataType) #Int16
		driver = ds.GetDriver().LongName #'GeoTIFF'
		
		# set a default NDV if none specified
		if (band.GetNoDataValue() == None):
			band.SetNoDataValue(-9999)
		ndv = band.GetNoDataValue()
		
		cellSizeX = transf[1]
		# Y-cell resolution is reported as negative
		cellSizeY = -1 * transf[5]

		minx = transf[0]
		maxy = transf[3]
		maxx = minx + (cols * cellSizeX)
		miny = maxy - (rows * cellSizeY)
		#print 'bbox(real-world coords):',minx,',',miny,',',maxx,',',maxy
		if ((x < minx) or (x > maxx) or (y < miny) or (y > maxy)):
			#print 'given point does not fall within grid'
			return ndv

		# calc point location in pixels
		xLoc = (x - minx) / cellSizeX
		xLoc = int(xLoc)
		yLoc = (maxy - y) / cellSizeY
		yLoc = int(yLoc)

		if ((xLoc < 0.5) or (xLoc > cols - 0.5)):
			return ndv

		if ((yLoc < 0.5) or (yLoc > rows - 0.5)):
			return ndv
  		#band.XSize, band.YSize, band.XSize, band.YSize
		structval = band.ReadRaster(xLoc, yLoc, 1, 1, 1, 1, buf_type = band.DataType )
		
		if (bandtype == 'Int16'):
			dblValue = struct.unpack('h', structval)
		elif (bandtype == 'Float32'):
			dblValue = struct.unpack('f', structval)
		elif (bandtype == 'Byte'):
			dblValue = struct.unpack('B', structval)
		else:
			QMessageBox.information( self,"Error", paste('unrecognized DataType:', bandtype) )
			return ndv
		 
		#self.cp_r.setText(     str( int(float(str( dblValue[0] )) * 10000) / 10000.0 )   )
		self.cgd_r.setText(  str( dblValue[0] )   )
		QMessageBox.information( self,"Resultado", u"Ondulación calculada !")
	
	
	def readRaster_GeograficasGMS(self):
		self.plugin_dir = os.path.dirname(__file__)
		fileName=os.path.join(self.plugin_dir, 'geoid','geoide_1mm_w.tif')

		ds = gdal.Open(fileName, GA_ReadOnly ) 
		if ds is None:
			QMessageBox.information( self,"Error", "No se pudo abrir el Geoide !")
		
		#print 'point (real-world coords): ',x,',',y
		
		
		self.cgms_lon_g.setValidator(QDoubleValidator())
		self.cgms_lon_m.setValidator(QDoubleValidator())
		self.cgms_lon_s.setValidator(QDoubleValidator())
		
		self.cgms_lat_g.setValidator(QDoubleValidator())
		self.cgms_lat_m.setValidator(QDoubleValidator())
		self.cgms_lat_s.setValidator(QDoubleValidator())
		
		
		lon_g=float(self.cgms_lon_g.text())
		lon_m=float(self.cgms_lon_m.text())
		lon_s=float(self.cgms_lon_s.text())
		
		lat_g=float(self.cgms_lat_g.text())
		lat_m=float(self.cgms_lat_m.text())
		lat_s=float(self.cgms_lat_s.text())
		
		
		x=(abs(lon_g) + (abs(lon_m)/60)+(abs(lon_s)/3600))*-1;
		y=(abs(lat_g) + (abs(lat_m)/60)+(abs(lat_s)/3600));
		
		#QMessageBox.information( self,"Resultado", str(x))
		#QMessageBox.information( self,"Resultado", str(y))
	
		
		#x=float(self.cgd_w.text())
		#y=float(self.cgd_n.text())
		
		transf = ds.GetGeoTransform()
		cols = ds.RasterXSize
		rows = ds.RasterYSize
		bands = ds.RasterCount #1
		band = ds.GetRasterBand(1)
		bandtype = gdal.GetDataTypeName(band.DataType) #Int16
		driver = ds.GetDriver().LongName #'GeoTIFF'
		
		# set a default NDV if none specified
		if (band.GetNoDataValue() == None):
			band.SetNoDataValue(-9999)
		ndv = band.GetNoDataValue()
		
		cellSizeX = transf[1]
		# Y-cell resolution is reported as negative
		cellSizeY = -1 * transf[5]

		minx = transf[0]
		maxy = transf[3]
		maxx = minx + (cols * cellSizeX)
		miny = maxy - (rows * cellSizeY)
		#print 'bbox(real-world coords):',minx,',',miny,',',maxx,',',maxy
		if ((x < minx) or (x > maxx) or (y < miny) or (y > maxy)):
			#print 'given point does not fall within grid'
			return ndv

		# calc point location in pixels
		xLoc = (x - minx) / cellSizeX
		xLoc = int(xLoc)
		yLoc = (maxy - y) / cellSizeY
		yLoc = int(yLoc)

		if ((xLoc < 0.5) or (xLoc > cols - 0.5)):
			return ndv

		if ((yLoc < 0.5) or (yLoc > rows - 0.5)):
			return ndv
  		#band.XSize, band.YSize, band.XSize, band.YSize
		structval = band.ReadRaster(xLoc, yLoc, 1, 1, 1, 1, buf_type = band.DataType )
		
		if (bandtype == 'Int16'):
			dblValue = struct.unpack('h', structval)
		elif (bandtype == 'Float32'):
			dblValue = struct.unpack('f', structval)
		elif (bandtype == 'Byte'):
			dblValue = struct.unpack('B', structval)
		else:
			QMessageBox.information( self,"Error", paste('unrecognized DataType:', bandtype) )
			return ndv
		 
		#self.cp_r.setText(     str( int(float(str( dblValue[0] )) * 10000) / 10000.0 )   )
		self.cgms_r.setText(  str( dblValue[0] )   )
		QMessageBox.information( self,"Resultado", u"Ondulación calculada !")
		
	def readRaster_Planas(self):
		self.plugin_dir = os.path.dirname(__file__)
		fileName=os.path.join(self.plugin_dir, 'geoid','geoide_1mm_w.tif')

		ds = gdal.Open(fileName, GA_ReadOnly ) 
		if ds is None:
			QMessageBox.information( self,"Error", "No se pudo abrir el Geoide !")
	
		#print 'point (real-world coords): ',x,',',y
		
		self.cp_e.setValidator(QDoubleValidator())
		self.cp_n.setValidator(QDoubleValidator())
		
		pointX = float(self.cp_e.text()) 
		pointY = float(self.cp_n.text())
		# Spatial Reference System
		inputEPSG = 3115
		outputEPSG = 4326
		# create a geometry from coordinates
		point = ogr.Geometry(ogr.wkbPoint)
		point.AddPoint(pointX, pointY)	
		# create coordinate transformation
		inSpatialRef = osr.SpatialReference()
		inSpatialRef.ImportFromEPSG(inputEPSG)
		outSpatialRef = osr.SpatialReference()
		outSpatialRef.ImportFromEPSG(outputEPSG)
		coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)
		# transform point
		point.Transform(coordTransform)
		# print point in EPSG 4326
		
		x=point.GetX()
		y=point.GetY()
		
		transf = ds.GetGeoTransform()
		cols = ds.RasterXSize
		rows = ds.RasterYSize
		bands = ds.RasterCount #1
		band = ds.GetRasterBand(1)
		bandtype = gdal.GetDataTypeName(band.DataType) #Int16
		driver = ds.GetDriver().LongName #'GeoTIFF'
		
		# set a default NDV if none specified
		if (band.GetNoDataValue() == None):
			band.SetNoDataValue(-9999)
		ndv = band.GetNoDataValue()
		
		cellSizeX = transf[1]
		# Y-cell resolution is reported as negative
		cellSizeY = -1 * transf[5]

		minx = transf[0]
		maxy = transf[3]
		maxx = minx + (cols * cellSizeX)
		miny = maxy - (rows * cellSizeY)
		#print 'bbox(real-world coords):',minx,',',miny,',',maxx,',',maxy
		if ((x < minx) or (x > maxx) or (y < miny) or (y > maxy)):
			#print 'given point does not fall within grid'
			return ndv

		# calc point location in pixels
		xLoc = (x - minx) / cellSizeX
		xLoc = int(xLoc)
		yLoc = (maxy - y) / cellSizeY
		yLoc = int(yLoc)

		if ((xLoc < 0.5) or (xLoc > cols - 0.5)):
			return ndv

		if ((yLoc < 0.5) or (yLoc > rows - 0.5)):
			return ndv
  		
		structval = band.ReadRaster(xLoc, yLoc, 1, 1, 1, 1, buf_type = band.DataType )
		
		if (bandtype == 'Int16'):
			dblValue = struct.unpack('h', structval)
		elif (bandtype == 'Float32'):
			dblValue = struct.unpack('f', structval)
		elif (bandtype == 'Byte'):
			dblValue = struct.unpack('B', structval)
		else:
			QMessageBox.information( self,"Error", 'unrecognized DataType: ' +bandtype  )
			return ndv
		 
		#self.cp_r.setText(     str( int(float(str( dblValue[0] )) * 10000) / 10000.0 )   )
		self.cp_r.setText(  str( dblValue[0] )   )
		QMessageBox.information( self,"Resultado", u"Ondulación calculada !")
	

	def readRaster_Arena(self):
		self.plugin_dir = os.path.dirname(__file__)
		fileName=os.path.join(self.plugin_dir, 'geoid','geoide_1mm_w.tif')

		ds = gdal.Open(fileName, GA_ReadOnly ) 
		if ds is None:
			QMessageBox.information( self,"Error", "No se pudo abrir el Geoide !")
	
		#print 'point (real-world coords): ',x,',',y
		
		self.ca_e.setValidator(QDoubleValidator())
		self.ca_n.setValidator(QDoubleValidator())
		
		pointX = float(self.ca_e.text()) 
		pointY = float(self.ca_n.text())
		# Spatial Reference System
		inputEPSG = 21896
		outputEPSG = 4326
		# create a geometry from coordinates
		point = ogr.Geometry(ogr.wkbPoint)
		point.AddPoint(pointX, pointY)	
		# create coordinate transformation
		inSpatialRef = osr.SpatialReference()
		inSpatialRef.ImportFromEPSG(inputEPSG)
		outSpatialRef = osr.SpatialReference()
		outSpatialRef.ImportFromEPSG(outputEPSG)
		coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)
		# transform point
		point.Transform(coordTransform)
		# print point in EPSG 4326
		
		x=point.GetX()
		y=point.GetY()
		
		transf = ds.GetGeoTransform()
		cols = ds.RasterXSize
		rows = ds.RasterYSize
		bands = ds.RasterCount #1
		band = ds.GetRasterBand(1)
		bandtype = gdal.GetDataTypeName(band.DataType) #Int16
		driver = ds.GetDriver().LongName #'GeoTIFF'
		
		# set a default NDV if none specified
		if (band.GetNoDataValue() == None):
			band.SetNoDataValue(-9999)
		ndv = band.GetNoDataValue()
		
		cellSizeX = transf[1]
		# Y-cell resolution is reported as negative
		cellSizeY = -1 * transf[5]

		minx = transf[0]
		maxy = transf[3]
		maxx = minx + (cols * cellSizeX)
		miny = maxy - (rows * cellSizeY)
		#print 'bbox(real-world coords):',minx,',',miny,',',maxx,',',maxy
		if ((x < minx) or (x > maxx) or (y < miny) or (y > maxy)):
			#print 'given point does not fall within grid'
			return ndv

		# calc point location in pixels
		xLoc = (x - minx) / cellSizeX
		xLoc = int(xLoc)
		yLoc = (maxy - y) / cellSizeY
		yLoc = int(yLoc)

		if ((xLoc < 0.5) or (xLoc > cols - 0.5)):
			return ndv

		if ((yLoc < 0.5) or (yLoc > rows - 0.5)):
			return ndv
  		
		structval = band.ReadRaster(xLoc, yLoc, 1, 1, 1, 1, buf_type = band.DataType )
		
		if (bandtype == 'Int16'):
			dblValue = struct.unpack('h', structval)
		elif (bandtype == 'Float32'):
			dblValue = struct.unpack('f', structval)
		elif (bandtype == 'Byte'):
			dblValue = struct.unpack('B', structval)
		else:
			QMessageBox.information( self,"Error", 'unrecognized DataType: ' +bandtype  )
			return ndv
		 
		#self.cp_r.setText(     str( int(float(str( dblValue[0] )) * 10000) / 10000.0 )   )
		self.ca_r.setText(  str( dblValue[0] )   )
		QMessageBox.information( self,"Resultado", u"Ondulación calculada !")
		
	def cplanas_calculo(self):
		if self.cp_n.text().strip() and self.cp_e.text().strip():
			self.readRaster_Planas()
		else:
			QMessageBox.critical( self,"Mensaje", u"Debe indicar unas coordenadas !")
		
	def cplanasarena_calculo(self):
		if self.ca_n.text().strip() and self.ca_e.text().strip():
			self.readRaster_Arena()
		else:
			QMessageBox.critical( self,"Mensaje", u"Debe indicar unas coordenadas !")
			
	def cgeodeg_calculo(self):
		if self.cgd_w.text().strip() and self.cgd_n.text().strip():
			self.readRaster_GeograficasDecimales()
		else:
			QMessageBox.critical( self,"Mensaje", u"Debe indicar unas coordenadas !")
		
		
	def cgeogms_calculo(self):
		if self.cgms_lon_g.text().strip() and self.cgms_lon_m.text().strip() and self.cgms_lon_s.text().strip() and self.cgms_lat_g.text().strip() and self.cgms_lat_m.text().strip() and self.cgms_lat_s.text().strip():
			self.readRaster_GeograficasGMS()	
		else:
			QMessageBox.critical( self,"Mensaje", u"Debe indicar unas coordenadas !")
		
		
	def limpiar1(self):
		self.cp_e.setText("")
		self.cp_n.setText("")
		self.cp_r.setText("")
	
	def limpiar2(self):
		self.ca_e.setText("")
		self.ca_n.setText("")
		self.ca_r.setText("")
		
	def limpiar3(self):
		self.cgms_lon_g.setText("")
		self.cgms_lon_m.setText("")
		self.cgms_lon_s.setText("")
		
		self.cgms_lat_g.setText("")
		self.cgms_lat_m.setText("")
		self.cgms_lat_s.setText("")

		self.cgms_r.setText("")
		
	def limpiar4(self):
		self.cgd_w.setText("")
		self.cgd_n.setText("")
		self.cgd_r.setText("")
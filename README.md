geovallecvc
===========

PlugIn para QGIS - Modelo Geoidal CVC del Valle del Cauca

Este plugin para QGIS entrega la ondulación geoidal para puntos de entrada en diferentes sistemas de referencia en el Valle del Cauca, para su calculo hace uso del Geoide local (GEOVALLE 1.0) (Opensource) desarrollado por la coorporación autonoma regional (CVC). Más información sobre el modelo geoidal GEOVALLE 1.0 en http://www.cvc.gov.co/

==========

Plugin para QGIS - Modelo Geoidal CVC del Valle del Cauca

Paso 1 : Descarga del plugin desde el repositorio, ubicado en http://54.245.115.218/plugin/plugins.xml



Paso 2: Descarga del plugin ( geovallecvc.zip )



Paso 3: Descomprimir plugin en carpeta de plugins de QGIS

UNIX/Mac: ~/.qgis/python/plugins and (qgis_prefix)/share/qgis/python/plugins
Windows: ~/.qgis/python/plugins and (qgis_prefix)/python/plugins
Directorio de inicio (denotado por  ~) en Windows usualmente es algo como C:\Documents and Settings\(usuario). Los subdirectorios en esta rutass son considerados como los paquetes de Python que se pueden importar a QGIS como plugins.



* Para mi caso, el archivo .zip lo descomprimi en C:\Users\Andres\.qgis2\python\plugins tal como muestra la grafica !

Paso 4: Iniciar QGIS y ir al menú de Complementos -> Administrar e instalar complementos



Paso 5: Habilitar plugin ( geovallecvc )



Paso 6: Iniciar plugin (geovallecvc ) desde el menú . Complementos -> geovallecvc -> Calculo Ondulación Geoidal



Ejecutando el plugin

* Ventana de Bienvenida y Acerca del plugin



a) Calculo de ondulación geoidal a partir de Coordenadas planas ( MAGNA-OESTE)



- Digitar coordenadas Este, Norte y click en boton ( Calcular Ondulación Geoidal )



- Una vez realice el calculo, un mensaje indicará que fiinalizo el calculo (1), y el resultado de la ondulación (m) aparecerá en (2).

b) Calculo de ondulación geoidal a partir de Coordenadas planas ( Bogota-OESTE) en antigúo sistema de referencia nacional (ARENA).



c) Calculo de ondulación geoidal a partir de Coordenadas Geográficas, en Grados,Minutos,Segundos ( DMS)



d) Calculo de ondulación geoidal a partir de Coordenadas Geográficas en (Decimales)



Comentarios finales

Espero que esta herramienta les sirva como utilidad, es mi primer plugin construido para QGIS realizado como ejercicio academico de exploración de funcionalidades avanzadas en QGIS, así que puede tener muchos Bugs, fue construido en más o menos 3 horas de desarrollo continuo, solo con conocimientos basicos de python, a continuación algunos de links que recopilan las fuentes que usé para contruir este plugin:

http://www.qgis.org/en/docs/pyqgis_developer_cookbook/plugins.html
http://gis.stackexchange.com/questions/26979/how-to-install-a-qgis-plugin-when-offline
http://www.qgisworkshop.org/html/workshop/python_in_qgis_tutorial1.html
http://www.spatialreference.org/ref/epsg/3115/
http://www.spatialreference.org/ref/epsg/21896/
http://www.spatialreference.org/ref/epsg/4326/
http://www.riverbankcomputing.co.uk/software/pyqt/intro
http://www.pythondiario.com/2013/11/como-instalar-pyqt4-en-windows-linux-y.htm
https://wiki.python.org/moin/PyQt
https://wiki.python.org/moin/PyQt4
https://pypi.python.org/pypi/GDAL/
http://www.gdal.org/
http://trac.osgeo.org/gdal/wiki/GdalOgrInPython
* Pronto la descarga se podra realizar directamente desde el repositorio de QGIS

http://plugins.qgis.org/plugins/geovallecvc/
Más acerca de geovalle ( Modelo geoidal para el valle del cauca )

http://geocvce.cvc.gov.co/visor/
http://www.cvc.gov.co/
 

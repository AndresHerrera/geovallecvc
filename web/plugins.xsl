<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<html>
    <head>
        <title>QGIS Python Plugins - Andres Herrera</title>
        <meta name="DESCRIPTION" content="Python QGIS Plugins Produced by Andres Herrera, Cali, Colombia."></meta>
        <meta name="KEYWORDS" content="QGIS, Python, Plugins, Raster Editing, GPS functions, Zoom Functions"></meta>
        <meta name="TYPE" content="andresherreracali.blogspot.com"></meta>
        <meta name="RATING" content="General"></meta>
        <meta name="DISTRIBUTION" content="global"></meta>
        <meta name="ABSTRACT" content="QGIS Python Plugins"></meta>
        <link rel="SHORTCUT ICON" href="NewAnimation.gif" />
    </head>
    <body align="center" style="background-color: rgb(199, 199, 199);">
        <p align="center"><i><b>
        <a href="http://andresherreracali.blogspot.com" target="_blank">
            <font color="#cc6600" face="Franklin Gothic Medium" size="5">Andres Herrera - Blog</font></a></b></i></p>
<table align="center" style="width: 994px; height: 70px;" border="0">

<tbody>
<tr>
<!-- <td colspan="1" rowspan="1" align="center" height="85" width="167"> -->
      <td colspan="1" rowspan="1"
 style="width: 994px; vertical-align: middle; height: 70px; text-align: center;">
      <font style="color: red; font-family: Franklin Gothic Medium;" size="45"><big>
      QGIS Python Plugins</big></font>
      </td>
</tr>
</tbody>
</table>
<table align="center" style="background-color: rgb(234, 255, 238); height: 59px; width: 994px;" border="2" cellpadding="1" cellspacing="0">
<tbody>
    <xsl:for-each select="//pyqgis_plugin">
        <tr>
            <td style="width: 33%; text-align: center;">
                <a href="{homepage}" target="_blank">
                    <small><i><b><font color="#cc6600" face="Franklin Gothic Medium" size="5">
                    <xsl:value-of select="@name"/>
                    </font></b></i></small></a></td>
            <td style="padding: 10px;" width="67%"><small><i><b><font color="#cc6600" face="Franklin Gothic Medium" size="5">
                <small><xsl:value-of select="description"/><br></br>
                Author: <xsl:value-of select="author_name"/><br></br>
                Version: <xsl:value-of select="@version"/><br></br>
                QGIS Minimum Version: <xsl:value-of select="qgis_minimum_version"/><br></br>
				QGIS Maximun Version: <xsl:value-of select="qgis_maximum_version"/><br></br>
                Download file:
                <a href="{download_url}"><xsl:value-of select="download_url"/></a>
                </small>
                </font>
                </b></i></small></td>
        </tr>
    </xsl:for-each>
</tbody>
</table>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>
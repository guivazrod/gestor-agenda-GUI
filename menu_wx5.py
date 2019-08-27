# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:18:09 2019

@author: Guillermo
"""

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

# contenido añadido
import os
import manager
import re

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 348,309 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.listaPrincipal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
        bSizer1.Add( self.listaPrincipal, 0, wx.ALL|wx.EXPAND, 5 )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.bLista = wx.Button( self, wx.ID_ANY, u"Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.bLista, 0, wx.ALL, 5 )
        
        self.bBusca = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.bBusca, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        self.bAnade = wx.Button( self, wx.ID_ANY, u"Añadir", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.bAnade, 0, wx.ALL, 5 )
        
        self.bBorra = wx.Button( self, wx.ID_ANY, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.bBorra, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( gSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.filemenu = wx.Menu()
        self.mAbrir = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Abrir", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.mAbrir )
        
        self.mGuardar = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.mGuardar )
        
        self.mguardarComo = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Guardar como", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.mguardarComo )
        
        self.filemenu.AppendSeparator()
        
        self.msalir = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
        self.filemenu.AppendItem( self.msalir )
        
        self.m_menubar1.Append( self.filemenu, u"Archivo" ) 
        
        self.mAccion = wx.Menu()
        self.mLista = wx.MenuItem( self.mAccion, wx.ID_ANY, u"Lista", wx.EmptyString, wx.ITEM_NORMAL )
        self.mAccion.AppendItem( self.mLista )
        
        self.mBusca = wx.MenuItem( self.mAccion, wx.ID_ANY, u"Buscar", wx.EmptyString, wx.ITEM_NORMAL )
        self.mAccion.AppendItem( self.mBusca )
        
        self.mAnade = wx.MenuItem( self.mAccion, wx.ID_ANY, u"Añadir", wx.EmptyString, wx.ITEM_NORMAL )
        self.mAccion.AppendItem( self.mAnade )
        
        self.mBorra = wx.MenuItem( self.mAccion, wx.ID_ANY, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL )
        self.mAccion.AppendItem( self.mBorra )
        
        self.m_menubar1.Append( self.mAccion, u"Acciones" ) 
        
        self.m_menu3 = wx.Menu()
        self.mAyuda = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Ayuda", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.mAyuda )
        
        self.mAcerca = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Acerca de...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.mAcerca )
        
        self.m_menubar1.Append( self.m_menu3, u"MyMenu" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.bLista.Bind( wx.EVT_BUTTON, self.lista )
        self.bBusca.Bind( wx.EVT_BUTTON, self.busca )
        self.bAnade.Bind( wx.EVT_BUTTON, self.anade )
        self.bBorra.Bind( wx.EVT_BUTTON, self.borra )
        self.Bind( wx.EVT_MENU, self.abrir, id = self.mAbrir.GetId() )
        self.Bind( wx.EVT_MENU, self.guardar, id = self.mGuardar.GetId() )
        self.Bind( wx.EVT_MENU, self.guardarComo, id = self.mguardarComo.GetId() )
        self.Bind( wx.EVT_MENU, self.salir, id = self.msalir.GetId() )
        self.Bind( wx.EVT_MENU, self.lista, id = self.mLista.GetId() )
        self.Bind( wx.EVT_MENU, self.busca, id = self.mBusca.GetId() )
        self.Bind( wx.EVT_MENU, self.anade, id = self.mAnade.GetId() )
        self.Bind( wx.EVT_MENU, self.borrar, id = self.mBorra.GetId() )


        # contenido añadido
        self.archivo='untitled.csv' # esta es la variable que almacena el nombre del fichero de trabajo por defecto

    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def lista(self, event):
        self.SetStatusText("")
        self.listaPrincipal.DeleteAllItems()
        for entrada in manager.agenda.entradas:
            self.listaPrincipal.Append(entrada.listacontenido())
        return    
    
    def busca( self, event ):
        self.SetStatusText("")
        dato = manager.Registro()
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Busqueda por DNI')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not re.match('[0-9]{2}[A-Z]', str(dlg.GetValue())):
                self.SetStatusText("Formato DNI incorrecto: "
                                   + str(dlg.GetValue()))
                dlg.SetValue("")
            else:
                dato.dni=dlg.GetValue()
                for item in manager.agenda.entradas:
                    if item.dni == dato.dni:
                        self.SetStatusText('{} {} {} {}'.format(
                                            "Registro encontrado: ",
                                            str(item.dni),
                                            str(item.nombre),
                                            str(item.apellidos))) 
        else:
            self.SetStatusText("Registro no encontrado")
            dlg.Destroy()
            return   
        for item in range(self.listaPrincipal.ItemCount):
            if self.listaPrincipal.GetItem(item, 0) == dato.dni:
                self.listaPrincipal.Select(item).SetState(wx.LIST_STATE_FOCUSED | wx.LIST_STATE_SELECTED)
        dlg.Destroy()
        return    
    
    def anade( self, event ):
        self.SetStatusText("")
        dato = manager.Registro()
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not re.match('[0-9]{2}[A-Z]', str(dlg.GetValue())):
                self.SetStatusText("Formato DNI incorrecto: "
                                   +str(dlg.GetValue()))
                dlg.SetValue("")
            else: 
                dato.dni=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        dlg = wx.TextEntryDialog(self, 'Introduce Nombre:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if len(str(dlg.GetValue())) > 20:
                self.SetStatusText("Formato nombre incorrecto: "
                                   +str(dlg.GetValue()))
                dlg.SetValue("")
            else:
                dato.nombre=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        dlg = wx.TextEntryDialog(self, 'Introduce Apellido:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if len(str(dlg.GetValue())) > 100:
                self.SetStatusText("Formato apellido incorrecto: "
                                   +str(dlg.GetValue()))
                dlg.SetValue("")
            else:
                dato.apellidos=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        manager.agenda.anade_registro(dato)
        self.SetStatusText('{} {} {} {}'.format(
            "Registro añadido: ",
            str(dato.dni),
            str(dato.nombre),
            str(dato.apellidos))) 
        self.lista(wx.ID_ANY)
        dlg.Destroy()
        return    
    
    def borra( self, event ):
        self.SetStatusText("")
        dato = manager.Registro()
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Borra registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not re.match('[0-9]{2}[A-Z]', str(dlg.GetValue())):
                self.SetStatusText("Formato DNI incorrecto: "
                                   +str(dlg.GetValue()))
                dlg.SetValue("")
            else:
                dato.dni = dlg.GetValue()
                if manager.agenda.busca_item_dni(dato.dni) == True:
                    dato = manager.agenda.devuelve_registro_dni(dato.dni)
                    if manager.agenda.borra_registro(dato.dni) == True:
                        self.SetStatusText('{} {} {} {}'.format(
                                "Registro borrado:",
                                str(dato.dni),
                                str(dato.nombre),
                                str(dato.apellidos)))
                        dlg.Destroy()
                        return
                else:
                    self.SetStatusText("Registro no encontrado")
                    dlg.Destroy()
                    return
        else:
            self.SetStatusText("Registro no encontrado")
        dlg.Destroy()
        return    
    
    def abrir( self, event ):
        """ Abre el fichero de trabajo usando un cuadro de dialogo """
        dlg=wx.FileDialog(self, "Abrir archivo", os.getcwd(), style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.archivo=dlg.GetPath()
            if manager.leefichero(self.archivo) == True:
                self.lista(wx.ID_ANY)
            else:
                self.SetStatusText("Fichero vacio: "
                                   +str(dlg.GetPath()))
        dlg.Destroy()
    
    def guardar( self, event ):
        """ Guarda el archivo actual """
        if hasattr(self, 'archivo'):
            manager.grabafichero(manager.agenda,self.archivo)
            self.SetTitle("Gestor de agenda 1.0  "+self.archivo)
        else:
            self.guardarComo(None)
    
    def guardarComo( self, event ):
        """ Guarda el archivo actual abriendo un cuadro de dialogo """
        dlg=wx.FileDialog(self, "Guardar", os.getcwd(), style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.archivo=dlg.GetPath()
            manager.grabafichero(manager.agenda,self.archivo)
            self.SetTitle("Gestor de agenda 1.0  "+self.archivo)
        dlg.Destroy()
    
    def salir( self, event ):
        self.Close()
    
if __name__=='__main__':
    app = wx.App()
    mainFrame = MyFrame1(None)
    mainFrame.Show()
    app.MainLoop()    
    
    
    


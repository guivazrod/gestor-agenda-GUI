# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:47:18 2019

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
import helpers
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gestor de agenda", pos = wx.DefaultPosition, size = wx.Size( 352,309 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.listaPrincipal = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
        bSizer1.Add( self.listaPrincipal, 0, wx.ALL|wx.EXPAND, 5 )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.b_lista = wx.Button( self, wx.ID_ANY, u"Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.b_lista, 0, wx.ALL, 5 )
        
        self.b_busca = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.b_busca, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        self.b_anade = wx.Button( self, wx.ID_ANY, u"Añadir", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.b_anade, 0, wx.ALL, 5 )
        
        self.b_borra = wx.Button( self, wx.ID_ANY, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.b_borra, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( gSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_archivo = wx.Menu()
        self.m_abrir = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Abrir", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_archivo.Append( self.m_abrir )
        
        self.m_guardar = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_archivo.Append( self.m_guardar )
        
        self.m_guardarComo = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Guardar como", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_archivo.Append( self.m_guardarComo )
        
        self.m_archivo.AppendSeparator()
        
        self.m_salir = wx.MenuItem( self.m_archivo, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_archivo.Append( self.m_salir )
        
        self.m_menubar1.Append( self.m_archivo, u"Archivo" ) 
        
        self.m_accion = wx.Menu()
        self.m_Lista = wx.MenuItem( self.m_accion, wx.ID_ANY, u"Lista", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_accion.Append( self.m_Lista )
        
        self.m_busca = wx.MenuItem( self.m_accion, wx.ID_ANY, u"Buscar", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_accion.Append( self.m_busca )
        
        self.m_anade = wx.MenuItem( self.m_accion, wx.ID_ANY, u"Añadir", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_accion.Append( self.m_anade )
        
        self.m_borra = wx.MenuItem( self.m_accion, wx.ID_ANY, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_accion.Append( self.m_borra )
        
        self.m_menubar1.Append( self.m_accion, u"Acciones" ) 
        
        self.m_general = wx.Menu()
        self.m_ayuda = wx.MenuItem( self.m_general, wx.ID_ANY, u"Ayuda", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_general.Append( self.m_ayuda )
        
        self.m_general.AppendSeparator()
        
        self.m_acerca = wx.MenuItem( self.m_general, wx.ID_ANY, u"Acerca de...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_general.Append( self.m_acerca )
        
        self.m_menubar1.Append( self.m_general, u"Ayuda" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.b_lista.Bind( wx.EVT_BUTTON, self.lista )
        self.b_busca.Bind( wx.EVT_BUTTON, self.busca )
        self.b_anade.Bind( wx.EVT_BUTTON, self.anade )
        self.b_borra.Bind( wx.EVT_BUTTON, self.borra )
        self.Bind( wx.EVT_MENU, self.abrir, id = self.m_abrir.GetId() )
        self.Bind( wx.EVT_MENU, self.guardar, id = self.m_guardar.GetId() )
        self.Bind( wx.EVT_MENU, self.guardarComo, id = self.m_guardarComo.GetId() )
        self.Bind( wx.EVT_MENU, self.salir, id = self.m_salir.GetId() )
        self.Bind( wx.EVT_MENU, self.lista, id = self.m_Lista.GetId() )
        self.Bind( wx.EVT_MENU, self.busca, id = self.m_busca.GetId() )
        self.Bind( wx.EVT_MENU, self.anade, id = self.m_anade.GetId() )
        self.Bind( wx.EVT_MENU, self.borra, id = self.m_borra.GetId() )
        self.Bind( wx.EVT_MENU, self.ayuda, id = self.m_ayuda.GetId() )
        self.Bind( wx.EVT_MENU, self.acerca, id = self.m_acerca.GetId() )
        
        # contenido añadido
        self.archivo='untitled.csv'
        self.listaPrincipal.InsertColumn(0, 'DNI', width=wx.LIST_AUTOSIZE)
        self.listaPrincipal.InsertColumn(1, 'Nombre', width=wx.LIST_AUTOSIZE)
        self.listaPrincipal.InsertColumn(2, 'Apellido', width=wx.LIST_AUTOSIZE)
    
    def __del__( self ):
        pass

    # contenido añadido
    
    def lista(self, event):
        self.SetStatusText("")
        self.listaPrincipal.DeleteAllItems()
        for entrada in manager.agenda.entradas:
            self.listaPrincipal.Append(entrada.listacontenido())
        return   
    
    def busca( self, event ):
        self.SetStatusText("")
        self.lista(wx.ID_ANY)
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Busqueda por DNI')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not helpers.valida_dni(str(dlg.GetValue())):
                self.SetStatusText("Formato DNI incorrecto: "
                                   + str(dlg.GetValue()))
                dlg.SetValue("")
            else:
                if manager.agenda.busca_item_dni(dlg.GetValue()):
                    dato = manager.agenda.devuelve_registro_dni(dlg.GetValue())
                    self.SetStatusText('{} {}'.format(
                        "Registro encontrado: ",
                        dato.strcontenido()))
                    index = self.listaPrincipal.FindItem(-1,dato.dni)
                    if index != wx.NOT_FOUND:
                        self.listaPrincipal.SetItemState(index, 
                                                         wx.LIST_STATE_SELECTED, 
                                                         wx.LIST_STATE_SELECTED)
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
    
    def anade( self, event ):
        self.SetStatusText("")
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not helpers.valida_dni(str(dlg.GetValue())):
                self.SetStatusText('{} {}'.format(
                        "Formato DNI incorrecto: ",
                        str(dlg.GetValue())))
                dlg.SetValue("")
            else: 
                dni=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        dlg = wx.TextEntryDialog(self, 'Introduce Nombre:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if len(str(dlg.GetValue())) > 20:
                self.SetStatusText('{} {}'.format(
                    "Formato nombre incorrecto: ",
                    str(dlg.GetValue())))
                dlg.SetValue("")
            else:
                nombre=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        dlg = wx.TextEntryDialog(self, 'Introduce Apellido:','Añade registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if len(str(dlg.GetValue())) > 100:
                self.SetStatusText('{} {}'.format(
                    "Formato apellido incorrecto: ",
                    str(dlg.GetValue())))
                dlg.SetValue("")
            else:
                apellidos=dlg.GetValue()
        else:
            self.SetStatusText("No se ha añadido ningun registro")
            dlg.Destroy()
            return
        dato = manager.Registro(dni, nombre, apellidos)
        manager.agenda.anade_registro(dato)
        self.SetStatusText('{} {}'.format(
            "Registro añadido: ",
            dato.strcontenido())) 
        self.lista(wx.ID_ANY)
        dlg.Destroy()
        return    
    
    def borra( self, event ):
        self.SetStatusText("")
        dlg = wx.TextEntryDialog(self, 'Introduce DNI:','Borra registro')
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("")
            if not helpers.valida_dni(str(dlg.GetValue())):
                self.SetStatusText('{} {}'.format(
                    "Formato DNI incorrecto: ",
                    str(dlg.GetValue())))
                dlg.SetValue("")
            else:
                if manager.agenda.busca_item_dni(dlg.GetValue()) == True:
                    dato = manager.agenda.devuelve_registro_dni(dlg.GetValue())
                    if manager.agenda.borra_registro(dato.dni) == True:
                        self.SetStatusText('{} {}'.format(
                                "Registro borrado:",
                                dato.strcontenido()))
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
            self.SetTitle("Gestor de agenda "+self.archivo)
        else:
            self.guardarComo(None)
    
    def guardarComo( self, event ):
        """ Guarda el archivo actual abriendo un cuadro de dialogo """
        dlg=wx.FileDialog(self, "Guardar", os.getcwd(), style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.archivo=dlg.GetPath()
            manager.grabafichero(manager.agenda,self.archivo)
            self.SetTitle("Gestor de agenda "+self.archivo)
        dlg.Destroy()
    
    def salir( self, event ):
        self.Close()
    
    def ayuda( self, event ):
        wx.MessageBox("No disponible","Gestor de agenda")
    
    def acerca( self, event ):
        descripcion=""" Gestor de agenda desarrollado en wxPython """
        info=wx.adv.AboutDialogInfo()
        info.SetName('Gestor de agenda')
        info.SetDescription(descripcion)
        info.SetVersion('1.0')
        info.SetLicense('')
        info.SetDevelopers(['GVR'])
        info.SetCopyright('(c) 2019')
        wx.adv.AboutBox(info)
    
if __name__=='__main__':
    app = wx.App()
    Frame = MyFrame1(None)
    Frame.Show()
    app.MainLoop()    


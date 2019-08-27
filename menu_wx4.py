# -*- coding: utf-8 -*-

import wx
import os
import manager
import re

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=None,title=title,size=(600,400))
        self.archivo='untitled.csv' # esta es la variable que almacena el nombre del fichero de trabajo por defecto

        # define el panel de la pventana principal y su sizer principal
#        p=wx.Panel(self, -1,size=wx.DefaultSize)
        mainSizer=wx.BoxSizer(wx.VERTICAL)
      
        # aqui se añade el widget para presentar la agenda
        sz1=wx.BoxSizer(wx.HORIZONTAL)
        self.listaPrincipal = wx.ListCtrl(self, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.listaPrincipal.InsertColumn(0, 'DNI', width=wx.LIST_AUTOSIZE)
        self.listaPrincipal.InsertColumn(1, 'Nombre', width=wx.LIST_AUTOSIZE)
        self.listaPrincipal.InsertColumn(2, 'Apellido', width=wx.LIST_AUTOSIZE)
        sz1.Add(self.listaPrincipal, 0, wx.ALL | wx.EXPAND, 5)        

        # botones de accion dentro de un sizer
        sz2=wx.GridSizer(1,4,0,0)
        self.bLista = wx.Button(self, label='Lista')
        self.bBusca = wx.Button(self, label='Busca')
        self.bAnnade = wx.Button(self, label='Añade')
        self.bBorra = wx.Button(self, label='Borra')
        sz2.Add(self.bLista, 0, wx.ALL | wx.SHAPED, 5)
        sz2.Add(self.bBusca, 0, wx.ALL | wx.SHAPED, 5)
        sz2.Add(self.bAnnade, 0, wx.ALL | wx.SHAPED, 5)
        sz2.Add(self.bBorra, 0, wx.ALL | wx.SHAPED, 5)

        # Eventos y acciones asociados a los botones
        self.bLista.Bind(wx.EVT_BUTTON, self.lista)
        self.bBusca.Bind(wx.EVT_BUTTON, self.busca)
        self.bAnnade.Bind(wx.EVT_BUTTON, self.annade)
        self.bBorra.Bind(wx.EVT_BUTTON, self.borra)

        # compone el sizer principal y lo aplica al panel
        mainSizer.Add(sz1)
        mainSizer.Add(sz2)
#        p.SetSizer(mainSizer)
        self.SetSizer(mainSizer)

        # Crea la barra de menu
        self.crearMenu()
        
        # Crea la status bar
        self.CreateStatusBar()
        self.SetStatusText("Gestor de agenda GUI")


    def crearMenu(self):
        """ Crea los diferentes menus """
        marchivo=wx.Menu()
        abrir=marchivo.Append(-1, "Abrir\tCtrl-O")
        guardar=marchivo.Append(-1, "Guardar\tCtrl-S")
        guardarComo=marchivo.Append(-1, "Guardar como...")
        marchivo.AppendSeparator()
        salir=marchivo.Append(-1, "Salir\tCtrl-Q")

        meditar=wx.Menu()
        copiar=meditar.Append(-1, "Copiar\tCtrl-C")
        pegar=meditar.Append(-1, "Pegar\tCtrl-V")

        macciones=wx.Menu()
        mLista=macciones.Append(-1, "Lista\tCtrl-L")
        mBusca=macciones.Append(-1, "Busca\tCtrl-B")
        mAnnade=macciones.Append(-1, "Añade\tCtrl-A")
        mBorra=macciones.Append(-1, "Borra\tCtrl-D")

        mayuda=wx.Menu()
        ayuda=mayuda.Append(-1, "Ayuda")
        acerca=mayuda.Append(-1, "Acerca de...")

        """ Crea la barra de menu con todos los elementos """
        barraMenu=wx.MenuBar()
        barraMenu.Append(marchivo, "Archivo")
        barraMenu.Append(meditar, "Editar")
        barraMenu.Append(macciones, "Acciones")
        barraMenu.Append(mayuda, "Ayuda")
        self.SetMenuBar(barraMenu)

        # Definición de "eventos" asociados a los diferentes elementos de la barra de menu
        self.Bind(wx.EVT_MENU, self.abrirArchivo, abrir)
        self.Bind(wx.EVT_MENU, self.guardarArchivoComo, guardarComo)
        self.Bind(wx.EVT_MENU, self.guardarArchivo, guardar)
        self.Bind(wx.EVT_MENU, self.salir, salir)
        
        self.Bind(wx.EVT_MENU, self.copiar, copiar)
        self.Bind(wx.EVT_MENU, self.pegar, pegar)

        self.Bind(wx.EVT_MENU, self.lista, mLista)
        self.Bind(wx.EVT_MENU, self.busca, mBusca)
        self.Bind(wx.EVT_MENU, self.annade, mAnnade)
        self.Bind(wx.EVT_MENU, self.borra, mBorra)

        self.Bind(wx.EVT_MENU, self.acerca, acerca)
        self.Bind(wx.EVT_MENU, self.ayuda, ayuda)

    """ 
        A partir de aqui la definicion de las acciones a ejecutar 
        sobre cada evento identificado en la definicion de la interfaz
    """
    
    def abrirArchivo(self, event):
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

    def guardarArchivoComo(self, event):
        """ Guarda el archivo actual abriendo un cuadro de dialogo """
        dlg=wx.FileDialog(self, "Guardar", os.getcwd(), style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.archivo=dlg.GetPath()
            manager.grabafichero(manager.agenda,self.archivo)
            self.SetTitle("Gestor de agenda 1.0  "+self.archivo)
        dlg.Destroy()

    def guardarArchivo(self,event):
        """ Guarda el archivo actual """
        if hasattr(self, 'archivo'):
            manager.grabafichero(manager.agenda,self.archivo)
            self.SetTitle("Gestor de agenda 1.0  "+self.archivo)
        else:
            self.guardarArchivoComo(None)
            
    def salir(self, event):
        self.Close(True)

    def copiar(self,event):
#        """ Copia el texto seleccionado al portapapeles """
#        texto=wx.TextDataObject(self.editor.GetStringSelection())
#        if wx.TheClipboard.Open():
#            wx.TheClipboard.SetData(texto)
#            wx.TheClipboard.Close()
        return

    def pegar(self,event):
#        """ Pega el texto ubicado en el portapapeles """
#        txt=wx.TextDataObject()
#        if wx.TheClipboard.Open():
#            success=wx.TheClipboard.GetData(txt)
#            wx.TheClipboard.Close()
#        if success:
#            self.editor.SetInsertionPoint(self.editor.GetInsertionPoint()) 
#            self.editor.write(txt.GetText())
        return

    def lista(self, event):
        self.SetStatusText("")
        self.listaPrincipal.DeleteAllItems()
        for entrada in manager.agenda.entradas:
            self.listaPrincipal.Append(entrada.listacontenido())
        return    

    def busca(self, event):
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

    def annade(self, event):
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

    def borra(self, event):
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

    def ayuda(self,event):
        wx.MessageBox("No disponible","Gestor de agenda")

    def acerca(self, event):
        descripcion=""" Gestor de agenda desarrollado en wxPython """
        info=wx.AboutDialogInfo()
        info.SetName('Gestor de agenda')
        info.SetDescription(descripcion)
        info.SetVersion('1.0')
        info.SetLicense('')
        info.SetDevelopers(['GVR'])
        info.SetCopyright('(c) 2019')
        wx.AboutBox(info)

if __name__=='__main__':
    app = wx.App()
    mainFrame = MainWindow(None, "Gestor de agenda 1.0")
    mainFrame.Show()
    app.MainLoop()
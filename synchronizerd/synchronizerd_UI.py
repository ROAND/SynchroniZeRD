# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SynchroniZeRD", pos = wx.DefaultPosition, size = wx.Size( 345,413 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 220,340 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		verticalMainSizer = wx.BoxSizer( wx.VERTICAL )
		
		synchronizeBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Synchronize" ), wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.off_picker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_DEFAULT_STYLE )
		fgSizer5.Add( self.off_picker, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.oft_picker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer5.Add( self.oft_picker, 0, wx.ALL, 5 )
		
		
		synchronizeBoxSizer.Add( fgSizer5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		verticalMainSizer.Add( synchronizeBoxSizer, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		statusBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )
		
		self.statusText = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		statusBoxSizer.Add( self.statusText, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		verticalMainSizer.Add( statusBoxSizer, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.synchronize_button = wx.Button( self, wx.ID_ANY, u"SynchroniZe!", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.synchronize_button.SetDefault() 
		verticalMainSizer.Add( self.synchronize_button, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( verticalMainSizer )
		self.Layout()
		self.mainMenuBar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.exit_menu_item = wx.MenuItem( self.file_menu, wx.ID_ANY, u"E&xit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.exit_menu_item )
		
		self.mainMenuBar.Append( self.file_menu, u"File" ) 
		
		self.help_menu = wx.Menu()
		self.about_menu_item = wx.MenuItem( self.help_menu, wx.ID_ANY, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.about_menu_item )
		
		self.mainMenuBar.Append( self.help_menu, u"&Help" ) 
		
		self.SetMenuBar( self.mainMenuBar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.off_picker.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_off_dir_changed )
		self.oft_picker.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_oft_dir_changed )
		self.synchronize_button.Bind( wx.EVT_BUTTON, self.synch_button_click )
		self.Bind( wx.EVT_MENU, self.on_exit_menu_selection, id = self.exit_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about_menu_selection, id = self.about_menu_item.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_off_dir_changed( self, event ):
		event.Skip()
	
	def on_oft_dir_changed( self, event ):
		event.Skip()
	
	def synch_button_click( self, event ):
		event.Skip()
	
	def on_exit_menu_selection( self, event ):
		event.Skip()
	
	def on_about_menu_selection( self, event ):
		event.Skip()
	


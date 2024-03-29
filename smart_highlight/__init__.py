# -*- encoding:utf-8 -*-


# __init__.py is part of smart-highlighting-Pluma.
#
#
# Copyright 2010-2012 swatch
#
# smart-highlighting-Pluma is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#



from gi.repository import GObject, Gtk, Pluma, Peas, PeasGtk

from .smart_highlight import SmartHighlightWindowHelper
from .config_ui import ConfigUI
#import config_manager

#class SmartHighlightingPlugin(GObject.Object, Pluma.WindowActivatable, PeasGtk.Configurable):
#class SmartHighlightingPlugin(GObject.Object, Peas.Activatable):
class SmartHighlightingPlugin(GObject.Object, Peas.Activatable, PeasGtk.Configurable):
	__gtype_name__ = "SmartHighlightingPlugin"
	#window = GObject.property(type=Pluma.Window)
	object = GObject.Property(type=GObject.Object)

	def __init__(self):
		GObject.Object.__init__(self)
		self.config_widget = None

	def do_activate(self):
		window=self.object
		self._plugin = SmartHighlightWindowHelper(self, window)

	def do_deactivate(self):
		self._plugin.deactivate()
		del self._plugin

	def do_update_state(self):
		self._plugin.update_ui()
		
	
	'''def do_create_configure_widget(self):
		#widget = Gtk.CheckButton("A configuration setting.")
		#widget.set_border_width(6)
		widget = ConfigUI(self.window, self.config).configWindow
		return widget
	'''
	
	def get_instance(self):
		return self._plugin, self.window


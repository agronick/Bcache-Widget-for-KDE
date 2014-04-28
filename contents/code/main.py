# -*- coding: iso-8859-1 -*-
#
# Author: Kyle Agronick <agronick@gmail.com>
# Date: Wed Apr 16 2014, 18:47:13
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation; either version 2, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU Library General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

# Import essential modules
from PyQt4.QtCore import *
from PyKDE4.kdecore import *
from PyKDE4 import plasmascript

import time
from BCStat import BCStat



class DEBCache(plasmascript.DataEngine):
    
    cItem = "";

    #   Constructor, forward initialization to its superclass
    #   Note: try to NOT modify this constructor; all the setup code
    #   should be placed in the init method.
    def __init__(self,parent,args=None):
        plasmascript.DataEngine.__init__(self,parent)

    #   init method
    #   Put here all the code needed to initialize our plasmoid
    def init(self):
        self.setMinimumPollingInterval(333)
        self.setPollingInterval(1000)
        self.files = {}; 
        self.files['../running'] = BCStat('Status', '../running');
        self.files['cache_hits'] = BCStat('Cache Hits', 'cache_hits');
        self.files['cache_misses'] = BCStat('Cache Misses', 'cache_misses');
        self.files['cache_hit_ratio'] = BCStat('Cache Hit Ratio', 'cache_hit_ratio');
        self.files['bypassed'] = BCStat('Bypassed Cache', 'bypassed');
        self.files['cache_bypass_hits'] = BCStat('Cache Bypass Hits', 'cache_bypass_hits');
        self.files['cache_bypass_misses'] = BCStat('Cache Bypass Misses', 'bypassed'); 
        
   
    
    #   sources method
    #   Used by applets to request what data source the DataEngine has
    def sources(self): 
        return BCStat.titleList;

    #   sourceRequestEvent method
    #   Called when an applet access the DataEngine and request for
    #   a specific source ( name )
    def sourceRequestEvent(self, name):  
        self.files[str(name)].refresh();
        return self.updateSourceEvent(name);

    #   updateSourceEvent method
    #   The main function for a DataEngine
    def updateSourceEvent(self, item): 
        self.setData(item, "Value", self.files[str(item)].last);
        self.setData(item, "Title", self.files[str(item)].title);
        return True;
    #   CreateDataEngine method
    #   Note: do NOT modify it, needed by Plasma
def CreateDataEngine(parent):
    return DEBCache(parent)

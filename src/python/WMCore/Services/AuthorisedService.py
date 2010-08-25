#!/usr/bin/env python
"""
_AuthorisedService_

An AuthorisedService is the same as a Service but sends a cert/key with the url
opener to access secured resources.
"""

__revision__ = "$Id: AuthorisedService.py,v 1.7 2009/07/11 08:34:27 metson Exp $"
__version__ = "$Revision: 1.7 $"

import datetime, os, urllib, time

from WMCore.WMException import WMException
from WMCore.WMExceptions import WMEXCEPTION
from WMCore.Services.Service import Service
from WMCore.Services.Requests import SecureRequests

class AuthorisedService(SecureRequests, Service):
    def __init__(self, dict={}):
        Service.__init__(self, dict)
        try:
            if not dict.has_key('key') or not dict.has_key('cert'):
                dict['key'], dict['cert'] = getKeyCert()
                
            self.setdefault("cert", dict['cert'])
            self.setdefault("key", dict['key'])
                
        except:
            self.logger.exception('Service requires a host certificate and key')
            raise WMException('Service requires a host certificate and key', 
                              "WMCORE-11")
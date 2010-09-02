#!/usr/bin/env python
"""
_BossLiteDBInterface_

"""



class BossLiteDBInterface(object):
    """
    _BossLiteDBInterface_
    
    This class is *strongly* specialized to use WMCore DB back-end
    """
    
    engine = None
    
    ##########################################################################

    def __init__(self):
        """
        __init__
        """
        
        
    ##########################################################################
    # Methods for DbObjects
    ##########################################################################
    
    def objExists(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError
    
    
    def objSave(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError
    
    
    def objCreate(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError   
        
    
    def objLoad(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError      
        
    
    def objUpdate(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError     
        
    
    def objRemove(self, obj):
        """
        put your description here...
        """
        
        raise NotImplementedError  

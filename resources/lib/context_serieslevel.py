# -*- coding: utf-8 -*-

'''
    script.skin.helper.service
    Contextmenu for go to the series level
'''

import xbmc
from utils import kodi_json, log_msg

#Kodi contextmenu item to go to the series level from a listing with episodes from multiple shows like in progress, recent etc.
if __name__ == '__main__':
    
    dbId = xbmc.getInfoLabel("ListItem.DBID")
    if not dbId or dbId == "-1":
        dbId = xbmc.getInfoLabel("ListItem.Property(DBID)")
        
    if dbId:
        log_msg("Context menu open series level for episodeId " + dbId,0)
        json_result = kodi_json('VideoLibrary.GetEpisodeDetails', { "episodeid": int(dbId), "properties": [ "tvshowid" ] })
        
        if json_result:
            path = "videodb://tvshows/titles/%s/" %str(json_result["tvshowid"])
            xbmc.executebuiltin("ActivateWindow(Videos,%s,return)" %path)
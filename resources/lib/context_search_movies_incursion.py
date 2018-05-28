# -*- coding: utf-8 -*-

'''
    script.skin.helper.service
    Contextmenu for movie search with incursion plugin
'''

import xbmc
from utils import kodi_json, log_msg

#Kodi contextmenu item to go to the series level from a listing with episodes from multiple shows like in progress, recent etc.
if __name__ == '__main__':
    
    dbId = xbmc.getInfoLabel("ListItem.DBID")
    if not dbId or dbId == "-1":
        dbId = xbmc.getInfoLabel("ListItem.Property(DBID)")
        
    if dbId:
        log_msg("Context menu search exodus for movieID " + dbId,0)
        json_result = kodi_json('VideoLibrary.GetMovieDetails', { "movieid": int(dbId), "properties": [ "title" ] })
        
        if json_result:
            title = "%s" %str(json_result["title"])
            title = title.replace(" ","%2B")
            #xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus",return)')
            #xbmc.sleep(5000)
            #xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=tvshowPage&url=http://api.trakt.tv/search/show?limit=20&page=1&query=%s",return)' %showtitle)
            exec_plugin = kodi_json("Addons.ExecuteAddon", { "addonid": "plugin.video.incursion", "params" : { "action": "moviePage", "url": "plugin://plugin.video.exodus/?action=moviePage&url=http%3A%2F%2Fapi.trakt.tv%2Fsearch%2Fmovie%3Flimit%3D20%26page%3D1%26query%3D"+title} })

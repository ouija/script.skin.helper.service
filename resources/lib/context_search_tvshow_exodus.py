# -*- coding: utf-8 -*-

'''
    script.skin.helper.service
    Contextmenu for tv show search with exodus plugin
'''

import xbmc
from utils import kodi_json, log_msg

if __name__ == '__main__':
    
    dbId = xbmc.getInfoLabel("ListItem.DBID")
    if not dbId or dbId == "-1":
        dbId = xbmc.getInfoLabel("ListItem.Property(DBID)")
        
    if dbId:
        log_msg("Context menu search exodus for episodeId " + dbId,0)
        json_result = kodi_json('VideoLibrary.GetEpisodeDetails', { "episodeid": int(dbId), "properties": [ "showtitle" ] })
        
        if json_result:
            showtitle = "%s" %str(json_result["showtitle"])
            showtitle = showtitle.replace(" ","%2B")
            #xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus",return)')
            #xbmc.sleep(5000)
            #xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=tvshowPage&url=http://api.trakt.tv/search/show?limit=20&page=1&query=%s",return)' %showtitle)
            exec_plugin = kodi_json("Addons.ExecuteAddon", { "addonid": "plugin.video.exodus", "params" : { "action": "tvshowPage", "url": "http%3A%2F%2Fapi.trakt.tv%2Fsearch%2Fshow%3Flimit%3D20%26page%3D1%26query%3D"+showtitle} })

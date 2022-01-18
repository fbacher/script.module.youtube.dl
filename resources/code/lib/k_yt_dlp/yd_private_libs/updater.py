# -*- coding: utf-8 -*-
import sys
from . import util

LATEST_URL = 'https://yt-dlp.org/latest/yt-dlp.tar.gz'
VERSION_URL = 'https://yt-dlp.org/latest/version'
PY3 = sys.version_info >= (3, 0)

def set_yt_dlp_importPath():
    return
    # if not util.getSetting('use_update_version',True): return
    import os
    from kodi_six import xbmc
    yt_dlp_path = os.path.join(util.PROFILE_PATH, 'yt-dlp')
    if not os.path.exists(yt_dlp_path):
        return


def saveVersion(version):
    from . import util
    util.setSetting('core_version', version)


def updateCore(force=False):
    if not force:
        return
    from kodi_six import xbmc
    from kodi_six import xbmcvfs
    try:
        from xbmcvfs import translatePath as xbmcTranslatePath
    except ImportError:
        from xbmc import translatePath as xbmcTranslatePath
    import os
    if PY3:
        from urllib.request import urlretrieve
    else:
        from urllib import urlretrieve
    import urllib2
    import tarfile

    util.LOG('Checking for new yt-dlp core version...')

    currentVersion = util.getSetting('core_version')
    try:
        newVersion = urllib2.urlopen(VERSION_URL).read().strip()
        if currentVersion == newVersion:
            util.LOG('Core version up to date')
            return False
    except Exception:
        util.ERROR()
        return False

    util.LOG('Updating yt-dlp core to new version: {0}'.format(newVersion))

    profile = xbmcTranslatePath(util.ADDON.getAddonInfo('profile')).decode('utf-8')
    archivePath = os.path.join(profile, 'yt-dlp.tar.gz')
    extractedPath = os.path.join(profile, 'yt-dlp')

    try:
        if os.path.exists(extractedPath):
            import shutil
            shutil.rmtree(extractedPath, ignore_errors=True)
            util.LOG('Old version removed')

        urlretrieve(LATEST_URL, filename=archivePath)
        with tarfile.open(archivePath, mode='r:gz') as tf:
            members = [m for m in tf.getmembers() if m.name.startswith('yt-dlp/yt-dlp')]  # get just the files from the yt-dlp source directory
            tf.extractall(path=profile, members=members)
    except Exception:
        util.ERROR('Core update FAILED')

    util.LOG('Core update complete')
    return True

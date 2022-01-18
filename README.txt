This addon originated from script.module.youtube-dl to provide the popular youtube-dl
tool for Kodi addons. However, with yt-dlp replacing youtube-dl, this
addon was created to make a clean break and to implement several minor, but
needed changes.  At this time no effort has been made to exploit any of the
newer capabilities of yt-dlp. Further, for the time being, the updater is
disabled. The updater allowed the yt-dlp code to be replaced independently
of the addon.

The only changes that an addon should need to make in order to replace
script.module.youtube.dl with script.module.yt-dlp are:
1) Change the addon dependency and version
2) Change the import path to library code:
   - A top-level directory has been added: 'k_ytdlp'
   - The youtube_dl directory is now the yt_dlp directory (due to the
     dependent code changing the paths).

Several items of interest to maintainers of this addon:
* To facilitate upgrading the yt-dlp to newer builds, the yt-dlp project is
a sub-module of this project and is attached/mounted at the top level
export directory. Instructions for copying the release and bumping the version
are in UPDATE_YT_DLP.sh.
* Several minor fixes made identified by Kodi code checker.

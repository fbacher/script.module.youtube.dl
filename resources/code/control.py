# -*- coding: utf-8 -*-

# Relative import to keep IDE happy. Could just import main, but then
# Kodi repo checker would be unhappy since it doesn't seem to know about
# addon.xml export of lib (or perhaps that was deemed bad style, which it
# may be).

from k_yt_dlp import main

main.main()

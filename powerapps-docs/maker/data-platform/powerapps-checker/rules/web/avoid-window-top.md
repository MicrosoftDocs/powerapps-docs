# `avoid-window-top`

Don't use `window.top` or `window.parent.parent`. Using either of these fields will likely result in cross-origin security errors when hosted outside of the primary web client. Develop an alternate approach.
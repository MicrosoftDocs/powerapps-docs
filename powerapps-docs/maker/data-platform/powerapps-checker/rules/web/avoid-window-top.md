# `avoid-window-top`

Do not use `window.top` or `window.parent.parent`. This will likely result in cross-origin security errors when hosted outside of the primary web client. Develop an alternate approach.
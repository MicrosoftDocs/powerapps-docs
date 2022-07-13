# `avoid-ui-refreshribbon`

Don't use `ui.refreshRibbon` during evaluation of ribbon rules. This API triggers duplicated network calls from ribbon and degrades performance. Use promises and asynchronous patterns.
# `avoid-ui-refreshribbon`

Do not use `ui.refreshRibbon` during evaluation of ribbon rules. This triggers duplicated network calls from ribbon and degrades performance. Use promises and asynchronous patterns.
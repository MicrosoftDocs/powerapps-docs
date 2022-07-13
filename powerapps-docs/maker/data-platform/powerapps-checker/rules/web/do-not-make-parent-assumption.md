# `do-not-make-parent-assumption`

Don't assume that the usage of `global.parent`, `window.parent`, `window.opener`, or `this.parent` from JavaScript web resources will result in the same context across versions or client types, for example mobile, tablet and browser. Consider a different approach when attempting to interact with one of these contexts.
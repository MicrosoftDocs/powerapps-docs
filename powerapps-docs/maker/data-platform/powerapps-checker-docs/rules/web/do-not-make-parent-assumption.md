# `do-not-make-parent-assumption`

Do not assume that the usage of `global.parent`, `window.parent`, `window.opener`, or `this.parent` from JavaScript web resources will result in the same context across versions as well as across client types, e.g. mobile, tablet and browser. Consider a different approach when attempting to interact with one of these contexts.
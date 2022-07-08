# `use-client-context`

Do not use `Xrm.Page`. Although `Xrm.Page` is deprecated, `parent.Xrm.Page` will continue to work in case of HTML web resources embedded in forms as this is the only way to access the form context from the HTML web resource. For a 
more comprehensive list of appropriate replacements for `Xrm.Page` functionality, see [Client API Deprecations](https://docs.microsoft.com/power-platform/important-changes-coming#some-client-apis-are-deprecated).
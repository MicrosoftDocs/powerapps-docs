# `use-org-setting`

Use organization settings. Specifically:
- Calls to `Xrm.Page.context.getIsAutoSaveEnabled()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.isAutoSaveEnabled`

- Calls to `Xrm.Page.context.getOrgLcid()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.languageId`

- Calls to `Xrm.Page.context.getOrgUniqueName()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.uniqueName`

## Recommendation

For more information, go to [Client API deprecations](/power-platform/important-changes-coming#some-client-apis-are-deprecated).

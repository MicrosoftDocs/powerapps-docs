# `use-getsecurityroleprivilegesinfo`

Avoid `userSettings.securityRolePrivileges`. This returns only privilege GUIDs which are difficult to work with. You might be making additional network calls to get further details about the privilege GUID and that degrades performance. Use [userSettings.getSecurityRolePrivilegesInfo()](https://docs.microsoft.com/power-apps/developer/model-driven-apps/clientapi/reference/xrm-utility/getglobalcontext/usersettings#getsecurityroleprivilegesinfo) instead which gives you more details about each security role privilege.

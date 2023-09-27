---
title: Control site creation in a tenant
description: Instructions to control portal creation in a tenant.
author: neerajnandwana-msft
ms.topic: conceptual
ms.custom: 
ms.date: 09/06/2023
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
    - sampatn
---

# Control site creation in a tenant

[!INCLUDE[cc-pages-banner](../../includes/cc-pages-banner.md)]

As a global administrator, if you want to disable site creation in a tenant by non-administrators, you can do it by enabling the `disablePortalsCreationByNonAdminUsers` tenant level setting through PowerShell. To run PowerShell cmdlets, you must first install the required modules. For information on installing the required PowerShell modules, see [Installation](/power-platform/admin/powerapps-powershell#installation).

After installing the modules, run the following command in a PowerShell window (run PowerShell as an administrator).

```
Set-TenantSettings -RequestBody @{ "disablePortalsCreationByNonAdminUsers" = $true }
```

Administrators are the users having one of the following Azure roles:

- [Global Administrator](admin/portal-admin-roles.md#global-administrator)
- [Dynamics 365 administrator](admin/portal-admin-roles.md#dynamics-365-administrator)
- [Power Platform admin](admin/portal-admin-roles.md#power-platform-administrator)

Users without these Azure roles are considered non-administrators.

When the site creation is disabled in a tenant, non-administrators see an error&mdash;`You don't have permissions to create a site in this environment. Choose another one or contact your administrator to request access.`

:::image type="content" source="media/site-creation-blocked-error.jpg" alt-text="A screenshot of Power Pages design studio displaying a message indicating that the user does not have permissions to create a site in the environment they've selected.":::

To enable site creation in a tenant, change the settings value from `$true` to `$false`.

```
Set-TenantSettings -RequestBody @{ "disablePortalsCreationByNonAdminUsers" = $false }
```

For more details about the required roles, and permissions to create a portal, go to [Required roles and permissions](admin/portal-admin-roles.md#required-roles-and-permissions).

## Next steps

[Manage a portal](manage-existing-portals.md)

### See also

[Create additional portals in an environment](create-additional-portals.md) <br>
[Administer Power Apps portals](/training/paths/administer-portals/) <br>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

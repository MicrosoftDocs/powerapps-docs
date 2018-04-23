---
title: PowerShell support | Microsoft Docs
description: Description of the different PowerShell cmdlets and a walkthrough of how to install and run them
services: powerapps
suite: powerapps
documentationcenter: na
author: jamesol-msft
manager: kfile
editor: ''
tags: ''
ms-topic: article

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 04/23/2018
ms.author: jamesol

---

# PowerShell support for PowerApps (preview)
With the preview launch of the PowerShell cmdlets for app creators and administrators, you can automate many of the monitoring and management tasks that are only possible manually today in [PowerApps](https://web.powerapps.com) or the [PowerApps Admin center](https://admin.powerapps.com).

## Installation
To run the PowerShell cmdlets for app makers, do the following:

1. Download the [PowerShell scripts file](https://go.microsoft.com/fwlink/?linkid=872358).

2. Unzip the file into a folder.

3. Open a PowerShell command window (as administrator) in that same folder.

4. Run the following one-time PowerShell command (this presumes you've never run PowerShell commands on the current machine):

    ```
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force
    ```

5. Import the necessary modules using the following commands:

    ```
    Import-Module .\Microsoft.PowerApps.Administration.PowerShell.psm1 -Force
    Import-Module .\Microsoft.PowerApps.PowerShell.psm1 -Force
    ```

6. Before accessing any of the commands, provide your credentials using the following command. These credentials are refreshed for up to ~8 hours before you're required to sign in again to continue using the cmdlets.

    ```
    Add-PowerAppsAccount
    ```

## PowerApps cmdlets for app makers (preview)

### Prerequisite
Users with a valid PowerApps license can perform the operations in these cmdlets, but they will only have access to the resources (for example, apps, flows, etc.) that have been created or shared with them.

### Cmdlet list
| Purpose | Cmdlet |
| --- | --- |
| Read environments | Get-PowerAppsEnvironment <br> Get-FlowEnvironment
| Read, update, and delete a canvas app | Get-App <br> Remove-App <br> Publish-App <br> Set-AppDisplayName <br> Get-AppVersion <br> Restore-AppVersion
| Read, update, and delete canvas app permissions | Get-AppRoleAssignment <br> Set-AppRoleAssignment <br> Remove-AppRoleAssignment
| Read, update, and delete a flow | Get-Flow <br> Get-FlowRun <br> Enable-Flow <br> Disable-Flow <br> Remove-Flow
| Read, update, and delete flow permissions | Get-FlowOwnerRole <br> Set-FlowOwnerRole <br> Remove-FlowOwnerRole
| Read and respond to flow approvals | Get-FlowApprovalRequest <br> Get-FlowApproval <br> RespondTo-FlowApprovalRequest
| Read and delete connections | Get-Connection <br> Remove-Connection
| Read, update, and delete connection permissions | Get-ConnectionRoleAssignment <br> Set-ConnectionRoleAssignment <br> Remove-ConnectionRoleAssignment
| Read and delete connectors | Get-Connector <br> Remove-Connector
| Read, update, and delete custom connector permissions | Get-ConnectorRoleAssignment <br> Set-ConnectorRoleAssignment <br> Remove-ConnectorRoleAssignment

> [!NOTE]
> Use the following commands to understand syntax and view samples for each of the cmdlets:
>```
>Get-Help Get-PowerAppsEnvironment
>Get-Help Get-PowerAppsEnvironment -Examples
>Get-Help Get-PowerAppsEnvironment -Detailed
>```

## PowerApps cmdlets for administrators (preview)

### Prerequisite
To perform the administration operations in the admin cmdlets, you'll need the following:

* A paid PowerApps Plan 2 license or a PowerApps Plan 2 trial license. You can sign-up for a 30-day trial license at [http://web.powerapps.com/trial](http://web.powerapps.com/trial). Trial licenses can be renewed if they've expired.

* [Office 365 Global Administrator](https://support.office.com/article/assign-admin-roles-in-office-365-for-business-eac4d046-1afd-4f1a-85fc-8219c79e1504) or [Azure Active Directory Global Administrator](https://docs.microsoft.com/azure/active-directory/active-directory-assign-admin-roles-azure-portal) permissions if you need to search through another user’s resources. (Note that Environment Admins only have access to those environments and environment resources for which they have permissions.)

### Cmdlet list
| Purpose | Cmdlets
| --- | ---
| Read and delete environments | Get-AdminEnvironment <br> Remove-AdminEnvironment
| Read, update, and delete environment permissions <br><br> *These cmdlets only work for environments that do not have a Common Data Service (CDS) for Apps database.* | Get-AdminEnvironmentRoleAssignment <br> Set-AdminEnvironmentRoleAssignment <br> Remove-AdminEnvironmentRoleAssignment
| Read and remove canvas apps | Get-AdminApp <br> Remove-AdminApp
| Read, update, and delete canvas app permissions | Get-AdminAppRoleAssignment <br> Remove-AdminAppRoleAssignment <br> Set-AdminAppRoleAssignment <br> Set-AdminAppOwner
| Read, update, and delete flows | Get-AdminFlow <br> Enable-AdminFlow <br> Disable-AdminFlow <br> Remove-AdminFlow  <br> Remove-AdminFlowOwnerRole

> [!NOTE]
> Use the following commands to understand syntax and view sample for each of the cmdlets:
>```
>Get-Help Get-AdminEnvironment
>Get-Help Get-AdminEnvironment -Examples
>Get-Help Get-AdminEnvironment -Detailed
>```

## Questions?

If you have any comments, suggestions, or questions, post them on the [Administering PowerApps community board](https://powerusers.microsoft.com/t5/Administering-PowerApps/bd-p/Admin_PowerApps).

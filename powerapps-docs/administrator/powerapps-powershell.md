---
title: PowerShell support (preview) | Microsoft Docs
description: Description of the different PowerShell cmdlets and a walkthrough of how to install and run them.
author: jamesol-msft
manager: kvivek
ms.service: powerapps
ms.component: pa-admin
ms.topic: reference
ms.date: 05/23/2018
ms.author: jamesol
---

# PowerShell support for PowerApps (preview)
With the preview launch of the PowerShell cmdlets for app creators and administrators, you can automate many of the monitoring and management tasks that are only possible manually today in [PowerApps](https://web.powerapps.com) or the [PowerApps Admin center](https://admin.powerapps.com).

## Installation
To run the PowerShell cmdlets for app creators, do the following:

1. Download the [PowerShell scripts file](https://go.microsoft.com/fwlink/?linkid=2006349).

2. Unzip the file into a folder.

3. Open a PowerShell command window (as administrator) in that same folder.

4. Run the following one-time PowerShell command (this presumes you've never run PowerShell commands on the current machine):

    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
    ```

5. Import the necessary modules using the following commands:

    ```
    Import-Module .\Microsoft.PowerApps.Administration.PowerShell.psm1 -Force
    Import-Module .\Microsoft.PowerApps.PowerShell.psm1 -Force
    ```

6.  There is a [known issue](https://powerusers.microsoft.com/t5/Administering-PowerApps/Getting-errors-when-I-try-to-import-the-preview-powerapps/td-p/109036) today that may also require you to manually unblock the PowerShell files using the following command:

    ```
    dir . | Unblock-File
    ```
7. Before accessing any of the commands, provide your credentials using the following command. These credentials are refreshed for up to ~8 hours before you're required to sign in again to continue using the cmdlets.

    ```
    # This call will open a prompt to collect the credentials (AAD account & password) that will be used by the commands
    Add-PowerAppsAccount
    ```

    ```
    # Here is how you can pass in credentials (avoiding opening a prompt)
    $pass = ConvertTo-SecureString "password" -AsPlainText -Force
    Add-PowerAppsAccount -Username foo@bar.com -Password $pass
    ```


## PowerApps cmdlets for app creators (preview)

### Prerequisite
Users with a valid PowerApps license can perform the operations in these cmdlets, but they will only have access to the resources (for example, apps, flows, etc.) that have been created or shared with them.

### Cmdlet list
> [!NOTE]
> We have updated some of the cmdlets function names in the latest release in order to add appropriate prefixes to prevent collisions. See the table below for an overview of what has changed.

| Purpose | Cmdlet |
| --- | --- |
| Read environments | Get-PowerAppEnvironment *(previously Get-PowerAppsEnvironment)* <br> Get-FlowEnvironment
| Read, update, and delete a canvas app | Get-App <br> Remove-App <br> Publish-App <br> Set-AppDisplayName <br> Get-AppVersion <br> Restore-AppVersion
| Read, update, and delete canvas app permissions | Get-PowerAppRoleAssignment *(previously Get-AppRoleAssignment)* <br> Set-PowerAppRoleAssignment *(previously Set-AppRoleAssignment)* <br> Remove-PowerAppRoleAssignment *(previously Remove-AppRoleAssignment)*
| Read, update, and delete a flow | Get-Flow <br> Get-FlowRun <br> Enable-Flow <br> Disable-Flow <br> Remove-Flow
| Read, update, and delete flow permissions | Get-FlowOwnerRole <br> Set-FlowOwnerRole <br> Remove-FlowOwnerRole
| Read and respond to flow approvals | Get-FlowApprovalRequest <br> Get-FlowApproval <br> RespondTo-FlowApprovalRequest
| Read and delete connections | Get-PowerAppConnection *(previously Get-Connection)* <br> Remove-PowerAppConnection *(previously Remove-Connection)*
| Read, update, and delete connection permissions | Get-PowerAppConnectionRoleAssignment *(previously Get-ConnectionRoleAssignment)* <br> Set-PowerAppConnectionRoleAssignment *(previously Set-ConnectionRoleAssignment)* <br> Remove-PowerAppConnectionRoleAssignment *(previously Remove-ConnectionRoleAssignment)*
| Read and delete connectors | Get-PowerAppConnector *(previously Get-Connector)* <br> Remove-PowerAppConnector *(previously Remove-Connector)*
| Read, update, and delete custom connector permissions | Get-PowerAppConnectorRoleAssignment *(previously Get-ConnectorRoleAssignment)* <br> Set-PowerAppConnectorRoleAssignment *(previously Set-ConnectorRoleAssignment)* <br> Remove-PowerAppConnectorRoleAssignment *(previously Remove-ConnectorRoleAssignment)*


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
> [!NOTE]
> We have updated some of the cmdlets function names in the latest release in order to add appropriate prefixes to prevent collisions. See the table below for an overview of what has changed.

| Purpose | Cmdlets
| --- | ---
| Read, update, and delete environments & Common Data Service for Apps databases | New-AdminPowerAppEnvironment **\*New\*** <br> Set-AdminPowerAppEnvironmentDisplayName **\*New\*** <br> Get-AdminPowerAppEnvironment *(previously Get-AdminEnvironment)* <br> Remove-AdminPowerAppEnvironment *(previously Remove-AdminEnvironment)* <br> New-AdminPowerAppCdsDatabase **\*New\*** <br> Get-AdminPowerAppCdsDatabaseLanguages **\*New\*** <br> Get-AdminPowerAppCdsDatabaseCurrencies **\*New\*** <br> Get-AdminPowerAppEnvironmentLocations **\*New\***
| Read, update, and delete environment permissions <br><br> *These cmdlets only work today for environments that do not have a Common Data Service (CDS) for Apps database.* | Get-AdminPowerAppEnvironmentRoleAssignment *(previously Get-AdminEnvironmentRoleAssignment)* <br> Set-AdminPowerAppEnvironmentRoleAssignment *(previously Set-AdminEnvironmentRoleAssignment)* <br> Remove-AdminPowerAppEnvironmentRoleAssignment *(previously Remove-AdminEnvironmentRoleAssignment)*
| Read, update, and remove canvas apps | Get-AdminPowerApp *(previously Get-AdminApp)* <br> Remove-AdminPowerApp *(previously Remove-AdminApp)* <br> Get-AdminPowerAppConnectionReferences **\*New\*** <br> Set-AdminPowerAppAsFeatured **\*New\*** <br> Clear-AdminPowerAppAsFeatured **\*New\*** <br> Set-AdminPowerAppAsHero **\*New\*** <br> Clear-AdminPowerAppAsHero **\*New\*** <br> Set-AdminPowerAppApisToBypassConsent **\*New\*** <br> Clear-AdminPowerAppApisToBypassConsent **\*New\***
| Read, update, and delete canvas app permissions | Get-AdminPowerAppRoleAssignment *(previously Get-AdminAppRoleAssignment)* <br> Remove-AdminPowerAppRoleAssignment *(previously Remove-AdminAppRoleAssignment)* <br> Set-AdminPowerAppRoleAssignment *(previously Set-AdminAppRoleAssignment)* <br> Set-AdminPowerAppOwner *(previously Set-AdminAppOwner)*
| Read, update, and delete flows | Get-AdminFlow <br> Enable-AdminFlow <br> Disable-AdminFlow <br> Remove-AdminFlow <br> Remove-AdminFlowApprovals **\*New\***
| Read, update, and delete flow permissions | Get-AdminFlowOwnerRole <br> Set-AdminFlowOwnerRole <br> Remove-AdminFlowOwnerRole
| Read and delete connections | Get-AdminPowerAppConnection *(previously Get-AdminConnection)* <br> Remove-AdminPowerAppConnection *(previously Remove-AdminConnection)*
| Read, update, and delete connection permissions | Get-AdminPowerAppConnectionRoleAssignment *(previously Get-AdminConnectionRoleAssignment)* <br> Set-AdminPowerAppEnvironmentConnectionRoleAssignment *(previously Set-AdminConnectionRoleAssignment)* <br> Remove-AdminPowerAppConnectionRoleAssignment *(previously Remove-AdminConnectionRoleAssignment)*
| Read and delete custom connectors | Get-AdminPowerAppConnector *(previously Get-AdminConnector)* <br> Remove-AdminPowerAppConnector *(previously Remove-AdminConnector)*
| Read, update, and delete custom connector permissions | Get-AdminPowerAppConnectorRoleAssignment *(previously Get-AdminConnectorRoleAssignment)*<br> Set-AdminPowerAppConnectorRoleAssignment *(previously Set-AdminConnectorRoleAssignment)* <br> Remove-AdminPowerAppConnectorRoleAssignment *(previously Remove-AdminConnectorRoleAssignment)*
| Read a user's PowerApps user settings, user-app settings, and notifications | Get-AdminPowerAppsUserDetails
| Read & delete a user's Microsoft Flow settings, which are not visible to user, but that support flow execution | Get-AdminFlowUserDetails <br> Remove-AdminFlowUserDetails
| Create, read, update & delete data loss prevention policies for your organization | Get-AdminDlpPolicy *(previously Get-AdminApiPolicy)* <br> Add-AdminDlpPolicy *(previously Add-AdminApiPolicy)* <br> Remove-AdminDlpPolicy *(previously Remove-AdminApiPolicy)* <br> Set-AdminDlpPolicy *(previously Set-AdminApiPolicy)* <br> Add-ConnectorToBusinessDataGroup <br>  Remove-ConnectorFromBusinessDataGroup

> [!NOTE]
> Use the following commands to understand syntax and view sample for each of the cmdlets:
>```
>Get-Help Get-AdminPowerAppEnvironment
>Get-Help Get-AdminPowerAppEnvironment -Examples
>Get-Help Get-AdminPowerAppEnvironment -Detailed
>```

## Questions?

If you have any comments, suggestions, or questions, post them on the [Administering PowerApps community board](https://powerusers.microsoft.com/t5/Administering-PowerApps/bd-p/Admin_PowerApps).

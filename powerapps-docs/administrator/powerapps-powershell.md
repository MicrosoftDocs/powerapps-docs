---
title: PowerShell support for PowerApps  | Microsoft Docs
description: PowerShell support for PowerApps
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
ms.date: 04/17/2018
ms.author: paulliew

---

# PowerShell support for PowerApps

## PowerApps Maker Cmdlets

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


## PowerApps Admin Cmdlets


'Get-AdminEnvironment', `
'Remove-AdminEnvironment', `

'Get-AdminEnvironmentRoleAssignment', `
'Set-AdminEnvironmentRoleAssignment', `
'Remove-AdminEnvironmentRoleAssignment', `

'Get-AdminApp', `
'Remove-AdminApp', `

'Get-AdminAppRoleAssignment', `
'Remove-AdminAppRoleAssignment', `
'Set-AdminAppRoleAssignment', `

'Set-AdminAppOwner', `
'Get-AdminFlow', `
'Enable-AdminFlow', `
'Disable-AdminFlow', `
'Remove-AdminFlow', `

'Set-AdminFlowOwnerRole', `
'Remove-AdminFlowOwnerRole', `
'Get-AdminFlowOwnerRole'

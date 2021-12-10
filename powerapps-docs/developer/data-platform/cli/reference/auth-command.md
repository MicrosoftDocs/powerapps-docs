---
title: Microsoft Power Platform CLI Auth command| Microsoft Docs
description: "Includes descriptions and supported parameters for the auth command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021
ms.service: "powerapps"
ms.topic: "article"
---

# Auth

Commands to [authenticate to Dataverse](../../../component-framework/import-custom-controls.md#connecting-to-your-environment).

## Parameters

|Parameter Name|Description|Example|
|-------------|-----------|-------|
|clear|Clears all the authentication profiles created on the local machine. This command has no arguments.| `pac auth clear`|
|create| Creates the authentication profile for your organization by passing the `url` parameter. Shows AAD dialog if sign in credentials are not specified, and has the following arguments:<ul><li> *name*: The name to give to this auth profile, maximum 12 characters (alias: -n). </li><li> *kind*: Kind of auth profile, defaults to Dataverse (alias: -k).</li><li> *url*: Resource URL to connect to (alias: -u).</li><li>  *username*: Optional: Username to authenticate with (alias: -un).</li><li> *password*: Optional: Password to authenticate with (alias: -p).</li><li> *applicationId*: Optional: Application ID to authenticate with (alias: -id).</li><li> *clientSecret*: Optional: Client secret to authenticate with (alias: -cs).</li><li> *tenant*: Optional: Tenant ID if using `app id` and `client secret` (alias: -t).</li><li>  *cloud*: Optional: Cloud instance to authenticate with. Values: Public, Tip1, Tip2, UsGov, UsGovHigh, UsGovDod (alias: -ci).</li></ul>|`pac auth create --url https://Myorg.crm.dynamics.com`|
|delete|Deletes the authentication profile created by passing  the `index` parameter.<br/>It has the following arguments:<ul><li> *index*: The index of the profile to be deleted (alias: -i).</li><li> *name*: The name of the profile to be deleted (alias: -n).</li></ul>|`pac auth delete --index 2`|
|list|Provides the list of authentication profiles stored on current computer. This command has no arguments.|`pac auth list`|
|select|Provides a way to switch between previously created authentication profiles by passing the `index` parameter.<br/>It has the following arguments:<ul><li> *index*: The index of the profile to be active (alias: -i).</li><li> *name*: The name of the profile to be active (alias: -n).</li></ul>|`pac auth select --index 2`|


### See also

[Power Apps component framework overview](../../../component-framework/overview.md)

[What is Microsoft Power Platform CLI](../../powerapps-cli.md)
---
title: Microsoft Power Platform CLI Application command| Microsoft Docs
description: "Includes descriptions and supported parameters for the auth command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021

ms.topic: "article"
---

# Application (Preview)

Commands to install AppSource Applications into your environment

## Parameters

|Parameter Name|Description|Example|
|-------------|-----------|-------|
|list| Lists all the Dataverse Applications available to install from AppSource <ul><li> *environment-id*: List the applications for a specific environment if not specified will list applications available for the tenant</li><li>*output*: Location of the JSON file to be created with the list of applications from Appsource (this is useful, if multiple applications need to be installed)</li></ul>| `pac application list --output c:\home\applicationslist.json`|
|install| Installs the application or applications to the given environment <ul><li> *environment-id*: Target environment where the application will be installed. </li><li> *application-name*: Unique name of the application to be installed</li><li> *application-list*: Location of the JSON file with the list of applications to be installed (application-name and application-list parameters should not be used together).</li></ul>|`pac application install --environment-id 9755b2cd-ce02-4e82-9d3f-9e61384c5382 --application-list c:\home\applicationslist.json `|
|


### See also

[Power Apps component framework overview](../../../component-framework/overview.md)

[What is Microsoft Power Platform CLI](../../powerapps-cli.md)
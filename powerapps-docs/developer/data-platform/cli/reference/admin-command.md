---
title: Microsoft Power Platform CLI Admin command| Microsoft Docs
description: "Includes descriptions and supported parameters for the admin command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021
ms.service: "powerapps"
ms.topic: "article"
---

# Admin

Commands to work with environment lifecycle features.

## Parameters

|Property Name|Description|
|-------------|-----------|
|list|Lists all environments from the tenant. It has the following parameters <ul><li>*environment-id*: List all environments that contain a given string in their ID (alias: -id).</li><li>*url*: List all environments that contain a given string in their URL (alias -u).</li><li>*type*: Lists all environments of the given type (alias: -t). </li><li>*name*: List all environments that contain a given string in their name (alias: -n). </li><li>*organization-id*: List all environments that contain a given string in their organization ID (alias: -oi).</li></ul> |
|create|Creates a new environment. It has the following parameters: <ul><li>*name*: Sets the name of the environment (alias: -n).</li><li>*region*: Sets the environment's region name. Defaults to `unitedstates` if not specified (alias -r).</li><li>*type*: Sets the type of the environment. Available values are Trial, Sandbox, Production, SubscriptionBasedTrial (alias: -t).</li><li>*currency*: Sets the default currency used in the environment. Defaults to USD if not specific (alias: -c).</li><li>*language*: Sets the default language of the environment. Defaults to English if not specified (alias: -l).</li><li>*templates*: Sets the Dynamics 365 apps that should be deployed to the environment. Pass as comma-separated values (alias: -t).</li><li>*domain*: Sets the domain name that's part of the environment URL. If the domain name is already in use, a numeric value will be appended to the domain name. For example, if `contoso` is already in use, the environment URL will become `https://contoso0.crm.dynamics.com` (alias -d).</li><li>*input-file*: Arguments can be passed in a `.json` input file instead of through the command line. For example, {"name" : "contoso"}. The arguments passed through the command line will take precedence over arguments from the `.json` input file (alias: -if).</li></ul> |
|backup|Takes the backup of an environment. It has the following parameters: <ul><li>*url*: URL of the environment to be backed up (alias: -u).</li><li>*label*: Sets the backup label as provided (alias: -l).</li><li>*environment-id*: ID of the environment to be backed up (alias: -id).</li><li>*notes*: Additional notes provided for the backup (alias: -n).</li></ul> |
|delete|Deletes an environment. It has the following parameters: <ul><li>*url*: URL of the environment to be deleted (alias: -u). </li><li>*environment-id*: ID of the environment to be deleted (alias: -id).</li></ul>|
|reset|Resets an environment. It has the following parameters: <ul><li>*url*: URL of the environment to reset (alias: -u)</li><li>*name*: Sets the name of the environment (alias: -n).</li><li>*currency*: Sets the default currency used in the environment. Defaults to USD if not specified (alias: -c)</li><li>*purpose*: Sets the description used to associate the environment with a specific intent (alias: -p) </li><li>*language*: Sets the default language of the environment. Defaults to English if not specified (alias: -l).</li><li>*templates*: Sets the Dynamics 365 apps that should be deployed to the environment. Pass as comma-separated values (alias: -t).</li><li>*domain*: Sets the domain name that's part of the environment URL. If the domain name is already in use, a numeric value will be appended to the domain name. For example, if `contoso` is already use, the environment URL will become `https://contoso0.crm.dynamics.com` (alias -d).</li><li>*input-file*: Arguments can be passed in a `.json` input file instead of through the command line. For example, {"name" : "contoso"}. The arguments passed through the command line will take precedence over arguments from the `.json` input file (alias: -if).</li></ul>|
|list-backups|Lists all available backups for the environment. It has the following parameters:<ul><li>*url*: URL of the environment for which you want to list backups (alias: -u).</li><li> *environment-id*: ID of the environment for which you want to list backups (alias: -id).</li></ul>|
|restore|Restores an environment from a given backup. It has the following parameters: <ul><li>*source-url*: URL of the source environment to be restored from (alias: -s). </li><li>*target-url*: URL of the target environment to be restored to (alias: -t). </li><li>*selected-backup*: DateTime of the backup in `mm/dd/yyyy hh:mm` format or latest (alias: -sb).</li><li>*name*: Optional name of the restored environment (alias: -n).</li></ul>|
|copy|Copies a source environment to a destination environment. It has the following parameters: <ul><li>*source-url*: URL of the source environment to be copied from (alias: -su).</li><li>*target-url*: URL of the target environment to be copied to (alias: -tu).</li><li>*source-environment-id*: ID of the source environment to be copied from (alias: -si).</li><li>*target-environment-id*: ID of the target environment to be copied to (alias: -ti). </li><li>*name*: Name to be used for the target environment (alias: -n).</li><li>*type*: Type of copy. Available values are: None, MinimalCopy, Fullcopy  (alias: -t).</li></ul>|

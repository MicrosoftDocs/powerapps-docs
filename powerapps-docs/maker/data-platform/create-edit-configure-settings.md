---
title: "Use settings to provide tailored app experiences | MicrosoftDocs"
description: "Use settings to provide tailored app experiences."
Keywords: settings, settings environment value, settings app value, model-driven app
author: aneesa
ms.subservice: dataverse-maker
ms.author: aneesa
ms.reviewer: matp
manager: kvivek
ms.date: 09/22/2021
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Settings overview 
Settings are solution components that enable makers and administrators to quickly configure and customize apps to provide a tailored experience. Settings can be used to enable or disable features or configure feature behavior for one specific app or all apps within an environment.

Settings are made up of three sub-components: Setting definition, setting environment value and setting app value.

| Sub-component | Description |
|:--------------|:-------------------------|
|**Setting definition** | A setting definition specifies the base properties of a settings like its name, description, data type and default value. |
|**Setting environment value** | Settting environment value is used to override the setting's default value for all apps in an environment. |
|**Setting app value** | Settting app value is used to override both the setting's default value and any setting environment value for a specific app. |

## Setting definition
A setting definition specifies the base properties of a settings. Some of these properties cannot be updated after the setting has been created.

| Property | Description |
|:--------------|:-------------------------|
|**Display name** | The name displayed to consumers of the setting in any framework generated UI. |
|**Name** | The unique name of the setting in an environment. Name is automatically generated based on the display name provided but can be changed before the settings is created. Once a setting is created the Name cannot be changed as it may be referenced in applications or code. <br> The Name has a prefix that maps to the solution (publisher)[create-solution.md#solution-publisher]. This prefix is intended to give your objects a unique name if you wish to import them into another environment in the future (which would have a different prefix). |
|**Description** | The description helps others understand what the setting is used for. |
|**Release level** | Rrelease level is used to inform the framework and other consumers of the setting about the state of the feature that the setting is used with. <br> It can be one of the two values: Generally Available or Preview. |
|**Overridable** | Overridable enables a setting’s default value to be overridden by an environment or an app. You cannot change overridable after a setting has been created. |
|**Data type** | The data type of a setting controls how the setting’s value is stored. Currently suppoYou cannot change the data type after a setting has been created. |
|**Default value** | The default value of the setting |

Settting environment value can be used to override the setting's default value for an environment. Setting environment value applies to all apps in that environment.
If a setting environment value exists for a setting, all apps in that environment will get that value instead of the setting's default value. If no setting environment value exists for a setting, all apps in that environment will get the setting's default value.

Settting app value can be used to override both the setting's default value as well as any setting environment value created for that setting in that environment. Setting app value applies only to one specific app. If a setting app value exists for a setting, that app will get that value instead of the setting's default value. If no setting app value exists for a setting, that app will get the setting's default value.

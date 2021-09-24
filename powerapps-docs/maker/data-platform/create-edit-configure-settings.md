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
|**Setting app value** | Settting app value is used to override the setting's default value and any setting environment value for a specific app. |

## Setting definition
A setting definition specifies the base properties of a settings. The full list of properties that can be configured on a setting definition are listed below. Some of these properties cannot be changed after the setting has been created.

| Property | Description |
|:--------------|:-------------------------|
|**Display name** | The name displayed to consumers of the setting in any framework generated UI. |
|**Name** | The unique name of the setting in an environment. Name is automatically generated based on the display name provided but can be changed before the settings is created. Once a setting is created the Name cannot be changed as it may be referenced in applications or code.<br> Name has a prefix that corresponds to the solution (publisher)[create-solution.md#solution-publisher]. This prefix is intended to give the setting a unique name if you wish to import them into another solution or environment in the future (which would have a different prefix). |
|**Description** | The description helps others understand what the setting is used for. |
|**Release level** | Release level is used to inform the framework and other consumers of the setting about the state of the feature that the setting is used with.<br> Release level can be set to Generally Available or Preview. |
|**Overridable** | Overridable enables a setting’s default value to be overridden by an environment (setting environment value) or an app (setting app value).<br> A setting that is Overridable can be further configured to enable the override behavior for app and environment, environment only or app only.<br> Overridable cannot be changed after the setting has been created. |
|**Data type** | The Data type of a setting controls how the setting’s value is stored. Data type can be set to Number, String or Yes/No. Data type cannot be changed after the setting has been created. |
|**Default value** | The default value specifies the setting's value that will be used until it is overridden by a setting environment value or a setting app value. |

### Creating a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. In the command bar, ensure you see **Solution preview on**. If you see **Solution preview off**, use the toggle to enable the preview.
1. From the list of solutions, open the solution you want to add the setting to.
1. In the command bar, select **New > More > Setting > Setting definition**.
1. In the **New Setting** dialog, provide values for each of the properties based on your requirements.
1. When you are done providing values for the properties, select **Save**.

### Updating a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. In the command bar, ensure you see **Solution preview on**. If you see **Solution preview off**, use the toggle to enable the preview.
1. From the list of solutions, open the solution you created the setting in.
1. In the tree view click on **Settings** or **Settings > Setting definitions**.
1. In the **Edit Setting** dialog, update values for any of the properties you want to change. Note that some properties cannot be updated after a setting has been created.
1. When you are done updating the values for the properties, select **Save**.

### Add existing setting

### Removing or deleting a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. In the command bar, ensure you see **Solution preview on**. If you see **Solution preview off**, use the toggle to enable the preview.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view click on **Settings** or **Settings > Setting definitions**.
1. Select the setting definition you wish to delete or remove.
1. In the command bar, select **Remove > Remove from this solution** or **Remove > Delete from this environment**.<br> **Remove from this solution** will remove the setting definition from the current solution but it will continue to be a part of the default solution or any other solutions it was added to.<br> **Delete from this environment** will delete the setting definition from the current environment and it will no longer be a part of any solutions in that environment.

## Setting environment value
Settting environment value is used to override the setting's default value for all apps in an environment.

## Setting app value
Settting app value is used to override the setting's default value and any setting environment value for a specific app.

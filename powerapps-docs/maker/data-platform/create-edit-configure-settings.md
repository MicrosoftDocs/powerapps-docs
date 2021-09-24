---
title: "Use settings to provide tailored app experiences | MicrosoftDocs"
description: "Use settings to provide tailored app experiences."
Keywords: settings, settings environment value, settings app value, model-driven app
author: aneesmsft
ms.subservice: dataverse-maker
ms.author: aneesmsft
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

> [!NOTE]
> To follow the steps listed below you need to have **Solution preview on**. When viewing the list of solutions, in the command bar, ensure you see **Solution preview on**. If you see **Solution preview off**, use the toggle to enable the preview.

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

### Adding a new setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting to.
1. In the command bar, select **New > More > Setting > Setting definition**.
1. In the **New setting** dialog, provide values for each of the properties based on your requirements.
1. When you are done providing values for the properties, select **Save**.

### Adding an existing setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting to.
1. In the command bar, select **Add existing > More > Setting**.
1. In the **Add existing setting definition** dialog, select one or more settings that you wish to add.
1. Select **Next**
1. In the **Selected setting definition** dialog, for each setting you have selected, you will have the option to **Include setting definition**. You can also **Include setting environment value** for each setting, if one exists. 
1. Select **Add** to add the setting definitions and/or setting environment values.

### Updating a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created the setting in.
1. In the tree view select **Settings > Setting definitions**.
1. Click on the setting definition that you wish to update.
1. In the **Edit setting** dialog, update values for any of the properties you want to change. Note that some properties cannot be updated after a setting has been created.
1. When you are done updating the values for the properties, select **Save**.

### Removing a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting definitions**.
1. Select the setting definition you wish to remove.
1. In the command bar, select **Remove > Remove from this solution**.<br> **Remove from this solution** will remove the setting definition from the current solution but it will continue to be a part of the default solution or any other solutions it was added to.

### Deleting a setting definition
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting definitions**.
1. Select the setting definition you wish to delete.
1. In the command bar, select **Remove > Delete from this environment**.<br> **Delete from this environment** will delete the setting definition from the current environment and it will no longer be a part of any solutions in that environment.

## Setting environment value
Settting environment value is used to override the setting's default value for all apps in an environment.

### Adding a new setting environment value
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting environment value to.
1. If the setting definition is available in the solution
   1. Click on the setting definition.
   1. In the **Edit setting value** dialog, in the **Setting environment value** section, select **New value**.
   1. Provide the value and select **Save**.
1. If the setting definition is not available in the solution
   1. In the command bar, select **New > More > Setting > Setting environment value**.
   1. Select the setting you wish to add the setting environment value for and select **Add**.
   1. In the **New setting environment value** dialog, in the **Setting environment value** section, select **New value**.
   1. Provide the value and select **Save**.

### Adding an existing setting environment value
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting environment value to.
1. If the setting definition is available in the solution
   1. Click on the setting definition.
   1. In the **Edit setting value** dialog, in the **Setting environment value** section, select **Add existing value**.
   1. Update the value if needed and select **Save**.
1. If the setting definition is not available in the solution
   1. In the command bar, select **Add existing > More > Setting**.
   1. In the **Add existing setting definition** dialog, select one or more settings that you wish to add setting environment values for.
   1. Select **Next**
   1. In the **Selected setting definition** dialog, for each setting you have selected, you will have the option to **Include setting environment value**, if one exists. You can also **Include setting definition** for each setting, if you want. 
   1. Select **Add** to add the setting environment values and/or setting definitions.

### Updating a setting environment value
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you added the settings environment value to.
1. In the tree view select **Settings > Setting environment values**.
1. Click on the setting environment value that you wish to update.
1. In the **Edit setting** dialog, in the **Setting environment value** section, update the value and select **Save**.

### Removing a setting environment value
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting environment values**.
1. Select the setting environment value you wish to remove.
1. In the command bar, select **Remove > Remove from this solution**.<br> **Remove from this solution** will remove the setting environment value from the current solution but it will continue to be a part of the default solution or any other solutions it was added to.

### Deleting a setting environment value
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting environment values**.
1. Select the setting definition you wish to delete.
1. In the command bar, select **Remove > Delete from this environment**.<br> **Delete from this environment** will delete the setting environment value from the current environment and it will no longer be a part of any solutions in that environment.

## Setting app value
Settting app value is used to override the setting's default value and any setting environment value for a specific app.

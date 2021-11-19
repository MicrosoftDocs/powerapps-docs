---
title: "Use settings to provide customized app experiences | MicrosoftDocs"
description: "Use settings to provide customized app experiences."
Keywords: settings, settings environment value, settings app value, model-driven app
author: aneesmsft
ms.subservice: dataverse-maker
ms.author: aneesa
ms.reviewer: matp
manager: kvivek
ms.date: 11/18/2021
ms.service: powerapps
ms.topic: how-to
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Use settings to provide customized app experiences

Settings are solution components that enable makers and administrators to quickly configure apps to provide a customized experience. Settings can be used to enable or disable features or configure feature behavior for a single app or all apps within an environment.

  > [!IMPORTANT]
  > - This is a preview feature and may not be available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

Settings are made up of three sub-components: Setting definition, setting environment value, and setting app value.

| Sub-component | Description |
|:--------------|:-------------------------|
|**Setting definition** | A setting definition specifies the base properties of a settings like its name, description, data type and default value. |
|**Setting environment value** | Setting environment value can be used to override the default value, as specified in the setting definition. A setting environment value applies to all apps in an environment. |
|**Setting app value** | Setting app value can be used to override the default value, as specified in the setting definition, and also the setting environment value (if one exists). A setting app value applies to a single app. |

> [!NOTE]
> To follow the steps listed below you need to have **Solution preview on**. From the **Solutions** area in Power Apps, on the command bar, ensure you have **Solution preview on**. If **Solution preview off** is displayed, select the option to enable the preview. More information: [Solution view](solutions-area.md)

## Setting definition

A setting definition specifies the base properties of a setting. The full list of properties that can be configured on a setting definition are listed below. Some of these properties can't be changed after the setting is created.

| Property | Description |
|:--------------|:-------------------------|
|**Display name** | The name displayed to consumers of the setting in all user interfaces where settings are displayed. |
|**Name** | The unique name of the setting in an environment.<br> Name is automatically generated based on the display name provided but can be changed before the setting is created. Once a setting is created the **Name** can't be changed as it may be referenced in applications or code.<br> **Name** has a prefix that corresponds to the solution [publisher](create-solution.md#solution-publisher). This prefix is intended to give the setting a unique name if you want to import them into another solution or environment in the future (which would have a different prefix). |
|**Description** | The description helps others understand what the setting is used for in all user interfaces where settings are displayed. |
|**Release level** | Release level is used to inform the framework and other consumers of the setting about the state of the feature that the setting is used with. Release level can be set to **Generally available** or **Preview**. |
|**Overridable** | Overridable enables a setting’s default value to be overridden by an environment (setting environment value) or an app (setting app value).<br> Overridable can't be changed after the setting is created. |
|**Value can be overridden for** | A setting that is overridable can be further configured to enable the override behavior.<ul><li>Environment and app, allows both the setting environment value and setting app values to override the default value.</li><li>Environment only, allows only the setting environment value to override the default value.</li><li>App only, allows only setting app values to override the default value.</li></ul>|
|**Data type** | The data type of a setting controls how the setting’s value is stored. Data type can be set to **Number**, **String**, or **Yes/No**. Data type can't be changed after the setting is created. |
|**Default value** | The default value specifies the setting's value that will be used unless it is overridden by a setting environment value or a setting app value. |

### Adding a new setting definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting to.
1. In the command bar, select **New > More > Setting > Setting definition**.
1. In the **New setting** dialog, provide values for each of the properties based on your requirements. For detailed information on setting definition properties please refer to: [Setting definition](#setting-definition)
1. When you are done providing values for the properties, select **Save**.

### Adding an existing setting definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting to.
1. In the command bar, select **Add existing > More > Setting**.
1. In the **Add existing setting definition** dialog, select one or more settings that you want to add.
1. When you are done selecting settings, select **Next**
1. In the **Selected setting definition** dialog, for each setting you have selected, you will have the option to **Include setting definition**. You can also **Include setting environment value** for each setting if one exists.
1. Select **Add** to add the setting definitions and/or setting environment values.

### Updating a setting definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created the setting in.
1. In the tree view select **Settings > Setting definitions**.
1. Select the setting definition that you want to update.
1. In the **Edit setting** dialog, update values for any of the properties you want to change. <br> Note that some properties can't be updated after a setting has been created. Additionally, in most cases you will not be able to update settings definitions that you don't own.
1. When you are done updating the values for the properties, select **Save**.

### Removing a setting definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting definitions**.
1. Select the setting definition you want to remove.
1. In the command bar, select **Remove > Remove from this solution**.<br> **Remove from this solution** removes the setting definition from the current solution, but it will continue to be a part of the default solution or any other solution it was added to.

### Deleting a setting definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting definitions**.
1. Select the setting definition you want to delete.
1. In the command bar, select **Remove > Delete from this environment**.<br> **Delete from this environment** deletes the setting definition from the current environment and it will no longer be a part of any solutions in that environment. Note that you can only delete setting definitions that you own.

## Setting environment value

Setting environment value is used to override the setting's default value for all apps in an environment. Use a setting environment value when the setting's default value is not what you want to be used for apps in your environment.

### Adding a new setting environment value

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting environment value to.
1. If the setting definition *is* available in the solution:
   1. Select the setting definition.
   1. In the **Edit setting value** dialog, in the **Setting environment value** section, select **New value**.
   1. Provide the value, and then select **Save**.
  
   If the setting definition *is not* available in the solution:
   1. On the command bar, select **New > More > Setting > Setting environment value**.
   1. Select the setting you want to add the setting environment value for, and then select **Add**.
   1. In the **New setting environment value** dialog, in the **Setting environment value** section, select **New value**.
   1. Provide the value, and then select **Save**.

### Adding an existing setting environment value

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting environment value to.
1. If the setting definition *is* available in the solution:
   1. Select the setting definition.
   1. In the **Edit setting value** dialog, in the **Setting environment value** section, select **Add existing value**.
   1. Update the value if needed, and then select **Save**.

   If the setting definition *is not* available in the solution:
   1. On the command bar, select **Add existing > More > Setting**.
   1. In the **Add existing setting definition** dialog, select one or more settings that you want to add setting environment values for.
   1. When you are done selecting settings, select **Next**
   1. In the **Selected setting definition** dialog, for each setting you have selected, you will have the option to **Include setting environment value**, if one exists. You can also **Include setting definition** for each setting if you want.
   1. Select **Add** to add the setting environment values and/or setting definitions.

### Updating a setting environment value

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you added the settings environment value to.
1. In the tree view select **Settings > Setting environment values**.
1. Select the setting environment value that you want to update.
1. In the **Edit setting** dialog, in the **Setting environment value** section, update the value, and then select **Save**.

### Removing a setting environment value

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting environment values**.
1. Select the setting environment value you want to remove.
1. On the command bar, select **Remove > Remove from this solution**.<br> **Remove from this solution** removes the setting environment value from the current solution but it will continue to be a part of the default solution or any other solution it was added to.

### Deleting a setting environment value

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you created or added the setting to.
1. In the tree view select **Settings > Setting environment values**.
1. Select the setting environment value you want to delete.
1. On the command bar, select **Remove > Delete from this environment**.<br> **Delete from this environment** deletes the setting environment value from the current environment and it will no longer be a part of any solutions in that environment.

## Setting app value

Setting app value is used to override the setting's default value and any setting environment value for a single app. Use a setting app value when the setting environment value is not what you want to be used for your app. If a setting environment value does not exist, use a setting app value when the setting's default value is not what you want to be used for your app.

> [!NOTE]
> To follow the steps listed below you need to use the new [app designer](../model-driven-apps/app-designer-overview.md). Currently the app designer only supports adding, updating, or deleting setting app values for Power Apps framework settings. Custom settings created by you will not appear in the app designer.

### Adding or updating a setting app value using the app designer

1. Open the app you want to add the setting app value for in the [app designer](../model-driven-apps/create-model-driven-app.md#create-an-app).
1. On the command bar, select **Settings**.
1. In the **Settings** dialog, select the **Features** or **Upcoming** tab.<br> The **Features** tab displays all settings that have release level set to **Generally available**. The **Upcoming** tab displays all settings that have release level set to **Preview**.
1. Add or update an app value for the setting you want.
1. Save and publish the app.

### Deleting a setting app value using the app designer

1. Open the app you want to remove the setting app value for in the [app designer](../model-driven-apps/create-model-driven-app.md#create-an-app).
1. On the command bar, select **Settings**.
1. In the **Settings** dialog, select the **Features** or **Upcoming** tab.
1. Select **Reset to environment value** next to the setting app value you want to delete. This makes the setting value fall back to the setting environment value if one exists. If no setting environment value exists, it will fallback to the setting's default value.<br> Note that the option to **Reset to environment value** is only displayed if a setting app value was previously added for that setting.
1. Save and publish the app.

### Adding or updating a setting app value using the solution explorer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to add the setting app value to.
1. If the setting definition or setting environment value is not available in the solution, add one of them. See [**Adding an existing setting definition**](create-edit-configure-settings.md#adding-an-existing-setting-definition) or [**Adding an existing setting environment value**](create-edit-configure-settings.md#adding-an-existing-setting-environment-value).
1. Select the setting definition or setting environment value.
1. In the **Edit setting value** dialog, in the **Setting app values** section, find the app that you want to add the setting app value for. Note that using the solution explorer you can only add setting app values for apps that are in the current solution.
1. Provide the value and select **Save**.
1. For the app setting value to take effect you will have to re-publish the app using the app designer or solution explorer.

### Deleting a setting app value using the solution explorer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Solutions**.
1. From the list of solutions, open the solution you want to delete the setting app value from.
1. If the setting definition or setting environment value is not available in the solution add one of them. More information: [Adding an existing setting definition](create-edit-configure-settings.md#adding-an-existing-setting-definition) or [Adding an existing setting environment value](create-edit-configure-settings.md#adding-an-existing-setting-environment-value).
1. Select the setting definition or setting environment value.
1. In the **Edit setting value** dialog, in the **Setting app values** section, find the app that you want to delete the setting app value for. Note that using the solution explorer you can only remove setting app values for apps that are in the current solution.
1. Select the ellipsis "***...***" next to the setting app value and then select **Reset to environment**.
1. Select **Save**.
1. For the deletion of the setting app value to take effect you will have to re-publish the app using the app designer or solution explorer.

## Getting or updating a setting value via code

### getCurrentAppSetting
Gets the value of a setting for the current app (app being used).

#### Parameters
| Name | Type | Required | Description |
|:--------------|:--------------|:--------------|:-------------------------|
|**settingName** | String | Yes | The name of the setting to get the value for. |

#### Return value
Type: Same as the type of the setting: Number, String, or Yes/No
Description: 
If the setting is overridable and 
Returns the setting app value. If a setting app value does not exist, then returns the setting environment value. If a setting environment value does not exist, then returns the default value as specified in the setting definition. Returns null if the setting name is incorrect or the setting could not be found.

### Add or update a setting value

## See also

[Solutions overview](solutions-overview.md)

[Overview of the model-driven app designer (preview)](../model-driven-apps/app-designer-overview.md)

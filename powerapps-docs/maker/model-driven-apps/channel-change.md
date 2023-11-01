---
title: Changing release channels for model-driven apps | MicrosoftDocs
description: Understand the release channels for Power Apps model-driven apps.
author: aorth
ms.service: powerapps
ms.subservice: mda-maker
ms.author: aorth
ms.reviewer: matp
ms.date: 08/24/2023
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
---
# Changing release channels for model-driven apps

The release channel affects the features that are shown to a user. When the monthly channel is enabled for an environment, makers need to validate that their customizations work with each monthly release. This article describes different approaches for a maker to change channels and validate an upcoming release..

## Flexible channel configuration

The release channel for model-driven apps can be changed in two primary ways.

- App channel (starting with build 23111)
- Environment channel

In addition, the release channel can be overriden with either of these options.

- User channel override (starting with build 23111)
- Browser session channel

> [!NOTE]
> - When the release channel is changed on the environment level, a user must refresh the browser tab twice to update the release channel information. The first refresh triggers a background update of feature configuration to a local cache. The second refresh uses the feature configuration local cache.
> - The browser session channel can be applied using a URL parameter, which is a temporary override.

## Changing the environment channel

The environment channel can be set using the Power Platform admin center or with code.

Power Platform admins can change the release channel using the environment's behavior settings. More information: [Manage behavior settings](/power-platform/admin/settings-behavior).

Developers can change the environment channel by updating the [ReleaseChannel](/power-apps/developer/data-platform/reference/entities/organization#BKMK_ReleaseChannel) column value for the row in the [Organization](/power-apps/developer/data-platform/reference/entities/organization) table. There's always a single row in the organization table.
More information:

* [Update a record using Web API](/power-apps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)
* [Update a record using the SDK for .NET](/power-apps/developer/data-platform/org-service/entity-operations-update-delete?tabs=late#basic-update)

## Changing the app channel

The app channel can be used to override the release channel for a model-driven app using Power Apps App Designer or Solution Explorer.

| Release Channel Name | Channel Value | Behavior |
| -- | -- | -- |
| Auto | 0 | App default value currently resolves to **Semi-annual** but will later change to **Monthly** at a future release wave |
| Monthly | 1 | App explicitly set to Monthly Channel |
| Semi-annual | 2 | App explicitly set to Semi-Annual Channel |

### Change app channel in App Designer

A maker can use App Designer to explicitly set the Release Channel for an app which overrides the environment channel.

1. Open https://make.powerapps.com/
1. Under **Solutions** open an existing solution containing the model-driven app
1. Open the app in the App Designer
1. Open **Settings** dialog
1. Under **General** tab expand **Advanced settings**
1. Use **App release channel** to change the app release value
1. Save and publish the app

### Change app channel in Solution Explorer

A maker can use Solution Explorer to explicitly set the Release Channel for multiple apps or all apps within the environment.

1. Open https://make.powerapps.com/
1. Under **Solutions** open an existing solution with one or more model-driven apps
1. Add the existing app setting "Allow new app channel default" into the solution
   1. Click Add existing > More > Setting
   1. Search for "app channel"
   1. Select the item "App channel"
   1. Click "Add"
1. To change the app channel for multiple apps
   1. Edit the setting "App channel"
   1. Find the app(s) under the section **Setting app values**
   1. Click **New app value** and enter the integer for the channel
   1. Click "Save"
1. To change the app channel for all apps in the environment
   1. Edit the setting "App channel"
   1. Find the app(s) under the section **Setting environment values**
   1. Click **New environment value** and enter the integer for the channel
   1. Click "Save"
1. After changing an app setting for a specific app(s), the app(s) must be republished to take affect

### Prevent new app defaulting to Monthly Channel

As part of the gradual migration to default all apps to use Monthly Channel, newly created model-driven apps will gradually start seeing the app channel defaulted. Admins or makers can control the release channel default for new apps using an app setting. The app setting "Allow new app channel default" defaults to **Yes** which means a newly created app will be set to **Monthly**. If the app setting is switched to **No**, new apps will be created with release channel **Auto**.

The following steps will change the default for all new apps within an environment. This app setting override can also be put into a solution which is migrated to all environments to prevent new apps from having a default set.

1. Open Solution Explorer to an existing or new solution
1. Add the existing app setting "Allow new app channel default" into the solution
   1. Click **Add existing** > **More** > **Setting**
   1. Search for "app channel default"
   1. Select the item "Allow new app channel default"
   1. Click "Add"
1. Edit the setting "Allow new app channel default"
   1. Click on "Allow new app channel default" in solution explorer
   1. Click **New environment value**
   1. Change environment value to **No**
   1. Click "Save"

## Changing the user channel

The user channel can be used to override both the environment channel and the app channel using the Power Platform admin center or with code.

Power Platform admins can change the release channel using the settings in the environment's user list. More information: [Manage user channel override](https://review.learn.microsoft.com/en-us/power-platform/admin/user-channel-override?branch=pr-en-us-7152).

Developers can change the user release channel by updating the [ReleaseChannel](/power-apps/developer/data-platform/reference/entities/usersettings#BKMK_ReleaseChannel) column value for the row in the [UserSettings](/power-apps/developer/data-platform/reference/entities/usersettings) table. The user channel can be programmatically updates with the same approach as the org channel.

## Changing the browser session channel

A single browser session can be changed by adding the URL parameter ```&channel=<channelname>```. This URL parameter is used for all navigation within the browser tab. It might not be copied to a new browser tab.

| Channel | URL parameter |
| --- | --- |
| Semi-annual | ```&channel=semiannual``` |
| Monthly | ```&channel=monthly``` |

When the channel is monthly, the monthly release can be changed using the URL parameter ```&channelrelease=<releasename>```. The release name format is the two digit year and two digit month, like *YYMM*. Additionally the next monthly release can be set using ```&channelrelease=next```.

| Monthly Release | Release Name Parameter |
| --- | --- |
| October 2023 | ```&channelrelease=2310``` |  
| November 2023 | ```&channelrelease=2311``` |  
| December 2023 | ```&channelrelease=2312``` |  
| January 2024 | ```&channelrelease=2401``` |  

> [!NOTE]
> Any valid ```YYMM``` release can be entered but future dates might not have any features defined.  

## Validating the next monthly release

Validation should be done for each monthly channel release before it's automatically enabled for users. Users can test when the validation build version has reached the environment.

1. Find the current monthly release a model-driven app by selecting **Settings** > **About**. The release version follows **Channel: Monthly** and is a date like *July 2023*.

1. Find the next monthly release short name by opening [Unified Interface monthly channel releases](/power-platform/released-versions/common-data-service/unified-interface-monthly-releases)

1. Add the URL parameter ```&channelrelease=next```. Alternative a specific release can be set with the URL parameter ```&channelrelease=`` with the next release short name like *2308*.

## Comparing features across channels and releases

When a user running the monthly channel report observes unexpected behavior, the following steps can help investigate where the behavior occurred.

- Check if the unexpected behavior exists in the semi-annual channel by using the URL parameter ```&channel=semiannual```. If the behavior also exists in the semi-annual channel, it's unrelated to the monthly channel and should follow normal support processes.
- Check if the unexpected behavior exists in the previous monthly release by using the URL parameter ```&channelrelease=``` with the prior release short name like *2308*. If the two monthly releases behave the same, then it's likely unrelated to a specific monthly channel release and should follow normal support processes.
- When a change is noticed between monthly releases, review the changed features in [Unified Interface monthly channel releases](/power-platform/released-versions/common-data-service/unified-interface-monthly-releases) to learn more.

## See also

[Release channel overview](channel-overview.md) <br />
[User About dialog - channel](../../user/about-dialog.md) <br />
[Power Platform admin center - Manage behavior settings](/power-platform/admin/settings-behavior)

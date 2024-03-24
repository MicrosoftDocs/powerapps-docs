---
title: Changing release channels for model-driven apps | MicrosoftDocs
description: Understand the release channels for Power Apps model-driven apps.
author: aorth
ms.service: powerapps
ms.subservice: mda-maker
ms.author: aorth
ms.reviewer: matp
ms.date: 11/07/2023
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
- sericks007
---
# Changing release channels for model-driven apps

The release channel affects the features that impact users. When the monthly channel is enabled for an environment, makers need to validate that their customizations work with each monthly release. This article describes different approaches for a maker to change channels and validate an upcoming release.

## Flexible channel configuration

The release channel for model-driven apps can be changed in two primary ways.

- App channel (starting with build 23111)
- Environment channel

In addition, the release channel can be overridden with either of these options.

- [User channel override](/power-platform/admin/user-channel-override) (starting with build 23111)
- Browser session channel

> [!NOTE]
> - When the release channel is changed on the environment level, a user must refresh the browser tab twice to update the release channel information. The first refresh triggers a background update of feature configuration to a local cache. The second refresh uses the feature configuration local cache.

## Changing the environment channel

The environment channel can be set using the Power Platform admin center or with code.

Power Platform admins can change the release channel using the environment's behavior settings. More information: [Manage behavior settings](/power-platform/admin/settings-behavior).

Developers can change the environment channel by updating the [ReleaseChannel](/power-apps/developer/data-platform/reference/entities/organization#BKMK_ReleaseChannel) column value for the row in the [Organization](/power-apps/developer/data-platform/reference/entities/organization) table. There's always a single row in the organization table.
More information:

* [Update a record using Web API](/power-apps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)
* [Update a record using the SDK for .NET](/power-apps/developer/data-platform/org-service/entity-operations-update-delete?tabs=late#basic-update)

## Changing the app channel

The app channel can be used to override the release channel for a model-driven app using Power Apps [app designer](model-driven-app-glossary.md#app-designer) or solutions area.

| App release channel | App setting value | Behavior |
|--|--|--|
| Auto | 0 | App default value is **Semi-annual**, but will later change to **Monthly** in a future release wave. |
| Monthly | 1 | App explicitly set to **Monthly Channel**. |
| Semi-annual | 2 | App explicitly set to **Semi-Annual Channel**. |

### Change app channel in app designer

A maker can use the app designer to explicitly set the release channel for an app, which overrides the environment channel.

1. Open https://make.powerapps.com/.
1. Under **Solutions** open an existing solution containing a model-driven app.
1. Open the app in the app designer.
1. Open **Settings** dialog.
1. Under the General tab, expand **Advanced settings**.
1. Use **App release channel** to change the app release value.
1. Save and publish the app.

### Change app channel in the solutions area

A maker can use the **Solutions** area to explicitly set the release channel for multiple apps or all apps within the environment.

1. Open https://make.powerapps.com/
1. Under **Solutions** open an existing solution with one or more model-driven apps:
1. Add the existing app setting **Allow new app channel default** into the solution:
   1. Select **Add existing** > **More** > **Setting**.
   1. Search for *app channel*.
   1. Select the item **App channel**.
   1. Select **Add**.
1. To change the app channel for multiple apps:
   1. Edit the setting **App channel**.
   1. Find the app(s) under the section **Setting app values**.
   1. Select **New app value** and then enter the integer for the channel.
   1. Select **Save**.
1. To change the app channel for all apps in the environment:
   1. Edit the setting **App channel**.
   1. Find the section **Setting environment values**.
   1. Select **New environment value** and then enter the integer for the channel.
   1. Select **Save**.
1. After changing an app setting for specific app(s), the app(s) must be republished for the change to take effect.

### Set the default for new apps to monthly channel

As part of the gradual migration to default all apps to use monthly channel, newly created model-driven apps will gradually start seeing the app channel defaulted. Admins or makers can control the release channel default for new apps using an app setting. The app setting **Allow new app channel default** defaults to **Yes**, which means a newly created app is set to **Monthly**.

### Prevent new app default to monthly channel

The new app default can be prevented by switching **Allow new app channel default** to **No**. This causes the new app to be created with release channel **Auto** value.

The following steps change the default for all new apps within an environment. This app setting override can also be put into a solution that's migrated to all environments to prevent new apps from having a default set.

1. Go to **Solutions** and open an existing or create a new solution.
1. Add the existing app setting **Allow new app channel default** into the solution:
   1. Select **Add existing** > **More** > **Setting**.
   1. Search for *app channel default*.
   1. Select the item **Allow new app channel default**.
   1. Select **Add**.
1. Edit the setting **Allow new app channel default**:
   1. Select **Allow new app channel default**.
   1. Select **New environment value**.
   1. Change the environment value to **No**.
   1. Select **Save**.

## Changing the user channel

The user channel can be used to override both the environment channel and the app channel using the Power Platform admin center or with code.

Power Platform admins can change the release channel using the settings in the environment's user list. More information: [Manage user channel override](/power-platform/admin/user-channel-override).

Developers can change the user release channel by updating the [ReleaseChannel](/power-apps/developer/data-platform/reference/entities/usersettings#BKMK_ReleaseChannel) column value for the row in the [UserSettings](/power-apps/developer/data-platform/reference/entities/usersettings) table. The user channel can be programmatically updated with the same approach as the environment channel.

## Changing the browser session channel

A single browser session can be changed by adding the URL parameter ```&channel=<channelname>``` as a temporary override. This URL parameter is used for all navigation within the browser tab. It might not be copied to a new browser tab.

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

Validation should be done for each monthly channel release before it's automatically enabled for users. Users can test when the validation build version reaches the environment.

The easiest way to validate is by appending ```&channelrelease=next``` that automatically sets the release channel to the next upcoming monthly release.

1. Find the current monthly release a model-driven app by selecting **Settings** > **About**. The release version follows **Channel: Monthly** and is a date like *July 2023*.

1. Append ```&channelrelease=next``` to the URL.

1. Repeat the first step to observe an updated release version.

To validate against a specific monthly release, the following steps can be used:

1. Find the current monthly release a model-driven app by selecting **Settings** > **About**. The release version follows **Channel: Monthly** and is a date like *July 2023*.

1. Find the monthly release short name by opening [Unified Interface monthly channel releases](/power-platform/released-versions/common-data-service/unified-interface-monthly-releases)

1. A specific release can be set with the URL parameter ```&channelrelease=`` with the next release short name like *2308*.

## Comparing features across channels and releases

When a user running the monthly channel observes unexpected behavior, the following steps can help investigate where the behavior occurred.

- Check if the unexpected behavior exists in the semi-annual channel by using the URL parameter ```&channel=semiannual```. If the behavior also exists in the semi-annual channel, it's unrelated to the monthly channel and should follow normal support processes.
- Check if the unexpected behavior exists in the previous monthly release by using the URL parameter ```&channelrelease=``` with the prior release short name like *2308*. If the two monthly releases behave the same, then it's likely unrelated to a specific monthly channel release and should follow normal support processes.
- When a change is noticed between monthly releases, review the changed features in [Unified Interface monthly channel releases](/power-platform/released-versions/common-data-service/unified-interface-monthly-releases) to learn more.

## See also

[Release channel overview](channel-overview.md) <br />
[User About dialog - channel](../../user/about-dialog.md) <br />
[Power Platform admin center - Manage behavior settings](/power-platform/admin/settings-behavior) <br />
[Power Platform admin center - Manage user channel override](/power-platform/admin/user-channel-override).

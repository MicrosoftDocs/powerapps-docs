---
title: "Release channel for your model-driven app | MicrosoftDocs" 
description: "This article outlines how release channels enable features within a model-driven app."
ms.custom: ""
ms.date: 9/04/2024
ms.reviewer: "matp"
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: overview
author: "aorth"
ms.author: "aorth"
search.audienceType: 
  - maker
---
# Release channels for your model-driven app

Microsoft provides new (and updated) features for your model-driven apps, regularly. You can control how often the users in your organization get these new features by specifying the release channel. The concept of multiple release channels originated from [Microsoft 365 channels](/deployoffice/updates/overview-update-channels) and provides Power Platform admins with a choice of how often end user impacting features are released.

The existing cadence of twice-yearly release waves is called the *Semi-annual channel* and is currently the default for all existing apps and environments. The new *monthly channel* option enables GA-ready features to be turned on each month with a four week preview notification period to allow customer validation with existing customizations.

The following table provides a comparison of monthly channel and semi-annual channel.

| Category | Monthly channel | Semi-annual channel |
| --- | --- | --- |
| Recommended use | Provide your users with new end user impacting features only once a month and on a predictable schedule. | For users in your organization where more training and extensive testing are needed before rollout out of new end user impacting features. | 
| Release frequency | Once a month, on the first release for the month and following the gradual weekly rollout. | Twice a year, starting early April and early October and following the gradual weekly rollout. |

Security and non-end user impacting changes continue to be delivered with the weekly releases and changes outlined in [Microsoft Unified Interface versions](/power-platform/released-versions/powerapps#all--microsoft-unified-interface-versions).

The key idea is that GA-ready end user impacting features release monthly instead of waiting for the twice-yearly release cadence. The same number of features are delivered in 12 smaller releases instead of two larger releases.

Microsoft 365 products experience consistently higher user satisfaction for monthly channel compared to the semi-annual channel. Currently, we observe a user satisfaction drop with the twice-yearly releases, and we're looking to improve this experience by following the Microsoft 365 channel approach.

## Configuring release channel

Release channel can be configured on the environment, app, or user level. The release channel is primarily managed on the environment or app. The user level is an override, which can be used for gradual rollout or to revert specific users.

Environment admins use the Power Platform admin center to select the channel for the environment. Makers use app designer or the solutions area to select the channel for one or more apps.

To allow gradually switching the default from semi-annual channel to monthly channel, the default value for both environment release channel and app release channel were renamed to **Auto**. There's an explicit choice for **Semi-annual** and **Monthly**. More information: [Changing release channels](channel-change.md).

With 2024 release wave 1, the Power Platform environments were changed to treat **Auto** app release channel as **Monthly** and newly created model-driven apps default to **Monthly**. With 2024 release wave 2, the Dynamics 365 environments are changing to treat **Auto** app release channel as **Monthly**. Admins and makers can select **Semi-annual** if they need the slower cadence. More information: [Keeping semi-annual release channel](channel-change.md#keeping-semi-annual-release-channel).

## Monthly release schedule

Model-driven apps release updates every week, which is gradually rolled out to groups of regions over several weeks. These are the region groups with each group happening in successive weekend updates.

1. First release environment (FRE)
1. Canada, South America, India, France, South Africa, Germany, Switzerland, Norway, Korea, Singapore
1. United Arab Emirates, Japan, Asia Pacific, Great Britain, Australia
1. Europe
1. United States

The monthly release is the first weekly release of each month. The release typically matches ```YYMM.1``` where ```YY``` is the release year and ```MM``` is the release month. The monthly release notes are published to [Released versions for Power Apps](/power-platform/released-versions/powerapps) four weeks before the release reaches the region group 2. Region group 2 is used because it's the first region group for production customer environments and region group 1 is used for customer early validation.

| Monthly release | Doc published | Feature release | Group 1 | Group 2 | Group 3 | Group 4 | Group 5 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Aug 2024 | Jul 19 | 2408.2 | Aug 16 | Aug 23 | Aug 30 | Sep 6 | Sep 13
| Sep 2024 | Aug 16 | 2409.1 | Sep 6 | Sep 13 | Sep 20 | Sep 27 | Oct 4
| Oct 2024 | Sep 20 | 2410.1 | Oct 11 | Oct 18 | Oct 25 | Nov 1 | Nov 8
| Nov 2024 | Oct 18 | 2411.1 | Nov 8 | Nov 15 | Nov 22 | Dec 6 | Dec 13 
| Dec 2024 | Nov 15 | 2412.2 | Dec 13 | Dec 20 | Jan 10 | Jan 17 | Jan 24

## See also

[Changing release channels](channel-change.md) <br />
[User about dialog - channel](../../user/about-dialog.md) <br />
[Power Platform admin center - Environment behavior settings](/power-platform/admin/settings-behavior) <br />
[Power Platform admin center - User settings](/power-platform/admin/users-settings)

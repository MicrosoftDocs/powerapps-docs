---
title: "Release Channel for your model-driven app | MicrosoftDocs" 
description: "This article outlines how release channels enable features within a model driven app."
ms.custom: ""
ms.date: 06/27/2023
ms.reviewer: ""
ms.subservice: mda-maker
ms.topic: "article"
author: "aorth"
ms.author: "matp"
search.audienceType: 
  - maker
---

# Release Channels for your model driven app

The concept of multiple release channels comes from [Microsoft 365 channels](https://learn.microsoft.com/deployoffice/updates/overview-update-channels) and provides customer admins with a choice of how often end user impacting features are released.

The default channel is the Semi-annual channel, which is the twice yearly release wave features. 

The following table provides a comparison of **Monthly Channel** and **Semi-Annual Channel**.

| Category | Monthly Channel | Semi-Annual Channel |
| --- | --- | --- |
| Recommended use | Provide your users with new end user impacting features only once a month and on a predictable schedule. | For users in your organization where more training and extensive testing are needed before rollout out new end user impacting features. | 
| Release frequency | Once a month, on the first release for the month and following the weekly station rollout | Twice a year, starting early April and early October and following the weekly station rollout |

Security and non-end user impacting changes continue to be delivered with the weekly releases and changes outlined in [Unified Interface Weekly Release Notes](/power-platform/released-versions/powerapps#all--microsoft-unified-interface-versions).

Environment admins use the Power Platform Admin Center to select the channel for the org. The existing cadence of twice-yearly release waves is called the "Semi-Annual channel" and is the default for all existing orgs. The new "Monthly channel" option enables GA-ready features to be turned on each month with a four week preview/notification period to allow customer validation with existing customizations.

The key idea is that GA-ready end user impacting features release monthly instead of waiting for the twice-yearly release cadence. The same number of features are delivered in 12 smaller releases instead of two larger releases.

The Microsoft 365 products have seen a consistently higher user satisfaction for monthly channel compared to semi-annual channel. Currently we see user satisfaction drop with the twice-yearly releases, and we're looking to improve this experience by following the Microsoft 365 channel approach.

## Monthly release schedule

The monthly release is the first weekly release of each month. The release would match ```YYMM.1``` where ```YY``` is the release year and ```MM``` is the release month. The monthly release notes are published to [Released versions for Power Apps](/power-platform/released-versions/powerapps) four weeks before the release reaches stations 2. Station 2 is used because it's the first production stations for customer orgs and Station 1 is used for customer early validation.

| Monthly Release | Doc Published | Feature Release | Station 1 | Station 2 | Station 3 | Station 4 | Station 5 | Station 6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| May 2023 | Apr 14 | 2305.1 | May 5 | May 12 | May 19 | May 26 | Jun 2 | Jun 9 |
| June 2023 |  May 12 | 2306.1 | Jun 9 | Jun 16 | Jun 23 | Jun 30 | Jul 7 | Jul 14 |
| July 2023 | Jun 16 | 2307.1 | Jul 7 | Jul 14 | Jul 21 | Jul 28 | Aug 4 | Aug 11 |
| August 2023 | Jul 14 | 2308.1 | Aug 11 | Aug 18 | Aug 25 | Sep 1 | Sep 8 | Sep 15 |

## Related links

* [Changing Release Channels](channel-change.md)
* [User About Dialog - Channel](../../user/about-dialog.md)
* [Power Platform Admin Center - Manage behavior settings](/power-platform/admin/settings-behavior)
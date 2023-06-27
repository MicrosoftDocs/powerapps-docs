---
title: "Release channel for your model-driven app | MicrosoftDocs" 
description: "This article outlines how release channels enable features within a model-driven app."
ms.custom: ""
ms.date: 06/27/2023
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

Microsoft provides new (and updated) features for your model-driven apps, on a regular basis. You can control how often the users in your organization get these new features by specifying the release channel. The concept of multiple release channels originated from [Microsoft 365 channels](/deployoffice/updates/overview-update-channels) and provides Power Platform admins with a choice of how often end user impacting features are released.

Environment admins use the Power Platform admin center to select the channel for the environment. The existing cadence of twice-yearly release waves is called the *Semi-annual channel* and is the default for all existing orgs. The new *monthly channel* option enables GA-ready features to be turned on each month with a four week preview notification period to allow customer validation with existing customizations.

The following table provides a comparison of monthly channel and semi-annual channel.

| Category | Monthly channel | Semi-annual channel |
| --- | --- | --- |
| Recommended use | Provide your users with new end user impacting features only once a month and on a predictable schedule. | For users in your organization where more training and extensive testing are needed before rollout out of new end user impacting features. | 
| Release frequency | Once a month, on the first release for the month and following the gradual weekly rollout. | Twice a year, starting early April and early October and following the gradual weekly rollout. |

Security and non-end user impacting changes continue to be delivered with the weekly releases and changes outlined in [Microsoft Unified Interface versions](/power-platform/released-versions/powerapps#all--microsoft-unified-interface-versions).

The key idea is that GA-ready end user impacting features release monthly instead of waiting for the twice-yearly release cadence. The same number of features are delivered in twelve smaller releases instead of two larger releases.

Microsoft 365 products have seen a consistently higher user satisfaction for monthly channel compared to the semi-annual channel. Currently, we observe a user satisfaction drop with the twice-yearly releases, and we're looking to improve this experience by following the Microsoft 365 channel approach.

## Monthly release schedule

Model-driven apps release updates every week, which are gradually rolled out to groups of regions over several weeks. Below are the region groups with each group happening in successive weekend updates.

1. First release environment (FRE)
1. Canada, South America, India, France, South Africa, Germany, Switzerland, Norway, Korea, Singapore
1. United Arab Emirates, Japan, Asia Pacific, Great Britain, Australia
1. Europe
1. United States

The monthly release is the first weekly release of each month. The release matches ```YYMM.1``` where ```YY``` is the release year and ```MM``` is the release month. The monthly release notes are published to [Released versions for Power Apps](/power-platform/released-versions/powerapps) four weeks before the release reaches the region group 2. Region group 2 is used because it's the first region group for production customer environments and region group 1 is used for customer early validation.

| Monthly release | Doc published | Feature release | Group 1 | Group 2 | Group 3 | Group 4 | Group 5 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| May 2023 | Apr 14 | 2305.1 | May 5 | May 12 | May 19 | May 26 | Jun 2 |
| June 2023 |  May 19 | 2306.1 | Jun 9 | Jun 16 | Jun 23 | Jun 30 | Jul 7 |
| July 2023 | Jun 16 | 2307.1 | Jul 7 | Jul 14 | Jul 21 | Jul 28 | Aug 4 |
| August 2023 | Jul 21 | 2308.1 | Aug 11 | Aug 18 | Aug 25 | Sep 1 | Sep 8 |
| September 2023 | Aug 18 | 2309.1 | Sep 8 | Sep 15 | Sep 22 | Sep 29 | Oct 6 |

## See also

[Changing release channels](channel-change.md) <br />
[User about dialog - channel](../../user/about-dialog.md) <br />
[Power Platform admin center - Manage behavior settings](/power-platform/admin/settings-behavior)
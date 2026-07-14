---
title: "Release channel for your model-driven app" 
description: "This article outlines how release channels enable features within a Power Apps model-driven app."
ms.custom: ""
ms.date: 07/12/2026
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

Microsoft regularly provides new and updated features for your model-driven apps. You can control how often the users in your organization get these new features by specifying the release channel. The concept of multiple release channels originated from [Microsoft 365 channels](/deployoffice/updates/overview-update-channels) and provides Power Platform admins with a choice of how often end user impacting features are released.

The twice-yearly release waves are delivered through the *semi-annual channel*, which is currently the default for all apps and environments. The *monthly channel* option enables generally available (GA) ready features to be turned on each month, with a one-week advance notification period so admins can validate new features against their customizations before they're enabled. Both channels deliver the same GA features - neither channel is a preview or early access program.

> [!NOTE]
> A release *channel* isn't the same as a release *wave*. A release wave (for example, 2025 wave 1) is the six-month period used to plan, document, and deliver a set of features, published in the [Dynamics 365](/dynamics365/release-plan/) and [Power Platform](/power-platform/release-plan/) release plans. A release channel is the cadence that turns GA features on in your environment: the semi-annual channel enables features twice a year (early April and early October), aligned with the release waves, while the monthly channel enables those same GA features each month.

This table provides a comparison of monthly channel and semi-annual channel.

| Category | Monthly channel | Semi-annual channel |
| --- | --- | --- |
| Recommended use | Provide your users with new end user impacting features only once a month and on a predictable schedule. | For users in your organization where more training and extensive testing are needed before rollout out of new end user impacting features. | 
| Release frequency | Once a month, on the first release for the month and following the gradual weekly rollout. | Twice a year, starting early April and early October and following the gradual weekly rollout. |

Security and non-end user impacting changes continue to be delivered with the weekly releases and changes outlined in [Microsoft Unified Interface versions](/power-platform/released-versions/powerapps#all--microsoft-unified-interface-versions).

The key idea is that GA-ready end user impacting features release monthly instead of waiting for the twice-yearly release cadence. The same number of features are delivered in 12 smaller releases instead of two larger releases.

Microsoft 365 products experience consistently higher user satisfaction for monthly channel compared to the semi-annual channel. Currently, we observe a user satisfaction drop with the twice-yearly releases, and we're looking to improve this experience by following the Microsoft 365 channel approach.

## How monthly and semi-annual channels relate

The monthly channel is cumulative. It includes everything from the most recent semi-annual release, plus the generally available features that each month turns on.

Most features appear in the monthly channel first and are later included in a semi-annual release, but the two channels aren't strictly sequential:

- A feature in the monthly channel might not be included in the *next* semi-annual release. For example, the feature might need more validation time or additional changes before it's turned on for semi-annual environments.
- Some changes go directly into a semi-annual release without first appearing in a monthly release.

As a result, the monthly channel isn't a preview of everything in the next semi-annual release, and not every semi-annual feature was in a monthly release first.

## Configuring release channel

Release channel can be configured on the environment, app, or user level. The release channel is primarily managed on the environment or app. The user level is an override, which can be used for gradual rollout or to revert specific users.

Environment admins use the Power Platform admin center to select the channel for the environment. Makers use app designer or the solutions area to select the channel for one or more apps.

To allow gradually switching the default from semi-annual channel to monthly channel, the default value for both environment release channel and app release channel were renamed to **Auto**. There's an explicit choice for **Semi-annual** and **Monthly**. More information: [Changing release channels](channel-change.md).

With 2024 release wave 1, the Power Platform environments were changed to treat **Auto** app release channel as **Monthly** and newly created model-driven apps default to **Monthly**. With 2024 release wave 2, the Dynamics 365 environments changed to treat **Auto** app release channel as **Monthly**. Admins and makers can select **Semi-annual** if they need the slower cadence. More information: [Keeping semi-annual release channel](channel-change.md#keep-semi-annual-release-channel).

## Monthly release schedule

Model-driven apps release updates every week. Each update is gradually rolled out to regions over several weeks, starting with the **first release** region for early validation and then reaching production regions in groups on successive weekends. To see the list of regions, their rollout order, and the weekend each region group updates, see [General availability deployment](/power-platform/admin/general-availability-deployment).

The monthly release is the first weekly release of each month. The release typically matches `YYMM.1`, where `YY` is the release year and `MM` is the release month. Notifications of upcoming monthly and semi-annual channel changes are published in the release plans for [Dynamics 365](/dynamics365/release-plan/) and [Power Platform](/power-platform/release-plan/) approximately one week before the release reaches the first production regions.

Because each region group updates on the following weekend, the release reaches all regions over roughly five weeks. The exact calendar dates change each month, but the relative sequence stays the same:

| Stage | Approximate timing |
| --- | --- |
| Release planner notification | ~1 week before production rollout |
| Early validation (first release region) | First weekend |
| Production rollout begins | +1 weekend |
| Remaining region groups | +2 to +4 weekends |

## Semi-annual release schedule

Through the semi-annual channel, the generally available features planned in each Dynamics 365 and Power Platform release wave are turned on twice a year, in early April and early October:

| Release wave | Rollout begins | Production build |
| --- | --- | --- |
| Wave 1 | Early April | `YY03.3` (for example, `2603.3`) |
| Wave 2 | Early October | `YY09.3` (for example, `2609.3`) |

Like the monthly channel, each semi-annual release follows the gradual weekly rollout across the same [region groups](#monthly-release-schedule), starting with the first release region and reaching each subsequent region group on the following weekend. The features included in a wave are planned and documented in the [Dynamics 365](/dynamics365/release-plan/) and [Power Platform](/power-platform/release-plan/) release plans.

## When features become available

For both the monthly and semi-annual channels, an environment gets new features when it receives the weekly build that contains those features. Builds are named `YYMM.W`, where `YY` is the year, `MM` is the month, and `W` is the weekly release within that month (for example, `2603.3`). Because builds roll out to the [region groups](#monthly-release-schedule) over successive weekends, the date an environment receives a given build depends on its region group.

To see the current build for a model-driven app, open the **Settings** menu and select **About**. For more information, see [User about dialog](../../user/about-dialog.md).

## See also

[Changing release channels](channel-change.md) <br />
[User about dialog - channel](../../user/about-dialog.md) <br />
[Power Platform admin center - Environment behavior settings](/power-platform/admin/settings-behavior) <br />
[Power Platform admin center - User settings](/power-platform/admin/users-settings)

---
title: Understand preview and experimental features | Microsoft Docs
description: Test and start to adopt new features.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 07/16/2018
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Understand experimental and preview features in PowerApps

With every release, we make changes and add features to make PowerApps the best tool to fit your needs. We move the product forward.  

We take backward compatibility very seriously. However, with any change or improvement, we might introduce an unintended side effect, and your app might not work exactly the way it did before.

To help balance improvement against impact on existing apps, we take larger features through a progression of stages. This article describes this process and how you can control your exposure to features that are under development.

## Feature roll-out stages

Features move through three stages on their way to becoming official parts of the product:

1. **Experimental**:  This feature is a work in progress. Don't depend on it yet; it may go through significant changes.
1. **Preview**:  This feature is almost done and is stable. Start to migrate existing apps to it now.
1. **Shipped**:  This feature is done. All apps have this feature enabled, and you can't turn it off.

At each stage, the number of people who use the feature rises, helping us to validate that the feature is what you need and that we're not introducing unintended side effects.

**Your feedback is critical to this process.**  Please post your feedback in the [PowerApps Community Forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).

How long does a feature remain in each stage? This varies from feature to feature. We look at many factors, including the number of apps that use the feature, the number of issues reported, and how urgently the feature is needed. Features can remain in a stage for weeks to many months.

This table may help you decide when you should jump in: 

| Stage | When should I use it? | Can I use it with confidence? | Is it enabled by default for new apps? | 
|----|----|----|-----|------|
| **Experimental** | If you're an early adopter, see something useful to you, and would like to help test the feature. | No.  Experimental features can radically change or completely disappear at any time. | No. You must explicitly opt in to the feature.  |  
| **Preview** | New apps automatically include this feature.  Start enabling and testing in existing apps because this feature will be eventually turned on for them too. | Yes. This feature is on track to become a permanent part of the product.  | Yes. You may want to turn it off if you run into a problem.  Please report issues; this is the main reason the feature is in Preview. | 
| **Shipped** (no longer appears in **Advanced settings**) | All apps have this feature. | Yes. | Yes.  Most can't be disabled.  |  

Toward the end of Preview, we might enable the feature for all apps one time, and we mark it as being in **final validation**.  This change gives the most people a last chance to try out the feature while they can still turn it off. Timely feedback is critical in this period because, in the next stage, the feature is fully shipped, and you can't turn it off.  

## Documentation

Where can you find information about these features?  We treat Preview features as finished features, and you can learn more about them just as you do any other product features: 
- [PowerApps documentation](https://docs.microsoft.com/powerapps/maker/canvas-apps/getting-started). We'll provide the basics on the new feature: the benefits, how to get started, and reference information.
- [PowerApps community forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).  Others will explore the new feature along with you. Learn from their experience, and share yours.
- [PowerApps blog](https://powerapps.microsoft.com/blog/).  Often, but not always, a blog post accompanies a new feature.

Experimental features are different.  They are works in progress, and we don't consider them finished. The short description in the **App settings** pane (see below) might be the only information about them. Experimental features don't normally appear in the documentation. The community forum is likely your best source of information.  In some cases, an early blog post describes the feature.  If you aren't finding enough information, ask in the forums, or wait for the feature to move to the Preview stage.

## Controlling which features are enabled

Experimental and preview features are listed in the app's **Advanced settings**.  From within the app, select the **File** menu, select **App settings**, and then select **Advanced settings**. Scroll down to the **Preview features** and **Experimental features** sections:

![](media/working-with-experimental/advanced-settings.png)

Each feature has a toggle switch.  **Off** means that the feature is disabled.  Having all switches turned off is the baseline and safest way to run your app.

In some cases, you might need to close and reopen the app after you change a setting.  The feature description should indicate when you must perform this step.

At the top of the **Advanced settings** panel, you can find settings for fully shipped features that aren't preview or experimental and that you can completely depend on. 

These settings are specific to each app, so changing a toggle switch affects only the app that's currently open. If you create an app, these switches revert to their default settings for that app.

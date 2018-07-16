---
title: Understand preview and experimental features | Microsoft Docs
description: Test and begin adoption of new features.
author: gregli-msft
manager: kvivek

ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 06/30/2018
ms.author: gregli

---
# Understand preview and experimental features in Microsoft PowerApps

With every release we make changes and add features to make PowerApps the best tool to fit your needs.  We move the product forward.  

But with any change or improvement there is a risk that we may introduce an unintended side effect and your existing app may not work exactly the way it did before.  We take backward compatibility very seriously.

To help balance improvements with impact on existing apps, we take larger features through a progression of stages.  This article describes this process and how you can control your exposure to features that are under development.

## Feature roll out stages

Features move through three stages on their way to becoming official parts of the product:

1. **Experimental**:  This is a work in progress.  Don't depend on it yet, it may go through significant changes. 
1. **Preview**:  This feature is almost done and is stable.  Start migrating existing apps to it now.  
1. **Shipped**:  This feature is done.  All apps have this feature enabled and it cannot be turned off.  

Each stage increases the size of the audience using the feature, helping us to validate that the feature is what you need and that there are no unintended side effects of introducing it.  

**Your feedback is critical to this process.**  Please post your feedback in the [PowerApps Community Forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).

How long does a feature remain in each stage?  This varies from feature to feature.  We look at many factors including the number of apps using the feature, the number of issues reported, and how urgently the feature is needed.  Features can remain in a stage for weeks to many months.

This table may help you decide when you should jump in: 

| Stage | When should I use it? | Can I use it with confidence? | Is it enabled by default for new apps? | 
|----|----|----|-----|------|
| **Experimental** | If you are an early adopter, see something useful to you, and would like to help test the feature. | No.  Experimental features can radically change or completely disappear at any time. | No. Authors must explicitly opt in to the feature.  |  
| **Preview** | New apps will automatically include this feature.  Start enabling and testing in existing apps as this feature will be eventually turned on for them too. | Yes. This feature is on track to become a permanent part of the product.  | Yes. You may want to turn it off if you run into a problem.  Please report issues, this is the main reason the feature is in Preview.  | 
| **Shipped** (no longer appears in Advanced settings) | All apps will have this feature. | Yes. | Yes.  Most cannot be disabled.  |  

Toward the end of Preview we may enable the feature for all existing apps one time.  When we do, we will mark the feature as being in **final validation**.  This gives the widest audience a last chance to try out the feature while still being able to turn it off.  Timely feedback is critical in this period as the next stage is fully shipped and it will no longer be possible to turn it off.  

## Documentation

Where should you go for information on these features?  We treat Preview features as finished features and you can learn more about them just as you do any other product features: 
- [PowerApps documentation](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/getting-started). We'll provide the basics on the new feature: the benefits, how to get started, and reference information.
- [PowerApps community forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).  Others will be working with the new feature too - learn from their experience and share your experience too.
- [PowerApps blog](https://powerapps.microsoft.com/en-us/blog/).  Often, but not always, there is a blog post to accompany a new feature.

Experimental features are a little different.  They are a work in progress and we do not consider them finished.  There may be no more information available than the short description in the App settings pane (see below).  Normally they do not appear in the documentation.  The community forum is likely your best source of information.  In some cases, there may be an early blog post that describes the feature.  If you aren't finding enough information, ask in the forums, or wait for the feature to move to the Preview stage.

## Controlling what features are enabled

Experimental and preview features are listed in the app's **Advanced settings**.  From within the app, select the **File** menu, then **App settings**, then **Advanced settings**, and then scroll down to the **Preview features** and **Experimental features** sections:

![](media/working-with-experimental/advanced-settings.png)

Each feature has a toggle switch.  "Off" means that the feature is disabled.  Having all switched turned off is the baseline and safest way to run your app.

In some cases, after changing a setting you may need to close and reopen the app.  The feature description should indicate when this is true.   

At the top of the **Advanced settings** panel appear settings for fully shipped features that are not preview or experimental and that you can completely depend on. 

Note that these settings are per app.  Changing a toggle switch will have an impact only for the app currently open.  Creating a new app will revert these switches to their default settings.

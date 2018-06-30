---
title: Understand preview and experimental features | Microsoft Docs
description: Test and begin adoption of new features.
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: canvas
ms.date: 06/30/2018
ms.author: gregli

---
# Understand preview and experimental features in Microsoft PowerApps

With every release we make changes and add features to make PowerApps the best tool to fit your needs.  We move the product forward.  

But with any change or improvement there is a risk that we may introduce an unintended side effect and your existing app may not work exactly the way it did before.  We take backward compatibility very seriously but it is impossible to catch all breaking changes.

## Feature roll out

To help balance improvements with impact on existing apps, we take larger features through a progression of stages.  In summary these stages are:

1. **Experimental**:  This is a work in progress.  Don't depend on it yet, it may go through significant changes. 
1. **Preview**:  This feature is almost done and is stable.  Start migrating existing apps to it now.  
1. **Shipped**:  This feature is done.  All apps have this feature enabled and it cannot be turned off.  

Each stage increases the size of the audience using the feature, helping us to validate that the feature is what you need and that there are no unintended side effects of introducing it.  

**Your feedback is critical to this process.**  Please post your feedback in the [PowerApps Community Forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).

Here are some more details of each stage:

| Stage | When should I use it? | Can I use it with confidence? | Is it enabled by default for new apps? | Where do I go for information? | 
|----|----|----|-----|------|-----|
| **Experimental** | If you are an early adopter, see something useful to you, and would like to help test the feature. | No.  Experimental features can radically change or completely disappear at any time. | No. Authors must explicitly opt in to the feature.  |  The description in the Advanced Settings may be all there is, especially in the early days of a feature.  The [PowerApps blog](https://powerapps.microsoft.com/en-us/blog/) may have additional information.  |
| **Preview** | New apps will automatically include this feature.  Start enabling and testing in existing apps as this feature will be eventually turned on for them too. | Yes. This feature is on track to become a permanent part of the product.  | Yes. You may want to turn it off if you run into a problem.  Please report issues, this is the main reason the feature is in Preview.  | [PowerApps documentation](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/getting-started) and [PowerApps Community Forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1).  There may also be a [PowerApps blog](https://powerapps.microsoft.com/en-us/blog/) post announcing the feature. | 
| **Shipped** (no longer appears in Advanced settings) | All apps will have this feature. | Yes. | Yes.  Most cannot be turned off.  |  [PowerApps documentation](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/getting-started) and [PowerApps Community Forum](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1). |

## Feature control

Experimental and preview features appear in the app's advanced settings.  From within the app, select the **File** menu, then **App settings**, then **Advanced settings**, and then scroll down to the **Preview features**:

![](media/working-with-experimental/advanced-settings.png)

In some cases, after changing a setting you may need to close and reopen the app.  The feature description should indicate when this is true.   

At the top of the **Advanced settings** panel appear settings for fully shipped features that are not preview or experimental and that you can completely depend on. 

Note that these settings are only for this app.  Creating a new app will revert these switches to their default settings.

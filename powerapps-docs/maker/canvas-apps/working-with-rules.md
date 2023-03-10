---
title: Convert rules to expressions
description: Learn about how convert rules to expressions in canvas apps.
author: gregli-msft

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 10/23/2019
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - mduelae
  - gregli-msft
---

# Convert rules to expressions

The rules feature that let you create rules in canvas apps to automatically modify an app based on specified criteria will be removed. The feature was retired in 2019 and it will be completely removed. 

You'll have a few months to use a converter to convert the rules into expressions. After this period, if you still  have rules in your canvas app that haven't been converted the system will automatically do it for you.

> [!IMPORTANT]
> Effective October 14, 2019, the rules feature in canvas apps is deprecated. More information: [Blog: Canvas Rules feature deprecation](https://powerapps.microsoft.com/blog/canvas-rules-feature-deprecation/).

## Convert rules

If your app has rules, then you'll get a prompted to convert them. The converter helps you migrate rules in your app to a format that will be compatible with future versions of Power Apps Studio. The converter uses the rules conditions in your app and replaces the references with corresponding inline expressions. 

Follow these steps to convert rules in your app:

1. Open your app for editing and edit a control with a rules.
2. On the warning message, select **Convert rules**.

     ![Convert rules.](./media/working-with-rules/convert-rules.png)

3. On the **Convert rules** dialog box select **Convert now**.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

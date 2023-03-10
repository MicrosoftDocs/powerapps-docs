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

The capability to create rules in canvas apps for automated app modification based on specified criteria will be removed. This feature was retired in 2019 and will now be fully removed.

You'll have a few months to convert the rules into expressions using a converter. If there are any rules remaining in your canvas app that have not been converted by the end of this period, the system will perform the conversion automatically.

> [!IMPORTANT]
> Effective October 14, 2019, the rules feature in canvas apps is deprecated. More information: [Blog: Canvas Rules feature deprecation](https://powerapps.microsoft.com/blog/canvas-rules-feature-deprecation/).

## Convert rules

When you edit an app that has rules, you will receive a prompt to convert them. The converter assists in migrating the rules within your app to a format that is compatible with future versions of Power Apps Studio. By utilizing the rules conditions in your app, the converter substitutes the references with corresponding inline expressions.

Follow these steps to convert rules in your app:

1. Open your app for editing and go to the the Rules panel.
2. On the warning message, select **Convert rules**.

     ![Convert rules.](./media/working-with-rules/convert-rules.png)

3. On the **Convert rules** dialog box select **Convert now**.

When the conversion is done, the rules are converted to the corresponding expression.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

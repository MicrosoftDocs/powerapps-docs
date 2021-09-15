---
title: Power Apps Ideas (Preview)
description: Learn about how to use Power Apps Ideas, its limitations and supportability, and benefit from the generated formulas.
author: norliu
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 09/17/2021
ms.subservice: canvas-maker
ms.author: norliu
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - norliu
  - tapanm-msft
---

# Power Apps Ideas (Preview)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

[Power Fx](/power-platform/power-fx/overview) is the open-source programming language for low code, and makes it possible for hundreds of millions of people with Excel-like skills to add advanced logic to their apps. However, sometimes it's not easy to write a formula, even for the most experienced Power Fx users, as it may sometimes take a lot of time searching for, learning about, and debugging complex formulas.

Power Apps Ideas is created to help everyone from the new makers to the seasoned IT pros to ease and speed up the formula authoring experience by using the power of AI models.

If you’re also struggling with Power Fx and you don’t actually want to spend that much time on it, try out Power Apps Ideas.

## Use Power Apps Ideas in your app

To use Power Apps Ideas, you'll find an Ideas pane on the right side of your canvas app, next to **Properties** and **Advanced** tabs.

There are two methods to benefit from Power Apps Ideas in your app.

### Method 1: Transform natural language to Power Fx formulas

You can enter your requirements in plain natural language (currently limited to English (en-us)), and Power Apps transforms your requirement to Power Fx formula.

For details, go to [Transform natural language to Power Fx formulas](power-apps-ideas-transform.md).

> [!NOTE]
> This capability only works on the **Items** property of [Gallery](controls/control-gallery.md) and [Data table](controls/control-data-table.md) controls. For more information, see [limitations](power-apps-ideas-transform.md#limitations), and [supported functions](power-apps-ideas-transform.md#supported-power-fx-functions).

### Method 2: Transform examples to Power Fx formulas

With method 1, you can transform natural language to formulas. However, we know that not all requirements are easy to describe even in our daily language. One of the typical use cases is data manipulation.

Let’s say you want to change a date field’s display format from the default to another format, and you don’t know how to describe that format. With Power Apps Ideas, you can now simply select that field, then in the ideas pane, enter your desired format, and press enter. One or a few formula suggestions will be popped out for you to select from.
Make sure your selection is a label within a Gallery field. Unlike method 1, method 2 doesn’t require you to use Dataverse specifically.

For details, go to [Transform examples to Power Fx formulas](power-apps-ideas-train-examples.md).

> [!NOTE]
> This method has support for specific capabilities. For more information, see [Supported and unsupported capabilities](power-apps-ideas-train-examples.md#supported-and-unsupported-capabilities).

## Next steps

- [Transform natural language to Power Fx formulas](power-apps-ideas-transform.md)
- [Transform examples to Power Fx formulas](power-apps-ideas-train-examples.md)

### See also

[Formula reference](formula-reference.md)

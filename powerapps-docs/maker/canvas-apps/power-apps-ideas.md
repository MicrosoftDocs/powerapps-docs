---
title: Power Apps Ideas
description: Learn about Power Apps Ideas, its limitations and supportability, and how to benefit from the generated formulas.
author: norliu

ms.topic: article
ms.custom: canvas
ms.date: 10/04/2022
ms.subservice: canvas-maker
ms.author: norliu
ms.reviewer: mkaur
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - norliu
  - tapanm-msft
---

# Power Apps Ideas


[Power Fx](/power-platform/power-fx/overview) is the open-source programming language for low code. It enables millions of people with Excel-like skills to add advanced logic to their apps. However, sometimes it's not easy to write a formula, even for the most experienced Power Fx users, as it can sometimes take a lot of time searching for, learning about, and debugging complex formulas.

Power Apps Ideas is created to help everyone from the new makers to the seasoned IT pros to ease and speed up the formula authoring experience by using the power of AI models.

If you’re struggling with Power Fx and don’t want to spend time on it, try Power Apps Ideas.

## Use Power Apps Ideas in your app


When you're building a canvas app, Power Apps Ideas will automatically suggest ideas for supported controls such as **Gallery**, **Data table**, **Text box**, **Drop down**, **Combo box**, and **Text label**. 

When you select the name field in a gallery, you'll see an idea for a formula that you may want to use. However, if you select the plus icon, then you won’t see an idea because we currently don’t have ideas for icons. 

:::image type="content" source="media/power-apps-ideas/ideas-example.gif" alt-text="Suggested ideas prompt.":::

There are two methods to benefit from Power Apps Ideas in your app.

### Method 1: Transform natural language to Power Fx formulas

You can enter your requirements in plain natural language (currently limited to English (en-us)), and Power Apps will transform your requirement to a Power Fx formula.

For details, go to [Transform natural language to Power Fx formulas](power-apps-ideas-transform.md).


### Method 2: Transform examples to Power Fx formulas

With method 1, you can transform natural language to formulas. However, we know that not all requirements are easy to describe even in our daily language. One of the typical use cases is data manipulation.

Let’s say you want to change a date field’s display format from the default to another format, and you don’t know how to describe that format. With Power Apps Ideas, you can now simply select that field, then enter your desired format in the ideas pane, and press enter. One or a few formula suggestions will be popped out for you to select from.

Make sure your selection is a label within a Gallery field or a column within a Data table.

For details, go to [Transform examples to Power Fx formulas](power-apps-ideas-train-examples.md).

> [!NOTE]
> This method has support for specific capabilities. For more information, see [Supported and unsupported capabilities](power-apps-ideas-train-examples.md#supported-and-unsupported-capabilities).

## Dismiss an idea

If you don’t want to see Ideas, select the close button (**X**) and then confirm that you don’t want to see Ideas anymore. 

If you want to see Ideas again, right-click on the control to see suggested Ideas.


## Next steps

- [Transform natural language to Power Fx formulas](power-apps-ideas-transform.md)
- [Transform examples to Power Fx formulas](power-apps-ideas-train-examples.md)

### See also

[Formula reference](formula-reference.md)

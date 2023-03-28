---
title: Overview of modern controls in canvas apps
description: Learn about modern controls in canvas apps.
author: yogeshgupta698

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur-msft
ms.date: 03/22/2023
ms.subservice: canvas-maker
ms.author: yogupta

search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - yogeshgupta698
---

# Overview of modern controls in canvas apps

[This article is pre-release document and is subject to change.]

Modern controls in Canvas apps are set of new controls available for our makers based on Microsoft design system. These controls bring in cohesive and world class design for app users with easier and faster configurations for app makers to be more productive. These controls are not only aesthetically pleasing but also highly functional and intuitive to use. They have been designed with a focus on accessibility, usability, and performance.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.


## Enable modern controls for your app
With your [canvas app open for editing](../../edit-app.md):
1.	On the command bar, select **Settings** > **Upcoming features**.
2.	From the Preview tab, set the toggle for **Try out the modern controls** to **On**.

 > [!div class="mx-imgBorder"]
   > ![Turn on modern controls](media/settings-panel.png)

3.	On the app authoring menu, select **Insert**.
4.	From the list of controls, select **Modern controls**.

You will see list of all the modern controls.

 > [!div class="mx-imgBorder"]
   > ![List of modern controls](media/modern-controls-list.png)


## Limitations and known issues

1. For the modern controls, if add items through an array such as PowerFx bar or advance properties. Then, you will need to additionally select “Value” field from the properties panel.

> [!div class="mx-imgBorder"]
   > ![List in items](media/array-list.png)

> [!div class="mx-imgBorder"]
   > ![Enable value field](media/select-value-field.png)

2. B.	While updating properties of controls in property panel, some of the property value updates in format of:
  ‘PowerApps.CoreControls.<Control name>.<Property name>’.<Value>
  This is a valid format, or you can update to value only. Both approaches will work for configuration of the control.
  
3. The property sets for new controls are different than property sets of original controls. Not all scenarios are supported on new controls yet and we will ship consistent improvements to enable new scenarios.
  
4. The modern controls don’t have support right now for properties to show up in command bar too. We currently only support property value updates through property panel.
  
5. E.	App checker rules like accessibility, formulas etc. don’t run on modern controls currently. The support will come soon as the feature develops.




## Upcoming updates


### See also






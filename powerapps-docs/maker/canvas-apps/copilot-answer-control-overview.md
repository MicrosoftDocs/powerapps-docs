---
title: Overivew of Copilot answer control for canvas apps
description: Use the Copilot answer control for canvas app.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: mkaur
ms.date: 2/13/2024
ms.subservice: canvas-maker
ms.author: arijitba
search.audienceType: 
  - maker
contributors:
  - mduelae
---

#  Use Copilot answer control for canvas apps (preview)

[This article is prerelease documentation and is subject to change.]

The Copilot answer control for Power Apps enables you Power Apps makers to set predefined questions that end users can quickly use to get generative answers through single click. This control has been optimized for mobile experiences and is powered by Microsoft Copilot.

![](media/image1.png)

## Building an app using the Copilot answer control

Makers can access this new preview control from the studio as shown below and can then drop it onto their canvas app. The control can be found at:

Insert &gt; Modern &gt; Copilot answer (preview) OR Insert &gt; Classic &gt; Copilot answer (preview)

![](media/image2.png)

Once the maker adds the control to the canvas app, they need to bind it to a data source (we currently support Dataverse) and then put in the question in the properties pane as shown. The maker can select other control properties and set them as applicable.

![A screenshot of a computer Description automatically generated](media/image3.png)

Once the properties are defined, the app can be tested and published.

## Using the Copilot answer control

The Power Apps end user will need to navigate to the Copilot answer control and press the "Arrow" button as shown to generate the responses and based on the predefined question, the user will be able to view the generative response.

![](media/image4.png)

Users have the option to regenerate the response and provide feedback on the quality of the response.

## Permissions and access requirements

To use this control, it must be enabled by the organization Power Platform administrator in the Power Platform admin center:

Power Platform admin center &gt; Environments &gt; copilot &gt; Settings &gt; Features

![A screenshot of a computer Description automatically generated](media/image5.jpeg)

This control can also be disabled tenant wide by the administrator.

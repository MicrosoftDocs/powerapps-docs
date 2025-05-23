---
title: Use deep links with wrapped native mobile apps
description:  Learn about deep linking in wrap functionality in Power Apps.
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 12/05/2022
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
contributors:
  - mduelae
---
# Use deep links with wrapped mobile apps

Deep links let users move from one application to another on computers and mobile devices. For example, a mobile app can deep link to Facebook to sign in. Deep linking an email address could open an email app to allow users to start composing a message. A website could use a deep link to an app store to start download for a specfic mobile app.

You can deep link to a wrapped native mobile app from other apps. Deep links for wrapped mobile apps should start with the following:

```ms-mobile-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>```

| **Parameter**        | **Description**                                                              |
|----------------------|------------------------------------------------------------------------------|
| &lt;app-id&gt;       | Opens the correct app module                                                 |
| &lt;tenantId&gt;     | Connects to the correct tenant                                               |

  
 For information on how to deep link into other apps in Power Apps, see [Use deep links with Power Apps mobile](/power-apps/mobile/mobile-deep-links).

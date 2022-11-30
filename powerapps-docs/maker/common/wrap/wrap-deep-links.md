---
title: Use deep links with wrapped native mobile apps
description: Learn about deep linking in wrap functionality in Power Apps.
author: makolomi
ms.topic: article
ms.custom: canvas
ms.reviewer: kaur
ms.date:12/01/2022
ms.subservice: canvas-maker
ms.author: makolomi
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

Deep links let users move from one application to another on computers and mobile devices. Simple examples include a mobile app deep-linking to Facebook to sign in, an email address deep-linking to a mail app to compose a message, or a website deep-linking to an app store to download a related mobile app.

# Creating deep links for wrapped mobile apps

Deep links for wrapped native mobile apps should start with the following:
*ms-mobile-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>*

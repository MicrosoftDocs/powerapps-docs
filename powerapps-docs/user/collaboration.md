---
title: "Collaborate with others in model-driven apps| MicrosoftDocs"
description: Collaborate with others in model-driven apps
author: sriharibs-msft
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/29/2023
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
ms.contributors:
- DanaMartens
---
# Collaborate with others in model-driven apps 

Collaborate with colleagues and share links in model-driven Power Apps the same way do you as in Microsoft Office.

### Multiplayer apps (preview)
[This section is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> This feature is rolling out gradually, slower than the standard, weekly deployments and will be enabled by default for all customers through April and August 2023. If you have enabled this capability before 2023 release wave 1, you may not see other users working on the same record intermittently. This will be addressed as part of the gradual rollout through April and August 2023.

When you're working on a record, you can also see other users who are working on the same record.

You can also select a user's picture to see their online status, send them an email, or start a Teams chat. 

> [!div class="mx-imgBorder"]
> ![View a user's online status.](media/collob-1.png "View a user's online status")

This feature uses the Azure Fluid Relay service, which must be available in your region. For more information, see [Azure Fluid Relay service availability](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=fluid-relay). Because this feature uses the [Azure Fluid Relay](/azure/azure-fluid-relay/overview/overview) service, users must be able to access fluidrelay.azure.com. 

### View a user's status and picture

App users, such as the record owner, as well as the users appearing in grids and lookups are displayed with their picture and online status.  This feature is now available on all model-driven apps and cannot be disabled.

> [!div class="mx-imgBorder"]
> ![VView a user's online status.](media/collob-2.png "View a user's online status.")

> [!NOTE]
> This feature will be extended to user lookups and grid user columns. 


### Share 
You can now easily share records with your colleagues using the new **Share** button.  Select **Copy link** or **Email link** in order to send a record link to your colleagues.

> [!Note]
> If you have the share privilege on a record and you email a record link to a colleague, the colleague will automatically get read access to the record.





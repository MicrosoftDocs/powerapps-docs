---
title: "Enable Office Delve with Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 4c8755d3-dd1e-480e-b077-88b45c787b92
caps.latest.revision: 4
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# About Office Delve/Graph

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

Office Graph integration for Dynamics 365 Customer Engagement will be removed on August 31, 2017, at the same time that [Office ends GQL query support](https://msdn.microsoft.com/office/office365/howto/query-office-graph-using-gql-with-search-rest-api). Customers can continue to use Office Graph integration through August 31, 2017. After August 31 that date, the Office Graph trending documents component will cease to function and you’ll see the following error message:

**We can't get to the trending documents. Try again later.**

To disable Office Graph:

1. Go to **Settings** > **Document Management** > **Office Graph Integration**.
2. Remove the Trending Documents dashboard component from existing dashboards.

For more information, see the blog: [Office Graph integration removal](https://blogs.msdn.microsoft.com/crm/2017/07/31/office-graph-integration-removal/).

### See also  
 [View relevant and trending information on a dashboard with Office Delve](https://docs.microsoft.com/dynamics365/customer-engagement/basics/view-relevant-trending-information-office-delve)
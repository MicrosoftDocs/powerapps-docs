---

title: Best practices to use an app for offline
description: Learn about the best practices for developing an app for offline use.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/13/2024
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Best practices to use an app for offline

## Tips

### Mobile offline synchronization
  
- Mobile offline synchronization with mobile devices occurs periodically. A synchronization cycle could last for several minutes, depending on Azure network latency, the volume of data that’s set for synchronization, and mobile network speed. Users can still use the mobile apps during synchronization.  
  
- The time for initial metadata download is determined by the number of total tables in offline-enabled app modules. Make sure to enable only those tables and app modules for offline that are necessary to optimize the experience for end users. 
  
- Ensure that any view that you want to work in offline doesn’t reference the tables that aren't offline enabled. For example, assuming Account is in the offline profile, then an Account view that references the primary contact when Contact isn't in the profile isn't available.

- Changes to a user’s security privileges are updated during the next synchronization cycle. Until that time, users can continue to access data according to their previous security privileges, but any changes they make are validated during the synchronization to the server. If they no longer have privileges to make changes for a row, they receive an error and the row won’t be created, updated, or deleted.

- Any changes to a user’s privilege to view a row won’t take effect on the mobile device until the next synchronization cycle.

- Mobile offline honors the mobile apps security model and the hierarchical security model except the [field level security and field sharing](/power-platform/admin/field-level-security).

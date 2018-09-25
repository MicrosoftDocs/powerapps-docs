---
title: "Search for records (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 08/29/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 899ec72f-f5f3-4b87-be2d-fe53f05737dc
caps.latest.revision: 21
ms.author: "t-mijosh"
manager: "ryjones"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Search for records

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

To find your records quickly in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)], you can search across multiple record types all at the same time.  The results of the search are shown in groups, sorted by entity type.  
  
 There are two ways to search.  
  
 ### Normal quick find 
  
- **Begins with** - results include records that begin with a specific word. For example, if you want to search for “Alpine Ski House”, type **alp** in the search box; if you type **ski**, the record won’t show up.  
  
- **Wildcard** - for example: *ski or *ski\*  
  
### Full text quick find (on-premises only)

- For Dynamics 365 (online), use Relevance Search.
  
- **Search within** - results include records that contain a field with all of the words in the search term.  The individual words can appear anywhere in the string and in any order.  For example, if you search for “Alpine Ski House”, you could find results for “I left the house today to go skiing in the Alpine Meadows.” since all of the search words appear somewhere in the string.  
  
-   Wildcards are not required in full text quick find.  
<!-- apparently the following is on-prem only>  
 For more information see, [Configure Quick Find options for the organization](https://technet.microsoft.com/library/dn919650.aspx).  
--> 
 
## Start a search  
  
1.  From the top nav bar, type one or more characters in the search box.  
  
2.  Choose the **Search** button next to the search box.  
  
## Filter search results  
  
-   To filter results by one record type, on the search screen, choose a record type from the **Filter with:** drop-down box.  
  
-   To search against all record types, choose **None** in the **Filter with:** drop-down box  
  
### See also  
 [Search and Find in Dynamics 365](search-and-find-header.md)<br />
 [Use Relevance Search for faster, comprehensive search results](relevance-search-results.md)<br />
 [Create, edit, or save an Advanced Find search](save-advanced-find-search.md)   

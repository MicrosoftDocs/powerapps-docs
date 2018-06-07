---
title: "Troubleshooting: Unblock URLs required for Dynamics 365 (online) | MicrosoftDocs"
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
ms.assetid: f2c4534a-2185-4404-b31a-8c61a9873285
caps.latest.revision: 7
author: "jimholtz"
ms.author: "jimholtz"
manager: kvivek
---
# Troubleshooting: Unblock required URLs

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

[!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] uses several Microsoft URLs to help provide security, services, and features. However, your computer or your organization’s computer network may block access to some of these URLs. Blocking any of the required URLs will cause [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] to operate incorrectly or not at all.  
  
 You may see a network or server error message if your computer or your organization's network blocks the URLs you need. The error message might look like one of these:  
  
-   "The specified [!INCLUDE[pn_microsoftcrm_server](../includes/pn-microsoftcrm-server.md)] address (URL) is not responding. Ask your administrator to verify that the server is turned on, and then try again."  
  
-   "There is a problem communicating with the [!INCLUDE[pn_microsoftcrm_server](../includes/pn-microsoftcrm-server.md)]. The server might be unavailable."  
  
You can unblock these URLs on your computer by adding them to a list of approved sites in your browser.  
  
> [!IMPORTANT]
>  If the following procedure doesn’t unblock the URLs required for [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)], ask your system administrator to unblock the URLs on the organization’s network.  
   
### Unblock Dynamics 365 URLs in Internet Explorer  
  
1.  On the Explorer bar, click or tap the **Tools** icon (the white gear shape), and then click or tap **Internet options**.  
  
2.  Click or tap the **Security** tab > **Trusted sites** > **Sites**.  
  
3.  In **Add this website to the zone**, type the URL for your Dynamics 365 (online) organization. For example, https://contoso.crm.dynamics.com  
  
4.  Click or tap **Add** > **Close** > **OK**.  
  
For a list of other URLs you may need to add to unblock, see [Internet accessible URLs required for Microsoft Dynamics CRM Online](http://support.microsoft.com/kb/2655102)

---
title:  Delete an instance | Microsoft Docs
description: In this quickstart, you learn how to download a list of apps created in your environments
services: 'powerapps'
suite: powerapps
documentationcenter: na
author: jimholtz
manager: kvivek
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/21/2018
ms.author: jimholtz

---
# Delete an instance

> [!NOTE]
> ![This page is under construction. Check back soon!](media/under_construction.png "Coming soon")  [!INCLUDE[cc-under-construction](../includes/cc-under-construction.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

You can delete [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] Sandbox instances to recover the licenses and storage space or to prevent them from being used by mistake. In order to delete a production instance, you must first switch to a Sandbox instance and then delete the Sandbox instance. You can delete a Support instance directly.
  
<a name="BKMK_Delete"></a>   
## Delete an instance  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select the instance that you want, and then click **Delete**.  
  
    > [!WARNING]
    >  Your data will be lost! Be sure you’ve selected the correct instance.  
  
5.  Click **Confirm** to delete the instance.  
  
Deleting an instance doesn’t change the number of your licenses purchased. For example, say you have two instances - one Sandbox and one production - and you decide to delete your Sandbox instance. After the delete has successfully completed, you’ll see one production instance and one instance to configure in the **Instance** tab of the **Manage your Dynamics 365 updates** page.  
  
### See also  
 [Manage Microsoft Dynamics 365 (online) instances](manage-online-environments.md)   
 [Switch an instance](switch-environment.md)

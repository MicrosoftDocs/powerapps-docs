---
title:  Switch an instance | Microsoft Docs
description: In this quickstart, you learn how to download a list of apps created in your environments
services: 'powerapps'
suite: powerapps
documentationcenter: na
author: jimholtz
manager: kfile
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
# Switch an instance

> [!NOTE]
> ![This page is under construction. Check back soon!](media/under_construction.png "Coming soon")  [!INCLUDE[cc-under-construction](../includes/cc-under-construction.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

You may decide that your customization work developed and tested on a Sandbox instance is now ready to go live. If you’ve placed your Sandbox instance in administration mode, only users with [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] System Administrator or System Customizer security roles are able to sign in to that instance. Once you switch the instance type to Production, all your users can access your Dynamics 365 organization. When you configure or edit an instance, you can switch the instance from:  
  
-   Production to Sandbox  
  
-   Sandbox to Production  
  
Switching an instance does not change the number of your purchased licenses. Review the **License considerations** section for how switching can impact license allocation.  
  
<a name="BKMK_Switch"></a>   
## Switch an instance  
  
1. [!INCLUDE[proc_office365_signin](../includes/proc-office365-signin.md)]  
  
2. [!INCLUDE[proc_office365_choose_admin_crm](../includes/proc-office365-choose-admin-crm.md)]  
  
3.  Choose the **Instances** tab.  
  
4.  Select the instance that you want, and then click **Edit**. If this is a new instance, click **Configure**.  
  
5.  Under **Instance type**, choose the instance type and then click **Next**.  
  
6.  Review the settings and then click **Save**.  
  
<a name="BKMK_Licenses"></a>   
## License considerations  
 Review the following table to see how switching an instance type is impacted by your Dynamics 365 (online) licenses.  
  
|Scenario|Result|Notes|  
|--------------|------------|-----------|  
|Switch a Production instance to Sandbox. You have unused Sandbox licenses.|A Sandbox license is used.|Sandbox instances have special features such as Reset and Administration modes. See [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md).|  
|Switch a Production instance to Sandbox. You do not have any unused Sandbox licenses. You have unused Production licenses.|A Production license is used.|Sandbox instances have special features such as Reset and Administration modes. See [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md).|  
|Switch a Production instance to Sandbox. You do not have any unused Sandbox or Production licenses.|The Production instance is not changed. You need to purchase a Sandbox instance.|Sandbox instances have special features such as Reset and Administration modes. See [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md).|  
|Switch a Sandbox instance to Production. You have unused Production licenses.|A Production license is used. A Sandbox instance becomes available.||  
|Switch a Sandbox instance to Production. You do not have any unused Production licenses.|You will need to purchase a Production license.|See [Add an instance to your subscription](add-environment-subscription.md).|  
  
### See also  
 [Manage Microsoft Dynamics 365 (online) instances](manage-online-environments.md)   
 [Manage Dynamics 365 (online) Sandbox instances](manage-sandbox-environments.md)   
 [Add an instance to your subscription](add-environment-subscription.md)

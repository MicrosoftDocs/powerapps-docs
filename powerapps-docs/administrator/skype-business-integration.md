---
title: "Skype for Business and Skype integration with Dynamics 365 Customer Engagement | MicrosoftDocs"
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
ms.assetid: 6cc410d4-2c5a-42f6-97a0-af7259182e9a
caps.latest.revision: 27
author: "Mattp123"
ms.author: "matp"
manager: kvivek
---
# Skype for Business and Skype integration

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

If your organization uses [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] (formerly known as [!INCLUDE[pn_Microsoft_Lync](../includes/pn-microsoft-lync.md)]) or [!INCLUDE[pn_skype](../includes/pn-skype.md)], you can take advantage of connectivity features like click-to-call or checking user availability from within [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] or [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](../includes/pn-microsoft-dynamics-crm-for-outlook.md)].  
  
<a name="BKMK_UseLync"></a>   
## Using Skype for Business with Dynamics 365  

 When you use [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] and [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] together, you can use [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)]) presence and click-to-call from within [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)].  
  
 Your organization must have one of the following products or subscriptions:  
  
- [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)]  
  
- [!INCLUDE[pn_skype_for_business_server_2015](../includes/pn-skype-for-business-server-2015.md)]  
  
- [!INCLUDE[pn_ms_lync_server_2013](../includes/pn-ms-lync-server-2013.md)]  
  
- [!INCLUDE[pn_MS_Lync_Server_2010](../includes/pn-ms-lync-server-2010.md)]  
  
 **Client requirements and [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] configuration**  
  
-   To use click-to-call, [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] must be selected as the telephony provider in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. You can set this on the General tab at Settings > Administration > System Settings.  
  
-   By default, [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] presence is enabled in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. System administrators can enable or disable presence in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. To do this, click **Settings** > **Administration** > **System Settings** and on the **General** tab, **Set the IM presence option** to **Yes** or **No**.  
  
-   Each user must have the [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] client installed and running on their PC.  
  
-   For [!INCLUDE[pn_skype_for_business](../includes/pn-skype-for-business.md)] presence, [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] users must have `https://*.dynamics.com` added to their web browsers trusted sites list in Internet options in [!INCLUDE[pn_Internet_Explorer](../includes/pn-internet-explorer.md)].  
  
### Supported devices and web browsers when you use Skype for Business with Microsoft Dynamics 365  
  
|Mobile app or web browser|Skype for Business click-to-call|Skype for Business presence|  
|-------------------------------|----------------------------------------|---------------------------------|  
|[!INCLUDE[pn_crm_for_ipad](../includes/pn-crm-for-ipad.md)]|Yes|No|  
|[!INCLUDE[pn_moca_CRM_Android](../includes/pn-moca-crm-android.md)]|Yes|No|  
|[!INCLUDE[pn_ms_Windows_short](../includes/pn-ms-windows-short.md)]-based tablets|Yes|No|  
|[!INCLUDE[pn_Internet_Explorer](../includes/pn-internet-explorer.md)]|Yes|Yes|  
|[!INCLUDE[tn_Google_Chrome](../includes/tn-google-chrome.md)]|Yes|No|  
|[!INCLUDE[tn_Mozilla_Firefox](../includes/tn-mozilla-firefox.md)]|Yes|No|  
|[!INCLUDE[tn_Apple_Safari](../includes/tn-apple-safari.md)]|Yes|No|  
  
<a name="BKMK_UseSkype"></a>   

## Using Skype with Dynamics 365  
 When you use [!INCLUDE[pn_skype](../includes/pn-skype.md)] and [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] together, you can use [!INCLUDE[pn_skype](../includes/pn-skype.md)] click-to-call from within [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)].  
  
**Client requirements and [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] configuration**  
  
-   Each user must have the [!INCLUDE[pn_skype_for_windows](../includes/pn-skype-for-windows.md)] desktop client or the [!INCLUDE[pn_skype_for_windows_8](../includes/pn-skype-for-windows-8.md)] app installed and running on their PC or [!INCLUDE[pn_windows8](../includes/pn-windows8.md)] device.  
  
- **Skype** must be selected as the telephony provider in [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)]. You can set this on the **General** tab at **Settings** > **Administration** > **System Settings**.  
  
### Supported devices and web browsers when you use Skype with Dynamics 365  
  
|Mobile app or web browser|Skype click-to-call|  
|-------------------------------|---------------------------|  
|[!INCLUDE[pn_crm_for_ipad](../includes/pn-crm-for-ipad.md)]|Yes|  
|[!INCLUDE[pn_moca_CRM_Android](../includes/pn-moca-crm-android.md)] on [!INCLUDE[tn_android](../includes/tn-android.md)] tablets|Yes|  
|[!INCLUDE[pn_ms_Windows_short](../includes/pn-ms-windows-short.md)]-based tablets|Yes|  
|[!INCLUDE[pn_Internet_Explorer](../includes/pn-internet-explorer.md)]|Yes|  
|[!INCLUDE[tn_Google_Chrome](../includes/tn-google-chrome.md)]|Yes*|  
|[!INCLUDE[tn_Mozilla_Firefox](../includes/tn-mozilla-firefox.md)]|Yes**|  
|[!INCLUDE[tn_Apple_Safari](../includes/tn-apple-safari.md)]|Yes|  
  
 \* The [Skype Click-to-call plugin](http://www.skype.com/go/clicktocall) must be installed on the [!INCLUDE[tn_chrome](../includes/tn-chrome.md)] browser and enabled. More information: [How do I enable Skype Click to Call in Chrome?](https://support.skype.com/en/faq/FA12243/how-do-i-enable-skype-click-to-call-in-chrome)  
  
 Additionally, [!INCLUDE[pn_skype](../includes/pn-skype.md)] click-to-call is supported with [!INCLUDE[pn_crm_for_windows_8](../includes/pn-crm-for-windows-8.md)], [!INCLUDE[pn_moca_CRM_Windows_8_1](../includes/pn-moca-crm-windows-8-1.md)], and [!INCLUDE[pn_windows_10](../includes/pn-windows-10.md)].  
  
### See also  
 [Set up Dynamics 365 (online) to use Skype or Skype for Business](set-up-skype-or-skype-for-business.md)   
 [Microsoft Dynamics 365 (online) requirements](online-requirements.md)

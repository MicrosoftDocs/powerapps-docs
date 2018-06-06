---
title: "Web application requirements for Dynamics 365 Customer Engagement | MicrosoftDocs"
description: ""
keywords: ""
ms.date: 01/09/2018
ms.service: crm-online
ms.custom: 
ms.topic: article
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 6404db68-f66b-4128-ac2f-84258503bc82
author: Mattp123
ms.author: matp
manager: brycho
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 123
topic-status: Drafting
---

# Web application requirements

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

<a name="CRMappandMobileReqs"></a> This section lists the hardware and software requirements for the [!INCLUDE[pn_crm_op_edition](../../includes/pn-crm-onprem.md)] and [!INCLUDE[pn_CRM_Online](../../includes/pn-crm-online.md)] web and mobile device client applications.  
  
<a name="webapp_hw_req"></a>   
## Dynamics 365 web application hardware requirements  
 The following table lists the minimum and recommended hardware requirements for the [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] web application.  
  
|Component|Minimum|Recommended|  
|---------------|-------------|-----------------|  
|Processor|1.9 gigahertz (GHz)  x86- or x64-bit dual core processor with SSE2 instruction set|3.3 gigahertz (GHz) or faster 64-bit dual core processor with SSE2 instruction set|  
|Memory|2-GB RAM|4-GB RAM or more|  
|Display|Super VGA with a resolution of 1024 x 768|Super VGA with a resolution of 1024 x 768|  
  
 Running [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] on a computer that has less than the recommended requirements may result in inadequate performance. Additionally, satisfactory performance may be experienced running systems that use a different hardware configuration than those published here—for example, a system with a modern quad-core processor, lower clock speed, and more RAM.  
  
 **Network requirements**  
  
 [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] is designed to work best over networks that have the following elements:  
  
-   Bandwidth greater than 50 KBps (400 kbps)  
  
-   Latency under 150 ms  
  
Notice that these values are recommendations and don’t guarantee satisfactory performance. The recommended values are based on systems using out-of-the box forms that aren’t customized. If you significantly customize the out-of-box forms, we recommend that you test the form response to understand bandwidth needs. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Verify network capacity and throughput for Dynamics 365 clients](https://docs.microsoft.com/dynamics365/customer-engagement/admin/verify-network-capacity-throughput-clients)  
  
### Network requirements when you use Dynamics 365 interactive service hub experience  
 The [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] interactive service hub experience is designed to work best over networks that have the following elements:  
  
-   Bandwidth greater than 1Megabit per second (125 KBps/Kilobyte per second)  
  
-   Latency under 150 ms  
  
Notice that the suggested network requirements include the metadata download needed for first run or newly published customizations. The [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] interactive service hub typically requires more bandwidth when metadata has to be downloaded. These values are recommendations and don’t guarantee satisfactory performance. The values are based on systems using uncustomized, out-of-the box forms. If you significantly customize the out-of-box forms, we recommend that you test the form response to understand bandwidth needs.  
  
<a name="SupportedOS"></a>   
## Supported versions of Internet Explorer and Microsoft Edge  
 The following table describes the [!INCLUDE[pn_ms_Windows_short](../../includes/pn-ms-windows-short.md)] and [!INCLUDE[pn_Internet_Explorer](../../includes/pn-internet-explorer.md)] or [!INCLUDE[pn_microsoft_edge](../../includes/pn-microsoft-edge.md)] versions supported for use with the [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] web application.  
  
|[!INCLUDE[pn_ms_Windows_short](../../includes/pn-ms-windows-short.md)] version|[!INCLUDE[pn_IE_10](../../includes/pn-ie-10.md)]|[!INCLUDE[pn_ie_11](../../includes/pn-ie-11.md)]<sup>2</sup>|[!INCLUDE[pn_microsoft_edge](../../includes/pn-microsoft-edge.md)]|  
|---------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------|  
|[!INCLUDE[pn_windows_10](../../includes/pn-windows-10.md)]|Not supported<sup>1</sup>|Supported|Supported|  
|[!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)]|Not supported<sup>1</sup>|Supported|Not supported|  
|[!INCLUDE[pn_windows8](../../includes/pn-windows8.md)]|Supported|Not supported<sup>1</sup>|Not supported|  
|[!INCLUDE[pn_Windows_7](../../includes/pn-windows-7.md)]|Supported|Supported|Not supported|  
  
 <sup>1</sup> This version of [!INCLUDE[pn_ms_Windows_short](../../includes/pn-ms-windows-short.md)] doesn’t support the version of [!INCLUDE[pn_Internet_Explorer](../../includes/pn-internet-explorer.md)]. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Internet Explorer 11 – FAQ for IT Pros](https://technet.microsoft.com/library/dn268945.aspx)  
 <sup>2</sup> Check requirements for individual apps, such as [Customer Service Hub application requirements](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/customer-service-hub-user-guide-basics).
  
> [!IMPORTANT]
>  Although you may be able to use [!INCLUDE[pn_IE_8](../../includes/pn-ie-8.md)], [!INCLUDE[pn_IE_9](../../includes/pn-ie-9.md)], or an [!INCLUDE[pn_Internet_Explorer](../../includes/pn-internet-explorer.md)] and [!INCLUDE[pn_ms_Windows_short](../../includes/pn-ms-windows-short.md)] combination that is not supported in the previous table, those web browsers are not recommended and are not supported with this version of [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)].  
>   
>  Using plug-ins or other third-party extensions in your browser can increase load times on pages with lists of data.  
  
<a name="BKMK_support_nonIE"></a>   
## Supported non-Internet Explorer web browsers  
 The [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] web application can run in any of the following web browsers running on the specified operating systems:  
  
- [!INCLUDE[tn_Mozilla_Firefox](../../includes/tn-mozilla-firefox.md)] (latest publicly-released version) running on [!INCLUDE[pn_windows_10](../../includes/pn-windows-10.md)], [!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)], [!INCLUDE[pn_windows8](../../includes/pn-windows8.md)], or [!INCLUDE[pn_Windows_7](../../includes/pn-windows-7.md)]  
  
- [!INCLUDE[tn_Google_Chrome](../../includes/tn-google-chrome.md)]
    - [!INCLUDE[tn_Google_Chrome](../../includes/tn-google-chrome.md)] (latest publicly-released version) running on [!INCLUDE[pn_windows_10](../../includes/pn-windows-10.md)], [!INCLUDE[pn_windows_8_1](../../includes/pn-windows-8-1.md)], [!INCLUDE[pn_windows8](../../includes/pn-windows8.md)], [!INCLUDE[pn_Windows_7](../../includes/pn-windows-7.md)], or [Google Nexus](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/support-phones-tablets#BKMK_Nexus) tablet 
    - Google Chrome (latest publicly-released version) running on [!INCLUDE[tn_Mac_OS_X](../../includes/tn-mac-os-x.md)] 10.8 (Mountain Lion), 10.9 (Mavericks), or 10.10 (Yosemite) 
  
- [!INCLUDE[tn_Apple_Safari](../../includes/tn-apple-safari.md)] (latest publicly-released version) running on [!INCLUDE[tn_Mac_OS_X](../../includes/tn-mac-os-x.md)] 10.8 (Mountain Lion), 10.9 (Mavericks), 10.10 (Yosemite), or [Apple iPad](https://docs.microsoft.com/dynamics365/customer-engagement/mobile-app/support-phones-tablets#BKMK_iPad)  
  
To find the latest release for these web browsers, visit the software manufacturer’s website.  
  
> [!IMPORTANT]
> - Using plug-ins or other third-party extensions in your browser can increase load times on pages with lists of data.  
> - [!INCLUDE[tn_Mozilla_Firefox](../../includes/tn-mozilla-firefox.md)] ESR (Extended Support Release) versions aren’t supported.  
  
<a name="SupportedMSOffice"></a>   
## Supported versions of Office  
 To use [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] with [!INCLUDE[pn_MS_Office](../../includes/pn-ms-office.md)] integration features, such as Export to Excel and Mail Merge, you must have one of the following [!INCLUDE[pn_MS_Office](../../includes/pn-ms-office.md)] versions on the computer that is running the [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] web application:  
  
- [!INCLUDE[pn_MS_Office_365](../../includes/pn-ms-office-365.md)]  
  
- [!INCLUDE[pn_microsoft_office_2016](../../includes/pn-microsoft-office-2016.md)]  
  
- [!INCLUDE[pn_ms_office_2013_long](../../includes/pn-ms-office-2013-long.md)]  
  
- [!INCLUDE[pn_Microsoft_Office_2010](../../includes/pn-microsoft-office-2010.md)]  
  
[!INCLUDE[cc_Office365PlanRequirement](../../includes/cc-office365planrequirement.md)]
  
<a name="BKMK_PrintRepots"></a>   
## Printing reports  
 The Reporting Services[!INCLUDE[pn_ms_ActiveX_long](../../includes/pn-ms-activex-long.md)] control is required to print reports. If you try to print a report and the control isn’t installed, you’ll be prompted to install it. The installer package is named RSClientPrint.cab and can found on the [!INCLUDE[pn_SQL_Server_Reporting](../../includes/pn-sql-server-reporting.md)] server at \<drive>:\Program files\Microsoft SQL Server\\<MSSQL\>\Reporting Services\ReportServer\bin.  

<a name="BKMK_TLS"></a> 
## Transport Layer Security (TLS) requirement
With the [!INCLUDE [pn-crm-9-0-0-online](../../includes/pn-crm-9-0-0-online.md)], web browsers and other client applications that only use Transport Layer Security (TLS) versions earlier than TLS 1.2 will be unable to connect to their [!INCLUDE [pn-crm-online-shortest](../../includes/pn-crm-online-shortest.md)] instances and the [!INCLUDE [pn-dyn-365-admin-center](../../includes/pn-dyn-365-admin-center.md)]. 

For more information, see these blog posts: 
- [Updates coming to Dynamics 365 Customer Engagement connection security](https://blogs.msdn.microsoft.com/crm/2017/09/28/updates-coming-to-dynamics-365-customer-engagement-connection-security/)
- [TLS 1.2 support at Microsoft](https://blogs.microsoft.com/microsoftsecure/2017/06/20/tls-1-2-support-at-microsoft/)
  
### See also  
 [Supported web browsers and mobile devices](https://docs.microsoft.com/dynamics365/customer-engagement/admin/supported-web-browsers-and-mobile-devices)   
 <!-- [64-bit supported configurations for Microsoft Dynamics 365](../admin/64-bit-supported-configurations-for-microsoft-dynamics-365.md) 
 [Microsoft Dynamics 365 system requirements and required technologies](Microsoft%20Dynamics%20365%20system%20requirements%20and%20required%20technologies.md) -->  

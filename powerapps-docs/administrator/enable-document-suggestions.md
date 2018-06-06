---
title: "Enable document suggestions for Dynamics 365 Customer Engagement | MicrosoftDocs"
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
ms.assetid: 80de5c8d-bec9-4779-a83f-1d900eecbf2d
caps.latest.revision: 19
author: "Mattp123"
ms.author: "matp"
manager: "brycho"
---
# Enable document suggestions to recommend related documents

[!INCLUDE[cc-applies-to-update-9-0-0](../../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../../includes/cc_applies_to_update_8_2_0.md)]

Enabling Document Suggestions helps your [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] web browser and mobile users be aware of important documents related to what they're working on in [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] such as a big sales opportunity. You, as the admin, define relevant fields. A recommendation engine using [!INCLUDE[pn_Windows_Azure](../../includes/pn-windows-azure.md)] text analytics uses keyword matching to associate related records to find similar documents. You create similarity rules in [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] to provide your own similarity logic. [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)] then presents a list of suggested documents to the user while the user works in the current record.  
  
 ![Document recommendations feature diagram](../media/document-recommendations.png "Document recommendations feature diagram")  
  
> [!NOTE]
>  The Document Suggestions feature doesn't require a connection to the [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service. If you choose not to use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics, Document Suggestions will use the built-in keyword matching  logic available in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)]. However, we recommend that you use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service for more advanced keyword matching.  
  
 Document Suggestions searches other like-entities to determine similarities found in documents located on a [!INCLUDE[pn_ms_SharePoint_long](../../includes/pn-ms-sharepoint-long.md)] site, [!INCLUDE[pn_onedrive](../../includes/pn-onedrive.md)], or external location. Suggested documents can be in several different formats such as [!INCLUDE[pn_ms_Word_short](../../includes/pn-ms-word-short.md)], [!INCLUDE[pn_Excel_short](../../includes/pn-excel-short.md)], [!INCLUDE[pn_MS_Powerpoint](../../includes/pn-ms-powerpoint.md)], [!INCLUDE[pn_onenote](../../includes/pn-onenote.md)], Adobe PDF, and text files. When similar documents are found Document Suggestions presents them offering  you  the ability to open the document or make a copy.  
  
## Requirements  
 The following are required to use Document Suggestions with [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)].  
  
- [!INCLUDE[pn_dynamics_crm_online](../../includes/pn-dynamics-crm-online.md)]  
  
-   To suggest documents located on [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)]:  
  
    -   Access to [!INCLUDE[pn_sharepoint_online](../../includes/pn-sharepoint-online.md)], [!INCLUDE[pn_microsoft_sharepoint_2013](../../includes/pn-microsoft-sharepoint-2013.md)], or [!INCLUDE[pn_sharepoint_2016](../../includes/pn-sharepoint-2016.md)].  
  
    -   Document management must be set up in [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)]. See [Set up SharePoint integration with Microsoft Dynamics 365](https://docs.microsoft.com/dynamics365/customer-engagement/admin/set-up-sharepoint-integration)  
  
-   Relevance Search must be enabled. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Configure Relevance Search for the organization](https://docs.microsoft.com/dynamics365/customer-engagement/admin/configure-relevance-search-organization)  
  
- Document Suggestions works with Web browser, [!INCLUDE[pn_moca_full](../../includes/pn-moca-full.md)] and [!INCLUDE[pn_dyn_365_phones](../../includes/pn-dyn-365-phones.md)].  
  
-   To use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] text analytics with Document Suggestions:  
  
    -   An [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] subscription is required to use the [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service.  
  
    -   A system administrator must enable the text analytics connection in [!INCLUDE[pn_crm_shortest](../../includes/pn-crm-shortest.md)]. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Set the Azure Machine Learning text analytics connection](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#Set_AzureMLconnection)  
  
-   A system administrator must define a similarity rule for each entity type that is to be included in Document Suggestions. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Create similar record suggestion mappings](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#create_similar_record_rules)  
  
## How it works  
 The entities that can use Document Suggestions are Contact, Opportunity, Lead, Account, Case, and custom entities.  
  
 You can use the built-in pattern matching that is included natively with the Document Suggestions feature, but we recommend that you use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service for more advanced keyword matching.  
  
 Document Suggestions searches only the locations and documents that the user has access to.  
  
 Locations where documents are found are searched in the following order:  
  
1. [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)] default site.  
  
2.  Other [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)] sites.  
  
3. [!INCLUDE[pn_onedrive](../../includes/pn-onedrive.md)]  
  
4. [!INCLUDE[pn_office_365_groups](../../includes/pn-office-365-groups.md)] (when solution is installed).  
  
5.  External URL (when configured).  
  
Currently, Document Suggestions does not search attachments that are added to Notes in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] records.  
  
<a name="addExternalURL"></a>   
### Adding an external URL to search another site  
 External sites, such as an on-premises [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)] document library can be included in Document Suggestions by adding an external URL for the site to be searched.  
  
> [!NOTE]
>  For the best results when using an external site for document suggestions, we recommend that you use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics, which provides more advanced keyword matching logic. [Set the text analytics connection](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#Set_AzureMLconnection)  
  
 Once you add the external URL to the enabled document suggestions feature, here is what your users will experience.  
  
-   Web browsers. When you run [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] from a Web browser, after clicking **Document Suggestions**, users can then click **Other Recommendations** in the **Document Suggestions** page to display another page that may include more document suggestions found on the external site. Notice that the user may be prompted to sign in to the external site.  
  
-   Mobile apps. For the [!INCLUDE[pn_moca_full](../../includes/pn-moca-full.md)] and [!INCLUDE[pn_dyn_365_phones](../../includes/pn-dyn-365-phones.md)] apps, after clicking **Document Suggestions**, users can click **Other Recommendations**, which opens the external site in the devices default web browser that may include more document suggestions found on the external site. Notice that the user may be prompted to sign in to the external site.  
  
#### Constructing the external URL  
 The external URL should be constructed in a format that is understood by the external site. For example, for sites that use a construct similar to *https://contoso.com/search?{0}*, where **https://contoso.com/search?** is the search URL structure and {0} is the keyword string, Document Suggestions passes the keywords in the {0} parameter. The keywords that are passed to the URL are derived from similar record rules that include entity mappings of **Text Match**. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Create similar record suggestion rules](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#create_similar_record_rules)  
  
 The values found in the text fields of the similarity rule mappings are used as keywords to build the query that is passed to the external site, similar to the below URL, where *keyword* is the text values found in the similarity rules mappings and *&* represents a whitespace that Document Suggestions uses to separate each keyword.  
  
 *https://contoso.com/search?keywordA&keywordB&keywordC*  
  
 For an on-premises SharePoint server, you can add an external URL that points to a subsite similar to this, where *mysharepoint* is the web site name *sites* is the site name and *subsitename* is the subsite name.  
  
 *https://mysharepoint/sites/subsitename/_layouts/15/osssearchresults.aspx?&k={0}*  
  
## Set up the Azure text analytics connection  
 To use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] text analytics with Document Suggestions, an [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] text analytics connection must be configured. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Set the Azure Machine Learning text analytics connection](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#Set_AzureMLconnection)  
  
> [!NOTE]
>  The Document Suggestions feature doesn't require a connection to the [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service. If you choose not to use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics, Document Suggestions will use the built-in keyword matching  logic available in [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)]. However, we recommend that you use [!INCLUDE[pn_azure_shortest](../../includes/pn-azure-shortest.md)] Text Analytics service for more advanced keyword matching.  
  
## Define and activate similarity rules  
 If you have not already defined similarity rules, see [Create similar record suggestion mappings](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#create_similar_record_rules).  
  
## Enable Document Suggestions  
 To enable Document Suggestions, do the following:  
  
1. [!INCLUDE[proc_settings_administration](../../includes/proc-settings-administration.md)]  
  
2.  Go to **System Settings** > **Document Management** > **Manage Document Suggestions**.  
  
3.  In the **Select Entities** area, select the entities that you want to include in Document Suggestions,  and then click **Apply**.  
  
    > [!TIP]
    >  If the entities (contact, opportunity, lead, account, or custom) aren't listed in the **Select Entities** area, it is because similarity rules for the entity have not been defined and activated.  [Create similar record suggestion mappings](https://docs.microsoft.com/dynamics365/customer-engagement/admin/public-preview-microsoft-cognitive-services-integration#create_similar_record_rules)  
  
4.  Set external URL to include in Document Suggestions. By default, Document Suggestions searches in [!INCLUDE[pn_MS_Office_365](../../includes/pn-ms-office-365.md)] services like [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)] or [!INCLUDE[pn_onedrive](../../includes/pn-onedrive.md)]. If you want to search  an external site in addition to the available [!INCLUDE[pn_Office_365](../../includes/pn-office-365.md)] services, such as an on-premise [!INCLUDE[pn_SharePoint_short](../../includes/pn-sharepoint-short.md)] site, enter the base URL to the external system. [!INCLUDE[pn_microsoftcrm](../../includes/pn-microsoftcrm.md)] will append a search query string to the base URL you provide. [!INCLUDE[proc_more_information](../../includes/proc-more-information.md)] [Adding an external URL to search other sites](#addExternalURL)  
  
### See also  

---
title: "Offline and Outlook filters and templates (Microsoft Dataverse)| Microsoft Docs"
description: "Data that should be synchronized between the Microsoft Dataverse and Dynamics 365 for Outlook is determined by Data Filters for Office Outlook"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "sriharibs-msft" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Offline and Outlook filters and templates

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Data filters for Office Outlook  determine what data should be synchronized between the Microsoft Dataverse and Dynamics 365 for Outlook. Dataverse supports the ability to change the default filter using the SDK and push these changes to any or all users.  
You can write code that allows administrators to create and publish filter templates. This allows a Dataverse administrator to create common or desirable filters that can be published to users for synchronizing with the Outlook Store and offline database. This also provides a way to customize the default filter template that will be applied for users who are added to the system after the templates are originally published. The administrator also has the ability to update or delete user filters after they are published.  
To support these customizations, there are four new query types for saved query (view). When you create a saved query (view) record, specify one of these types in the `SavedQuery.QueryType` attribute, using the <xref:Microsoft.Crm.Sdk.SavedQueryQueryType> enumeration. These are only accessible by using the methods described here; there is no UI available to change them. You can specify different filters so that you can avoid synchronizing everything to Outlook for your mobile phone. Filter templates are solution aware so they can be exported along with a solution.  
  
 The following table lists the new query types used for filters and filter templates.  
  
|Query type|Description|  
|----------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OutlookFilters>|Defines the subset of an entity to be synchronized with Dynamics 365 for Outlook. The subset of data defined by these filters will synchronize to Outlook folders such as Contacts, Calendar, and so on.|  
|<xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OfflineFilters>|Defines the subset of an entity to be synchronized with Dynamics 365 for Microsoft Office Outlook with Offline Access. The subset of data defined by these filters will synchronize to the offline database.|  
|<xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OutlookTemplate>|Defines a filter template applied to new users for synchronization with Dynamics 365 for Outlook.|  
|<xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OfflineTemplate>|Defines a filter template applied to new users for synchronization with Dynamics 365 for Microsoft Office Outlook with Offline Access.|  
  
## Instantiate a filter

Default filter templates are automatically instantiated to the `UserQuery` entity for each user when the synchronization subscription is created. When synchronization to Outlook or to the offline database is initiated, the filters for that user are collected and used to filter the collections of entries and attributes that are being synchronized. If multiple filters are specified for a particular entity, the resulting set of entries will be a union of results of individual filters.  

There is a new privilege allowing the administrator to access other user's filters: `prvAdminFilter`. This is called Manage User Synchronization Filters in the Web application. The system administrator role includes this privilege because without it, only the user can see his or her filters. Calling the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method on the user query will retrieve records only for the owning user, unless the caller has the `prvAdminFilter` privilege The query must contain conditions where `QueryType` equals <xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OutlookFilters> or <xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OfflineFilters> AND `OwnerId` equals `UserId`, where the `UserId` is not equal to caller. If any other conditions are added to the query, this will not work.  

New users automatically are given the filters from the filter templates that are marked as default in the `SavedQuery.IsDefault` attribute. Administrators need to know that they can change this value to affect this. Each entity can have only one filter template that is marked as default. There can be no default filters, only filter templates. If you create a custom entity, and set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAvailableOffline> property, a default filter template is created automatically.  

There is a new type of filter that administrators can define, called system filters. These filters are defined as `SavedQuery` records with the query type of <xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OutlookFilters> or <xref:Microsoft.Crm.Sdk.SavedQueryQueryType.OfflineFilters>. System filters automatically apply to all users, and cannot be modified by the users.  

There is a limit on the number of filters you can add. This setting is controlled by the Dataverse deployment administrator to prevent users or administrators from creating too many filters, which affects server performance. The same limit setting is applied to all entities.  

By default, there are unlimited settings for both system filters and user filters.  

## Instantiate a template

You can instantiate one or more filters per user. To do this manually, use the <xref:Microsoft.Crm.Sdk.Messages.InstantiateFiltersRequest> to instantiate a filter, creating a user query record. Each user query record contains a reference back to the filter. If you update the filter, you can call instantiate again to refresh or override the user’s changes to the filter (user query record).  
  
## Reset a user’s filters to the default

You can reset the filters for a user to the default by using the <xref:Microsoft.Crm.Sdk.Messages.ResetUserFiltersRequest>.  
  
### See also

[Extend Dynamics 365 for Outlook](extend-dynamics-365-outlook.md)<br />
[SavedQuery Entity Reference](../reference/entities/savedquery.md)<br />
[Sample: Retrieve Outlook Filters](sample-create-retrieve-outlook-filters.md)<br /> 
<xref:Microsoft.Crm.Sdk.Messages.InstantiateFiltersRequest><br />
<xref:Microsoft.Crm.Sdk.Messages.ResetUserFiltersRequest>


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
---
title: "Open forms, views, and dashboards in Dynamics 365 mobile client with a URL (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the new application handler for Dynamics 365 mobile clients to directly link to Dynamics 365 forms, views, and dashboards from external applications so that when you click on the link in an external application, the target element opens in Dynamics 365 for phones or Dynamics 365 for tablets." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: mda-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Open forms, views, and dashboards in mobile client with a URL

Use the new application handler for mobile clients to directly link to forms, views, and dashboards from external applications so that when you click on the link in an external application, the target element opens in Dynamics 365 for phones or Dynamics 365 for tablets. You can also open an empty form for creating a table record.  
  
If you are already signed in to your instance in Dynamics 365 for phones or Dynamics 365 for tablets, the target record is displayed in the mobile client when you click the link in external application. Otherwise, you’re prompted to sign in to your instance in the mobile client, and upon doing so, the target element is displayed. You must have Dynamics 365 for phones or Dynamics 365 for tablets installed on your mobile device to use this feature.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]
  
<a name="Parameters"></a>

## Query string parameters for the URL

 Use the following application handler and query string parameters to compose the URL.  
  
```  
ms-dynamicsxrm://?pagetype=<VALUE>&etn=<VALUE>&id=<VALUE>  
```  
  
 The query string parameters shown in the following table are used.  
  
|Query string parameter|Description|  
|----------------------------|-----------------|  
|pagetype|Specify the page type to open. Valid values are `entity`, `view`, `dashboard`, and `create`.<br /><br /> This parameter is required.|  
|etn|Specify the logical name of the table for which you want to open or create a record.  Logical name of tables are in lowercase, and defined in the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName> property.<br /><br /> This parameter is required if the `pagetype` parameter is set to `entity`, `view`, or `create`.|  
|id|Specify the ID of the table, view, or dashboard record that you want to open.<br /><br /> This parameter is required if the `pagetype` parameter is set to `entity` or `dashboard`.<br /><br /> It is optional if the `pagetype` parameter is set to `view`. If you do not specify the view ID, the default view for the table specified in the `etn` parameter is displayed.|  
  
<a name="Example"></a>

## Example URLs

 Here are some example URLs for opening forms, views, and dashboards.  
  
|Action|Example URL|  
|------------|-----------------|  
|Open an account with account record ID as 91330924-802A-4B0D-A900-34FD9D790829|`ms-dynamicsxrm://?pagetype=entity&etn=account&id=91330924-802A-4B0D-A900-34FD9D790829`|  
|Open a view with the view record ID as 899D4FCF-F4D3-E011-9D26-00155DBA3819 for the contact table|`ms-dynamicsxrm://?pagetype=view&etn=contact&id=899D4FCF-F4D3-E011-9D26-00155DBA3819`|  
|Open a default view for the account table|`ms-dynamicsxrm://?pagetype=view&etn=account`|  
|Open a dashboard with the dashboard record ID as 2E3D0841-FA6D-DF11-986C-00155D2E3002|`ms-dynamicsxrm://?pagetype=dashboard&id=2E3D0841-FA6D-DF11-986C-00155D2E3002`|  
|Open a form for creating an account record|`ms-dynamicsxrm://?pagetype=create&etn=account`|  
  
### See also

 [Open forms, views, dialogs, and reports with a URL](open-forms-views-dialogs-reports-url.md)  
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
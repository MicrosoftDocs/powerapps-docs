---
title: "Actions on dashboards (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about performing actions such as create, retrieve, update, or delete, on organization-owned and user-owned dashboards." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 339eb79d-5dec-885b-496f-bfa26e9cae08
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Actions on dashboards

You can perform actions such as create, retrieve, update, or delete, on organization-owned and user-owned dashboards.  
  
## Actions on an organization-owned dashboard  

 To perform the following actions on an organization-owned dashboard (`SystemForm`), you must have the System Administrator or the System Customizer role assigned to your account in Microsoft Dataverse:  
  
- Create, retrieve, update, and delete. You can create or update an organization-owned dashboard by using the Dataverse web services or by customizing the form. For detailed information about creating a dashboard, see [Create a dashboard](create-dashboard.md).  
  
- Set an organization-owned dashboard as the default dashboard for an organization by setting the `SystemForm.IsDefault` value to `true` while creating or updating the dashboard.  
  
  > [!IMPORTANT]
  >  Using the methods available in the Dataverse Web Services, it is possible to set two dashboards as the default. Make sure that no other dashboard is the default dashboard for the organization before updating this setting programmatically.  
  
  After you update an organization-owned dashboard, you must publish the metadata changes to make it visible across the organization. You can use the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message or <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest> message to publish the changes made for an organization-owned dashboard. For a sample code that demonstrates this, see [Sample: Create, retrieve, update, and delete (CRUD) a dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsDashboard).  
  
  For a list of supported messages on the organization-owned dashboard table, see [SystemForm table](../data-platform/reference/entities/systemform.md).  
  
[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Actions on a user-owned dashboard  

 You can perform the following actions on a user-owned dashboard (`UserForm`):  
  
- Create, retrieve, update, and delete. For detailed information about creating a user-owned dashboard, see [Create a dashboard](create-dashboard.md).  
  
- Change the ownership of a user-owned dashboard by assigning it to another user or team using the <xref:Microsoft.Crm.Sdk.Messages.AssignRequest> message.  
  
- Retrieve the access that the specified security principal (user or team) has to a user-owned dashboard using the <xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest> message. You can also retrieve all the security principals (users or teams) that have access to a user-owned dashboard, along with their access rights to the user dashboard using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest> message.  
  
- Collaborate with other users and teams on specific areas by sharing a user-owned dashboard with them using the <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>, <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>, and <xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest> messages.  
  
  For a list of supported messages on the user-owned dashboard table, see [UserForm table](../data-platform/reference/entities/userform.md).  
  
### See also  

 [Dashboards for Microsoft Dataverse](analyze-data-with-dashboards.md)   
 [Using FormXML for dashboards](understand-dashboards-dashboard-components-formxml.md)   
 [Create a dashboard](create-dashboard.md)   
 [Sample dashboards](sample-dashboards.md)     
 [Sample: Create, retrieve, update, and delete (CRUD) a dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsDashboard)  
 [Sample: Assign a user-owned dashboard to another user](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssignUserOwnedDashboardToAnother)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
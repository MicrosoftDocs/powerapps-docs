---
title: "Field security entities (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using field security entities to apply field-level security, which restricts field access to specified users and teams." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Field security tables

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You use field security tables to apply field-level security, which restricts field access to specified users and teams. The scope of field-level security is global, which means that it applies to all records within the organization, regardless of the business unit hierarchical level to which the record or the user belongs. Field security works in all Microsoft Dataverse clients, including the Web client, Dynamics 365 for Outlook, and Dynamics. It applies to all components, such as the Dataverse web services, reports, search, offline, filtered views, auditing, and duplicate detection. For this release, field security can be applied to both custom fields and many out-of-box (OOB) fields.    
  
> [!IMPORTANT]
>  Field-level security profiles prevent unintended users from getting access to Dataverse data based on the profile definitions. If the SQL Server ACLs are misconfigured, or if there is a SQL injection issue, adversaries can get direct access to data in SQL Server thereby bypassing field level security restrictions. For more information, see [Overview of Web Application Security Threats](/previous-versions/f13d73y6(v=vs.140)).  
  
<a name="bkmk_setup"></a>   

## Set up and use field security  
 To use field security you must do the following:  
  
1. Create a field security profile record.  
  
2. Add users or teams to the profile.  
  
3. Find a columns that can be secured at the field level.  
  
4. Secure the column, either when you create the column or by updating the column definition.  
  
5. Publish the customizations.  
  
6. Create a field permission record that defines what access (create, update, read) the profile will have for the custom column.  
  
   For sample code about how to perform these steps, see [Sample: Enable Field Security For An Entity](org-service/samples/enable-field-security-entity.md).  
  
   Use the following field permission columns to set whether the specified field security profile can create, read, or update a column. 
   You can set or compare the value for these columns by using the `field_security_permission_type` global choice:  
  
-   `FieldPermission`.`CanCreate`  
  
-   `FieldPermission`.`CanRead`  
  
-   `FieldPermission`.`CanUpdate`  
  
> [!IMPORTANT]
>  If low privilege users are given Read access to the field security profile entity, they can see what profiles other users have and find other users with access to secured attributes they are interested in. They can then use social engineering techniques to get assigned a profile with access to those secured attributes.  
  
<a name="bkmk_whichattributes"></a>   

## Which attributes can be secured?  
 To see which columns can be secured, you can query the table definition for the following properties:  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForCreate>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForRead>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForUpdate>  
  
  There are a few additional rules that apply to certain attribute data types:  
  
- Boolean attributes can be secured for create and update operations but not for read.  
  
- Option set attributes can be secured for create, update, and read when a default value is unspecified.  
  
  There are thousands of columns that can be secured, so there are two easier ways to look for this information. To view the table definition for your organization, install the Table definition browser solution described in [Browse table definition in your environment](browse-your-metadata.md). You can also browse the reference documentation for entities in the [Table/entity reference](reference/about-entity-reference.md).  
  
<a name="bkmk_sharing"></a>   
## Share secured fields  
 You can share secured fields much as you can share records. To do this, you create, update, or delete a `PrincipalObjectAttributeAccess` (field sharing) record, where you specify the user or team, the entity, and the permissions.  
  
 The following table lists the corresponding methods for securing a field compared to securing a record.  
  
|Record sharing|Field access sharing|  
|--------------------|--------------------------|  
|Use the <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest> message to grant record access for a user or team.|Use the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message or the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method to grant secured field access for a user or team.|  
|Use the <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest> message to update record access for a user or team.|Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message or the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method to update secured field access for a user or team.|  
|Use the <xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest> message to remove record access for a user or team.|Use the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> message or the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method to remove secured field access for a user or team.|  
  
### See also  
 [Security and data access](security-model.md)   
 [FieldSecurityProfile Entity](reference/entities/fieldsecurityprofile.md)   
 [FieldPermission Entity](reference/entities/fieldpermission.md)   
 [PrincipalObjectAttributeAccess Entity](reference/entities/principalobjectattributeaccess.md)    
 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

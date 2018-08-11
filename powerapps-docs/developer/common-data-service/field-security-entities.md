---
title: "Field security entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using field security entities to apply field-level security, which restricts field access to specified users and teams." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Field security entities

You use field security entities to apply field-level security, which restricts field access to specified users and teams. The scope of field-level security is global, which means that it applies to all records within the organization, regardless of the business unit hierarchical level to which the record or the user belongs. Field security works in all Common Data Service for Apps clients, including the Web client, Dynamics 365 for Outlook, and Dynamics. It applies to all components, such as the CDS for Apps web services, reports, search, offline, filtered views, auditing, and duplicate detection. For this release, field security can be applied to both custom fields and many out-of-box (OOB) fields.  
  
 For more information about how secured fields change the behavior of methods, see [How Field Security Can Be Used to Control Access to Field Values in Dynamics 365](security-dev/use-field-security-control-access-field-values.md).  
  
> [!IMPORTANT]
>  Field-level security profiles prevent unintended users from getting access to CDS for Apps data based on the profile definitions. If the SQL Server ACLs are misconfigured, or if there is a SQL injection issue, adversaries can get direct access to data in SQL Server thereby bypassing field level security restrictions. For more information, see [Overview of Web Application Security Threats](https://msdn.microsoft.com/library/f13d73y6.aspx).  
  
<a name="bkmk_setup"></a>   

## Set up and use field security  
 To use field security you must do the following:  
  
1. Create a field security profile record  
  
2. Add users or teams to the profile  
  
3. Find an attribute that can be secured at the field level  
  
4. Secure the attribute, either when you create the attribute or by updating the attribute metadata  
  
5. Publish the attribute customizations  
  
6. Create a field permission record that defines what access (create, update, read) the profile will have for the custom attribute  
  
   For sample code about how to perform these steps, see [Sample: Enable Field Security For An Entity](/dynamics365/customer-engagement/developer/sample-enable-field-security-entity).  
  
   Use the following field permission attributes to set whether the specified field security profile can create, read, or update an attribute. 
   You can set or compare the value for these attributes by using the `field_security_permission_type` global option set:  
  
-   `FieldPermission`.`CanCreate`  
  
-   `FieldPermission`.`CanRead`  
  
-   `FieldPermission`.`CanUpdate`  
  
> [!IMPORTANT]
>  If low privilege users are given Read access to the field security profile entity, they can see what profiles other users have and find other users with access to secured attributes they are interested in. They can then use social engineering techniques to get assigned a profile with access to those secured attributes.  
  
<a name="bkmk_whichattributes"></a>   

## Which attributes can be secured?  
 To see which attributes can be secured, you can query the entity metadata for the following properties:  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForCreate>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForRead>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanBeSecuredForUpdate>  
  
  There are a few additional rules that apply to certain attribute data types:  
  
- Boolean attributes can be secured for create and update operations but not for read.  
  
- Option set attributes can be secured for create, update, and read when a default value is unspecified.  
  
  There are thousands of attributes that can be secured, so there are two easier ways to look for this information. To view the entity metadata for your organization, install the Metadata Browser solution described in [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata). You can also browse the reference documentation for entities in the [Entity Reference](/dynamics365/customer-engagement/developer/about-entity-reference).  
  
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
 [The Security Model of Dynamics 365](/dynamics365/customer-engagement/developer/security-dev/security-model)   
 [Administration and security entities](/dynamics365/customer-engagement/developer/administration-security-entities)   
 [FieldSecurityProfile Entity](/reference/entities/fieldsecurityprofile.md)   
 [FieldPermission Entity](/reference/entities/fieldpermission.md)   
 [PrincipalObjectAttributeAccess Entity](/reference/entities/principalobjectattributeaccess.md)   
 [Field-level data encryption](field-level-data-encryption.md)   
 [Sample: Retrieve Field Permissions](/dynamics365/customer-engagement/developer/sample-retrieve-field-permissions)   
 [Sample: Enable Field Security For An Entity](/dynamics365/customer-engagement/developer/sample-enable-field-security-entity)   
 [Sample: Retrieve Field Sharing Records](/dynamics365/customer-engagement/developer/sample-retrieve-field-sharing-records)
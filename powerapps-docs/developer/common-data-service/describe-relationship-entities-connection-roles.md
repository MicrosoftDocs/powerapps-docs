---
title: "Describe a relationship between entities with connection roles (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describing a relationship between entities using create connection roles and connection role categories." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Describe a relationship between entities with connection roles

You can describe the relationship between records through the roles that you assign to them.  
  
 There are several ways you can use the connection roles in a connection:  
  
-   Apply the same role to the source record and to the target record. A “friend”, a “team member”, or a “colleague” are examples of roles that could be applied to both records in the connection.  
  
-   Apply a role to the source record or to the target record, but not to both. A “salesperson” role in a contact to opportunity connection is an example of such role. The records, such as opportunity, invoice, or sales order usually contain sufficient information about what they represent and do not require a role assigned to them.  
  
-   Apply two matching roles (sometimes referred to as reciprocal roles). One role applies to a source record and the other role applies to a target record. A “doctor” and a “patient”, a “parent” and a “child” are examples of matching roles.  
  
## Connection Role Categories  
 When you create connection roles, you can specify what category they belong to. For example, you can use the following categories:  
  
- Business (supplier, buyer, competitor)  
  
- Family (father, sister, cousin)  
  
- Social (tennis partner, club member, friend)  
  
  The category list is customizable. You can add the categories that best fit your business model.  
  
## Create Connection Roles  
 To create a connection role you must specify the following information:  
  
- Use the `ConnectionRole.Name` attribute to specify a role name.  
  
- Use the `ConnectionRole.Description` attribute to add a role description.  
  
- Use the `ConnectionRole.Category` attribute to specify a role category. The possible values for this attribute are defined in the `connectionrole_category` global option set.  
  
- When you create a connection role, you can specify an entity type that the role will be applied to, such as lead, account, or competitor. If you do not specify a particular entity type, then you can apply a connection role to all CDS for Apps entities. To specify the entity type, use the `ConnectionRoleObjectTypeCode.AssociatedObjectTypeCode` attribute. To link the connection role to a particular entity type, use the `ConnectionRoleObjectTypeCode.ConnectionRoleId` attribute. A connection role record can be referenced by multiple connection role object type code records. If you remove all references to the connection role record, you can apply this connection role to all CDS for Apps entities.  
  
  > [!TIP]
  >  To find the connection roles for an account entity, in the query, specify all roles that are linked to the account entity (Entity Type Code = 1) or to all entities (Entity Type Code = 0).  
  
## Associate and Disassociate Connection Roles  
 To associate the roles in the connection, use the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*> method. To disassociate the roles, use the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*> method. For more information about the `Associate` message and the `Disassociate` message, see [Introduction to Entities in Dynamics 365](/dynamics365/customer-engagement/developer/introduction-entities).  
  
### See also  
 [Connection Entities](connection-entities.md)   
 [Sample Code for Connection Entities](/dynamics365/customer-engagement/developer/sample-code-connection-entities)   
 [Sample: Create Reciprocal Connection Role (Early Bound)](/dynamics365/customer-engagement/developer/sample-create-reciprocal-connection-role-early-bound)   
 [Connection Entity](/reference/entities/connection.md)
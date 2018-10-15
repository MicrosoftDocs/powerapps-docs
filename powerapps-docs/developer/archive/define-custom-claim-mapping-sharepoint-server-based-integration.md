---
title: "Define custom claim mapping for SharePoint server-base integration (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Define custom claim mapping for SharePoint server-based integration

For server-based integration with SharePoint, CDS for Apps uses claims to authenticate and authorize Common Data Service for Apps users to access the documents stored in SharePoint. For more information about claims-based authentication, see [Claims-based identity in SharePoint 2013](https://msdn.microsoft.com/library/office/ee535242.aspx).  

 By default, CDS for Apps uses the following claims  to integrate with SharePoint:  


|                                                                              Scenario                                                                               |                                                                                                                                              Claims                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      CDS for Apps and SharePoint Online      |                                                   `NameId (PUID)`<br /><br /> Both Dynamics 365 and SharePoint share Azure Active Directory for user identity.                                                   |
| CDS for Apps and SharePoint on-premises | `SMTP (email)`<br /><br /> No shared active directory infrastructure for user identity; claims sent as SMTP address. The claims is picked from WindowsLiveID field in Dynamics 365 and mapped to work email address from SharePoint. |
|                                Dynamics 365 on-premises and SharePoint Online                                |                            `SMTP (email)`<br /><br /> No shared active directory infrastructure for user identity; claims sent as SMTP address. The claims is picked from PrimaryEmailAddess field in Dynamics 365 and mapped to work email address from SharePoint.                             |
|                           Dynamics 365 on-premises and SharePoint on-premises                           |                                                                           `Security Identifier (SID)`<br /><br /> Both Dynamics 365 and SharePoint share Microsoft Windows Server Active Directory for user identity.                                                                            |

 You can use the `UserMapping` entity to specify custom claim mappings in CDS for Apps to use a value other than the default value used by CDS for Apps to authenticate and authorize CDS for Apps users in SharePoint. For example, you can use the “last name” and “first name” of the user instead of “email” to authenticate CDS for Apps users in SharePoint. Custom claim mappings override the default claim mappings used by CDS for Apps. You can define multiple custom claim mappings in CDS for Apps. By default, only users having the System Administrator role have access to the `UserMapping` entity.  

 To define a custom claim mapping in CDS for Apps, create a `UserMapping` entity record, and specify the attribute values listed in the following table.  


|               Attribute               |                                                                     Value                                                                      |                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UserMapping.PartnerApplicationType`  | -   `0`: SharePoint<br />-   `1`: For internal use only. |                                                                                                                                                                                     The partner application type for which this claim mapping is to be used. In the current release, only `0` (SharePoint) is supported.                                                                                                                                                                                      |
| `UserMapping.SystemUserAttributeName` |                                                                  String value                                                                  | The logical name of the attribute in the `SystemUser` (user) entity from where the value for the claims will be used. **Note:**  If the attribute used for custom claim mapping doesn’t contain a value, the default claim mapping is used by CDS for Apps. For example, if you want to use the first name of the user as the attribute for custom claim mapping and a user’s first name is missing, CDS for Apps will use the default claim mapping (PUID or email). |
|        `UserMapping.ClaimType`        |                                                                  String value                                                                  |                     Specify the claim type to be sent to SharePoint. For a list of claim types, see [ClaimTypes Members](https://msdn.microsoft.com/library/microsoft.identitymodel.claims.claimtypes_members.aspx). **Note:**  The referred claim type list is just for reference. All the claim types listed there might not be supported by SharePoint, or might not contain all the claim types supported by SharePoint.                      |

 The following sample code shows how to define a custom claim mapping using the `UserMapping` entity.  

```csharp
UserMapping customMapping = new UserMapping  
{  
   PartnerApplicationType = new OptionSetValue(0),  
   SystemUserAttributeName = "personalemailaddress",  
   ClaimType = "smtp"  
};  
_serviceProxy.Create(customMapping);  
```  

> [!NOTE]
>  Any instance of the `UserMapping` entity with valid values will override the default claim mappings used by CDS for Apps.  

 By default, SharePoint supports the following claim types: NameId (PUID), SMTP (email), and UPN (user principal name). If you’re passing a claim of any other type, you must also create corresponding claim type mappings in SharePoint. More information: [New-SPClaimTypeMapping](https://technet.microsoft.com/library/ff607650.aspx)  

### See Also
 [UserMapping Entity](reference/entities/usermapping.md)   
 [Integrate Microsoft Dynamics 365 with SharePoint](integrate-sharepoint.md)

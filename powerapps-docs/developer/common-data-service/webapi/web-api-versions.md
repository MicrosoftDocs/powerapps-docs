---
title: "Common Data Service Web API Versions (Common Data Service)| Microsoft Docs"
description: "Read how versioning of Common Data Service Web API works. Common Data Service Web API versions support version specific differences in the same environment which is different from the behavior in the v8.x releases in which new capabilities were additive"
ms.custom: ""
ms.date: 07/25/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d9bb79a5-2bfa-4ffe-8cb4-60f192359489
caps.latest.revision: 34
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Common Data Service Web API Versions

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Beginning with the v9.0 release of Dynamics 365, the Web API supports version specific differences in the same environment.  
  
This is different from the behavior for in the v8.*x* releases. In the previous releases new capabilities were available to any version of the service depending on the update applied to the environment.  After an upgrade to v8.2, the v8.0, and v8.1 services were all identical. This was possible because all the changes were additive. Nothing was removed or introduced breaking changes. As a result, the specific version referenced in the service URL for the v8.*x* wasn't actually important.  
  
Going forward the capabilities of the service can change, including potentially breaking changes such as removing specific operations. This will allow for improvements to be applied on an on-going basis. This topic will record any version specific differences and any limitations where the Web API hasn't yet achieved parity with the organization service.  
  
## Web API version specific differences

<a name="BKMK_fetchresponse"></a>

### Encoding for special characters in FetchXML query response

For v8.*x* versions, response of FetchXML queries containing link-entities and their attributes contains Unicode special characters such that '.' becomes '_x002e_' and '@' becomes '_x0040_'. This encoding for special characters is not present in response of FetchXML queries for v9.*x* release.

### Same name for entity and attribute

If the name of an entity and one of its attributes is same, then "1" gets appended to the attribute name in v8.x instances. For example, if an entity **new_zipcode** has an attribute with name as **new_zipcode** then, the attribute name will change to **new_zipcode1**.

For v9.*x* instances, nothing gets appended to the attribute name.

## New operations added  

The following operations have been added to the Web API for the v9.x release.  
  
|Operations|Operations (cont'd)|Operations (cont'd)|  
|-|-|-|  
|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|  

## Web API Limitations  

The Common Data Service Web API provides complete parity with the capabilities of the organization service. For Common Data Service, this topic describes the limitations carried forward from the Common Data Service v8.x release. For earlier releases, see [Dynamics CRM 2016 Web API Limitations](https://msdn.microsoft.com/library/mt628816\(CRM.8\).aspx).  
 
> [!NOTE] 
> If you defined a custom action which included a complex return value and a simple return value, a corresponding Action was not available in the Web API but was available using the 2011 SOAP endpoint. A complex return value is an `EntityReference`, `Entity`, or `EntityCollection`. You can have any combination of simple return values or a single complex return value. More information: [Create your own actions](/dynamics365/customer-engagement/developer/create-own-actions).

### See also  

[Use the Common Data Service Web API](overview.md)<br />
[Authenticate to Common Data Service with the Web API](authenticate-web-api.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)
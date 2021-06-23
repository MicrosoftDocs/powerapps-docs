---
title: "Microsoft Dataverse Web API versions (Dataverse)| Microsoft Docs"
description: "Read how versioning of Microsoft Dataverse Web API works. Dataverse Web API versions support version specific differences in the same environment which is different from the behavior in the v8.x releases in which new capabilities were additive"
ms.custom: ""
ms.date: 06/14/2021
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
# Microsoft Dataverse Web API Versions

Beginning with the v9.0 release of Dynamics 365, the Web API supports version specific differences in the same environment.  
  
This is different from the behavior for in the v8.*x* releases. In the previous releases new capabilities were available to any version of the service depending on the update applied to the environment.  After an upgrade to v8.2, the v8.0, and v8.1 services were all identical. This was possible because all the changes were additive. Nothing was removed or introduced breaking changes. As a result, the specific version referenced in the service URL for the v8.*x* wasn't actually important.  
  
Going forward the capabilities of the service can change, including potentially breaking changes such as removing specific operations. This will allow for improvements to be applied on an on-going basis. This topic will record any version specific differences and any limitations where the Web API hasn't yet achieved parity with the organization service.  

> [!NOTE]
> While the v9.x releases can support specific differences, there have been no breaking changes added to v9.0, v9.1, or v9.2 releases. Each of these releases are have identical Web API behaviors.
>
> Differences in API behavior is driven more by the solutions installed in the system rather than version of the product. However, if we need to make a fundamental change that is not backward compatible, it will be included in a new version number.
>
> **Guidance**: Use the version number that was current when your code was written. Do not automatically use a newer version without looking for documented differences here and testing. Do not assume a newer version wll be fully backward compatible.
  
## Web API version specific differences

The differences below refer to changes in the v8.2 and v9.0 versions of the Web API.

<a name="BKMK_fetchresponse"></a>

### Encoding for special characters in FetchXML query response

For v8.*x* versions, response of FetchXML queries containing link-entities and their attributes contains Unicode special characters such that '.' becomes '_x002e_' and '@' becomes '_x0040_'. This encoding for special characters is not present in response of FetchXML queries for v9.*x* release.

### Same name for table and column

If the name of a table (entity) and one of its columns (attributes) is the same, then "1" gets appended to the attribute name in v8.x instances. For example, if an entity **new_zipcode** has an attribute with name as **new_zipcode** then, the attribute name will change to **new_zipcode1**.

For v9.*x* instances, nothing gets appended to the attribute name.

## New operations added  

The following operations have been added to the Web API for the v9.x release.  
  
|Operations|Operations (cont'd)|Operations (cont'd)|  
|-|-|-|  
|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|  

## Web API Limitations  

The Dataverse Web API provides complete parity with the capabilities of the Organization service. For Dataverse, this topic describes the limitations carried forward from the Dataverse v8.x release. For earlier releases, see [Dynamics CRM 2016 Web API Limitations](https://msdn.microsoft.com/library/mt628816\(CRM.8\).aspx).  
 
> [!NOTE] 
> If you defined a custom action which included a complex return value and a simple return value, a corresponding Action was not available in the Web API but was available using the 2011 SOAP endpoint. A complex return value is an `EntityReference`, `Entity`, or `EntityCollection`. You can have any combination of simple return values or a single complex return value. More information: [Create your own actions](/dynamics365/customer-engagement/developer/create-own-actions).

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Authenticate to Dataverse with the Web API](authenticate-web-api.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
---
title: "Microsoft Dataverse Web API Versions"
description: "Learn how Microsoft Dataverse Web API versioning works, including version-specific differences and breaking changes starting with v9.0 release."
ms.date: 03/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Microsoft Dataverse Web API versions

Starting with the v9.0 release of Dynamics 365, the Web API supports version-specific differences in the same environment.  
  
This support differs from the behavior in the v8.*x* releases. In the previous releases, new capabilities were available to any version of the service depending on the update applied to the environment. After an upgrade to v8.2, the v8.0, and v8.1 services were all identical. This was possible because all the changes were additive. Nothing was removed or introduced breaking changes. As a result, the specific version referenced in the service URL for the v8.*x* wasn't actually important.    
  
Going forward, the capabilities of the service can change, including potentially breaking changes such as removing specific operations. This change allows for improvements to be applied on an on-going basis. This topic records any version-specific differences and any limitations where the Web API hasn't yet achieved parity with the SDK for .NET.  

> [!NOTE]
> While the v9.x releases can support specific differences, the v9.0, v9.1, and v9.2 releases don't include any breaking changes. Each of these releases has identical Web API behaviors.
>
> Differences in API behavior are driven more by the solutions installed in the system rather than version of the product. However, if Microsoft needs to make a fundamental change that isn't backward compatible, it includes the change in a new version number.
>
> **Guidance**: Use the version number that was current when you wrote your code. Don't automatically use a newer version without looking for documented differences and testing. Don't assume a newer version is fully backward compatible.
  
## Web API version specific differences

The following differences refer to changes in the v8.2 and v9.0 versions of the Web API.

<a name="BKMK_fetchresponse"></a>

### Encoding for special characters in FetchXML query response

For v8.*x* versions, the response to FetchXML queries that contain link-entities and their attributes includes Unicode special characters such that '.' becomes '_x002e_' and '@' becomes '_x0040_'. This encoding for special characters isn't present in the response to FetchXML queries for v9.*x* release.

### Same name for table and column

If the name of a table (entity) and one of its columns (attributes) is the same, the system appends "1" to the attribute name in v8.x instances. For example, if an entity **new_zipcode** has an attribute with the name **new_zipcode**, the attribute name changes to **new_zipcode1**.

For v9.*x* instances, the system doesn't append anything to the attribute name.

## New operations added  

The following operations are added to the Web API for the v9.x release.  
  
:::row:::
   :::column:::
      <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>
   :::column-end:::
:::row-end:::

## Web API limitations  

The Dataverse Web API provides complete parity with the capabilities of the SDK for .NET. For Dataverse, this topic describes the limitations carried forward from the Dataverse v8.x release. For earlier releases, see [Dynamics CRM 2016 Web API Limitations](/previous-versions/dynamicscrm-2016/developers-guide/mt628816(v=crm.8)).  
 
> [!NOTE] 
> If you define a custom action that includes both a complex return value and a simple return value, the Web API doesn't provide a corresponding action. However, the Organization service provides this action. A complex return value is an `EntityReference`, `Entity`, or `EntityCollection`. You can have any combination of simple return values or a single complex return value. For more information, see [Create your own messages](../custom-actions.md).

### See also  

[Use the Dataverse Web API](overview.md)   
[Authenticate to Dataverse with the Web API](authenticate-web-api.md)   
[Web API types and operations](web-api-types-operations.md)   
[Perform operations using the Web API](perform-operations-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

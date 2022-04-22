---
title: "AADUser table request examples (Microsoft Dataverse)| Microsoft Docs"
description: "This collection of code samples demonstrates how to send HTTP requests for common AAD user table operations using the Microsoft Dataverse Web API."
ms.date: 04/22/2022
author: nhelgren
ms.author: nhelgren
ms.reviewer: pehecke
manager: sunilg
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# AADUser table request examples

This article contains HTTP request examples for accessing data from the AADUser table.

## Retrieving data

The following example demonstrate retrieving data from the AADUser table.

**Retrieve all AADUser table rows**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers  
```

**Retrieve AADUser records with surname 'admin'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=surname eq 'admin'
```

**Retrieve AADUser records with surname 'admin' or 'admin02'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=(surname eq 'Admin02') or (surname eq 'Admin')
```

**Retrieve AADUser records whose companyname is not null**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=companyname ne null
```

**Retrieve AADUser records whose usertype is 'Member'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=usertype eq 'Member'
```

**Retrieve AADUser records whose businessphones contains is '123-555-1212'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=contains(businessphones, '123-555-1212')
```

**Retrieve AADUser records whose givenname starts with 'test'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=startswith(givenname, 'test')
```

**Retrieve AADUser records whose givenname does NOT starts with 'test'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=not startswith(givenname, 'test')
```

**Retrieve related Account records that referencing an AADUser record**  
Below, "new_aaduser_account" is the name of the 1:N relationship between AADUser and the Account entity.

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers(<user ID>)?$expand=new_aaduser_account($select=accountid,name)
```

## Referencing an AADUser row

The following example demonstrates referencing an AADUser table row.

**Set lookup field value referencing an AADUser row**  
In this example "new_testaaduserId" is the ReferencingNavigationPropertyName of the 1:N relationship between AADUser and Account entity.

```http
PATCH
https://[Organization URI].crm.dynamics.com/api/data/v9.0/accounts(<account ID>)
{
  new_testaaduserId@odata.bind : "/aadusers(user ID)"
}
```

### See also

[Azure Active Directory user table](../aaduser-entity.md)  
[aaduser table/entity reference](../reference/entities/aaduser.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
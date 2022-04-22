---
title: "AAD user table Web API samples (Microsoft Dataverse)| Microsoft Docs"
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

# AAD user table Web API samples

This article contains HTTP request examples for accessing data from the AAD user table.

## Retrieving data

The following example demonstrate retrieving data from the AAD user table.

**Retrieve all AAD user table rows**

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

**title**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers
```

### See also

[Azure Active Directory user table](../aaduser-entity.md)  
[aaduser table/entity reference](../reference/entities/aaduser.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
---
title: "Security roles and templates (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Microsoft Dataverse provides security roles that can be assigned to system users allowing or restricting access to table data. In addition, standard templates provide a means to obtain security roles that are valid across environments."
ms.custom: intro-internal
ms.date: 11/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "paulliew" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Security roles and templates

You should use <!-- Add xref -->`RoleTemplateId` when you try to lookup or process Microsoft Dataverse security roles.  These role template IDs are unique and constant in all environments.  If you try to use role IDs, a failure can occur because the role IDs are not unique for a given security role.

> [!IMPORTANT]
> A security role can exist in the root business unit (BU) and replicated to different BU's, and therefore the role ID is not unique across environments.

More information: [Environments with a Dataverse database](/power-platform/admin/database-security#environments-with-a-dataverse-database)

## Standard role templates

Below is a list of standard role template GUIDs that exist in all environments.

```csharp
public const string SystemAdmin = "{627090FF-40A3-4053-8790-584EDC5BE201}";
public const string Customizer = "{119F245C-3CC8-4b62-B31C-D1A046CED15D}";
public const string Support = "{2D101BB3-5CED-4122-83F1-94D5EFDE4E3B}";
public const string Proxy = "{D892CC0B-28C7-4e88-BD92-72F2C366BAED}";
public const string CDSUser = "{236750CD-45AE-4939-AB12-B24B920CED93}";
public const string BizMgr = "{85937B6B-91A1-46ED-9778-929FC9F61812}";
public const string VPSales = "{29123793-6AE5-4955-9F1A-F10CEB9705F1}";
public const string SalesMgr = "{C0ED2F4F-6F92-4691-92BA-78F2931E8FBA}";
public const string SalesRep = "{A4BE89FF-7C35-4D69-9900-999C3F603E6F}";
public const string CSR = "{ECFD0B44-5720-45E3-AE68-417DDB0FB654}";
public const string CSRMgr = "{1808B939-DD07-4CA7-AA99-DDD2734378F1}";
public const string MarketingProfessional = "{09A25608-D28B-4D47-B57C-79271FE6A525}";
public const string ScheduleMgr = "{DEBEC338-BCA7-4882-AE04-84E6DDDA2984}";
public const string VPMarketing = "{6CABA073-59A8-4D6B-8E7B-4CCB50C5166B}";
public const string MarketingMgr = "{D9D602DB-2761-4170-877F-983494567C08}";
public const string Scheduler = "{DCD60B89-421C-44ae-BFF0-DD6323DF885C}";
public const string KnowledgeMgr = "{B4B40B17-CF37-4EA8-B2C5-B580F2F48654}";
```

## Using the role templates

Let's take a look at some code that demonstrate use of the role templates.

<!-- Web API snippet -->
This Web API request returns a System Administrator role using the template. The parameters in <> are left for you to fill in.

```http
http://<env-name>.api.<region>.dynamics.com/api/data/v9.1/roles(_roletemplateid_value=627090FF-40A3-4053-8790-584EDC5BE201,_businessunitid_value=<bu-ID>,componentstate=0,overwritetime=1900-01-01T00:00:00Z)
```

This HTTP request is returning a role for role IDs that are constant like the EnvironmentMaker role. Use this request for roles not having a role template.
  
```http
http://<env-name>.api.<region>.dynamics.com/api/data/v9.1/roles(_parentrootroleid_value=<role-ID>,_businessunitid_value=<bu-ID>,componentstate=0,overwritetime=1900-01-01T00:00:00Z)
```

### See also

[Configure user security to resources in an environment](/power-platform/admin/database-security)
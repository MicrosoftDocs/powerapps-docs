---
title: Terminology changes in Power Apps portals | Microsoft Docs
description: Learn about the changes to terms used in Power Apps portals, and changes from Microsoft Dataverse.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/26/2021
ms.author: sandhan
ms.reviewer: tapanm
searchScope:
  - "Power Apps"
---

# Terminology changes in Power Apps portals

## Overview

Effective November 2020, Common Data Service has been renamed to Microsoft Dataverse. More information: [Common Data Service is now Microsoft Dataverse](https://aka.ms/PAuAppBlog). Some terminology in Microsoft Dataverse has also been updated. For example, *entity* is now *table* and *field* is now *column*. More information: [Terminology updates in Dataverse](https://go.microsoft.com/fwlink/?linkid=2147247)

Based on the terminology changes in Dataverse, customer feedback, and data from user research, effective March 2021, we're updating some terminology in Power Apps portals to be more intuitive and make its usage more productive. The terminology updates are listed below, and we're in the process of rolling them out across Microsoft Power Platform.

> [!IMPORTANT]
> We're in the process of rolling out the terminology changes for Power Apps portals interface, Power Apps portals Studio, Portal Management app, and [Power Apps](https://make.powerapps.com). During this process, your environment may show legacy or current terminology depending on the rollout stage. Power Apps portals articles will be updated soon to reflect the latest terminology.

## Key terminology changes for portals

The following table lists key terminology changes in portals.

| Legacy term | Current term |
| - | - |
| Entity form | Basic form |
| Web form | Advanced form |
| Entity list | List |
| Entity permission | Table permission |
| Entity Name | Table Name |

All references to the key terminology changes are going to be updated including Power Apps portals inteface, Portal Management app, portals Studio, and [Power Apps](https://make.powerapps.com).

## Terminology changes inside Portal Management app

Terminology updates apply to references of legacy terms. For example, if the legacy term used in the user interface is "Enable search on entity list", the term is updated to "Enable search on list" as "entity list" is the legacy term, and "list" is the current term.

The following table includes terminology changes inside Portal Management app.

| Feature area or location of the term used | Legacy term | Current term |
| - | - | - |
| View name for Entity List  | Active Entity Lists | Active Lists |
| View name for Entity List | Entity List Advanced Find View | List Advanced Find View |
| View name for Entity List | Entity List Associated View | List Associated View |
| View name for Entity List | Entity List Lookup View | List Lookup View |
| View name for Entity List | Inactive Entity Lists | Inactive Lists |
| View name for Entity List | Quick Find Active Entity Lists | Quick Find Active Lists |
| Entity Permission | Scope | Access Type |
| View name for Entity Permission | Active Entity Permissions | Active Table Permissions |
| View name for Entity Permission | Child Entity Permissions | Child Table Permissions |
| View name for Entity Permission | Entity Permissions Advanced Find View | Table Permission Advanced Find View |
| View name for Entity Permission | Entity Permission Associated View | Table Permission Associated View |
| View name for Entity Permission | Entity Permission Lookup View | Table Permission Lookup View |
| View name for Entity Permission | Inactive Entity Permissions | Inactive Table Permissions |
| View name for Entity Permission | Quick Find Active Entity Permissions | Quick Find Active Table Permissions |
| View name for Entity Form | Active Entity Forms | Active Basic Forms |
| View name for Entity Form | Entity Form Advanced Find View | Basic Form Advanced Find View |
| View name for Entity Form | Entity Form Associated View | Basic Form Associated View |
| View name for Entity Form | Entity Form Lookup View | Basic Form Lookup View |
| View name for Entity Form | Inactive Entity Forms | Inactive Basic Forms |
| View name for Entity Form | Quick Find Active Entity Forms | Quick Find Active Basic Forms |
| View name for Web Form | Active Web Forms | Active Advanced Forms |
| View name for Web Form | Inactive Web Forms | Inactive Advanced Forms |
| View name for Web Form | Quick Find Active Web Forms | Quick Find Active Advanced Forms |
| View name for Web Form | Web Form Advanced Find View | Advanced Form Advanced Find View |
| View name for Web Form | Web Form Associated View | Advanced Form Associated View |
| View name for Web Form | Web Form Lookup View | Advanced Form Lookup View |
| Checkbox for Entity Permission | Enable Entity Permission | Enable Table Permission | Lookup label for Parent Entity Permission | Parent Entity Permission | Parent Table Permission |
| Tab name for entity reference | Entity Reference | Associated Table Reference |
| Metadata for Entity Form | Entity Form Metadata | Basic Form Metadata |
| View name for Entity Form Metadata | Active Entity Form Metadata | Active Basic Form Metadata |
| View name for Entity Form Metadata | Entity Form Metadata Advanced Find View | Basic Form Metadata Advanced Find View |
| View name for Entity Form Metadata | Entity Form Metadata Associated View | Basic Form Metadata Associated View |
| View name for Entity Form Metadata | Entity Form Metadata Lookup View | Basic Form Metadata Lookup View |
| View name for Entity Form Metadata | Inactive Entity Form Metadata | Inactive Basic Form Metadata |
| View name for Entity Form Metadata | Quick Find Active Entity Form Metadata | Quick Find Active Basic Form Metadata |
| Name for option to set entity reference on save | Set Entity Reference On Save | Set Table Reference On Save |
| Section for Entity Reference Source | Entity Reference Source | Table Reference Source |
| Type of referenced entity | Reference Entity Source Type | Source Type |
| Additional setting for Entity or Web form | Target Entity Portal User Lookup Attribute | Portal User Lookup Column |
| Entity List OData Feed option for set name | Entity Set Name | OData Entity Set Name |
| Entity List OData Feed option for type name | Entity Type Name | OData Entity Type Name |
| Option to choose entity form for create | Entity Form for Create | Basic Form for Create |
| Display name of entity form field | Reference Entity Primary Key Logical Name | Reference Table Primary Key Logical Name |
| Display name of entity form field | Record Source Entity Logical Name | Record Source Table Logical Name |
| Label for query string parameter name for On success action of Redirect on entity form | Record ID Query String Parameter Name | Record ID Parameter Name |


## Terminology changes inside portals Studio

Terminology updates apply to references of legacy terms. For example, if portals Studio referred to an "Entity", the term is updated to "Table".

The following table includes terminology changes inside portals Studio.

| Feature area | Legacy term | Current term |
| - | - | - |
| Drop down option for Entity | Entity | Table |
| Search setting checkbox label for Entity Lists | Enable search on entity list | Enable search on list |
| Checkbox label to enable entity permissions | Enable entity permissions | Enable table permissions |

## Next steps

[Creating a starter portal](create-portal.md)

### See also

[Microsoft Learn: Get started with Power Apps portals](https://docs.microsoft.com/learn/paths/get-started-power-apps-portals/) <br>
[Power Apps portals lifecycle](admin/portal-lifecycle.md) <br>
[Available portal templates](portal-templates.md) <br>
[Portals connectivity to a Microsoft Dataverse environment](admin/connectivity.md) <br>
[Server-side cache in portals](admin/clear-server-side-cache.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
---
title: "Use SQL to query data (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to query Common Data Service entity data using SQL." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/01/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use SQL to query data (Preview)

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!WARNING]
> A problem has been identified with the Tabular Data Stream (TDS) endpoint. This feature is presently globally disabled as we work to address a security issue. A fix for the issue has been developed. Deployment of the fix and feature re-enablement to all public regions is planned for the first week of November 2020. A safe deployment practice is being followed so the feature may be available in your region earlier. Thank you for your patience on this matter.



A SQL data connection is available on the Common Data Service endpoint. The SQL connection provides read-only access to the entity data of the target Common Data Service environment. This allows you to write and execute SQL queries against the entity data table. Table columns provide the attribute data of the entity. No custom views of the data have been provided.



> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - Instructions to enable the feature can be found here: [View entity data in Power BI Desktop](/powerapps/maker/common-data-service/view-entity-data-power-bi), and [Manage feature settings](/power-platform/admin/settings-features) (see TDS endpoint setting).

## Applications support

You can use the **Analyze in Power BI** option (**Data** > **Entities** > **Analyze in Power BI**) in Power Apps (https://make.powerapps.com) to use the SQL connection feature to analyze data in Power BI Desktop. More information: [View entity data in Power BI Desktop](/powerapps/maker/common-data-service/view-entity-data-power-bi)

> [!NOTE]
> To verify if your target environment has the Common Data Service SQL connection feature enabled, do the following:
> 1. Sign into Power Apps, on the left navigation pane expand **Data**, and then select **Entities**.
> 2. On the command bar, you should see a button **Analyze in Power BI**. If you do not see this button, your environment does not yet have the feature.

You can also use [SQL Server Management Studio](/sql/ssms/download-sql-server-management-studio-ssms) (SSMS) version 18.4 or later with the Common Data Service endpoint SQL connection. Examples of using SSMS with the SQL data connection are provided below.

![Expanded account table](media/ssms-table-expanded.PNG)

## Security and authentication

The Common Data Service endpoint SQL connection uses the Common Data Service security model for data access. Data can be obtained for all entities to which a user has access to in Common Data Service.

Only Azure Active Directory authentication is supported. SQL authentication and Windows authentication are not supported. Below is an example of how to logon to the SQL connection in SSMS. Notice the server name is the organization address URL followed by a comma and the port value of 5558.

![Connec dialog](media/ssms-connect-dialog.PNG)

## Example entity data queries

Below are a couple of example queries composed in SSMS. The first image shows a simple query using aliases and result ordering.

```tsql
select top 5 a.name as [VIP customer], a.address1_postalcode as [ZIP code] from account a order by a.address1_postalcode desc
```

![Simple query using aliases and ordering](media/ssms-simple-query.PNG)

This next query shows a JOIN.

```tsql
select name, fullname from account a inner join contact c on a.primarycontactid = c.contactid
```

![Another query using a JOIN](media/ssms-join-query.PNG)

## Supported operations and data types

The list of supported SQL operations includes:

- Batch operations
- SELECT
- Aggregation functions (i.e., Count() and Max() functions)
- UNIONs and JOINs
- Filtering

Any operation that attempts to modify data (i.e., INSERT, UPDATE) will not work as this is a read-only SQL data connection. Common Data Service option sets are represented as \<OptionSet\>Name and \<OptionSet\>Label in a result set.

The following Common Data Service datatypes are not supported with the SQL connection: `binary`, `image`,
`ntext`, `sql_variant`, `varbinary`, `virtual`, `HierarchyId`, `managedproperty`, `file`, `xml`, `partylist`, `timestamp`.

> [!TIP]
> `partylist` attributes can instead be queried by joining to the `activityparty` table as shown below.
> 
> ```tsql
> select act.activityid, act.subject, string_agg([to].partyidname, ', ')
> from activitypointer as act
> left outer join activityparty as [to] on act.activityid = [to].activityid and [to].participationtypemask = 2
> group by act.activityid, act.subject
> ```

## Plug-ins

Querying data using SQL does not trigger any plug-ins registered on the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> messages. Any re-writing of the query or results that would normally be performed by such a plug-in will therefore not take effect for a SQL query.

### See also

[How Common Data Service SQL differs from Transact-SQL](how-cds-sql-differs-from-transact-sql.md)  
[Use FetchXML to construct a query](cds-sql-query.md)

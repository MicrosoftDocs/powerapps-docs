---
title: "Use SQL to query data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to query Microsoft Dataverse entity data using SQL." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 02/02/2021
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

[This topic is pre-release documentation and is subject to change. Note that only the SQL data connection is in preview. Power BI is General Availability (GA)]

A SQL data connection is available on the Microsoft Dataverse endpoint. The SQL connection provides read-only access to the entity data of the target Dataverse environment thereby allowing you to execute SQL queries against the entity data table. Table columns provide the attribute data of the entity. No custom views of the data have been provided.

## Applications support

TDS (SQL) endpoint applications support for Power BI and SQL Server Management Studio is described below.

### Power BI

You can use the **Analyze in Power BI** option (**Data** > **Entities** > **Analyze in Power BI**) in Power Apps (https://make.powerapps.com) to use the Dataverse connector to analyze data in Power BI Desktop. More information: [View entity data in Power BI Desktop](/powerapps/maker/data-platform/view-entity-data-power-bi)

> [!NOTE]
> To enable this feature, see the TDS endpoint setting in [Manage feature settings](/power-platform/admin/settings-features). Once enabled you should see a button **Analyze in Power BI** in the command bar of Power Apps.

### SQL Server Management Studio

You can also use [SQL Server Management Studio](/sql/ssms/download-sql-server-management-studio-ssms) (SSMS) version 18.4 or later with the Dataverse endpoint SQL connection. Examples of using SSMS with the SQL data connection are provided below.

![Expanded account table](media/ssms-table-expanded.PNG)

## Security and authentication

The Dataverse endpoint SQL connection uses the Dataverse security model for data access. Data can be obtained for all entities to which a user has access to in Dataverse.

Only Azure Active Directory authentication is supported. SQL authentication and Windows authentication aren't supported. Below is an example of how to logon to the SQL connection in SSMS. Notice the server name is the organization address URL.

![Connec dialog](media/ssms-connect-dialog.PNG)

> [!NOTE]
> Ports 1433 and/or 5558 need to be enabled to use the TDS endpoint from a client application such as SSMS. If you only enable port 5558, the user must append that port number to the server name in the **Connect to Server** dialog of SSMS - for example: myorgname.crm.dynamics.com;5558.

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

For a detailed list of supported SQL operations on the Dataverse endpoint, see [How Dataverse SQL differs from Transact-SQL](how-dataverse-sql-differs-from-transact-sql.md).

Any operation that attempts to modify data (that is, INSERT, UPDATE) will not work with this read-only SQL data connection. Dataverse option sets are represented as \<OptionSet\>Name and \<OptionSet\>Label in a result set.

The following Dataverse datatypes are not supported with the SQL connection: `binary`, `image`,
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

## Limitations

There is an 80-MB maximum size limit for query results returned from the Dataverse endpoint. Consider using data integration tools such as [Export to data lake](https://docs.microsoft.com/powerapps/maker/data-platform/export-to-data-lake) and [dataflows](https://docs.microsoft.com/power-bi/transform-model/dataflows/dataflows-introduction-self-service) for large data queries that return over 80 MB of data. More information: [Importing and exporting data](/powerapps/maker/data-platform/import-export-data)

Dates returned in query results are formatted as Universal Time Coordinated (UTC). Previously, dates were returned in local time.

> [!NOTE]
> Until a service update planned for January 2021 has deployed, using date filters will be slow.

Querying data using SQL does not trigger any plug-ins registered on the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> messages. Any rewriting of the query or results that would normally be performed by such a plug-in will therefore not take effect for a SQL query.

Queries using the TDS endpoint execute under the service protection API limits.

## Troubleshooting connection problems

Below are some know error conditions and how to resolve them.

### Authentication

Only Azure Active Directory authentication is supported on the Dataverse endpoint SQL connection. The preferred authentication mechanism is "Azure Active Directory – Universal" with multi-factor authentication (MFA). However, "Azure Active Directory – Password" will work if MFA is not configured. If you try to use other forms of authentication, you will see errors like the following.

- Error returned when using **Azure Active Directory – Integrated** authentication.

“Login failed: The HTTP request was forbidden with client authentication scheme 'Anonymous'.
RequestId: TDS;81d8a4f7-0d49-4d21-8f50-04364bddd370;2
Time: 2020-12-17T01:10:59.8628578Z (.Net SqlClient Data Provider)”

- Error returned when using **SQL Server** authentication.

“Login failed: Request is not authenticated.
RequestId: TDS;918aa372-ccc4-438a-813e-91b086355343;1
Time: 2020-12-17T01:13:14.4986739Z (.Net SqlClient Data Provider)”

- Error returned when using **Windows** authentication.

“Login failed: Request is not authenticated.
RequestId: TDS;fda17c60-93f7-4d5a-ad79-7ddfbb917979;1
Time: 2020-12-17T01:15:01.0497703Z (.Net SqlClient Data Provider)”

### Blocked ports

A blocked port error may look something like the following.

![Error message](media/TDS-SQL-blocked-port-error.png)

The solution is to verify the TCP ports 1433 or 5558 from the client are unblocked. One possible method to do that is described below.

#### Establish a telnet session to the TDS service listener

1. On a Microsoft Windows computer, install/enable telnet.
    1. Choose **Start**.
    1. Select **Control Panel**.
    1. Choose **Programs and features**.
    1. Select **Turn Windows features on or off**.
    1. Choose the **Telnet Client** option.
    1. Select **OK**. A dialog box appears to confirm the installation. The telnet command should now be available.
1. Run a telnet command in a Command window.<br/> `telnet <environmentname>.crm.dynamics.com 1433`

If the connection is successful, you will be in an active telnet session. If unsuccessful, you will receive the error:

“Connecting to <environmentname>.crm.dynamics.com… Could not open connection to the host, on port 1433: connect failed”. 

This means the port has been blocked at the client.

### See also

[Use FetchXML to construct a query](dataverse-sql-query.md)  
[Service Protection API Limits](api-limits.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
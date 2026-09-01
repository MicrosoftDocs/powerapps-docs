---
title: "Custom virtual table data providers (Microsoft Dataverse) | Microsoft Docs"
description: "Using the Microsoft Dataverse Data SDK, .NET Developers have the option of creating custom virtual table data providers to help integrate external data source types that are not supported by an existing data provider."
ms.date: 08/27/2026
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: "NHelgren" # GitHub ID
ms.author: nhelgren
ms.reviewer: pehecke
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Custom virtual table data providers

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

By using the Microsoft Dataverse Data SDK, .NET developers can create custom virtual table data providers to help integrate external data source types that aren't supported by an existing data provider. Each data provider is composed of a reusable set of Dataverse plug-ins that implement the supported CRUD operations. For each virtual table, also known as a virtual entity, developers can create plug-ins and register them representing each of the **Create**, **Update**, **Retrieve**, **RetrieveMultiple**, and **Delete** operations. This section provides fundamental information about data providers and approaches to developing custom providers, including example code.

> [!NOTE]
> Instead of creating a custom data source provider, consider adapting your data source to an existing data provider. For example, if you create an OData v4 interface to your external data source, you can directly access it by using the supplied standard OData v4 Data Provider, which supports CRUD operations. The mechanism for adding this REST interface varies with the underlying data service technology. For example, see [WCF Data Services 4.5](/dotnet/framework/data/wcf/). OData has broad industry support, with a wide range of dedicated tools and compatible technologies.

## Prerequisites

Custom data providers require substantial development resources to create and maintain. You must have fundamental knowledge of the following areas:

- The external data source schema and associated data access techniques.  This domain knowledge is specific to the external data source type.
- Dataverse definition schema: More information: [Work with table and column definitions using code](../metadata-services.md).
- Dataverse event framework: More information: [Event Framework](../event-framework.md). 
- Dataverse plug-in architecture and development: More information: [Use plug-ins to extend business processes](../plug-ins.md).

The `Microsoft.Xrm.Sdk.Data.dll` assembly is available as a NuGet package: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/)

## Categories of providers

You can create two general categories of data providers by using the virtual table data SDK assemblies: generic or targeted. The following table describes these approaches and matches them to the data provider development model best suited for each approach.

|**Category**|**Dev Model**|**Description**|
|------------|-------------|---------------|
|Generic|"Bare metal" provider|These providers flexibly translate FetchXML query expressions to the associated request to the external data source, and then return the resulting records. You can reuse such a provider for all instances of this data source type. This approach is the most general but is more complicated to develop. If the schema of the data source changes, you only need to remap the affected virtual tables.|
|Targeted|LINQ provider for known schema|Such a provider narrowly translates queries into the associated LINQ call to a known, existing data source instance. The data source must be a LINQ provider as described in the article [Enabling a Data Source for LINQ Querying](/dotnet/csharp/programming-guide/concepts/linq/enabling-a-data-source-for-linq-querying1). This approach is limited to a specific data source instance, but requires much less coding. If the schema of the data source changes, you must update and rebuild the data provider.|

The standard OData v4 Data Provider and the Azure Cosmos DB Data Provider are examples of generic providers.

## Steps to use a custom data provider

To create a virtual table data provider solution that you can import into your Dataverse applications, complete the following steps:

1. Develop the custom data provider plug-in DLL or set of DLLs.
2. Register the custom data provider with your Dataverse service by using the Plug-in Registration Tool (PRT).
3. Create a data provider solution.
4. Customize the data source table to reflect your data type or specific instance.
5. Export the custom data provider solution.

For more information, see [Sample: Custom virtual table provider with CRUD operations](sample-ve-provider-crud-operations.md).

### Plug-in development

Because virtual tables support CRUD operations, write the data provider as a plug-in that you register on the **Create**, **Update**, **Retrieve**, **RetrieveMultiple**, and **Delete** events. Each event includes information in the execution context that describes the kind of data to return. 

|**Event**|**Execution Context**|
|---------|---------------------|
|**Retrieve**|Describes which table to retrieve as well as the columns and any related tables to include.|
|**RetrieveMultiple**|Contains a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> object defining the query. The framework contains a **QueryExpressionVisitor** class designed to inspect different parts of the query expression tree.|

For both events, you must:

1. Convert the respective information in the execution context into a query that works for your external data source.
2. Retrieve the data from the external system.
3. For **Retrieve**, convert the data into an <xref:Microsoft.Xrm.Sdk.Entity>; otherwise, for **RetrieveMultiple**, convert it to an <xref:Microsoft.Xrm.Sdk.EntityCollection>. Dataverse returns this result through to the user executing the query.  

The classes in the <xref:Microsoft.Xrm.Sdk.Data> namespace provide a framework to assist in mapping the Dataverse query information from the execution context into a query in the format appropriate for your external data source. This framework helps you convert the data returned into the appropriate <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityCollection> types expected by the Dataverse platform. 

#### Data provider exceptions

If your code can't achieve the expected result, throw the appropriate error. The <xref:Microsoft.Xrm.Sdk.Data.Exceptions> namespace contains the following exception classes, derived from <xref:Microsoft.Xrm.Sdk.SdkExceptionBase>, that you can use for this purpose:  

|**Exception Class**|**Description**|
|---------------|-----------|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.AuthenticationException>|An error occurred during security authentication to the external data source service; for example, HTTP status 401 received from the external data service. Typically occurs because the current user doesn't have proper privileges or the connection information in the associated **EntityDataSource** is incorrect.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.EndpointException>|The endpoint configuration in the data source table is invalid or the endpoint doesn't exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.GenericDataAccessException>|A general data access error, used when the error doesn't map to a more specific exception.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidMetadataException>| |
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidQueryException>|The specified query is invalid; for example, it contains an invalid clause combination or unsupported comparison operator.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.ObjectNotFoundException>|The specified record in the external data source doesn't exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.TimeoutException>|The external operation didn't complete within the allowed time; for example, the result of an HTTP status 408 from the external data service.|

### Plug-in registration

Unlike an ordinary plug-in, use the Plug-in Registration Tool (PRT) to register the assembly and the plug-ins for each event. Don't register specific steps. Your plug-in runs in stage 30, the main core transaction stage for the operation that isn't available for ordinary plug-in steps. Instead of registering steps, configure your data provider by using the following table. 


|**Table**|**Description**|
|-----|-----|
|[EntityDataProvider](../reference/entities/entitydataprovider.md)|Defines the plug-ins to use for each event and the logical name of the data source.|

When you configure the definitions for your virtual table, register your plug-ins by using the PRT and set the correct configuration data in the **EntityDataProvider** table. Your virtual table starts to respond to requests.

For more information, see [Creating data provider and adding plug-ins to the provider](sample-ve-provider-crud-operations.md#step-2-creating-data-provider-and-adding-plug-ins-to-the-provider).

### Debugging plug-ins

A custom virtual table provider is a type of plug-in. Use the information in these articles to debug plug-ins for custom virtual table providers: [Debug plug-ins](../debug-plug-in.md) and [Tutorial: Debug a plug-in](../tutorial-debug-plug-in.md).


### See also

[Get started with virtual tables](get-started-ve.md)<br />
[API considerations of virtual tables](api-considerations-ve.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

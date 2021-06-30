---
title: "Custom virtual table data providers (Microsoft Dataverse) | Microsoft Docs"
description: "Using the Microsoft Dataverse Data SDK, .NET Developers have the option of creating custom virtual table data providers to help integrate external data source types that are not supported by an existing data provider."
ms.date: 04/09/2021
ms.service: powerapps
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996d22
author: "Sunil-Garg" # GitHub ID
ms.author: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Custom virtual table data providers

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Using the Microsoft Dataverse Data SDK, .NET Developers have the option of creating custom virtual table data providers to help integrate external data source types that are not supported by an existing data provider. Each data provider is composed of a reusable set of Dataverse plug-ins that implement the supported CRUD operations. For each virtual table, also known as a virtual entity, developers can create plug-ins and register them representing each of the **Create**, **Update**, **Retrieve**, **RetrieveMultiple** and **Delete** operation.  This section provides fundamental information about data providers and approaches to developing custom providers, including example code.

> [!NOTE]
> As an alternative to creating a custom data source provider, you should consider adapting your data source to an existing data provider. For example, if you create an OData v4 interface to your external data source, then you can directly access it with the supplied standard OData v4 Data Provider, which supports CRUD operations as well. The mechanism of adding this REST interface varies with the underlying data service technology, for example see [WCF Data Services 4.5](https://docs.microsoft.com/dotnet/framework/data/wcf/). OData has broad industry support, with a wide range of dedicated tools and compatible technologies.

## Prerequisites

Custom data providers require substantial development resources to create and maintain. You must have fundamental knowledge of the following areas:

- The external data source schema and associated data access techniques.  This domain knowledge is specific to the external data source type.
- Dataverse definition schema: More information: [Work with table and column definitions using code](../metadata-services.md).
- Dataverse event framework: More information: [Event Framework](../event-framework.md). 
- Dataverse plug-in architecture and development: More information: [Use plug-ins to extend business processes](../plug-ins.md).

The `Microsoft.Xrm.Sdk.Data.dll` assembly is available as a NuGet package: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/)

## Categories of providers

There are two general categories of data provider you can create using the virtual table data SDK assemblies: generic or targeted. The table below describes these approaches and matches them to the data provider development model best suited for that approach.

|**Category**|**Dev Model**|**Description**|
|------------|-------------|---------------|
|Generic|"Bare metal" provider|These providers can flexibly translate FetchXML query expressions to the associated request to the external data source, then return the resulting table instances. Such a provider can be reused for all instances of this data source type. This approach is the most general but is more complicated to develop.  If the schema of the data source changes, the affected virtual tables must only be remapped.|
|Targeted|LINQ provider for known schema|Such a provider only narrowly translates queries into the associated LINQ call to a known, existing data source instance. The data source must be a LINQ provider as described in the topic [Enabling a Data Source for LINQ Querying](/dotnet/csharp/programming-guide/concepts/linq/enabling-a-data-source-for-linq-querying1). This approach is limited to a specific data source instance, but requires much less coding. If the schema of the data source changes, the data provider must be updated and rebuilt.|

The standard OData v4 Data Provider and the Cosmos DB Data Provider are examples of generic providers.

## Steps to use a custom data provider

There are several steps that are required to create a virtual table data provider solution that can be imported into your Dataverse applications:

1. Develop the custom data provider plug-in DLL (or set of DLLs).
2. Register the custom data provider with your Dataverse service using the Plug-in Registration Tool (PRT).
3. Create a data provider solution.
4. Customize the data source table to reflect your data type or specific instance.
5. Export the custom data provider solution.


### Plug-in development

Because virtual tables support CRUD operations, you will write the data provider in the form of a plug-in registered on the **Create**, **Update**, **Retrieve**, **RetrieveMultiple** and **Delete** events. Each respective event will include information in the execution context which describes the kind of data to return. 

|**Event**|**Execution Context**|
|---------|---------------------|
|**Retrieve**|Describes which table to retrieve as well as the columns and any related tables to include.|
|**RetrieveMultiple**|Contains a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> object defining the query. The framework contains a **QueryExpressionVisitor** class designed to inspect different parts of the query expression tree.|

For both events, you must :

1. Convert the respective information in the execution context into a query that will work for your external data source.
2. Retrieve the data from the external system.
3. For **Retrieve**, convert the data into an <xref:Microsoft.Xrm.Sdk.Entity>; otherwise, for **RetrieveMultiple**, convert it to an <xref:Microsoft.Xrm.Sdk.EntityCollection>. This result is returned through the Dataverse platform to the user executing the query. 

The classes in the <xref:Microsoft.Xrm.Sdk.Data> namespace provide a framework to assist in mapping the Dataverse query information from the execution context into a query in the format appropriate for your external data source. This framework will help you convert the data returned in to the appropriate <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityCollection> types expected by the Dataverse platform. 

#### Data provider exceptions

If for any reason your code cannot achieve the expected result, you must throw the appropriate error. The <xref:Microsoft.Xrm.Sdk.Data.Exceptions> namespace contains the following exception classes, derived from <xref:Microsoft.Xrm.Sdk.SdkExceptionBase>, that you can use for this purpose:  

|**Exception Class**|**Description**|
|---------------|-----------|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.AuthenticationException>|An error occurred during security authentication to the external data source service; for example HTTP status 401 received from the external data service. Typically occurs because the current user does not have proper privileges or the connection information in the associated **EntityDataSource** is incorrect.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.EndpointException>|The endpoint configuration in the data source table is invalid or the endpoint does not exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.GenericDataAccessException>|A general data access error, used when the error does not map to a more specific exception.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidMetadataException>| |
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidQueryException>|The specified query is invalid; for example it an invalid clause combination or unsupported comparison operator.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.ObjectNotFoundException>|The specified record in the external data source does not exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.TimeoutException>|The external operation did not complete within the allowed time; for example, the result of a HTTP status 408 from the external data service.|


### Plug-in registration

Unlike an ordinary plug-in, you will only use the Plug-in Registration Tool (PRT) to register the assembly and the plug-ins for each event. You will not register specific steps. Your plug-in will run in stage 30, the main core transaction stage for the operation that is not available for ordinary plug-in steps. Instead of registering steps, you will configure your data provider using the following tables. 


|**Table**|**Description**|
|-----|-----|
|[EntityDataProvider](../reference/entities/entitydataprovider.md)|Defines the plug-ins to use for each event and the logical name of the data source.|

When the definitions for your virtual table is configured, your plug-ins are registered using the PRT and the correct configuration data is set in the **EntityDataProvider** table, your virtual table will start to respond to requests.

### Debugging plug-ins

A custom virtual table provider is a type of plug-in. Use the information in these topics to debug plug-ins for custom virtual table providers: [Debug plug-ins](../debug-plug-in.md) and [Tutorial: Debug a plug-in](../tutorial-debug-plug-in.md).


### See also

[Get started with virtual tables](get-started-ve.md)<br />
[API considerations of virtual tables](api-considerations-ve.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

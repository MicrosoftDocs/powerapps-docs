---
title: "Custom virtual entity data providers (Common Data Service for Apps) | Microsoft Docs"
ms.date: 06/17/2018
ms.service: "crm-online"
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996d22
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---

# Custom virtual entity data providers

Using the CDS for Apps Data SDK, .NET Developers have the option of creating custom virtual entity data providers to help integrate external data source types that are not supported by an existing data provider. Each data provider is composed of a reusable set of CDS for Apps plug-ins that implement the supported CRUD operations. (The initial release is limited to the **Retrieve** and **RetrieveMultiple** read operations.)  This section provides fundamental information about data providers and approaches to developing custom providers, including example code.

> [!NOTE]
> As an alternative to creating a custom data source provider, you should consider adapting your data source to an existing data provider. For example, if you create an OData v4 interface to your external data source, then you can directly access it with the supplied standard OData v4 Data Provider. The mechanism of adding this REST interface varies with the underlying data service technology, for example see [WCF Data Services 4.5](https://docs.microsoft.com/dotnet/framework/data/wcf/). OData has broad industry support, with a wide range of dedicated tools and compatible technologies.


## Prerequisites

Custom data providers require substantial development resources to create and maintain. You must have fundamental knowledge of the following areas:

- The external data source schema and associated data access techniques.  This domain knowledge is specific to the external data source type.


<!-- TODO:
- CDS for Apps metadata schema: More information: [The metadata and data models in Microsoft Dynamics 365](../metadata-data-models.md).
- CDS for Apps event system: More information: [Introduction to the event framework](../introduction-event-framework.md). 
- CDS for Apps plug-in architecture and development: More information: [Plug-in development](../plugin-development.md). -->

The `Microsoft.Xrm.Sdk.Data.dll` assembly is available as a NuGet package: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/)

<!-- ## Data Provider Architecture -->
<!-- TODO: it would be nice to have a more detailed architecture diagram of a data provider and add discussion. -->


## Categories of providers

There are two general categories of data provider you can create using the virtual entity data SDK assemblies: generic or targeted. The table below describes these approaches and matches them to the data provider development model best suited for that approach.

|**Category**|**Dev Model**|**Description**|
|------------|-------------|---------------|
|Generic|"Bare metal" provider|These providers can flexibly translate FetchXML query expressions to the associated request to the external data source, then return the resulting entity instances. Such a provider can be reused for all instances of this data source type. This approach is the most general but is more complicated to develop.  If the schema of the data source changes, the affected virtual entities must only be remapped.|
|Targeted|LINQ provider for known schema|Such a provider only narrowly translates queries into the associated LINQ call to a known, existing data source instance. The data source must be a LINQ provider as described in the topic [Enabling a Data Source for LINQ Querying](/dotnet/csharp/programming-guide/concepts/linq/enabling-a-data-source-for-linq-querying1). This approach is limited to a specific data source instance, but requires much less coding. If the schema of the data source changes, the data provider must be updated and rebuilt.|

The standard Odata v4 Data Provider and the Cosmos DB Data Provider are examples of generic providers.

## Steps to use a custom data provider

There are several steps that are required to create a virtual entity data provider solution that can be imported into your CDS for Apps applications:

1. Develop the custom data provider plug-in DLL (or set of DLLs).
2. Register the custom data provider with your CDS for Apps service using the Plug-in Registration Tool (PRT).
3. Create a data provider solution.
4. Customize the data source entity to reflect your data type or specific instance.
5. Export the custom data provider solution.


### Plug-in development

Because virtual entities in this release are read-only, you will write the data provider in the form of a plug-in registered on the **Retrieve** and **RetrieveMultiple** events. Each respective event will include information in the execution context which describes the kind of data to return. 

|**Event**|**Execution Context**|
|---------|---------------------|
|**Retrieve**|Describes which entity to retrieve as well as the attributes and any related entities to include.|
|**RetrieveMultiple**|Contains a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> object defining the query. The framework contains a **QueryExpressionVisitor** class designed to inspect different parts of the query expression tree.|

For both events, you must :

1. Convert the respective information in the execution context into a query that will work for your external data source.
2. Retrieve the data from the external system.
3. For **Retrieve**, convert the data into an <xref:Microsoft.Xrm.Sdk.Entity>; otherwise, for **RetrieveMultiple**, convert it to an <xref:Microsoft.Xrm.Sdk.EntityCollection>. This result is returned through the CDS for Apps platform to the user executing the query. 

The classes in the <xref:Microsoft.Xrm.Sdk.Data> namespace provide a framework to assist in mapping the CDS for Apps query information from the execution context into a query in the format appropriate for your external data source. This framework will help you convert the data returned in to the appropriate <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityCollection> types expected by the CDS for Apps platform. 

#### Data provider exceptions

If for any reason your code cannot achieve the expected result, you must throw the appropriate error. The <xref:Microsoft.Xrm.Sdk.Data.Exceptions> namespace contains the following exception classes, derived from <xref:Microsoft.Xrm.Sdk.SdkExceptionBase>, that you can use for this purpose:  

|**Exception Class**|**Description**|
|---------------|-----------|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.AttributeNotFoundException>|The query specifies an attribute that was not found in the associated external data record. Typically occurs as a result of faulty type mapping or a external data source schema change.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.AuthenticationException>|An error occurred during security authentication to the external data source service; for example HTTP status 401 received from the external data service. Typically occurs because the current user does not have proper privileges or the connection information in the associated **EntityDataSource** is incorrect.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.EndpointException>|The endpoint configuration in the data source entity is invalid or the endpoint does not exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.EntityNotFoundException>|The query targets an entity which does not exist. Typically occurs as a result of faulty type mapping or a external data source schema change.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.GenericDataAccessException>|A general data access error, used when the error does not map to a more specific exception.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidMetadataException>| |
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.InvalidQueryException>|The specified query is invalid; for example it an invalid clause combination or unsupported comparison operator.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.ObjectNotFoundException>|The specified record in the external data source does not exist.|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions.TimeoutException>|The external operation did not complete within the allowed time; for example, the result of a HTTP status 408 from the external data service.|

<!-- 
  TODO:
  To assist you in plug-in development, the Data SDK contains the _Plugin Profiler and Debugger_; for more information see [TBD]TODO: Obtain information on this tool, create subtopic. 
-->


### Plug-in registration

Unlike an ordinary plugin, you will only use the Plugin Registration Tool (PRT) to register the assembly and the plugins for each event. You will not register specific steps. Your plugin will run in stage 30, the main core transaction stage for the operation that is not available for ordinary plugin steps. Instead of registering steps, you will configure your data provider using the following entities. 


|**Entity**|**Description**|
|-----|-----|
|[EntityDataProvider](../reference/entities/entitydataprovider.md)|Defines the plugins to use for each event and the logical name of the data source.|
|[EntityDataSource](../reference/entities/entitydatasource.md)|Provides the entity context and any connection information required for the external data source, including any secrets required to authenticate.|

When the metadata for your virtual entity is configured, your plugins are registered using the PRT and the correct configuration data is set in the **EntityDataProvider** and **EntityDataSource** entities, your virtual entity will start to respond to requests.

### See also

[Get started with virtual entities](get-started-ve.md)<br />
[API considerations of virtual entities](api-considerations-ve.md)<br />
[Sample: Generic virtual entity data provider plug-in](sample-generic-ve-plugin.md)

 
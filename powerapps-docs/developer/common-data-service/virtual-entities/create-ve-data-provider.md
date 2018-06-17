---
title: "Create a virtual entity data provider (Developer Guide for Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996d01
author: "jimdaly"
ms.author: "jdaly"
manager: "amyla"
---

# Create a virtual entity data provider

[!INCLUDE[](../../includes/cc_applies_to_update_9_0_0.md)]

There are two general categories of data provider you can create using the virtual entity data SDK assemblies: generic or targeted.

|Category |Description|
|---------|-----------|
|Generic | These providers understand how to use the Dynamics 365 metadata and the service documents for your external data to translate Dynamics 365 queries to the appropriate query for these services. With this kind of data provider, the integration can be achieved without writing any code, but these the most complex kind of data provider to create. The Odata v4 and Azure DocumentDB data providers provided by Dynamics 365 are re-usable generic providers.|
|Targeted |Rather than attempt to create a generic data provider, you can use your domain knowledge of Dynamics 365 and your external data to create a data provider which only attempts to provide a solution to the limited scope of this specific solution.|
| | |

Because virtual entities in this release are read-only, you will write the data provider in the form of a plugin registered on the **Retrieve** and **RetrieveMultiple** events. Each respective event will include information in the execution context which describe the kind of data to return. 

|Event |Execution Context|
|------|-----------------|
|**Retrieve**|Describes which entity to retrieve as well as the attributes and any related entities to include.|
|**RetrieveMultiple**|A [QueryExpression](https://msdn.microsoft.com/library/microsoft.xrm.sdk.query.queryexpression.aspx) object defining the query|
| | |

For both events, you must :
1. Convert the respective information in the execution context into a query that will work for your external data source.
2. Retrieve the data from the external system.
3. Convert the data into either an [Entity](https://msdn.microsoft.com/library/microsoft.xrm.sdk.entity.aspx) or [EntityCollection](https://msdn.microsoft.com/library/microsoft.xrm.sdk.entitycollection.aspx) to be returned through the Dynamics 365 platform to the user executing the query.  
If for any reason your code cannot achieve the expected result, you must throw the appropriate error. The virtual entity data SDK provides a set of specific errors you can throw.

The virtual entity data SDK provides a framework you can use to map the Dynamics 365 query information from the execution context into a query in the format appropriate for your external data source. The same framework will help you convert the data returned in to the appropriate **Entity** or **EntityCollection** types expected by the Dynamics 365 platform.

Unlike an ordinary plugin, you will only use the Plugin Registration Tool (PRT) to register the assembly and the plugins for each event. You will not register specific steps. Your plugin will run in stage 30, the main core transaction stage for the operation that is not available for ordinary plugin steps. Instead of registering steps, you will configure your data provider using the [EntityDataProvider](../entities/entitydataprovider.md) and [EntityDataSource](../entities/entitydatasource.md) entities. 

|Entity |Descrption|
|-----|-----|
|**EntityDataProvider**|Defines the plugins to use for each event and the logical name of the data source.|
|**EntityDataSource**|Provides the entity and any connection information required for the external data source, including any secrets required to authenticate.|
| | |

When the metadata for your virtual entity is configured, your plugins are registered using the PRT and the correct configuration data is set in the **EntityDataProvider** and **EntityDataSource** entities, your virtual entity will start to respond to requests.



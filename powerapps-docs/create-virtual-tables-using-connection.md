---
title: Create a virtual table using a connection in Power Apps
description: Learn how to create a virtual table that uses a connection
author: Mattp123
ms.author: matp
ms.service: power-apps
ms.topic: how-to 
ms.date: 12/09/2022
ms.custom: template-how-to
---
# Create a virtual table using a connection (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Virtual tables enable integrating data from external data sources by seamlessly representing that data as tables in Microsoft Dataverse, without data replication. Solutions, apps, flows, and more can use virtual tables as if they were native Dataverse tables. Virtual tables allow for full create, read, update, and delete privileges unless the data source they are connecting to specifically forbids it. More information about virtual tables: [Create and edit virtual tables that contain data from an external data source](create-edit-virtual-entities.md).

In this public preview release, we're introducing a new user experience using the Maker portal to create virtual tables using the following virtual connector providers:

- [SQL Server](/connectors/sql/) 
- [Microsoft SharePoint](/connectors/sharepointonline/)

## Overview

Virtual tables include the following components:

:::image type="content" source="media/ve-components.png" alt-text="Virtual table components":::

- Data Source – the location where the external data is stored.
- Data Provider – defines the behavior of the virtual table.
- Connection – this sets up the ability to connect to the data source and authentication.
- Connection reference – this provides a way for Dataverse to use the connection to the data source.
- 
- If you were to create a virtual table using a custom data provider, you would need to write plugins that define how every Dataverse API would interact with the API on the system where the data is stored. This is a long process which requires knowledge of coding. Virtual connector providers streamline the creation experience by automating some of the creation for you and removing the need to use code to create the virtual tables.

When you establish a remote connection to an external source using a connector data source, the virtual connector provider automatically retrieves a list of all the available tables and lists by retrieving table definitions (metadata) from the external data source. You then select these tables and lists to generate the virtual table.

The underlying data source is key for allowing the provider to establish an authenticated remote connection to the external data. It uses a connection reference that stores pertinent details regarding the external source. The information stored in the connection reference is specific to the connector type and the connection it refers to.

:::image type="content" source="media/ve-connector-provider-overview.png" alt-text="Virtual connectors provider overview":::

When setting up the connection and connection reference for your data sources, specific information will be needed. For example, setting up the **SQL Server** connector needs server name, database name, the authentication method, username, password, and (optionally) gateway connection details. Each external data source will need a connection reference to be defined to create the virtual table. When using the Power Apps (make.powerapps.com) experience the connection reference can be generated automatically for you unless you wish to provide custom naming.

The connector permissions enforce the ability for organizational users to access and operate on the virtual table. The connection can be shared with one user or can be shared with entire organization. This allows users to access and operate virtual tables using a shared connection. Through the use of security roles, virtual table access can be restricted to a specific set of users within your organization. You can even specify which roles have create, read, update, or delete privileges in this way.

Application lifecycle management (ALM) is supported for virtual tables created using the virtual connector provider, you can even create the virtual tables from directly within the solution when using Power Apps (make.powerapps.com) portal. Virtual tables should be part of the managed solution along with the connection reference to distribute the solution. The solution can have other components, such as a model-driven app that uses virtual tables.

More information about application lifecycle management (ALM) and solutions:

- [Application lifecycle management (ALM) in Microsoft Power Platform](/power-platform/alm/)
- [Solutions overview](solutions-overview.md)


## Prerequisites

To create a virtual table, you must have a Microsoft Dataverse license through Power Apps or Microsoft Dynamics 365. Microsoft 365 or Teams licenses can't be used to create virtual tables.


## [Section 1 heading]
<!-- Introduction paragraph -->
1. <!-- Step 1 -->
1. <!-- Step 2 -->
1. <!-- Step n -->


## Next steps


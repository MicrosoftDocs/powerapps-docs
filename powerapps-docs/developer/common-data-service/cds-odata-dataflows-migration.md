---
title: Migrate data between Common Data Service instances with dataflow OData connector
author: demora
ms.reviewer: "nabuthuk"
description: Migrate data between Common data Service instance using Power Platform OData connector.
no-loc: [Title, Document]
ms.date: 05/05/2020
ms.service: powerapps
ms.topic: "article"
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer, maker
search.app: 
  - PowerApps
---

# Migrate data between Common Data Service instances using the dataflows OData connector

Common Data Service web API works with any technology that supports OData and OAuth. There are many options available to move data in and out of Common Data Service. OData connector is one of the dataflows, which is designed to support migration and synchronization of large datasets in Common Data Service. 

In this article, we walk you through how to migrate data between Common Data Service instances using the dataflows OData connector. 

## Prerequisites

1. System Administrator or System Customizer security role permission on both source and the target environments.

1. Premium Power Apps, Power Automate, or Common Data Service license (per app or per user)

1. Two environments with Common Data Service instances provisioned.

## Scenarios

 - A one-time cross-environment or cross tenant migration is needed (for example, geo-migration)

 - Developer needs to update an app that is being used in production. Test data is needed in their development environment to easily build out changes. 

## Steps

The following steps are required to migrate data:

1. [Plan out the dataflow](#plan-out-the-dataflow)
1. [Get the OData endpoint](#get-the-odata-endpoint)
1. [Create a new OData dataflow](#create-a-new-odata-dataflow)
1. [Select and transform data with the Power Query experience](#select-and-transform-data-with-the-power-query)
1. [Configure destination environment settings](#configure-destination-environment-settings)
1. [Run the dataflow](#run-the-dataflow)

## Plan out the dataflow

1. Identify the source and target environments.

    - The **source environment** is where the data comes from. 

    - The **target environment** is where the data is migrated. 


     > [!NOTE]
     > Switch to **source** and **target** environments by selecting the **Environment** on the top right corner and select the appropriate environment from the list.
1. Make sure that the entities are already defined in the target environment. Ideally both environments should have the same entities defined with the same solution.

1. When importing relationships, multiple dataflows are required.
    - One (parent/independent) to many (children/dependent) entities require separate dataflows. Configure the parent dataflow to run before any child entities, since the data in the parent needs to be loaded first to correctly map to the fields in the corresponding child entities.

> [!NOTE]
> The words to describe a Common Data Service `instance` and `environment` are used interchangeably in this article. Each environment in the Power Platform can have 0 or 1 Common Data Service instance(s). More information: [Create Common Data Service database](https://docs.microsoft.com/power-platform/admin/create-database).

## Get the OData endpoint 

Common Data Service provides an OData endpoint that does not require any additional configuration to authenticate with the dataflows connector. It is relatively easy process to connect to the source instance. 

This article will walk through how to set up a new dataflow with the OData connector. See, [Creating dataflows](https://docs.microsoft.com/powerapps/maker/common-data-service/create-and-use-dataflows) article for connecting to all data sources supported by dataflows.

From the **source** environment, get the [OData endpoint](https://docs.microsoft.com/powerapps/developer/common-data-service/view-download-developer-resources) (aka Service Root URL) for that instance:

1. Go to [Power Apps maker portal](https://make.powerapps.com)

1. Make sure you are in the desired **"source"** environment.

1. Select the gear icon and select **Advanced Settings**.

1. In the top ribbon expand the **Settings** menu, in the **Customizations** tab select **Customizations**.

1. Select **Developer Resources**.

1. Copy the **Service Root URL** and save it in notepad.

    > [!div class="mx-imgBorder"]
    > ![Copy the service root URL in the developer resources](./media/get-odata-endpoint-url.png)
 
## Create a new OData dataflow

In the **target** environment, create a new dataflow with the OData connector.

1. Go to [Power Apps maker portal](https://make.powerapps.com).

1. Make sure you are in the desired **target** environment.

1. In the left navigation pane, expand the **Data** menu, then select **Dataflows**.

1. Select **New dataflow** to create a new dataflow. Provide a meaningful name for the dataflow. 

1. Select **Create**.
   > [!div class="mx-imgBorder"]
   > ![Prompt for a new dataflow](./media/enter-name-for-new-dataflow.png)

1. Select the OData connector, and enter the field values:

    > [!div class="mx-imgBorder"]
    > ![Select OData source](media/select-odata-data-source.png)

    | Field | Description |
    |--|--|
    | URL | Provide the Service Root URL in the URL field of the connection settings |
    | Connection | Create new connection. This will be automatically chosen if you have not made an OData connection in dataflows before. |
    | Connection name | Optionally rename the connection name, but a value is automatically populated |  |
    | On-premise data gateway | None. An on-premises data gateway is not needed for connections to this cloud service. |
    | Authentication kind | Organizational account. Select the Sign in button to open the login dialog that authenticates the account associated with the connection. |

    > [!div class="mx-imgBorder"]
    > ![Confirm the field values are correct](./media/enter-odata-connector-parameters.png)

    > [!IMPORTANT] 
    > Disable pop-up and cookies blocker in your browser in order to configure the AAD authentication. This is orthogonal to the fact that you are using the Common Data Service OData endpoint or any other OAuth based authentication data source. 
    
1. Select **Next** in the bottom right.

## Select and transform data with the Power Query 

Use the Power Query, which allows to select the tables and also allows the transformation of data.

First, select the entities that need to be transferred. You can browse all entities in the source instance and preview some of the data in each entity.

> [!div class="mx-imgBorder"]
> ![Power query navigator](./media/edit-queries-for-selected-entities.png)

1. Select one or multiple entities as needed, then select **Transform data**.

    > [!NOTE]
    > When importing relationships, remember that the parent entity dataflow need to be imported before the child ones. The data for the child dataflow will require data to be in the parent entity for it to correctly map, otherwise it might throw an error.
 
1. In the **Power Query - Edit queries** window, you can transform the query before import.

    - If you are only migrating data, there should not be a need to modify anything here. 

    - Reducing the number of unnecessary columns will improve the dataflow performance for larger data sets.

    > [!TIP]
    > You can go back to choose more tables in the **Get data** ribbon option for the same OData connector.

1. Select **Next** in the bottom right.

## Configure destination environment settings

This section describes how to define the target instance settings.

### Map entities 

For each entity chosen, select the behavior for importing that entity in these settings and select **Next**.

> [!div class="mx-imgBorder"]
> ![Map entities](./media/map-entities-to-target.png)

- **Load to existing Entity (recommended)**

    - The dataflow syncs data from the source environment's entity to the target environment, and the same entity schema is already defined in the target environment.

    - Ideally, use the same solution in both target and source environments to make data transfer seamless. Another advantage to having a pre-defined entity is more control over which solution the entity is defined in and the prefix.
    
    - Choose the **Delete rows that no longer exist in the query output**. This ensures that the relationships will map correctly because it maintains the values for the lookups.
    
    - If the schema is identical in both source and target tables, you can select the **Auto map** button to quickly map the fields.
    
    - Requires a key configuration in the target environment (as the unique identifier fields is not available to modify).

- **Load to new entity (not recommended)**

    - Ideally there should be an entity pre-defined in the target environment from the same solution import as the source environment. However, there are cases where this might not be feasible, so there is this option to choose if there is no existing entity to load to. 

    - It creates a new custom entity in the target environment's default solution.

- There is an option to **Do not load**, but do not include entities in the dataflow that are not being loaded. You can select **Back** from this menu to return to the Power Query menu and remove the entities that are not needed.

### Refresh settings

Select **Refresh manually** since this is a one-time migration ad select **Create**. 

### Run the dataflow

The initial dataflow load initiates when you select the **Create** button. 

> [!div class="mx-imgBorder"]
> ![Refresh manually](./media/initiate-dataflow-process.png)

You can manually initiate a dataflow by selecting **(...)** in the dataflows list. Make sure to run dependent dataflows after the parent flows have completed.

> [!div class="mx-imgBorder"]
> ![Refresh manually](./media/refresh-dataflow-manually.png) 

## Tips

- Try out one entity first to walk through the steps, then build out all the dataflows.

- If there are more entities that contain larger amounts of data, consider configuring multiple separate dataflows for individual entities.

- One to many relationships will require separate dataflows for each entity. Configure and run the parent (aka one, or independently) entity dataflow before the child (aka many, or dependent) entity.

- If there are errors with the dataflow refresh, you can view the refresh history in the **(...)** menu in the dataflows list and download each refresh log.

## Limitations

1. Many to many relationship data imports are not supported.

1. Parent dataflows must be manually configured to run before child dataflows.

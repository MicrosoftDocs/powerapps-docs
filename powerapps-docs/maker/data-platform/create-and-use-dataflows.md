---
title: "Create and use dataflows in Power Apps"
description: "Learn how to create and use dataflows in Power Apps"
ms.custom: ""
ms.date: 08/20/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 
ms.subservice: dataverse-maker
ms.author: "matp"
tags: 
search.audienceType: 
  - maker
---
# Create and use dataflows in Power Apps

With advanced data preparation available in Power Apps, you can create a
collection of data called a dataflow, which you can then use to connect with
business data from various sources, clean the data, transform it, and then load
it to Microsoft Dataverse or your organization’s Azure Data Lake Gen2 storage
account.

A dataflow is a collection of tables that are created and managed in environments in the Power Apps service. You can add and edit tables in your dataflow, as well as manage data refresh
schedules, directly from the environment in which your dataflow was created.

Once you create a dataflow in the Power Apps portal, you can get data from it
using the Dataverse connector or Power BI Desktop Dataflow connector, depending on
which destination you chose when creating the dataflow.

There are three primary steps to using a dataflow:

1. Author the dataflow in the Power Apps portal. You select the destination to load the output data to, the source to get the data from, and the Power Query steps to transform the data using Microsoft tools that are designed to make doing so straightforward.

2. Schedule dataflow runs. This is the frequency in which the Power Platform Dataflow should refresh the data that your dataflow will load and transform.

3. Use the data you loaded to the destination storage. You can build apps, flows, Power BI reports, and dashboards or connect directly to the dataflow’s Common Data Model folder in your organization’s lake using Azure data services like Azure Data Factory, Azure Databricks, or any other service that supports the Common Data Model folder standard.

The following sections look at each of these steps so you can become familiar with the tools provided to complete each step.

## Create a dataflow

Dataflows are created in one environment. Therefore, you'll only be able to see and manage them from that environment. In addition, individuals who want to get data from your dataflow must have access to the environment in which you created
it.

> [!NOTE]
>
> - Creating dataflows is currently not available with Power Apps Developer Plan licenses.
> - The Firefox web browser currently isn't supported for use in creating and maintaining dataflows in Power Apps. More information: [You receive the error message "There was a problem refreshing the dataflow"](#you-receive-the-error-message-there-was-a-problem-refreshing-the-dataflow)

1. Sign in to Power Apps, and verify which environment you're in, find the environment switcher near the right side of the command bar.

    ![Environment switcher.](media/environment-switcher.png)

1. On the left navigation pane, select **Dataflows**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New dataflow**. On the **New Dataflow** page, enter a **Name** for the dataflow. By default, dataflows store tables in Dataverse. Select **Analytical entities only** if you want tables to be stored in your organization's Azure Data Lake storage account. Select **Create**.

     > [!IMPORTANT]
     > There's only one owner of any dataflow—the person who created it. Only the owner can edit the dataflow. Authorization
     > and access to data created by the dataflow depend on the destination you loaded
     > data to. Data loaded into Dataverse will be available via the Dataverse
     > Connector and requires the person accessing the data to be authorized to Dataverse.
     > Data loaded into your organization’s Azure Data Lake Gen2 storage account is
     > accessible via the Power Platform Dataflow connector and access to it requires
     > membership within the environment it was created in.

1. On the **Choose data source** page, select the data source where the tables are stored. The selection of data sources displayed allows you to create dataflow tables. 

    :::image type="content" source="media/choose-data-source.png" alt-text="Choose data source" lightbox="media/choose-data-source.png":::

1. After you select a data source, you’re prompted to provide the connection
settings, including the account to use when connecting to the data source. Select **Next**.

    ![Connect to data source.](media/data-source-provide-cred.png)

1. Once connected, you select the data to use for your table. When you
choose data and a source, the Power Platform Dataflow service will subsequently
reconnect to the data source in order to keep the data in your dataflow
refreshed, at the frequency you select later in the setup process.

    ![Choose data.](media/choose-data.png)

Now that you've selected the data to use in the table, you can use the dataflow editor to shape or transform that data into the format necessary for use in your dataflow.

## Use the dataflow editor to shape or transform data

You can shape your data selection into a form that works best for your table using a Power Query editing experience, similar to the Power Query Editor in Power BI Desktop. To learn more about Power Query, see [Query overview in Power BI Desktop](/power-bi/desktop-query-overview).

If you want to see the code that Query Editor is creating with each step, or if you want to create your own shaping code, you can use the advanced editor.

![Advanced editor.](media/advanced-editor.png)

## Dataflows and the Common Data Model

Dataflows tables include new tools to easily map your business data to the Common Data Model, enrich it with Microsoft and non-Microsoft data, and gain simplified access to machine learning. These new capabilities can be leveraged to provide intelligent and actionable insights into your business data. Once you’ve completed any transformations in the edit queries step described below, you can map columns from your data source tables to standard table columns as defined by the Common Data Model. Standard tables have a known schema defined by the Common Data Model.

For more information about this approach, and about the Common Data Model, see [The Common Data Model](/common-data-model/).

To leverage the Common Data Model with your dataflow, select the **Map to Standard** transformation in the **Edit Queries** dialog. In the **Map tables** screen that appears, select the standard table that you want to map.

![Map to standard table.](media/map-to-standard-entity.png)

When you map a source column to a standard column, the following occurs:

1. The source column takes on the standard column name (the column is renamed if
    the names are different).

2. The source column gets the standard column data type.

To keep the Common Data Model standard table, all standard columns that aren't mapped get *Null* values.

All source columns that aren't mapped remain as is to ensure that the result of the mapping is a standard table with custom columns.

Once you’ve completed your selections and your table and its data settings are complete, you’re ready for the next step, which is selecting the refresh frequency of your dataflow.

## Set the refresh frequency

Once your tables have been defined, you should schedule the refresh frequency for each of your connected data sources.

Dataflows use a data refresh process to keep data up to date. In the **Power Platform Dataflow authoring tool**, you can choose to refresh your dataflow manually or automatically on a scheduled interval of your choice.

### Schedule a refresh automatically

1. Select **Refresh automatically**.

2. Enter the dataflow frequency: 
   - **Frequency-based refresh**. Set how often in 30-minute increments, start date, and time in UTC.
   - **Refresh on specific days and times**. Choose time zone, frequency (daily or weekly) and time of day in 30-minute increments.

     ![Refresh automatically option.](media/refresh-automatically.png)

3. Select **Publish.**

Some organizations might want to use their own storage for creation and management of dataflows. You can integrate dataflows with Azure Data Lake Storage Gen2 if you follow the requirements to set up the storage account properly. More information: [Connect Azure Data Lake Storage Gen2 for dataflow storage](/power-query/dataflows/connect-azure-data-lake-storage-for-dataflow) 

## Troubleshooting data connections

There might be occasions when connecting to data sources for dataflows runs into issues. This section provides troubleshooting tips when issues occur.

- **Salesforce connector.** Using a trial account for Salesforce with dataflows results in a connection failure with no information provided. To resolve this, use a production Salesforce account or a developer account for
    testing.

- **SharePoint connector.** Make sure you supply the root address of the SharePoint site, without any subfolders or documents. For example, use a link similar to `https://microsoft.sharepoint.com/teams/ObjectModel`.

- **JSON File connector.** Currently you can connect to a JSON file using basic authentication only. For example, a URL similar to `https://XXXXX.blob.core.windows.net/path/file.json?sv=2019-01-01&si=something&sr=c&sig=123456abcdefg` is currently not supported.

- **Azure Synapse Analytics.** Dataflows don't currently support Microsoft Entra authentication for Azure Synapse Analytics. Use basic authentication for this scenario.

> [!NOTE]
> If you use data loss prevention (DLP) policies to block the **HTTP with Microsoft Entra (preauthorized)** connector then **SharePoint** and **OData** connectors will fail. The **HTTP with Microsoft Entra (preauthorized)** connector needs to be allowed in DLP policies for **SharePoint** and **OData** connectors to work.

### Troubleshoot the error: Connection to Dataverse failed. Please check the link below on how to fix this issue

Users might receive an error message if the connection they're using for export requires a fix. In this case, the user receives an error message that states **Connection to Dataverse failed. Please check the link below on how to fix this issue**.

To resolve this issue:

1. In Power Apps (make.powerapps.com), select **Connections** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
2. Locate the **Microsoft Dataverse (legacy)** connection.
3. Select the **Fix connection** link in the **Status** column, and follow the instructions on your screen.

After the fix completes, retry the export.

### You receive the error message "There was a problem refreshing the dataflow"

This error occurs when you try to refresh the dataflow while using the Firefox web browser. To work around this issue use a different web browser, such as Microsoft Edge or Google Chrome.

## Next steps

The following articles are useful for further information and scenarios when using dataflows:

-   [Add data to a table in Dataverse](/power-query/dataflows/add-data-power-query)

-   [Using an on-premises data gateway in Power Platform dataflows](/power-query/dataflows/using-dataflows-with-on-premises-data)

-   [Connect Azure Data Lake Storage Gen2 for dataflow storage](/power-query/dataflows/connect-azure-data-lake-storage-for-dataflow)

-   [Use dataflows in solutions](/power-query/dataflows/dataflow-solution-awareness)

For more information about the Common Data Model:

-   [Common Data Model - overview](/common-data-model/)

-   [Learn more about the Common Data Model schema and tables on GitHub](https://github.com/Microsoft/CDM)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

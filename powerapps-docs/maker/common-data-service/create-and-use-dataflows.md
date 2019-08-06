**Create and use dataflows in PowerApps**

With advanced data preparation available in **PowerApps**, you can create a
collection of data called a dataflow, which you can then use to connect with
business data from various sources, clean the data, transform it, and then load
it to Common Data Service or your organization’s Azure Data Lake Gen2 storage
account.

A **dataflow** is a collection of *entities* (entities are similar to tables)
that are created and managed in environments in the PowerApps service. You can
add and edit entities in your dataflow, as well as manage data refresh
schedules, directly from the environment in which your dataflow was created.

Once you create a dataflow in the PowerApps portal, you can get data from it
using the CDS connector or **Power BI Desktop** Dataflow connector, depending on
which destination you chose when creating the dataflow.

There are three primary steps to using a dataflow:

1.  Author the dataflow in the PowerApps portal. You will select the destination
    to load the output data to, the source to get the data from and the Power
    Query steps to transform to the data, using Microsoft tools that are
    designed to make doing so straightforward

2.  Schedule dataflow runs. This is the frequency in which the Power Platform
    Dataflow should refresh the data your dataflow will load and transform

3.  Use the data you loaded to the destination storage. You can build PowerApps,
    Flows, Power BI reports and dashboards or connect directly to the dataflow’s
    CDM Folder in your organization’s lake using Azure Data Services like Azure
    Data Factory, Azure Databricks or any other service that supports the CDM
    Folder standard.

In the following sections, we look at each of these steps and become familiar
with the tools provided to complete each step. Let’s get started.

**Create a dataflow**

Dataflows are created in one environment. therefore you will only be able to see
and manage them from that environment. In addition, individuals who want to get
data from your dataflow must have access to the environment in which you created
it.

1.  Sign in to PowerApps, and verify which environment you're in, find the
    environment switcher near the right side of the header.

    ![Environment switcher](media/02bce0f04ff38d4eba176fc34df8158b.png)

2.  Click or tap the down arrow for **Data** near the left edge.

![](media/83fa7f84fc28545e359d45718c645bff.png)

>   PowerApps home page

1.  In the list that appears, click or tap **Dataflows**, and then click or tap
    **New Dataflow** near the upper-right corner of the window.

It's important to know that there is only *one owner* of any dataflow, which is
the person who creates it. Only the owner can edit the dataflow. Authorzation
and access to data created by the dataflow depends on the destination you loaded
data to. Data loaded into Common Data Services will be available via the CDS
Connector and requires the person accessing the data to be authorized to CDS.
Data loaded into your organization’s Azure Data Lake Gen2 storage account, is
accessible via the Power Platform Dataflow connector and access to it requires
being a member of the environment it was created in.

![](media/acad12d2f984793be74e63036936e2a9.png)

From there, you select the destination storage where you want **Entities** to be
stored.

![](media/24f45f54440f3a0452284fef28f6a678.png)

**Select destination**

Dataflows can store entities in CDS or in your Organizations Azure Data Lake
storage account. Once you select a destination to load data to, provide a name
for the dataflow and click **Create**.

**Add entities**

An **entity** is a set of fields that are used to store data, much like a table
within a database. In the following image, you see the selection of data sources
from which you can create dataflow entities.

![](media/3a69d499cc057097f128dbe9252b01f4.png)

When you select a data source, you’re prompted to provide the connection
settings, including the account to use when connecting to the data source, as
shown in the following image.

![Connect to data source](media/a0f1b726606a22f9a886c67ebe5df43c.png)

Once connected, you can select which data to use for your entity. When you
choose data and a source, Power Platform Dataflow service will subsequently
reconnect to the data source in order to keep the data in your dataflow
refreshed, at the frequency you select later in the setup process.

![](media/7f1030dda94cc6b89dd3348805f908b5.png)

Once you select the data for use in the entity, you can use dataflow editor to
shape or transform that data into the format necessary for use in your dataflow.

**Use the dataflow editor**

Once you select which data from your source to use for your entity, you can
shape your data selection into a form that works best for your entity, using a
Power Query editing experience, similar to the Power Query Editor in Power BI
Desktop. You can learn more about Power Query (Power Query is incorporated into
Power BI Desktop as the Power Query Editor) in the [Query overview
article](https://docs.microsoft.com/en-us/power-bi/desktop-query-overview) for
Power BI Desktop.

If you want to see the code that Query Editor is creating with each step, or
want to create your own shaping code, you can use the Advanced Editor.

![](media/bf73d74354a12b6577d46f5657d48ab5.png)

**Dataflows and the Common Data Model (CDM)**

Dataflows entities include new tools to easily map your business data to the
Common Data Model (Microsoft’s standardized schema), enrich it with Microsoft
and third-party data, and gain simplified access to machine learning. These new
capabilities can be leveraged to provide intelligent and actionable insights
into your business data. Once you’ve completed any transformations in the Edit
Queries step, you can map columns from your data source tables to standard
entity fields as defined by the Common Data Model. Standard entities have a
known schema defined by the common data model.

Get more information about this approach, and about the Common Data Model, from
the [what is the Common Data
Model](https://docs.microsoft.com/powerapps/common-data-model/overview) article.

To leverage the Common Data Model with your dataflow, click on the **Map to
Standard** transformation in the **Edit Queries** dialog. In the **Map
Entities** screen that appears, you can select the standard entity to which you
want to map.

![](media/ec80ed002f70af46d723c777efe547db.png)

When you map a source column to standard field, the following occurs:

1.  The source column takes on the standard field name (the column is renamed if
    the names are different)

2.  The sources column gets the standard field data type

To keep the Common Data Model standard entity, all standard fields that are not
mapped get *Null* values.

All source columns that are not mapped remain as-is, to ensure that the result
of the mapping is a standard entity with custom fields.

Once you’ve completed your selections and your entity and its data settings are
complete,

you’re ready for the next step, which is selecting the refresh frequency of your
dataflow.

### Setting the refresh frequency

Once your entities have been defined, you’ll want to schedule the refresh
frequency for each of your connected data sources.

Dataflows use data refresh process to keep your data up to date. In the **Power
Platform Dataflow authoring tool,**

you can choose to refresh your dataflow manually or automatically on a scheduled
interval of your choice. To schedule refresh automatically, select **Refresh
automatically**, as shown in the following image.

![](media/4ee15b837d36486fcc6d5adba94c677a.png)

When you select the **refresh automatically** option you’re taken you set the
dataflow refresh frequency and start date and time, in UTC.

Once you’ve completed your dataflow refresh configuration your dataflow is ready
to be created, select **Create.**

**Connect to your dataflow in Power BI Desktop**

Once you’ve created your dataflow and you have scheduled the refresh frequency
for each data source that will populate the model, you’re ready for the third
and final step, which is connecting to your dataflow from within **Power BI
Desktop**.

To connect to the dataflow, in Power BI Desktop select **Get Data \> Power
Platform \> Power Platform dataflows (Beta)** as shown in the following image.

![](media/0bd68c2ac30442c7e7a18a6a4933d15a.png)

From there, navigate to the environment where you saved your dataflow, select
the dataflow and then select the entities that you created from the list.

You can also use the search bar, near the top of the window, to quickly find the
name of your dataflow or entities from among many dataflow entities.

When you select the entity and then select the **Load** button, the entities
appear in the **Fields** pane in Power BI Desktop, and appear and behave just
like tables from any other dataset.

**Using dataflows stored in Azure Data Lake Storage Gen2**

Some organizations may want to use their own storage for creation and management
of dataflows. You can integrate dataflows with Azure Data Lake Storage Gen2, if
you follow the requirements to set up the storage account properly.
Documentation of all the requirements for this approach can be found beginning
with the, Connect Azure Data Lake Storage Gen2 for dataflow storage article.

**Troubleshooting data connections**

There may be occasions when connecting to data sources for dataflows run into
issues. This section provides troubleshooting tips when such issues arise.

-   **Salesforce connector** - Using a trial account for Salesforce with
    dataflows results in a connection failure with no information provided. To
    resolve this, use a production Salesforce account or a developer account for
    testing.

-   **SharePoint connector** - Make sure you supply the root address of the
    SharePoint site, without any subfolders or documents. For example, use link
    similar to the following:
    [https://microsoft.sharepoint.com/teams/ObjectModel/](https://microsoft.sharepoint.com/teams/ObjectModel)

-   **JSON File connector** - Currently you can connect to a JSON file using
    basic authentication only. Connecting to a JSON file by providing the
    credentials within the URL (for example,
    <https://XXXXX.blob.core.windows.net/path/file.json?sv=2019-01-01&si=something&sr=c&sig=123456abcdefg..>.
    ) is **not** currently supported.

-   **Azure SQL Data Warehouse** - Dataflows do not currently support Azure
    Active Directory (AAD) authentication for Azure SQL Data Warehouse. Use
    Basic authentication for this scenario.

**Next steps**

This article described how you can create your own dataflow and refresh it. .
The following articles are useful for further information and scenarios when
using dataflows:

-   Add data to an entity in Common Data Service

-   Using dataflows with on-premises data sources

-   Connect Azure Data Lake Storage Gen2 for dataflow storage

For more information about the Common Data Model, you can read its overview
article:

-   [Common Data Model - overview
    ](https://docs.microsoft.com/powerapps/common-data-model/overview)

-   Learn more about the Common Data Model schema and entities on GitHub

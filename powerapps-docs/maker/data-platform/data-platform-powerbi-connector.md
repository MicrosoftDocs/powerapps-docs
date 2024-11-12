---
title: Create a Power BI report using the Microsoft Dataverse connector
description: Connect to your Microsoft Dataverse data from Power BI Desktop using the connector.
author: Mattp123
ms.component: cds
ms.topic: how-to
ms.date: 10/15/2024
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# Create a Power BI report using data from Dataverse

Microsoft Dataverse allows you to connect directly to your data using Power BI Desktop to create reports and publish them to Power BI. From Power BI, reports can be used in dashboards, shared to other users, and accessed cross platform on Power BI mobile apps.

![Power BI Desktop.](./media/data-platform-cds-powerbi-connector/PBIDesktop.png "Power BI Desktop")

## Prerequisites

To use Power BI with Dataverse, you need the following items:

* Download and install Power BI Desktop, which is a free application that runs on your local computer. You can download Power BI desktop [here](https://powerbi.microsoft.com/desktop/).
* A Power Platform environment with the following privileges: 
   * To access data in a table, you must have read privileges to the table.
   * To modify a table in Power Apps (make.powerapps.com), you must have a security role that includes maker privileges, such as system customizer or environment maker.
* You must have the appropriate Power BI [license](/power-bi/admin/service-admin-licensing-organization) to build and share Power BI reports.
* To use the **Dataverse** connector, the **Enable TDS endpoint** setting must be enabled in your environment. More information: [Manage feature settings](/power-platform/admin/settings-features)

> [!NOTE]
> Most proxy servers don’t handle the Tabular Data Stream (TDS) protocol data used by the Dataverse connector for Power BI.

## Connect to Dataverse using a connector

# [Dataverse connector](#tab/Dataverse)

1. Open **Power BI Desktop**. Select **Get data from other sources**.
1. In the **Get Data** list, select **Dataverse**, and then select  **Connect**.
1. If you're prompted, select or enter your user credentials, and then select **Connect**.
1. The list of Power Platform environments with Dataverse appears. In the list of environments, expand the environment you want, select the tables you want, and then select **Load**.
1. Select from the following **Data Connectivity** mode options:
   * **Import**: We recommend that you import data to Power BI wherever possible. With this mode, data is cached in the Power BI service and imported on a scheduled interval.
   * **DirectQuery**: Connects directly to the data in Dataverse.  Use this mode for real-time data retrieval. This mode can also more strictly enforce the Dataverse security model. More information: [DirectQuery model guidance in Power BI Desktop](/power-bi/guidance/directquery-model-guidance).
1. Select **OK**. You might be prompted to sign in using the same credentials you use to connect to Power Apps and Dataverse. Select **Connect**.

> [!IMPORTANT]
> To use the Dataverse connector, TCP ports 1433 and/or 5558 need to be open to connect. If only port 5558 is enabled, you must append that port number to the environment URL, such as *yourenvironmentid.crm.dynamics.com,5558*.

# [Dataverse (Legacy)](#tab/Legacy)

1. Open **Power BI Desktop**. Select **File** > **Get Data** > **Power Platform**.

1. Select the **Common Data Service (Legacy)** connector, and then select **Connect**.

   > [!NOTE]
   > This is the earlier version of the Dataverse connector. Use this connector when the query results will be greater than 80 MB. This version also supports paging of the query results and building reports that use the image data type.

1. In the dialog box that appears, paste in your complete environment URL into the **Server Url** box, in the format *https://org.crm.dynamics.com/*. More information: [Find your environment URL](#find-your-environment-url)

1. Select **OK**. You might be prompted to sign in using the same credentials you use to connect to Power Apps and Dataverse. Select **Connect**

1. The **Navigator** displays all tables available for your environment, such as the account and contact tables. Expand **Entities** to view and select the tables you want. For example, select the **account** table to see a preview of your data in the right pane. Select **Load**.
    > [!div class="mx-imgBorder"] 
    > ![Load account table rows.](./media/data-platform-cds-powerbi-connector/CreateReport5.png "Load account table rows")

---

## Build reports using Dataverse tables

After loading the tables by using a connector, you can begin building reports, or repeat the previous steps to add additional tables. For example, in the **Columns** pane, select the **name** column and then select the **numberofemployees** column. In the **Visualizations** pane, select **Pie chart**. These selections add a new visualization to your report canvas.

:::image type="content" source="./media/data-platform-cds-powerbi-connector/CreateReport7.png" alt-text="Power BI Desktop visualization." lightbox="./media/data-platform-cds-powerbi-connector/CreateReport7.png":::

## Special column types

### Choice columns

Choice columns are used in tables to provide a drop-down list of items to a user to make a single selection in apps and flows. When using the Dataverse connector, choice columns are presented as two columns to show both the unique value, and the display item value.

For example, if you had a choice column on your table called `approvalstatus`, you would see two columns in Power BI:

* `approvalstatus`  - This column shows a unique integer value for each item in your choice. `approvalstatus` can help when you apply filters so the filters won't be impacted when you make future changes to the display name.
* `approvalstatusname`  - This column shows the friendly display name of the item and is most commonly used when presenting the option in a table or chart.

    |`approvalstatus` |`approvalstatusname` |
    |---------|---------|
    1|Submitted
    2|In Review
    3|Approved
    4|Rejected

#### Performance impact and choice name columns

When retrieving the label name for a choice column, Dataverse makes a join with the internal `stringmap` table (where localized labels are stored). This is executed for each label/name column. Note that, this join and doing filters against the label name column, rather than the value column, can significantly impact report query performance.

### Choices columns

Choices are similar to choice columns with the difference being that users can select multiple items from the list. Choices aren't currently fully supported with the Dataverse connector.  When you use the Dataverse connector with choices columns, you only receive the integer values, which are comma separated. The item label name columns aren't returned. For more information about the Dataverse data types not supported with the Dataverse connector, see [Supported operations and data types](../../developer/data-platform/dataverse-sql-query.md#supported-operations-and-data-types).

### Lookups

Lookup columns use a many-to-one (N:1) table relationship between the table you’re working with and the target row type defined for the lookup. Lookups are presented in Power BI Desktop as two columns, `lookupid` and `lookupid-name`.

## Navigating relationships

Relationships in Dataverse require you to create a relationship within Power BI desktop between the two tables using a GUID column, this is a system-generated unique identifier that ensures relationships are created for the create rows where ambiguity or duplication might exist with other columns. You can read more about managing relationships in Power BI desktop [here](/power-bi/desktop-create-and-manage-relationships).

While some relationships might be automatically created, you can still review and ensure the correct relationships are established when creating your report:

* The lookup column on the table contains the GUID of the row in the related table.
* The related table has a column in the format "[tableName]ID" that contains the GUID, for example `Accountid` or `MyCustomtableid`
* Using the Power BI desktop Manage Relationships feature, you would create a new relationship between your lookup column, and the ID column on the related table.

## Find your environment URL

1. Open [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select the environment you're going to connect to, select **Settings** in the top-right corner, and then select **Session details**.

   :::image type="content" source="media/session-details.png" alt-text="Session details.":::
1. In the **Power Apps session details** dialog box, select **Copy Details**.
1. Paste the session details somewhere such as Notepad so that you can copy only the **Instance url**. The instance URL is the unique URL for your environment. The URL is in the format: `https://yourenvironmentid.crm.dynamics.com/`. Keep this somewhere handy so you can use it when creating your Power BI reports.

## Troubleshooting 

#### Workaround for very large number of lookups or choice columns

If the error message occurs in Power BI when you try to connect to a table with a very large number of lookups or choice columns, the following manual workaround might allow you to connect to the table. The  account, contact, and opportunity table might encounter this issue when they're extensively customized with additional lookups or choice columns.

Manually connect to the table in a Power BI report:

1. In Power BI desktop with the report loaded, select **Transform Data** to load Power Query.
2. Select **New Source** > **Blank Query**.
3. **Name** your query.
4. Select **Advanced Editor** on the **Home** tab of Power BI Desktop.
5. Replace the query text with this query text. 

   ```
   let
       Source = CommonDataService.Database("<myenvironment.crmX>.dynamics.com"),
       dbo_contact = Source{[Schema="dbo",Item="contact"]}[Data],
       #"selectedcolumns" = Table.SelectColumns(dbo_contact,{"fullname", "emailaddress1"})
   in
       #"selectedcolumns"
   ```
6. Replace *myenvironment.crmX* in the query text with your environment domain value, such as *contoso.crm4*.
7. Select **Done**.
8. Select **Choose columns** to add any additional needed columns.
9. Select **Close and Apply** to save model changes.
10. When prompted, select **Direct Query** for the new query.

The query can now be used in the report.

### Error message: Unable to connect (provider Named Pipes Provider, error: 40 – Could not open a connection to SQL Server)

When this error message occurs, the connector fails to connect to the TDS endpoint. This can occur when the URL used with the connector includes *https://* and/or the ending */*.

:::image type="content" source="media/tls-unable-to-connect.png" alt-text="Unable to connect error message.":::
Remove the https:// and ending forward slash so that the URL is in the form *orgname.crm.dynamics.com*.

### Troubleshooting connection issues

For information about troubleshooting connection issues when using the TDS endpoint, see [Troubleshooting connection problems](/powerapps/developer/data-platform/dataverse-sql-query#troubleshooting-connection-problems).

### See also

[Use composite models in Power BI Desktop](/power-bi/transform-model/desktop-composite-models)

[View Dataverse for Teams table data in Power BI Desktop](../../teams/view-table-data-power-bi.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

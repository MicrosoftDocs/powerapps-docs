---
title: Dataverse direct integration with Microsoft Fabric
description: Use Azure Synapse Link to export your Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 09/07/2023
ms.custom: template-how-to
---
# View in Microsoft Fabric

Dataverse direct integration with Microsoft Fabric enables organizations to extend their Dynamics 365 enterprise applications and business processes into Microsoft Fabric. **View in Microsoft Fabric** feature built into PowerApps makes all your Dynamics 365 data available for analysis in Microsoft Fabric.

-   No need to export data, build ETL pipelines, or use third-party integration tools.
-   You can link data from Dataverse directly into Microsoft Fabric, no need to bring your own storage
-   You can link existing Synapse Links or new links created with your own Azure storage 

With just one click, you’ll get more insights from your business data stored in Dataverse. ![View in Microsoft Fabric](media/Fabric/Azure-Synapse-Link-two-experiences.png)

As data gets updated, changes are reflected in Microsoft Fabric automatically. Dataverse also generates an enterprise-ready Synapse Lakehouse and SQL endpoint for your Dynamics 365 data. This makes it easier for data engineers and database admins to combine data from multiple sources and build custom analytics with Spark, Python, or SQL.

Microsoft Fabric’s lake-centric approach helps to eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers.

Makers can build low-code apps and automations to orchestrate business processes and react to insights found in Microsoft Fabric using connectors to over 1,000 apps. Add those insights back to Dataverse as external or virtual tables through the SQL endpoint and makers can turn them into low-code apps with Power Apps, Power Pages, or Power Automate using skills they already have.

Dataverse integration with Microsoft Fabric is currently in preview. 

## Launch Microsoft Fabric from PowerApps maker portal

Low code makers can use PowerApps maker portal to work with their data and build new Apps and automations using PowerApps, Power Automate and other tools already available in the Power platform. 

![View in Microsoft Fabric built into Power Apps Maker portal](media/Fabric/Maker-portal-view-in-fabric-2.png)

Now, makers can choose one or more tables from Dataverse and launch Microsoft Fabric with the “View in Microsoft Fabric” option. First time, System creates a workspace in your Power BI subscription and creates shortcuts in Fabric to Dataverse tables. System also creates a Synapse Lake house and a default data warehouse, enabling makers to explore data with SQL or work with Spark and other Fabric tools.

Makers can continue to add more data and launch Microsoft Fabric from the maker portal. Default Synapse Lakehouse and the Data warehouse gets updated with new data as changes happen in Dataverse.

## Add more data and manage your link
When makers choose to view in Fabric from maker portal, system creates optimized replicas of your data in Dataverse storage such that your operational workloads are not impacted. This replica is governed and secured by Dataverse while enabling Fabric workloads to operate on this data.
IT admins can manage this replica in Synapse Link page shown as **Managed Store** or **Microsoft OneLake**. IT admins can see tables added by makers and add/ remove tables as well as migrate the link to other environments. They can also see storage consumption in Power platform admin portal.

>**NOTES**
>
> 1.	You can’t add Dynamics Finance and Operations tables into Managed Store at this point in time. 
> 2.	Dataverse environment life cycle operations (ELO) such as environment move operations may impact reports built using this feature. See Known limitations section for more information. 
>

## Link existing Synapse Link profiles to Microsoft Fabric 
Synapse Link enabled IT admins to simplify their data integrations by provisioning and configuring Azure resources such as Azure Data lake storage and Azure Synapse. Now, you can enable Fabric links for your existing Synapse links and benefit from the innovations in Microsoft Fabric without any additional efforts or copying data. Microsoft Fabric integration further simplifies data integration efforts with features like Power BI DirectLake mode reports as well as query engine improvements in next generation Synapse Data warehouse. 

![View in Microsoft Fabric in Synapse Link](media/Fabric/Azure-Syunapse-Link-with-View-In-Fabric.png)

You can also add or removing tables from existing links and/or creating new Fabric links within a single experience. 
Customers can also use Synapse Link to choose tables and Entities from Dynamics 365 Finance and Operations (F&O). See <…>>


> NOTE
> 
> You need to create a Synapse Link profile and enable Delta/ parquet conversion for Fabric link option to be available. This option is not available for  Synapse Link profiles that use the CSV output format.
> 

## Build PowerApps with data from Microsoft Fabric

Makers can build Apps and automations with enterprise-wide data available in One Lake – the data store behind Microsoft Fabric. They can define external tables using the SQL endpoint available for Microsoft Fabric data and work with the data as if they were native Dataverse tables.




# Configure your environment

You can use an existing PowerApps environment or create a new developer environment using the link here: [Create a developer environment - Power Platform \| Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/developer/create-developer-environment)

You need system administrator permissions for your PowerApps environment to continue.

## Create a connection to your PowerApps environment
You need to perform this onetime operation in your Power BI environment for each Power Apps environment. This connection is used by Microsoft Fabric environment to connect to the Dataverse environment to access data. – this pre-requisite is temporary and may go away in the future.

1.  Choose Power BI settings (**Gear icon** on top right of Power BI window) and select **Manage connections and gateways**

![](media/Fabric/Fabric-launch-connections-and-gateways.png)

2.  In the Data (preview) window, choose **+ New** option to create a new connection.
3.  Choose **Cloud** and choose Connection type as **dataverse**
4.  Provide **Connection name** and the **Environment Domain**. You can obtain the connection name from the power platform Admin center. You must enter the **Environment URL** you get from admin center into both the fields. Remember to remove https:// and the trailing /

    ![Create a one time connection](media/Fabric/Fabric-setting-up-connection.png)

5.  Choose **OAth2** as the Authentical model
6.  Choose the Edit credentials link and confirm your credentials.
7.  Review the connection information and choose **Create**.

Now you are ready to link your Data with Fabric.  




# Launch Microsoft Fabric from PowerApps 
After configuration, you can launch Microsoft Fabric from the PowerApps maker portal in 2 ways. 

- **Tables menu:** System create a Power BI workspace and lakehouse with default settings. This is the quickest approach to get started.
- **Synapse Link menu:** This option lets you choose your own Power BI workspace and provides granular control. Synapse Link menu also enables monitoring and managing links. 


## Launch Microsoft Fabric from Tables menu in PowerApps
You can create a Link simply by choosing tables from the PowerApps maker portal. System creates a Power BI workspace, a link and launches Microsoft Fabric with default settings. You can add more tables to this link later from Tables menu in PowerApps maker portal. 

![View in Microsoft Fabric built into Power Apps Maker portal](media/Fabric/Maker-portal-view-in-fabric-2.png)


1.  Launch Power apps maker portal with the URL and the feature flags shown below

    **https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true**

2.  In case you have multiple environments, choose the environment you configured  
3.  Choose **Tables** on the left navigation and choose **Account** table.
4.  Click on “**…”** and choose **view in Microsoft Fabric**. You can also choose view in Microsoft Fabric option in the top menu
5.  For the first time, you will see a dialog box confirming the name of the Power BI workspace. Select OK to continue. Subsequent table selections will be added to the same workspace. You will not be asked to confirm.
6.  Synapse Lake house should launch in a separate browser window

>  **NOTE**:
>
>  The system may take \~15 mins to update data in managed lake including conversion to Delta-parquet format. If you have selected a larger table, the initial load time make take a little longer. When you launch Fabric lake house, you will see the links as “unidentified” until the initial sync is completed. See known limitation section to trouble-shoot any issues you may see on screen.
>
> 


## Manage Microsoft Fabric links 
You can add/remove tables in the default Fabric link or create new links using the Synapse Link menu. You can also link existing Synapse Link profiles with Microsoft Fabric using this option. You need to be a system administrator in the PowerApps environment to manage Fabric links.


### Manage the default link (aka. Managed store or Microsoft OneLake)
If you or someone else launched maker portal and linked tables earlier, you will notice a default Fabric link called **Managed Store** or **Microsoft OneLake**. All tables chosen in the maker experience (ie. previous step) will be included in the Managed Store. 

You can add more tables or remove tables included in the Default link. 

Managed store uses Dataverse provisioned file storage. When you purchase PowerApps or Dynamics licenses, you will receive a storage quota for your organization. When you add more tables to Managed store, this quota is consumed depending on the size of table. You can purchase additional storage as required to expand the quota. You can see storage consumption in the PowerApps admin portal.



1.  Launch Power apps maker portal with the URL and the feature flags shown below

    **https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true**

2. Select **Azure Synapse Link** option from the left navigation in PowerApps maker portal.
3.  You will notice the default Synapse link profile called **Managed Store** or **Microsoft OneLake**. You can choose **view in Microsoft Fabric** by selecting Managed store.
4.  If you or a user in this environment launched maker portal and linked tables earlier, you will notice all tables chosen in the maker experience (ie. previous step).
5.  You can add, remove tables linked to Fabric by choosing the **Manage Tables** option. You can select one or more tables from this option.
6.  When you add a table, the system will perform an initial sync and replicate data in Dataverse storage. When the initial sync is completed, system will create a Dataverse shortcut to Fabric. You can see the status of tables added via Tables menu in maker portal as well as tables added using Manage tables option here.
7.  When the Sync status is **Active**, as data gets updated, your data changes are shown in reports created in Microsoft Fabric.
8.  If you or someone added a new column to a table that’s already added to Managed Lake (also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You may need to review the report and downstream data flows to see that they are not impacted by the change.
9.  You can launch Fabric by selecting **view in Microsoft Fabric** option
10.  You can also **Unlink**, ie. remove Fabric Links created by the system. When ulinking, the system does not remove the Fabric workspace or the lakehouse created since you may have added your own tables and links. You do need to visit Microsoft Fabric and remove the lakehouse and/or workspace yourself.

>
> **NOTE**:
> Depending on the size of data, the initial copy may take longer to complete. For subsequent updates, system may take \~15 mins to update data in managed lake including conversion to Delta-parquet format. When you launch Fabric lake house you will see the links as “unidentified” until the initial sync is completed.
>
> See known limitation section to trouble-shoot any issues you may see on screen.
>


## Link existing Synapse Links with Microsoft Fabric

You can link your existing Synapse Link profiles with Microsoft Fabric from the Synapse Link menu. You need to choose the “Enable Parquet/ Delta lake option” to enable view in Microsoft Fabric feature for Synapse Link profiles. 

To enable an existing Synapse link, 

1.	Launch Power apps maker portal with the URL and the feature flags shown below
**https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true**

2. Select **Azure Synapse Link** option from the left navigation in PowerApps maker portal.
3. Choose your existing Synapse Link profile and select **Link to Microsoft Fabric**.
4. You will be asked to choose a Power BI premium workspace to continue. System will show a list of worspaces in the same region as your environment. See the next section if you don’t see a workspace shown in the drop down list. You may need to create a workspace and revisit this step.
5. Select OK. System will perform validations and create the required artifacts in Fabric.  
6.	You can click the **View in Microsoft Fabric** option to launch Fabric Lakehouse. 
7.	You can add or remove tables using the **Manage tables** option. When you add a table, the system will perform an initial sync. When the initial sync is completed, select the **Refresh Fabric tables** option to refresh Dataverse shortcut already added to your Fabric Lakehouse.

>
> **NOTES:**
> You need to choose the “Enable Parquet/ Delta lake option” to enable view in Microsoft Fabric.
> Existing Synapse Link profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.
>

## Create a Fabric workspace 
You need to create a new Fabric workspace or choose an existing workspace to link with an existing Synapse Link. It is recommended that you create a new workspace to direct link to Dataverse. 

This feature is only available in Fabric (or Power BI) premium workspaces. If you don’t have Power BI premium or Fabric capacity, you can sign-up for a Free Fabric trial capacity by visiting here: [Fabric (preview) trial - Microsoft Fabric \| Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)

To confirm that you can create a premium workspace. Choose **workspace settings \> premium** and ensure that you have **Trial** or **Premium capacity** selected. The workspace you choose to link with Dataverse must be assigned to a Premium capacity in the same region as your Dataverse. 

![Premium or Trial capacity assigned to a Fabric workspace](media/Fabric/Fabric-trial-capacity.png)

Launch Microsoft Fabric with the URL shown below (notice the new URL, you can also get to preview by launching PowerBI.com)
https://fabric.microsoft.com

Contact your Power BI administrator if you don't have permissions to create workspaces. 



# Working with Dataverse data in Microsoft Fabric

You can view the Synapse Lakehouse, SQL endpoint and the default dataset generated by Dataverse in the Microsoft Fabric workspace you have chosen earlier.

When you choose **view in Microsoft Fabric** option PowerApps maker portal or in Synapse Link, Dataverse generated Synapse lake house will be launched. You can navigate into other Fabric features yourself and work with Fabric and Power BI.

## Explore Dataverse generated Synapse Lakehouse

You will notice the tables you have selected being added to the Synapse Lakehouse as shown below. These tables are linked to your PowerApps environment using **Dataverse shortcuts**. As data changes in Dataverse, the Dataverse shortcuts in Fabric will reflect the latest data. 
Also note that Dataverse manages these shortcuts. You should not delete or remove these shortcuts in Microsoft fabric. If you delete them inadvertently, you can revisit the Synapse Link menu in PowerApps and choose **Refresh Fabric Links** option to recreate the links.


![Dataverse generated Synapse Lakehouse](media/Fabric/Fabric-with-DV-shortcuts-shown.png)

**NOTE**: During preview, the system make take \~15minute or more to reflect the tables. You may see table names as **undefined** during that time.

## Explore data with SQL endpoint
You can launch SQL endpoint and query Dataverse data with SQL and generate views in Microsoft Fabric

![Choose SQL endpoint](media/Fabric/Fabric-choose-SQL-endpoint.png)

Select SQL endpoint from the top right context menu and the same data will be shown in a SQL friendly experience where you can create SQL queries and views.

![SQL endpoint with Dataverse generated shortcuts](media/Fabric/Fabric-SQL-endpoint-shortcuts-shown.png)


## Auto create a Power BI report

You can choose the default dataset generated by Dataverse and choose Auto create a report. The system generates a PowerBI report with the data you have selected as shown below.

![](media/Fabric/Fabric-autocreated-PBI-report.png)

## Secure data in the workspace 
You have linked PowerApps and Fabric workspaces as a system administrator. You need to secure the data in this workspace before you share this data with others. 
>
> **NOTE:**
>
> In the future, you will be able to apply security definitions in PowerApps to data in the workspace.
>

# Build Apps and automations with Fabric data in Maker portal

By now, you may have explored Dataverse data with the Synapse Lakehouse, SQL endpoint as well as Power BI. You can also bring your own data into Microsoft Fabric and combine, re-shape and aggregate data with data from Dataverse. You can use Fabric tools such as SQL, Spark, Data flows to work with your data within Microsoft Fabric. For an example;

-	Combine financial data from Dynamics 365 with financial data from other systems to derive consolidated insights
-	Merge historical data (ingested into OneLake from legacy systems) with current business data from Dynamics and PowerApps
-	Combine weblogs and telemetry data from your web site with product and order details from Dynamics 
-	Apply machine learning and detect anomalies and exceptions within your data.
  
Insights are not complete unless you can drive action and business processes. You can bring data in OneLake into Dataverse as external tables and use that data to build PowerApps or create business automations.

## Choose data from Microsoft Fabric
1.	You can bring data in a Lakehouse into Dataverse by choosing the corresponding SQL endpoint. Choose the SQL endpoint corresponding to the Lakehouse
2.	You can also bring data from a data warehouse into Dataverse.
3.	In either the SQL endpoint or the data warehouse, Select the gear icon on top left to launch the properties window.
4.	Copy the (1) SQL connection string and the (2) name from the properties window

![Choose SQL endpoint](media/Fabric/Fabric-SQL-endpoint-for-defining-virtual-tables.png)


## Define Dataverse external tables
5.	Launch PowerApps maker portal and select Tables menu. Choose **Create a virtual table** 

![Create virtual table](media/Fabric/Fabric-choose-SQL-endpoint-new-experience.png)

6.	Select SQL server as the connection. 
7.	Paste the SQL connection string you copied in step (1) above. 
8.	Enter the name of the data warehouse or SQL endpoint you copied (2) above. 
9.	Choose tables from the Fabric. When complete, you can continue to work with the tables and build Apps.


# Known limitations.

1.  This feature is in preview. Preview features are not ready for production use and are provided to validate and to provide feedback to product team
2.  Depending on the size of data, initial sync may take 15min or more. In case of very large tables, initial sync may take much longer before you can consume data in Microsoft Fabric.
3.  After the initial sync, data changes in Dataverse will be reflected in Microsoft Fabric upto 15mins later.

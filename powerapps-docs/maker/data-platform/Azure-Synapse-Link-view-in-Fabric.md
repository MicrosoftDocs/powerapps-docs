
# Overview

Dataverse direct integration with Microsoft Fabric enables organizations to extend their Dynamics 365 enterprise applications and business processes into Fabric. **View in Microsoft Fabric** feature built into PowerApps maker portal makes all your Dynamics 365 data available for analysis in Microsoft Fabric.

-   No need to copy data, build ETL pipelines, or use third-party integration tools.
-   You can use Dataverse provisioned storage, ie. the data lake build into Dataverse, no need to bring your own storage or Synapse compute
-   You can integrate existing Synapse Links or new links created with your own Azure storage

With just one click, you’ll get more insights from your business data stored in Dataverse. ![A screenshot of a computer Description automatically generated](media/56e40ffbfe294b0418216d111bb4e558.png)

As data gets updated, changes are reflected in Microsoft Fabric automatically. Dataverse also generates an enterprise-ready Synapse Lakehouse and SQL endpoint for your Dynamics 365 data. This makes it easier for data engineers and DB admins to combine data from multiple sources and build custom analytics with Spark, Python, or SQL.

Microsoft Fabric’s lake-centric approach helps to eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers.

Makers can build low-code apps and automations to orchestrate business processes and react to insights found in Microsoft Fabric using connectors to over 1,000 apps. Add those insights back to Dataverse as external or virtual tables through the SQL endpoint and makers can turn them into low-code apps with Power Apps, Power Pages, or Power Automate using skills they already have.

Dataverse integration with Microsoft Fabric is currently in private preview. To join the preview, visit [https://aka.ms/DataverseExtendsToFabric](https://aka.ms/DataverseExtendsToFabric  ).

# View in Microsoft Fabric in PowerApps maker portal

Low code makers can use PowerApps maker portal to work with their data and build new Apps and automations using PowerApps, Power Automate and other tools already available in the Power platform. ![A screenshot of a computer Description automatically generated](media/d52815e01e49e42594fea32f9991c0fb.png)

Now, makers can choose one or more tables from Dataverse and launch Microsoft Fabric with the “View in Microsoft Fabric” option. First time, System creates a workspace in your Power BI subscription and creates shortcuts in Fabric to Dataverse tables. System also creates a Synapse Lake house and a default data warehouse, enabling makers to explore data with SQL or work with Spark and other Fabric tools.

Makers can continue to add more data and launch Microsoft Fabric from the maker portal. Default Synapse Lakehouse and the Data warehouse gets updated with new data as changes happen in Dataverse.

# Build Apps and automations with data from Microsoft Fabric and One Lake

Makers can build Apps and automations with enterprise-wide data available in One Lake – the data store behind Microsoft Fabric. They can define external tables using the SQL endpoint available for Microsoft Fabric data and work with the data as if they were native Dataverse tables.

# IT admins can direct link to Microsoft Fabric

Synapse Link feature in Dataverse is used by IT admins to integrate Dynamics and PowerApps data with Azure Synapse. Synapse Link helped with configuring and provisioning Azure resources in the past. IT admins had to work with Synapse query and integrate Power BI for reporting (or Azure data factory to integrate data).

![A screenshot of a computer Description automatically generated](media/755cd92a5f6993d5623cfc69bbec0134.png)Now Synapse Link enables IT admins to direct link to Microsoft Fabric and work with SQL and other workloads without provisioning Synapse and other services.

**NOTES:**

1.  If you would like to use Dataverse provisioned storage, you can use the “Managed Store” link already available and add tables.
2.  If you are using your own storage, you need to create a Synapse Link profile and enable Delta/ parquet conversion for this option to be available. This option is not available for Synapse Link profiles that use the CSV output format.
3.  Dataverse environment life cycle operations (ELO) such as environment move operations may impact reports built using this feature. See Known limitations section for more information.

# Configure your environment

1.  You can use an existing PowerApps environment or create a new developer environment using the link here: [Create a developer environment - Power Platform \| Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/developer/create-developer-environment)
2.  Launch Power apps maker portal with the URL (notice additional parameters switches you need to include to enable the new experiences)

    **https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true**

3.  This feature is only available in Power BI premium workspaces. If you don’t have Power BI premium capacity, you can sign-up for a Free Fabric trial capacity by visiting here: [Fabric (preview) trial - Microsoft Fabric \| Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)
4.  It is highly recommended that you create a new Power BI workspace to direct link to Dataverse. You can use this workspace to validate Synapse Link scenario.
5.  To confirm that you can create a premium workspace. Choose **workspace settings \> premium** and ensure that you have **Trial** or **Premium capacity** selected.

![A screenshot of a computer Description automatically generated](media/319368344bd004b4df96367184cd8fbc.png)

1.  Launch Power BI with Microsoft Fabric with the URL to work with Microsoft Fabric

    **https://app.powerbi.com?trident=1**

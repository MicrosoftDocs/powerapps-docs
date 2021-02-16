---
title: "Ingest Microsoft Dataverse data with Azure Data Factory | MicrosoftDocs"
ms.custom: ""
ms.date: 07/29/2020
ms.reviewer: "matp"
author: sabinn-msft
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "powerapps"
ms.assetid: 
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Ingest exported Microsoft Dataverse data with Azure Data Factory

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

After exporting data from Dataverse to Azure Data Lake Storage Gen2 with the Export to Data Lake service, you can use Azure Data Factory to create dataflows, transform your data, and run analysis.

This article shows you how to perform the following tasks: 

1.  Generate a manifest.json from the existing model.json in the Data Lake Storage Gen2 storage account that holds the exported data.

2.  Set the Data Lake Storage Gen2 storage account with the Dataverse data as a *source* in a Data Factory dataflow.

3.  Set the Data Lake Storage Gen2 storage account with the Dataverse data as a *sink* in a Data Factory dataflow.

4.  Run your dataflow by creating a pipeline.

## Prerequisites

This section describes the prerequisites necessary to ingest exported Dataverse data with Data Factory.
 
### Azure roles

The user account that's used to sign in to Azure must be a member of the
*contributor* or *owner* role, or an *administrator* of the Azure subscription.
To view the permissions that you have in the subscription, go to the [Azure portal](https://portal.azure.com/), select your username in the upper-right corner, select **...**, and then select **My permissions**. If you have access to multiple subscriptions, select the appropriate one. To create and manage child resources for Data Factory in the Azure portal&mdash;including datasets, linked services, pipelines, triggers, and integration runtimes&mdash;you must belong to the *Data Factory Contributor* role at the resource group level or above.

### Export to data lake

This article assumes that you've already exported Dataverse data by using the [Export to Data Lake service](export-to-data-lake.md).

In this example, account table data is exported to the data lake.

## Generate the manifest.json from the model.json

1.  Go to [this GitHub repository](https://github.com/t-sazaki/ConvertModelJsonToManifestOriginal) and download it to your computer.

2.  Go to ConvertModelJsonToManifest-master/ConvertModelJsonToManifest-master/ConvertModelJsonToManifest.sln.

3.  Right-click to select the file, and then open it in Visual Studio. If you don't have Visual Studio, you can follow this article to install it: [Install Visual Studio](/visualstudio/install/install-visual-studio?view=vs-2019).

4.  Go to **Project** > **Manage NuGet Packages**, and ensure that the
    following NuGet packages are installed:

    -   Microsoft.CommonDataModel.ObjectModel

    -   Microsoft.CommonDataModel.ObjectModel.Adapter.Adls

    -   Microsoft.IdtableModel.Clients.ActiveDirectory

    -   Newtonsoft.Json

    -   NLog

5. If you're missing the Common Data Model packages or they're unavailable, you can add them by following these steps:

    1. Select the gear icon to access package settings.
       ![Package settings gear icon](media/package-settings-gear.png "Package settings gear icon")

    2. Select **+** in the pop-up window to add a new package source. 
       ![Add a new package](media/add-new-package.png "Add a new package")

    3.  Configure the new package source, and then select **OK**:

        1.  For **Name**, enter **CDM**.

        2.  For **Source**, enter **https[]()://commondatamodel.pkgs.visualstudio.com/_packaging/CDM/nuget/v3/index.json**.

    4.  Make sure that the package source is set to **All**.

8.  In Program.cs, fill in the storage container information on line 26, as indicated here:

    1. Replace **your-storage-account** by substituting the name of your storage account.
       ![Your storage account substitution](media/your-storage-account.png "Your storage account substitution")

    1. Replace **your-folder-name** with the folder containing the model.json file. Go to your storage account **Overview** > **Storage Explorer** > **Containers**, and then select the correct folder name. 
      ![Replace your folder name](media/replace-your-folder-name.png "Replace your folder name")

    1.  Replace the access key with the access key for this storage account. Go to your storage account, and on the left panel under **Settings**, select **Access Keys**. Select **Copy** to copy the access key and replace it in the code.

9.  Optionally, you can change the name of the manifest file as indicated in the code comments.

10.  Run the code, and refresh your storage container to find the new manifest, table, resolved table, and config files.

> [!NOTE]
> If there are changes made to the metadata of the table, you must delete the generated files from the Data Lake and regenerate an updated manifest file by running the code again. It is recommended that you maintain the same name of the manifest file, so there is no need to update any Azure Data Factory dataflows or pipelines.

## Set the Data Lake Storage Gen2 storage account as a source

1.  Open [Azure Data Factory](https://ms-adf.azure.com/home?factory=%2Fsubscriptions%2Fd410b7d3-02af-45c8-895e-dc27c5b35342%2FresourceGroups%2Fsama%2Fproviders%2FMicrosoft.DataFactory%2Ffactories%2Fadfathena), and then select **Create data flow**. 

2.  Turn on **Data flow debug** mode. This might take up to 10 minutes, but you
    can proceed with the following steps.

    ![Dataflow debug mode](media/data-flow-debug.png "Dataflow debug mode")

3.  Select **Add Source.**

    ![Add source](media/add-source.png "Add source")

4.  Under **Source settings**, do the following<!--Suggested. It's "configure the following options" here and "select the following options" in the next procedure, but these are a combination of entering and selecting.-->:

    - **Output stream name**: Enter the name you want. 
    - **Source type**: Select **Common Data Model**.
    - **Linked Service**: Select the storage account from the drop-down menu, and then link a new service by providing your subscription details and leaving all default configurations.
    - **Sampling**: If you want to use all your data, select **Disable**.

5.  Under **Source options**, do the following:

    - **Metadata format**: Select **Manifest**. 
    - **Root location**: In the first box (**Container**), enter the container name. In the second box (**Folder path**), enter **/**. 
    - **Manifest file**: Leave the first box (**table path**) blank, and in the second box (**Manifest name (default)**), enter the first part of the manifest file name, such as *test.manifest.cdm.json* **/** *test*).

       ![Source options, part one](media/source-options.png "Source options, part one")

    - **Schema linked service**: Select the same storage container as the source settings.
    - **Container**: Enter the container name.
    - **Corpus folder**: Leave blank.
    - **table**: Enter text in the format **/*table*Res.cdm.json/*table***, replacing *table* with the table name you want, such as account.

       ![Source options, part two](media/source-options-two.png "Source options, part two")

## Set the Data Lake Storage Gen2 storage account 

After setting the exported Dataverse data in the Data Lake Storage Gen2 storage account as a source in the Data Factory dataflow, there are many possibilities for transforming your data. More information: [Azure Data Factory](/azure/data-factory/introduction)

Ultimately, you must set a sink for your dataflow. Follow these instructions to set the Data Lake Storage Gen2 storage account with the data exported by the Export to Data Lake service as your sink.

1.  Select **+** in the lower-right corner, and then search for and select **Sink**.

2.  On the **Sink** tab, do the following:

    - **Output stream name**: Enter the name you want, such as *Sink1*.
    - **Incoming stream**: Select the source name you want. 
    - **Sink type**: Select **Common Data Model**. 
    - **Linked service**: Select your Data Lake Storage Gen2 storage container that has the data you exported by using the Export to Data Lake service.

      ![Configure the Sink tab](media/configure-sink.png "Configure the Sink tab")

3. On the **Settings** tab, do the following:

    - **Schema linked service**: Select the final destination storage container. 
    - **Container**: Enter the container name. 
    - **Corpus folder**: Enter **/** 
    - **table**: Enter text in the format **/*table*Res.cdm.json/*table***, replacing *table* with the table name you want, such as account.

      ![Configure the sink Settings tab, part one](media/configure-settings.png "Configure the sink Settings tab, part one")

    - **Root Location**: In the first box (**Container**), enter the container name. In the second box (**Folder path**), enter **/**. 
    - **Manifest file**: Leave the first box (**table path**) blank, and in the second box (**Manifest name (default)**), enter the first part of the manifest file name, such as *test.manifest.cdm.json / test*.
    - **Format type**: Select your file format preference.

      ![Configure the sink Settings tab, part two](media/configure-settings-two.png "Configure the sink Settings tab, part two")

## Run your dataflow

1.  In the left pane under **Factory Resources**, select **+**, and then select **Pipeline**.

     ![Create a new pipeline](media/create-pipeline.png "Create a new pipeline")

2.  Under **Activities**, select **Move & Transform**, and then drag **Data flow** to the workspace.

3.  Select **Use existing data flow**, and then select the dataflow that you
    created in the previous steps.

4.  Select **Debug** from the command bar.

5.  Let the dataflow run until the bottom view shows that is has been completed. This might take a few minutes.

6.  Go to the final destination storage container, and find the transformed table data file.

### See also

[Analyze Dataverse data in Azure Data Lake Storage Gen2 with Power BI](export-to-data-lake-data-powerbi.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
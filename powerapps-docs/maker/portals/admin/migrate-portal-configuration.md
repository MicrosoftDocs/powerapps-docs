---
title: Migrate portal configuration
description: Learn how to migrate portal configuration.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/03/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Migrate portal configuration

Portal development involves several configurations and customizations to achieve a desired experience for portal end users.

After you have completed development or configuration of your portal instance, you might want to migrate your latest portal configuration from development to testing or the production environments. 

Migration involves exporting the existing configuration from the source Microsoft Dataverse environment, and then importing it into the target Dataverse environment.

## Prepare the target environment

> [!NOTE]
> Preparing the target environment is a one-time process. You will need to provision a new portal in order to install the managed portal solutions on Dataverse as well as configure the portal web application. The process also installs default portal metadata which will be replaced with portal metadata from your source environment.

1. [Provision a new portal](../create-portal.md) in your target environment. Use the same [portal template](../create-dynamics-portal.md) as you provisioned on your source environment. For example, if you provisioned the **Dynamics 365 Customer Self-Service** portal on your source environment, provision the **Dynamics 365 Customer Self-Service** portal on your target environment.

1. On the *target* environment, using the [Portal Management app](../configure/configure-portal.md), delete the newly created website record. This will remove the default portal configuration data from the target environment.

    :::image type="content" source="media/migrate-portal-config/delete-website.png" alt-text="Delete website record.":::

1. On the *target* environment, delete the portal app. This will remove the portal app currently configured to render the default portal.

    > [!NOTE]
    > Do not delete the Portal Management app!

    :::image type="content" source="media/migrate-portal-config/delete-portal.png" alt-text="Delete portal app.":::

1. Transfer the portal metadata from the source environment using the [Power Platform CLI](#transfer-portal-configuration-using-power-platform-cli) or the [Configuration Migration Tool](#transfer-portal-configuration-using-the-configuration-migration-tool). 

1. On the target environment, provision a new portal using the existing portal website option. This process will configure a portal using the portal configuration you transferred from the source environment.

    :::image type="content" source="media/migrate-portal-config/provision-portal.png" alt-text="Provision new portal.":::

1. The portal updates from the source environment should be reflected in this new target environment. Going forward, you should be able to transfer configuration from your source to target environments by transferring the portal configuration data.

## Transfer portal metadata

# [Power Platform CLI](#tab/CLI)

### Transfer portal configuration using Power Platform CLI

The Microsoft Power Platform CLI provides many features specifically for [portals](../power-apps-cli.md). These commands allow you to download portal configuration from a source environment and transfer it to a target environment. These commands can also be incorporated into your ALM processes.

1. Create Power Platform CLI authentication profiles to connect to both your source and target environments. You can give them a name to easily identify the target and source environments.

    ```powershell
    pac auth create --name [name] --url [environment url]
    ```

    **Example**

    ```powershell
    pac auth create --name PORTALDEV --url https://contoso-org.crm.dynamics.com
    ```

1. When the authentication profiles are created, they'll have an associated index that can be determined using the list command.

    ```powershell
    pac auth list
    ```

    :::image type="content" source="media/migrate-portal-config/pac-auth-list.png" alt-text="List of environments.":::

1. Select the Power Platform CLI authentication profile connected to the source environment.

    ```powershell
    pac auth select --index [source environment index]
    ```

    **Example**

    ```powershell
    pac auth select --index 1
    ```

1. Determine the website ID for the source portal.

    ```powershell
    pac paportal list
    ```

    :::image type="content" source="media/migrate-portal-config/portal-list.png" alt-text="List of portals.":::

1. Download the portal configuration data to your local workstation. Use the *--overwrite* option set to *true* if you have previous downloaded portal configuration to the same path.

    ```powershell
    pac paportal download --path [path] --webSiteId [website id]
    ```

    **Example**

    ```powershell
    pac paportal download --path c:\paportals\ --webSiteId db9db518-ea5c-ec11-8f8f-00224804e6cd
    ```

1. Select the Power Platform CLI authentication profile connected to the target environment.

    ```powershell
    pac auth select --index [target environment index]
    ```

    **Example**

    ```powershell
    pac auth select --index 2
    ```

1. Upload the portal configuration data to the target environment.

    ```powershell
    pac paportal upload --path [path]
    ```

    **Example**

    ```powershell
    pac paportal upload --path "C:\paportals\portaldev"
    ```

> [!NOTE]
> The Power Platform CLI tool does not migrate tables or table schema. Migration may fail with missing elements such as tables and fields when configuration data is mismatched with selected schema.
> During import, ensure the destination environment contains the same portal type already installed with any additional customizations such as tables, fields, forms or views imported separately as solutions.

# [Configuration Migration Tool](#tab/CMT)

### Transfer portal configuration using the Configuration Migration Tool

>[!NOTE]
> The preferred method is to use the [Power Platform CLI](#transfer-portal-configuration-using-power-platform-cli) to transfer portal metadata.

To export configuration data, you would need to use the Configuration Migration tool and a portal-specific configuration schema file. For more information about this tool, see [Manage configuration data](/dynamics365/customer-engagement/admin/manage-configuration-data).

> [!NOTE]
> - We recommend you to use the latest version of the Configuration Migration tool. The Configuration Migration tool can be downloaded from NuGet. More information for downloading the tool: [Download tools from NuGet](/dynamics365/customer-engagement/developer/download-tools-nuget).
> - The minimum solution version of portals supported by schema files for configuration migration is 8.4.0.275. However, we recommend that you use the latest solution version.
> - Source and destination organizations must have same default language for the migration to work successfully.

Schema files are available for the following portal types:

- **Portals created in an environment with Dataverse**
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/p/?linkid=2110477)
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/p/?linkid=2162831) (for version [9.2.2103.x](../versions/package-version-9.2.2103.md))
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/?linkid=2186536) (for version [9.3.2201.x](../versions/package-version-9.3.2201.md) or higher)

- **Portals created in an environment containing customer engagement apps (such as Dynamics 365 Sales and Dynamics 365 Customer Service)**
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/p/?linkid=2019804)
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/p/?linkid=2162733) (for version [9.2.2103.x](../versions/package-version-9.2.2103.md))
    - [Custom portal (Blank portal)](https://go.microsoft.com/fwlink/?linkid=2186261) (for version [9.3.2201.x](../versions/package-version-9.3.2201.md) or higher)
    - [Community portal](https://go.microsoft.com/fwlink/p/?linkid=2019704)
    - [Customer Self-Service portal](https://go.microsoft.com/fwlink/p/?linkid=2019705)
    - [Partner portal](https://go.microsoft.com/fwlink/p/?linkid=2019803)
    - [Employee Self-Service portal](https://go.microsoft.com/fwlink/p/?linkid=2019802)

The default schema files contain information about portal tables, relationships, and uniqueness definitions for each entity. More information: [Export portal configuration data](#export-portal-configuration-data)

After exporting the configuration data, you must import it into the target environment. More information: [Import portal configuration data](#import-portal-configuration-data)

> [!NOTE]
> The Configuration Migration tool uses schema to export and import configuration data. The tool does not migrate tables or table schema. Migration may fail with missing elements such as tables and fields when configuration data has mismatch with selected schema.
>
> During export, ensure the source environment contains portal tables as specified in Configuration Migration tool schema file. You can still alter the schema files to add, remove, and modify tables, attributes, and so on to migrate subset of configuration data.
>
> During import, ensure the destination environment contains the same portal type already installed with any additional customizations such as tables, fields, forms or views imported separately as solutions.


## Export portal configuration data

You can export portal configuration data from a source system by using portal-specific configuration schema files.

1.	Download the Configuration Migration tool and extract to the desired folder.

2.	Download a portal configuration schema file using links provided above for your portal type.

3.	Double-click the **DataMigrationUtility.exe** file in the 
`<your_folder>\Tools\ConfigurationMigration` folder to run the Configuration Migration tool, choose **Export data** in the main screen, and then select **Continue**.
    
    > [!div class=mx-imgBorder]
    > ![Export configuration data.](../media/export-config-data.png "Export configuration data")

4.	On the **Login** screen, provide authentication details to connect to your Dataverse environment from where you want to export data. If you have multiple organizations on the Dataverse environment from where to export the data, select the **Display list of available organizations** check box, and then select **Login**.

    > [!div class=mx-imgBorder]
    > ![Provide authentication details to connect to your Dataverse environment from where you want to export data.](../media/export-config-login.png "Provide authentication details to connect to your Dataverse environment from where you want to export data")

5.	If you have multiple organizations, and you had selected the **Display list of available organizations** check box in the previous step, the next screen allows you to choose the organization that you want to connect to. Select a Dataverse environment to connect to. 

    > [!NOTE]
    > If you do not have multiple organizations, this screen is not displayed.

6.	In **Schema file**, browse and select the portal-specific configuration schema file to be used for the data export.

7.	In **Save to data file**, specify the name and location of the data file to be exported.

    > [!div class=mx-imgBorder]
    > ![Specify schema and target files.](../media/export-config-file-name.png "Specify schema and target files")

8.	Select **Export Data**. The screen displays the export progress status and the location of the exported file at the bottom of the screen once the export is complete.

    > [!div class=mx-imgBorder]
    > ![Progress of configuration data export.](../media/export-config-status.png "Progress of configuration data export")

9.	Select **Exit** to close the tool.

## Import portal configuration data

1.	Run the Configuration Migration tool and choose **Import data** in the main screen, and then select **Continue**.

    > [!div class=mx-imgBorder]
    > ![Import configuration data.](../media/import-config-data.png "Import configuration data")

2.	On the **Login** screen, provide authentication details to connect to your Dataverse environment from where you want to export data. If you have multiple organizations on the Dataverse environment from where to export the data, select the **Display list of available organizations** check box, and then select **Login**.

3.	If you have multiple organizations, and you had selected the **Display list of available organizations** check box in the previous step, the next screen allows you to choose the organization that you want to connect to. Select a Dataverse environment to connect to. 

    > [!NOTE]
    > - If you do not have multiple organizations, this screen is not displayed.
    > - Ensure that the portal solution is already installed for the organization where you plan to import the configurations.

4.	The next screen prompts you to provide the data file (.zip) to be imported. Browse to the data file, select it, and then select **Import Data**. 

    > [!div class=mx-imgBorder]
    > ![Progress of configuration data import.](../media/import-config-status.png "Progress of configuration data import")

5.	The next screen displays the import status of your records. The data import is done in multiple passes to first import the foundation data while queuing up the dependent data, and then import the dependent data in the subsequent passes to handle any data dependencies or linkages. This action ensures clean and consistent data import. 

6.	Select **Exit** to close the tool. 

---

### Create new portal using migrated data

If the migration process is updating an existing portal, the updates should now be visible in the target environment. If the migration is for a new portal, you can now create the new portal for the imported website record by using the option **Use data from existing website record**. More information: [Create portal](../create-portal.md)

## Tenant-to-tenant migration

Power Apps portals doesn't support tenant-to-tenant migration. To migrate a portal from one tenant to another, you must follow these steps:

1. [Reset](reset-portal.md) your portal in the source tenant.

1. Provision a new portal in an environment [with Dataverse](../create-portal.md) or [containing customer engagement apps](../create-dynamics-portal.md).

1. Migrate portal configurations and customizations using the [steps](#transfer-portal-metadata) explained in this article earlier.

### See also

- [Track changes to Power Apps portals configuration](../faq.yml#how-do-i-track-changes-to-power-apps-portals-configuration-).
- [Portals support for Microsoft Power Platform CLI](../power-apps-cli.md).
- Tenant-to-tenant migration of a [Power Platform environment](/power-platform/admin/move-environment-tenant).
- Tenant-to-tenant migration of [model-driven apps](/dynamics365/admin/move-instance-tenant) in Dynamics 365 such as Sales, Customer Service, Marketing, Field Service, and Project Service Automation.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
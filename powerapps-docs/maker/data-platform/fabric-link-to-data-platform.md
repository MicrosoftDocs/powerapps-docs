---
title: Configure your environment and link to Microsoft Fabric
description: This article shows you how to configure your Power Platform environment so you can link it to Microsoft Fabric.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
contributors: saviegas
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 07/06/2026
ms.custom: template-how-to
---
# Link to Microsoft Fabric

Microsoft Fabric integration with Microsoft Dataverse allows you to seamlessly link your Power Platform environment to Microsoft Fabric, enabling advanced data analysis and reporting capabilities. This guide provides step-by-step instructions on configuring your environment, linking it to Microsoft Fabric, and managing linked tables.

You can use an existing Dataverse environment or create a new developer environment if you want to try this feature. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Prerequisites

- You must have the System Administrator security role in the Power Platform environment to enable **Link to Fabric** or **Synapse Link**. This role is also required to add application users in your environment who need access to work with this feature by using the Power Platform admin center.
- You must be an administrator of the Power BI workspace. 
- If you want the system to create a Power BI workspace, you need to have Power BI Capacity Administrator access to a capacity within the same region as the Dataverse environment.
- A Power BI premium license or Fabric capacity within the same Azure geographical region as your Dataverse environment is required. If you don’t have Power BI premium license or Fabric capacity within the same geographical region, you can buy a capacity or sign up for a free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)
- Your administrator needs to grant you access to create Fabric lakehouses and artifacts. You can find these settings in the Fabric admin portal. Go to **Tenant Settings** > **Microsoft Fabric** > **Users can create Fabric items**, **Tenant settings** > **Workspace settings** > **Create workspaces** as well as **Tenant settings** > **oneLake settings** > **Users can access data stored in OneLake with apps external to Fabric**.
- If you plan to use workspace identity authentication, you must be a workspace admin to create and manage a workspace identity. The workspace you're creating the identity for can't be a My Workspace. More information: [Workspace identity in Fabric](/fabric/security/workspace-identity)
- If you plan to use workspace identity authentication, the workspace identity must be onboarded as an application user in the Dataverse environment and granted the appropriate role (commonly System Administrator) so it can access Dataverse data on behalf of Fabric.
- You must have permissions in Fabric to manage connections via **Settings** > **Manage connections and gateways**.
- To confirm whether you have access to the required premium capacity, go to [Power BI](https://app.powerbi.com), open the workspace, and select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected.
   :::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

## Create a link to Fabric

The **Link data** page in Power Apps is the home for every way you move Dataverse data out for analytics. It has two sections: **Fabric Links** for links to Microsoft Fabric, and **Other Links** for Azure Synapse Link and other targets. Start a Fabric link from this page:

1. Sign in to [Power Apps](https://make.powerapps.com) and select the environment you want.
1. On the left navigation pane, select **Link data**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

   :::image type="content" source="media/fabric/link-data-01.png" alt-text="Screenshot of the Link data page showing the Fabric Links and Other Links sections and the option to create a new Fabric link." lightbox="media/fabric/link-data-01.png":::

1. Select **+ New link**, and then in the **Create new link** pane, select the **Link data via Fabric** tile, which is marked **Recommended**.

   :::image type="content" source="media/fabric/link-data-create-new-link.png" alt-text="Screenshot of the Create new link pane with Link data via Fabric marked Recommended and Azure Synapse listed under other available links." lightbox="media/Fabric/link-data-create-new-link.png":::

> [!TIP]
> You can also start a Fabric link in context from the Power Apps **Tables** area: select **Analyze** > **Analyze in Fabric** on the command bar. This shortcut opens the same wizard. The **Tables** > **Analyze** menu creates Fabric links only. You can no longer create an Azure Synapse Link from **Tables** > **Analyze**. To create an Azure Synapse Link, use the **Link data** page and select **Other Links**.

The Fabric link wizard guides you through four steps: **Getting started**, **Setup Configuration**, **Select Tables**, and **Review and create**.

### Step 1: Getting started

The wizard opens on a **Getting started** page that summarizes what the link does and checks your prerequisites and Fabric capacity. If you don't have a Fabric capacity in the same geography or region as your Dataverse environment, the wizard notifies you to get a capacity in the required geography. Select **Next** to continue.

:::image type="content" source="media/fabric/link-data-wizard-01.png" alt-text="Screenshot of the Getting started step in the Fabric link wizard." lightbox="media/fabric/link-data-wizard-01.png":::

### Step 2: Set up configuration

On the **Setup Configuration** step, select the target Fabric **workspace**, and then create the **Connection** that authenticates to Fabric. When you create the connection, choose one of three authentication options. **Workspace identity** is the recommended option: it removes the need to manage secrets and avoids the service principal misconfiguration that is the most common Fabric link setup failure.

> [!IMPORTANT]
> Workspace identity is a property of the Fabric *workspace*, not the Dataverse link. A Fabric workspace admin enables it once on the workspace, outside Dataverse. After it exists on the workspace, every Dataverse link to that workspace can use it. To enable it, go to [Create and manage a workspace identity](/fabric/security/workspace-identity#create-and-manage-a-workspace-identity).

   - **Workspace Identity**:  
     To use this option, you must first create a workspace identity in Fabric:  
       1. In Fabric, open the target workspace.  
       2. Go to **Workspace settings** > **Workspace Identity**.  
       3. Select **+ Workspace Identity** to create it.  
          - Note the name of the workspace identity (it matches the workspace name).  
          :::image type="content" source="media/fabric/fabric-link-workspace-identity.png" alt-text="Workspace identity page in Fabric. The name, such as `srr-athena-test` in this example, is used later when adding the application user in Dataverse.":::
 
       4. For more information, go to [Workspace identity in Fabric](/fabric/security/workspace-identity).  

   - **Create an application user with workspace identity**:  
     After you create the identity, add it as an application user in Dataverse:  
       - Go to **Power Platform admin center** > **Users (See all)** > **App users list**.  
       - Select **+ New app user**, then **+ Add an app**, search for the workspace name you noted earlier (srr-athena-test in the above example), and add it.  
       - Assign the correct **Business unit** and **System Administrator** role, then select **Create**.  
     For detailed steps, go to the [Create an application user in Dataverse](/power-platform/admin/manage-application-users?tabs=new#create-an-application-user) step.

   - **Service Principal**:  
       To use this option, go to the create an application user with workspace identity previous step to create a service principal. Then, follow these steps:  
       1. First, add the service principal as an application user in Dataverse following the same process described in the **Workspace Identity** section.  
       2. After adding the application user, return to the **Link to Fabric** wizard.  
       3. In the connection setup, provide the following details for your service principal:  
          - **Tenant ID**: Your Azure tenant identifier.
          - **Client ID**: The application (client) ID of your service principal.
          - **Key**: The client secret or certificate for authentication.
       4. Save the connection to complete the setup.

   - **Organizational Account**:  
     Provide your credentials and save the connection. To change credentials later, select **Switch account** and provide new credentials.

When the selected workspace has a workspace identity configured, the wizard recommends selecting it as the authentication kind for the connection.

:::image type="content" source="media/fabric/link-data-wizard-03.png" alt-text="Screenshot of the Setup Configuration step showing a workspace that has a workspace identity configured, with a note recommending you select it for the connection." lightbox="media/fabric/link-data-wizard-03.png":::

If the selected workspace doesn't have a workspace identity yet, the wizard tells you so. You can continue with an organizational account or service principal, or ask a Fabric workspace admin to add a workspace identity to the workspace.

:::image type="content" source="media/fabric/link-data-wizard-02.png" alt-text="Screenshot of the Setup Configuration step showing that the selected workspace doesn't have a workspace identity configured, with the option to continue using an organizational account or service principal." lightbox="media/fabric/link-data-wizard-02.png":::

When the connection is established, the step shows a success confirmation. Select **Next** to continue.

:::image type="content" source="media/fabric/link-data-wizard-04.png" alt-text="Screenshot of the Setup Configuration step showing the connection to Microsoft Fabric established successfully." lightbox="media/fabric/link-data-wizard-04.png":::

> [!NOTE]
> If you use workspace identity or service principal authentication, onboard the identity as an application user in the Dataverse environment and grant the appropriate role (commonly System Administrator) so it can access Dataverse data on behalf of Fabric. For more information, see [Create an application user in Dataverse](/power-platform/admin/manage-application-users?tabs=new#create-an-application-user).

### Step 3: Select tables

1. On the **Select Tables** step, choose the Dataverse tables you want to sync to Fabric. If your environment is linked to finance and operations apps, you can also select tables from those apps. By default, the wizard selects Dataverse tables that have the **Track changes** property enabled. Clear any tables you don't want to sync. Only selected tables consume storage in Fabric, so you can optimize costs by excluding tables you don't need.
1. Select **Next**.

   :::image type="content" source="media/fabric/link-data-wizard-05.png" alt-text="Screenshot of the Select Tables step in the Fabric link wizard showing Dataverse and finance and operations tables with checkboxes and a count of selected tables." lightbox="media/fabric/link-data-wizard-05.png":::

> [!NOTE]
> You can change this selection any time after setup from the standalone **Manage tables** surface. You no longer have to edit the link to add or remove tables. For more information, see [Add or remove tables linked to Fabric](#add-or-remove-tables-linked-to-fabric).

### Step 4: Review and create

On the **Review and create** step, review your selections, and then select **Finish**. The wizard creates the workspace artifacts, creates the shortcuts, and performs the first initialization. You can watch the progress of each task on this step.

:::image type="content" source="media/fabric/link-data-wizard-08.png" alt-text="Screenshot of the Review and create step showing the link creation tasks completed." lightbox="media/fabric/link-data-wizard-08.png":::

When the link is created, it appears under **Fabric Links** on the **Link data** page. You land directly in the standalone **Manage tables** surface for the new link, which you can also open at any time from the command bar.

:::image type="content" source="media/fabric/link-data-wizard-09.png" alt-text="Screenshot of the Fabric link created successfully and listed under Fabric Links on the Link data page." lightbox="media/fabric/link-data-wizard-09.png":::

> [!NOTE]
>
> It might take up to 60 minutes to update data in OneLake including the conversion to delta parquet format. If you selected a table that contains a lot of data, the initial load time might take longer. When you open Fabric lakehouse, the links appear as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](fabric-troubleshoot.md)
>
> When the initial sync is complete, the system continuously refreshes updates in Dataverse in the lakehouse. It might take up to 60 minutes for the data to be refreshed especially during peak load periods.
>
> If you have more than 2,000 active Dataverse tables, Link to Fabric can fail with an error. Go to [Troubleshooting common issues](fabric-troubleshoot.md) for help with resolving issues.
>
> The link was labeled as **Microsoft OneLake** and is now labeled **Link to Fabric**.

> [!IMPORTANT]
> The lakehouse created by Link to Fabric currently follows the naming pattern `<environmentname>_<internalprofile>_<workspace>_<uniquevalue>` (for example, the `internalprofile` portion appears as `CDS2` or `CDS3`). Don't take a dependency on this lakehouse name in your downstream code, queries, or pipelines. The name format is subject to change without notice, and the historical significance of the `CDS2` or `CDS3` segment no longer applies and is likely to be dropped in the future. Reference the lakehouse through stable identifiers (such as the workspace and lakehouse ID) instead of parsing the display name.

## Low-latency sync

Low-latency sync is a faster sync engine for Link to Fabric. It writes data directly from the Dataverse database to Delta Parquet, removing the intermediate CSV step used by the previous pipeline.

Benefits:

- Faster initial sync.
- Faster delta sync for incremental changes.
- Higher throughput for finance and operations apps tables, up to 1M or more records per hour per table. Actual sync times depend on initial load, data churn, table sizes, and number of columns.

Low-latency sync rolls out by station and is enabled automatically. There's no separate opt-in. Once your station is enabled, new Link to Fabric setups use the new engine through the same setup experience.

To confirm a profile is running on low-latency sync, select **Link data** from the left navigation, and then select your Fabric link under **Fabric Links**. If you see the **Low-latency mode** flag on your Fabric link in the link list, low-latency sync is enabled for that profile.

:::image type="content" source="media/fabric/low-latency-sync-page.png" alt-text="Link data page showing the Low-latency mode flag on a Fabric link." lightbox="media/Fabric/low-latency-sync-page.png":::

Existing Fabric link profiles continue to use the previous sync engine. To move an existing profile to low-latency sync after it's available in your station, unlink the profile and relink it.

> [!NOTE]
> Unlinking and relinking triggers a full initial sync for all configured tables.

> [!IMPORTANT]
>
> If you use long-term retention and currently see live and retained data together through Fabric shortcuts, note the following before you unlink and relink for low-latency sync:
> - After you relink, the shortcuts include **live data only**. Retained data is no longer surfaced through the shortcuts for the tables you relinked, so reporting on retained data through Fabric isn't available for those tables.
> - Long-term retention itself isn't affected. Retention jobs continue to run as configured, and your retained data is preserved. Only the shortcut-based reporting view of retained data is impacted.
> - We're working on migrating retained data to the low-latency sync format. Once that migration completes, your previously retained data starts appearing through the relinked profile alongside live data, with no further action required from you.
> - Low-latency sync writes timestamp columns as **INT64**. The **INT96** timestamp format used by the previous Fabric link sync engine isn't supported. Review any downstream dependencies such as queries, pipelines, semantic models, or external readers that explicitly handle INT96 timestamps and update them to read INT64.

### Prerequisites for finance and operations apps

If you're running finance and operations apps, your environment must be on a supported build before low-latency sync works. The following table lists the minimum required builds by app version.

| Finance and operations version | Minimum platform build | Minimum application build |
|---|---|---|
| 10.0.46 | 7.0.7778.126 | 10.0.2428.196 |
| 10.0.47 | 7.0.7858.115 | 10.0.2527.135 |
| 10.0.48 | 7.0.7996.48 | 10.0.2645.55 |

To check your build, in your finance and operations environment, go to **Help & Support** > **About** to see your current platform and application build numbers.

If your build is below the minimum listed for your app version, apply the latest quality update for your version before setting up low-latency sync.

> [!NOTE]
> If you're not sure which app version you're on, contact your system administrator or Microsoft support team.

## Manage link to Fabric

This section describes how to add or remove tables linked to Fabric, configure the link to use workspace identity, and share the data connection with other users.

### Add or remove tables linked to Fabric

Manage the tables linked to Fabric from the standalone **Manage tables** surface. Open it from the command bar on your Fabric link at any time. You don't need to edit the link to add or remove tables. Your Fabric links appear under **Fabric Links** on the **Link data** page.

:::image type="content" source="media/fabric/link-data-manage-tables.png" alt-text="Screenshot of a Fabric link selected on the Link data page with Manage tables and other actions available on the command bar." lightbox="media/fabric/link-data-manage-tables.png":::

#### Add tables to Fabric

1. Sign in to [Power Apps](https://make.powerapps.com). 
   > [!NOTE]
   > This feature is enabled by default on all environments. Power Platform admins can disable this feature in the Power Platform admin center. More information: [Environment settings: Microsoft Fabric](/power-platform/admin/settings-features?tabs=new#microsoft-fabric)

1. Select **Link data** from the left navigation pane, and then select your Fabric link under **Fabric Links**.
1. Open Fabric by selecting **View in Microsoft Fabric**.
1. Add more table links to Fabric by selecting **Manage tables**.
1. When you add a table, the system performs an initial sync and indexes the data. When the initial sync is completed, a shortcut to OneLake is created. View the status of tables by selecting **Manage tables**. Use the **Refresh Fabric tables** option to add the newly enabled table in Fabric. You might need to review the report and downstream data flows to ensure that they're not impacted by the change.

   > [!NOTE]
   > If your environment is linked to a Dynamics 365 finance and operations environment, the add tables option enables you to include tables from finance and operations apps. Learn more: [Choose finance and operations data in Azure Synapse Link for Dataverse](azure-synapse-link-select-FnO-data.md)

1. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
1. If you add a new column to a table that’s already part of the profile (also known as a metadata change), use the **Refresh Fabric tables** option from the command bar to update the change in Fabric. The update occurs after the next table data change is triggered. You might need to review the report and downstream data flows to confirm that they're not impacted by the change.
1. You can also **Unlink**, which removes the Fabric link to your Dataverse environment. When unlinking, the Fabric lakehouse is also removed.

> [!NOTE]
> If you've installed Dynamics 365 apps such as Customer Insights, the tables required for the app are also included in the **Link to Fabric** link.

#### Remove tables from Fabric

You can stop syncing specific Dataverse and finance and operations apps tables to reduce storage costs and optimize your Fabric workspace. After accessing **Manage tables** (as described in step 4 in [Manage link to Fabric](#manage-link-to-fabric)), follow these steps to unlink tables:

1. The **Manage tables** pane shows all Dataverse and finance and operations apps tables currently linked to Fabric.
1. Tables that are already syncing are checked.
1. To stop syncing a table, clear the option to select it.

   :::image type="content" source="media/fabric/manage-tables-unlink.png" alt-text="Screenshot of the Manage tables pane showing checked and unchecked tables for syncing to Fabric." lightbox="media/fabric/manage-tables-unlink.png":::

1. To keep syncing, leave it checked.
1. After making your selections, select **Save**.
1. A confirmation dialog appears listing the tables that stop syncing.

   :::image type="content" source="media/fabric/unlink-confirmation-dialog.png" alt-text="Screenshot of the confirmation dialog showing tables that will be unlinked from Fabric and stop syncing." lightbox="media/fabric/unlink-confirmation-dialog.png":::

1. Review the list, and then select **Confirm**.

After confirmation:

- Shortcuts for the unselected tables are removed from the Fabric lakehouse.
- Selected tables are removed from the internal storage that are synchronized to Fabric via shortcuts. This ensures that you're paying only for the storage of tables that you selected.
- Synchronization stops immediately for those tables no longer selected.
- Remaining tables continue syncing without interruption.

> [!IMPORTANT]
>
> - Some system tables and tables required by Microsoft add-ins can't be removed. More information: [Are there system tables that are automatically synchronized and can't be unlinked?](fabric-link-faq.yml#are-there-system-tables-that-are-automatically-synchronized-and-can-t-be-unlinked)
> - Removing a table doesn't delete the table in Dataverse; it only removes the OneLake shortcut and stops data sync.
> - If you need to add tables later, repeat the same steps and check the tables you want to include. More information: [Manage link to Fabric](#manage-link-to-fabric).

### Configure Fabric link to use workspace identity

If you linked your Dataverse environment to Fabric earlier using an organizational account, you can switch to workspace identity or service principal. Workspace identity is a Fabric managed service principal bound to a specific workspace; it removes the need to manage secrets and enables secure, keyless authentication for Fabric items that connect to Dataverse.

#### Things to verify before you begin

Before proceeding, ensure you meet the requirements described in the [Prerequisites](#prerequisites) section, and specifically verify these three essential items:

- Workspace identity exists: The target Fabric workspace must have a workspace identity configured. Go to **Workspace settings** > **Workspace Identity**. If the identity doesn't exist, create it first. More information: [Workspace identity in Fabric](/fabric/security/workspace-identity)
- Dataverse application user: The same workspace identity must be onboarded as an application user in the Dataverse environment and granted the appropriate role (commonly System Administrator) so it can access Dataverse data on behalf of Fabric. This might already be in place if you followed the **Workspace Identity** steps in the [Create a link to Fabric](#create-a-link-to-fabric) section previously.
- Rights to edit connections: You must have permissions in Fabric to manage connections via **Settings** > **Manage connections and gateways**.

#### What changes?

After you update the connection's authentication method to Workspace identity, all Fabric items that use that connection (for example, Lakehouses via OneLake shortcuts, Dataflows Gen2, pipelines, semantic models) authenticate with your workspace identity going forward.

#### Before you begin

Identify the connection name. When you used **Link to Microsoft Fabric**, the system created a Dataverse connection that typically includes (or matches) your environment name. You update this specific connection.

#### Switch to workspace identity authentication

1. **Open Fabric settings**
   - In Microsoft Fabric, select the gear icon (top right) and choose **Settings** > **Manage connections and gateways**.

   :::image type="content" source="media/fabric/fabric-settings-manage-connections.png" alt-text="Screenshot showing how to access Fabric settings by selecting the gear icon and choosing Settings > Manage connections and gateways." lightbox="media/Fabric/fabric-settings-manage-connections.png":::

1. **Locate the Dataverse connection created by Link to Fabric**
   - In **Manage connections and gateways**, open the **Connections** tab (if not already selected).
   - Find the connection associated with your Dataverse environment. The **Link to Fabric** wizard typically creates this connection and names it using your environment's name so it's easy to recognize.

1. **Open the connection's management pane**
   - Select the ellipsis (⋮) next to the connection and choose **Settings** to open its settings.

   :::image type="content" source="media/fabric/fabric-connection-settings-authentication.png" alt-text="Screenshot showing the connection settings pane with Authentication section and Authentication method dropdown showing Workspace identity, OAuth 2.0, and Service Principal options." lightbox="media/Fabric/fabric-connection-settings-authentication.png":::

1. **Switch the authentication method to Workspace identity**
   - In the connection's **Settings** pane, go to **Authentication**.
   - From the **Authentication method** dropdown, select **Workspace identity**.
   - Select **Save** to apply the change.

> [!NOTE]
> If your items run through a gateway, review your gateway and cloud connection policies as applicable. Fabric's manage connections and gateways experience governs connection usage, including gateway scenarios for shareable cloud connections.

### Share the data connection with other users

The system creates a data connection between the Power Platform environment and Fabric workspace using the credentials of the user at the time of link creation. If you use the **Fabric link** option from the Power Apps **Tables** area, the system creates the connection and asks you to save it. If you use the **Synapse Link** option, you must create a data connection yourself before enabling the link. 

The system uses this connection to enable Fabric users to connect to Dataverse - the data store behind the Power Platform environment. If you want to enable other users to add or remove tables to Fabric link, you need to share this data connection with other users. 

1. Follow steps 1-2 from [Switch to workspace identity authentication](#switch-to-workspace-identity-authentication) to access **Manage connections and gateways** and locate your Dataverse connection.
1. Once you select the correct data connection, select **...** > **Manage users**. Then you're shown users who have access to this connection.
1. Enter the name or email of other users who need access to data. When you select a user, specify either the **Owner** role or **Reader** role. You only need to provide reader role to enable them to consume data. The users you specify receive an e-mail confirming access to data.

You might need to grant access to other users to this workspace so that they can work with data. Depending on the need for data access, you might need to secure the data in this workspace before you share this data with others. You can secure the lakehouse as well as tables within the lakehouse using OneLake security. More information: [OneLake security overview](/fabric/onelake/security/get-started-security)

You can only create user based connections at this time.

## Link existing Azure Synapse Link for Dataverse links with Fabric

You can link your existing Azure Synapse Link for Dataverse profiles with Fabric. These profiles appear under **Other Links** on the **Link data** page. You need to select the **Enable Parquet/Delta lake** option to enable the view in the Fabric feature for Azure Synapse Link for Dataverse profiles.

To enable an existing link, follow these steps:

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Select **Link data** from the left navigation, and then select **Other Links**.
1. Select an existing Azure Synapse Link for Dataverse profile, and then select **Link to Microsoft Fabric**.
1. You're prompted to choose a Power BI premium workspace to continue. A list of workspaces in the same region as your environment are displayed. If you don’t see a workspace in the drop-down list, you might need to create one, and then return to this task. More information [Link to Microsoft Fabric](#link-to-microsoft-fabric)
1. Select **OK**. Validations are performed and the required artifacts are created in Fabric.  
1. Select **View in Microsoft Fabric** open Fabric lakehouse.
1. You can add or remove tables by selecting **Manage tables**. When you add a table, an initial sync is performed. When the initial sync is completed, select **Refresh Fabric tables** to refresh the Dataverse shortcut added to your Fabric lakehouse.

> [!NOTE]
>
> - Select **Enable Parquet/Delta lake** to enable the view in Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.
> - Currently, Azure Synapse Link profiles secured with managed identities, formerly Managed Service Identity (MSI), can't be linked to Microsoft Fabric.  

## Next steps

[Work with Dataverse data and generate Power BI reports](fabric-work-data-and-power-bi.md)

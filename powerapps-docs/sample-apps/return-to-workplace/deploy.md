---
title: Deploy the Return to Workplace solution
description: Provides an overview of how to deploy the Return to the Workplace Solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/05/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Deploy the Return to the Workplace solution

This article provides step-by-step instructions to IT administrators for deploying the Return to the Workplace solution.

Estimated time to complete these steps: 60&ndash;90 minutes

## Prerequisites

- You should be a Global administrator or Microsoft Power Platform administrator to perform the installation.

- You must be a Global administrator and must have a Power BI Pro license to configure and publish reports.

- Sign in to Power BI and create a workspace to publish the report. More information: [Create the new workspaces in Power BI](https://docs.microsoft.com/power-bi/collaborate-share/service-create-the-new-workspaces) and [Share the workspace with others](https://docs.microsoft.com/power-bi/collaborate-share/service-create-the-new-workspaces#give-access-to-your-workspace)

## Step 1: Sign up for Power Apps and create an environment

Sign up for [Power Apps](https://docs.microsoft.com/power-platform/admin/signup-for-powerapps-admin) if you don't have it already, and purchase an appropriate license. More information: [Power Apps pricing](https://powerapps.microsoft.com/pricing/)

After you've purchased Power Apps, create an environment with a Common Data Service database.

1. Sign in to the [Power Platform admin center](https://aka.ms/ppac).

2. Create a Common Data Service environment with a database. More information: [Create and manage environments](https://docs.microsoft.com/power-platform/admin/create-environment)

   > [!IMPORTANT]
   > If you select a security group for the database while you're creating it, the apps can be shared only with users who are members of the security group.

3. Create appropriate users, and assign security roles. More information: [Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles)

After you've created your environment and it is ready, you can access it by using the following URL: `https://[myenv].[region].dynamics.com`, where [myenv] is the name of your environment and [region] is the deployment region, for example, crm for US. Make a note of this environment URL.

## Step 2: Install the package

You can install the Return to the Workplace solution from AppSource. 

> [!NOTE]
> If you are a US Government customer, you'll have to install using the deployment package available on GitHub. More information: [Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)](#appendix-deploy-the-app-and-publish-power-bi-dashboard-us-government-customers-only).

1. Go to [AppSource](https://aka.ms/rtw-app) to install the **Return to the Workplace solution**.

    > [!div class="mx-imgBorder"]
    > ![Installation page](media/return-to-workplace-installationpage.png "Installation page")

2. Select **GET IT NOW** to install the solution in your environment. You'll be redirected to the actual installation page, where you can select the environment where you want to install it. Installation starts after you select the environment and accept the terms and agreement.

3. After the app is installed, sign in to [Power Apps](https://make.powerapps.com) and select your environment from the upper-right corner. In the left pane, select **Apps** to see the new apps.

    > [!div class="mx-imgBorder"]
    > ![List of apps](media/rtw-apps1.png "List of apps")

> [!TIP]
> Note the URL of your Common Data Service environment instance. You'll need it to connect the template app to the data.

## Step 3: Configure and publish Power BI dashboards

The Return to the Workplace solution has three Power BI dashboards, one for executive leadership, one for facility managers, and one for Health and Safety leaders. You can publish the Power BI dashboards by using the template app from AppSource.

> [!NOTE]
> If you are a US Government customer, you'll have to publish Power BI dashboards using the deployment package available on GitHub. More information: [Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)](#appendix-deploy-the-app-and-publish-power-bi-dashboard-us-government-customers-only).

### Install template app for dashboards

1. Go to AppSource to install [Return to the Workplace – Location Readiness](https://aka.ms/rtw-leadershippbi), [Return to the Workplace - Location Management](https://aka.ms/rtw-facilitypbi) and [Return to the Workplace - Workplace Care Management](https://aka.ms/rtw-workplacepbi) dashboards. 

2. Select **GET IT NOW** to install the solution in your environment.
    > [!div class="mx-imgBorder"]
    > ![GET IT NOW](media/deploy-install-get-it-now.png "GET IT NOW")

    You're directed to an agreement pop-up window. Select **Continue** if you agree to the terms.

3. Sign in to Power BI, and then select **Install**.  
    > [!div class="mx-imgBorder"]
    > ![Install](media/deploy-install-install-app.png "Install")

4. Enter a name for the workspace, and then select **Continue**.
    > [!div class="mx-imgBorder"]
    > ![Workspace](media/deploy-create-workspace.png "Workspace")

   > [!NOTE]
   > Share the workspace with other users who require access. More information: [Give access to workspace](https://docs.microsoft.com/power-bi/collaborate-share/service-create-the-new-workspaces#give-access-to-your-workspace)

### Connect to data sources

1. Select the icon on your Apps page to open the app.

2. On the splash screen, select **Connect**.
    > [!div class="mx-imgBorder"]
    > ![Connect](media/deploy-connect-data-source.png "Connect")

3. Enter the URL of the Common Data Service environment (for example, https://[myenv].[region].dynamics.com), and then select **Next**.
    > [!div class="mx-imgBorder"]
    > ![Common Data Service environment name](media/deploy-connect-CDS.png "Common Data Service environment name")

4. Determine where the displayed URL is pointing to in the Common Data Service environment:

    - If it's pointing to Common Data Service, set the **Authentication method** to **OAuth2** and set **Privacy level setting for this data source** to **Organizational**. Select **Sign in**.
    - If it's not pointing to Common Data Service, set the **Authentication method** to **Anonymous** and set **Privacy level setting for this data source** to **Public**. Select **Sign in**
    > [!div class="mx-imgBorder"]
    > ![Privacy](media/deploy-privacy-level.png "Privacy")

After you've configured your data sources, the report will be populated with your data. Repeat these steps for both dashboards.

Next, we'll configure the data refresh settings for the dataset.

## Step 4: Schedule report refresh

1. On the **Datasets** tab of your workspace, select **Schedule refresh** for the dataset of your report.

      > [!div class="mx-imgBorder"] 
      > ![Report available in the workspace](media/deploy-schedule-refresh-dataset.png "Report available in the workspace")

2. The first time you try to schedule data refresh, the **Settings** page displays a message that your credentials aren't valid. Under **Data source credentials**, select **Edit credentials** to specify your credentials.

      > [!div class="mx-imgBorder"] 
      > ![Update your credentials](media/deploy-schedule-refresh-edit-credentials.png "Update your credentials")

3. On the next screen for the Common Data Service data source, do the following:

      - For **Authentication method**, select **Microsoft account**.

      - For **Privacy level setting for this data source**, select **Organizational**.

      - Select **Sign in**.

        > [!div class="mx-imgBorder"] 
        > ![Configure Common Data Service data source credentials](media/deploy-schedule-refresh-cds-credentials.png "Configure Common Data Service data source credentials")

      You'll be prompted to specify your credentials and sign in. After you've successfully signed in, you'll return to the **Settings** page.

      For all other data sources, do the following:
      - For **Authentication method**, select **Anonymous**.

      - For **Privacy level setting for this data source**, select **Public**.

      - Select **Sign in**.

          > [!div class="mx-imgBorder"] 
          > ![Configure other data source credentials](media/deploy-schedule-refresh-web-credentials.png "Configure other data source credentials")

4. On the **Settings** page, expand **Scheduled refresh**, and then specify the schedule you want for refreshing data. Select **Apply**.

      > [!div class="mx-imgBorder"] 
      > ![Schedule refresh data](media/deploy-schedule-refresh.png "Schedule refresh data")

      > [!NOTE]
      > - There are limits to how many times data can be refreshed. Power BI limits datasets on shared capacity to eight daily refreshes. If the dataset resides on a Power BI Premium capacity node, you can schedule up to 48 refreshes per day in the dataset settings. More information: [Refresh data](https://docs.microsoft.com/power-bi/refresh-data#data-refresh)
      > - We recommend scheduling data to be refreshed every 30 minutes.

5. Go back to your workspace, select the **Reports** tab, and then select the report to open it in a browser.

## Step 5: Embed the Power BI report in the model-driven app

The facility manager Power BI dashboard is used in the model-driven app. Because these reports are published in a different location, you need to change the location.

1. Go to [Power Apps](https://make.powerapps.com), select **Solutions** in the left pane, and create a new solution. After opening the solution, select **Add existing**, and then select **Entity**.

2. From the list of entities, select **Facility (msft_facility)** > **select components**, under the **Forms** tab, select **Main - Information Form**, and then select **Add** to finish the process. 

   > [!div class="mx-imgBorder"]
   > ![Enable Power BI](media/deploy-settings-report1.png "Enable Power BI")

3. Within the newly created solution, select **Export**. On the right side of your browser a window pops up, select **Publish**, select **Run** to check whether the solution has any issues or dependencies, and then select **Next**.  With the **Version number** and **Unmanaged** option selected, select **Export**.

4. In the **Download** dialog box, select **Save**, and in the **Download complete** dialog box, select **Open Folder**. Right-click to select the compressed .zip file that you downloaded, and then select **Extract All**. Select a location to extract the files to, and then select **Extract**. The customizations.xml file is the file that you'll edit.

5. Open the customization.xml file, look for the section similar to the XML code specified in this example: https://docs.microsoft.com/powerapps/maker/model-driven-apps/embed-powerbi-report-in-system-form#embed-without-contextual-filtering  

    In this XML file you need to update the **PowerBIGroupID**, **PowerBIReportID**, and **TileURL** according to your Power BI workspace and report. You can find this information by opening the Facility Manager report in Power BI and examine the URL: https://powerbi.com/groups/PowerBIGroupID/reports/PowerBIReportID/ReportSection 

    The `TileURL` can be found within the Power BI report. You can find it at the following destination **... (ellipsis)** > **Embed** > **Website or portal**. 

   > [!div class="mx-imgBorder"]
   > ![Power BI TileURL](media/deploy-settings-report2.png "Power BI TileURL")

   From the displayed `Secure embed code` window, capture the content of the link in the first field up to the end of the `PowerBIReportID` (as shown in the example code). 

    See the article [Embed Power BI report](https://docs.microsoft.com/powerapps/maker/model-driven-apps/embed-powerbi-report-in-system-form#remove-unmodified-attribute-before-import) and verify if the changes that you made to the XML file apply as in the example. 

6. **Save** the XML file with the modifications you made and zip the files in the folder again. Now you have a .zip file with three files in it, including the updated customizations.xml file.  

7. Sign in to [Power Apps](https://make.powerapps.com), and select **Solutions** from the left pane.
On the command bar, select **Import**.  On the **Select Solution Package** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import.

8. Select **Next**. On the page that displays information about the solution, select **Import**.

You might need to wait a few moments while the import is completed. View the results, and then select **Close**.

Open a facility record in the Facility Safety Management app and you’ll see the embedded report on the **General** tab.
 
## Step 6: Publish a theme

You can change the look and feel of the app by applying themes to match your company branding.

1. Open the **Facility Safety Management** app or the **Workplace Care Management** app, in the top right select the gear icon and select **Advanced Settings**.

   > [!div class="mx-imgBorder"]
   > ![Advanced Settings](media/deploy-advanced-settings.png "Advanced Settings")

2. Go to **Settings** > **Customizations**.

   > [!div class="mx-imgBorder"]
   > ![Customizations](media/deploy-settings-customizations.png "Customizations")

3. Select **Themes**.

   > [!div class="mx-imgBorder"]
   > ![Select themes](media/deploy-settings-solutions.png "Select themes")

4. Select **New**. Enter the **Name** and determine which colors you want to use. You can also specify the logo, which is used in the site map.

   > [!div class="mx-imgBorder"]
   > ![Deploy themes](media/deploy-themes.png "Deploy themes")

5. Select **Save**, and then **Publish**. 

   > [!div class="mx-imgBorder"]
   > ![Sample theme](media/deploy-theme-colors.png "Sample theme")

## Step 7: Share the canvas app to users

1. Sign in to [Power Apps](https://make.powerapps.com). Select the **Environment** from the upper-right corner.

2. On the left pane, select **Apps**.

3. Select the **Employee Return to the Workplace App**.
 
   > [!div class="mx-imgBorder"]
   > ![Select app](media/deploy-select-app-employee.png "Select app")

4. Select the app, and then select **Share**.

   > [!div class="mx-imgBorder"]
   > ![Share app](media/deploy-share-app.png "Share app")

5. Select users from the list of available users or groups with whom you want to share the app.

> [!IMPORTANT]
> Even if the user has access to the canvas app, you should still need to assign users with the **Return to the Workplace - Employee** security role. 

## Step 8: Set the security roles

In the Return to the Workplace solution, the following security roles are defined:

- Return to the Workplace - Employee, which is used to check in and look at the details of a location.

- Return to the Workplace - Facility Manager, which is used to look at facilities and plan phasing.

- Return to the Workplace - Leadership, which is used to view details over the entire system.

- Return to the Workplace - Health & Safety Leader, which is used to manage employee cases.

> [!IMPORTANT]
> These security roles are indicative. They provide broad access for test and demonstration purpose. Review these roles carefully before moving to a production environment or when importing sensitive data.

**To assign security roles**

1. Open the **Facility Safety Management** app or the **Workplace Care Management** app, in the top right select the gear icon and then select **Advanced Settings**.

   > [!div class="mx-imgBorder"]
   > ![Customizations Advance Settings](media/deploy-advanced-settings.png " Customizations Advanced Settings")

2. Go to **Settings** > **Security**.

   > [!div class="mx-imgBorder"]
   > ![Security](media/deploy-settings-security.png "Security")

3. Select **Users**, and then select the user to whom you want to give permissions.

   > [!div class="mx-imgBorder"]
   > ![Select user](media/deploy-settings-security-users.png "Select user")

4. Select the user, and then select **Manage Roles**. After assigning the roles, select **OK**.

   > [!div class="mx-imgBorder"]
   > ![Select roles](media/deploy-settings-security-enabled-users.png "Select roles")
   

   > [!NOTE]
   > When you want to assign security roles in bulk, you can use teams privileges. Teams privileges which are based on Azure Active Directory security groups or Office365 groups, can assign security roles based on the organization. More information: [Manage teams](https://docs.microsoft.com/power-platform/admin/manage-teams). When applying teams privileges based on Azure Active Directory security groups or Office365 groups, you need change the user and team privileges in the security roles to **Direct User/Basic access level and Team privileges**. More information: [Security roles](https://docs.microsoft.com/power-platform/admin/security-roles-privileges#team-members-privilege-inheritance)
   
## Step 9: Enable flows

1. Sign in to [Power Apps](https://make.powerapps.com). Select the **Environment** from the upper-right corner.

2. On the left pane, select **Solutions**.

3. Select the **Default Solution** from the list of solutions.

4. Select the **Employee App Email Flow** solution and then select **Edit**. Connect the flow with **Common Data Service (current environment)** and **Office 365 Outlook** connector. After that select **Save**, go back and then select **Turn On**. Validate whether the flow is turned on, so it can be used.
   
   
## Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)

> [!NOTE]
> There are notable differences between the commercially available service and the service for Dynamics 365 U.S. Government. Review these differences thoroughly before deciding in which environment to implement. More details: [Dynamics 365 US Government - Feature availability](https://docs.microsoft.com/power-platform/admin/government-feature-availability)

This section provides information for US Government customers about how to install the app and publish the Power BI dashboard using the deployment package.

> - [Step 1: Download the latest deployment package](#step-1-download-the-latest-deployment-package)
> - [Step 2: Install the app by using the deployment package](#step-2-install-the-app-by-using-the-deployment-package)
> - [Step 3: Publish by using the .pbit file in the deployment package](#step-3-publish-by-using-the-pbit-file-in-the-deployment-package)

### Step 1: Download the latest deployment package

Download the latest deployment package (.zip) from <https://aka.ms/rtw-solution>. Before extracting the .zip file, you must unblock it.

**To unblock the .zip file**

1. Right-click the .zip file, and then select **Properties**.

2. In the **Properties** dialog box, select the **Unblock** check box, select **Apply**, and then select **OK**.

    > [!div class="mx-imgBorder"] 
    > ![Solution package properties](media/deploy-deployment-package.png "Solution package properties")

After extracting the .zip file, you'll see the following in the extracted folder.

|Folder  |Description |
|---------|---------|
|Package | Contains the Package Deployer tool and the package that you'll import later to set up the solution in your environment.       |
|Power BI | Contains the Power BI Reports that will be used to configure reporting. More information: [Step 3: Configure and publish Power BI dashboards](#step-3-configure-and-publish-power-bi-dashboards)| 


### Step 2: Install the app by using the deployment package

1. Go to the location where you extracted the deployment package (.zip file). Open the **Package** folder, and then run **PackageDeployer.exe**.

2. On the next screen, select **Continue**.

3. You'll be prompted to connect to your environment. Select **Office 365** as the **Deployment Type**, select **Show Advanced**, and then type your credentials to connect to your environment.

    > [!div class="mx-imgBorder"] 
    > ![Deploy package](media/deploy-connect-to-environment.png "Deploy package")

4. Select **Login** to continue.

5. If you have access to more than one Common Data Service environment, the next screen will prompt you to select the environment where you want to install the package. Select an environment, and then select **Login**.

    > [!div class="mx-imgBorder"] 
    > ![Select an environment](media/deploy-select-environment.png "Select an environment")

6. On the next screen, select **Next.**

7. The next screen displays the environment name where the package will be installed. Review the information, and then select **Next**.

8. The next screen validates whether all dependencies are available in your environment. Select **Next**.

9. The next screen displays the installation status of the package. It might take a while for the package installation to be completed.

10. After the installation is complete, select **Next**.

11. On the next screen, select **Finish** to complete and close the setup.

12. After the app is installed, sign in to [Power Apps](https://make.powerapps.com) and select your environment from the upper-right corner. In the left pane, select **Apps** to see the new apps.

    > [!div class="mx-imgBorder"]
    > ![List of apps](media/rtw-apps1.png "List of apps")

> [!TIP]
> After installing the Return to Workplace solution, note the URL of your Common Data Service environment instance. You'll need it to connect the template app to the data.

### Step 3: Publish by using the .pbit file in the deployment package

This section provides information about how GCC customers can use the **Return to the Workplace - Location Readiness** and **Return to the Workplace - Facility Manager** dashboard .pbit files available in the deployment package to publish the dashboards.

#### Prerequisites for installing Power BI

Install Power BI Desktop from Microsoft Store: [Power BI Desktop](https://aka.ms/pbidesktop)

> [!NOTE]
> If you installed Power BI Desktop by downloading it directly from the Download Center page in the past, remove it and then download it from Microsoft Store. The Microsoft Store version will be updated automatically as new releases become available. If you can't install from Microsoft Store, install the latest non&ndash;Microsoft Store version from the [Download Center page](https://www.microsoft.com/download/details.aspx?id=58494).

**Process**

Follow the steps below for each .pbit file.

1. Open Power BI Desktop, and sign in using your account.

2. Go to the location where you extracted the deployment package (.zip file). In the **Power BI Template** folder, you'll find the appropriate .pbit file.

3. Open the .pbit file in Power BI Desktop. You'll be prompted to enter the following value: **Common Data Service Environment**. Enter the URL of the Common Data Service environment (for example, https://*[myenv]*.crm.dynamics.com, where [myenv] is the name of your environment). Select **Load**.

    > [!div class="mx-imgBorder"] 
    > ![Configure the Power BI dashboard](media/deploy-gcc-cds-env.png "Configure the Power BI dashboard")

4. You'll be prompted to enter the credentials to connect to your Common Data Service environment. Select **Organizational account** > **Sign in** to specify your Common Data Service credentials.

    > [!div class="mx-imgBorder"] 
    > ![Connect to your Common Data Service environment](media/deploy-gcc-cds-singin.png "Connect to your Common Data Service environment")

5. After signing in, select **Connect** to connect to your data in Common Data Service.

6. After connecting to your Common Data Service environment, you'll see a series of pop-up windows to configure access to data sources. These access-level and privacy-level settings should be configured to connect to the public data sources for the COVID-19 report data. Complete access level and privacy selections as shown in the following screenshots.
     
    > [!div class="mx-imgBorder"] 
    > ![Access Web Content level](media/deploy-access-web-content-level.png "Access Web Content level")

    > [!div class="mx-imgBorder"] 
    > ![Grant anonymous access to the Web Content](media/deploy-gcc-web-acesss-level-connect.png "Grant anonymous access to the Web Content")

    > [!div class="mx-imgBorder"] 
    > ![Anonymous access to the Web Content](media/deploy-gcc-web-acesss-level.png "Anonymous access to the Web Content")

    > [!div class="mx-imgBorder"] 
    > ![Privacy level](media/deploy-gcc-web-acesss-privacy-levels.png "Privacy level")

    > [!div class="mx-imgBorder"] 
    > ![Anonymous privacy select](media/deploy-gcc-web-acesss-privacy-select-anonymous.png "Anonymous privacy select")
    
    > [!div class="mx-imgBorder"] 
    > ![Privacy level blob storage](media/deploy-gcc-web-acesss-privacy-levels-blob-storage-public.png "Privacy level blob storage")

    After you've configured the access and privacy levels for COVID-19 public data, you must set the privacy level for Common Data Service data to **Organizational**. 

    > [!div class="mx-imgBorder"] 
    > ![Access Web Content level CDS](media/deploy-gcc-web-acesss-privacy-levels-CDS.png "Access Web Content level CDS")

7. After a connection is successfully made, the Power BI report will be displayed. You'll be prompted to apply pending changes to your query. Select **Apply changes**.

    > [!NOTE]
    > The report is blank because you haven't yet added data in the system.

8. Select **Publish**. When prompted to save your changes, select **Save**.

     > [!div class="mx-imgBorder"] 
     > ![Save the Power BI workspace](media/deploy-gcc-publish.png "Save the Power BI workspace")

9. You'll be prompted to save the file as a .pbix file along with your Common Data Service environment information. Enter a name, and save it on your computer. The file name you enter is displayed in your Power BI website.

10. After saving the .pbix file, you'll be prompted to publish the report. In the **Publish to Power BI** page, select the workspace where you want to publish, and then select **Select**.

    > [!div class="mx-imgBorder"] 
    > ![Publish to Power BI](media/deploy-gcc-select-destination.png "Publish to Power BI")

    The report becomes available in your workspace.

11. For the facility manager dashboard, the URL will be in the following format:
    https://app.powerbi.com/groups/3d6db5d0-22c7-4674-b957-0605c021511d/reports/bf9cd5a1-c176-4786-9c4e-684a79678575/ReportSection?redirectedFromSignup=1<br/>
    Copy the Power BI report URL to a text file, because you'll need to embed it in the model-driven app.

12. Follow steps 1 through 11 for each dashboard.

Next, you must configure the data refresh settings for the dataset. More information: [Step 4: Schedule report refresh](#step-4-schedule-report-refresh)

### Service URLs for US Government customers

There is a different set of URLs to access Power Apps US Government environments and Power BI US Government tenants. The commercial version of the service URLs is used throughout the article. If you have a US Government organization, use the respective US Government URL for your deployment:

| **Commercial version URL**| **US Government version URL**  |
|-------------------|--------------------------------|
| [https://make.powerapps.com](https://make.powerapps.com)  | [https://make.gov.powerapps.us](https://make.gov.powerapps.us) (GCC)<br/><br/>[https://make.high.powerapps.us](https://make.high.powerapps.us) (GCC High)                |
| [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) | [https://gcc.admin.powerplatform.microsoft.us](https://gcc.admin.powerplatform.microsoft.us) (GCC)<br/><br/>[https://high.admin.powerplatform.microsoft.us](https://high.admin.powerplatform.microsoft.us) (GCC High) |
| [https://app.powerbi.com/](https://app.powerbi.com/)                  | [https://app.powerbigov.us](https://app.powerbigov.us) (GCC)<br/><br/>[https://app.high.powerbigov.us](https://app.high.powerbigov.us) (GCC High)                 |

For detailed information about the US Government plans for Power Apps and Power BI, see:

- [Power Apps for US Government](https://docs.microsoft.com/power-platform/admin/powerapps-us-government)
- [Power BI for US Government](https://docs.microsoft.com/power-bi/service-govus-overview)

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.

## Next step

[Configure the Return to the Workplace solution](configure.md)

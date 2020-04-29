---
title: Deploy the Hospital Emergency Response app | Microsoft Docs
description: Provides provides detailed instructions for hospital IT admins to deploy and configure the sample app for their organization.
author: pankajarora-msft
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/29/2020
ms.author: pankar
ms.reviewer: kvivek
searchScope:
  - PowerApps
---
# Deploy the Hospital Emergency Response app

The Hospital Emergency Response app requires a small amount of setup to adapt to your needs. This article provides step-by-step instructions for hospital IT admins to deploy and configure the application for their organization.

Estimated time to complete these steps: **35–40 minutes**.

## Demo: Deploy the Hospital Emergency Response app

Watch how you can deploy and configure the Hospital Emergency Response app.

<br/>

> [!VIDEO https://www.youtube.com/embed/-1g44wNiuWI]


## Service URLs for US Government customers

The Hospital Emergency Response solution is also available for US Government customers. There is a different set of URLs to access Power Apps US Government environments and Power BI than the commercial version.

The commercial version of the service URL is used throughout this article. If you're a US Government customer, use the respective US Government URL for your deployment as mentioned here:


| **Commercial version URL**                | **US Government version URL**  |
|-------------------------------------------|--------------------------------|
| [https://make.powerapps.com](https://make.powerapps.com)                | [https://make.gov.powerapps.us (GCC)](https://make.gov.powerapps.us) <br/><br/>[https://make.high.powerapps.us (GCC High)](https://make.high.powerapps.us)                |
| [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) | [https://gcc.admin.powerplatform.microsoft.us (GCC)](https://gcc.admin.powerplatform.microsoft.us)<br/><br/>[https://high.admin.powerplatform.microsoft.us (GCC High)](https://high.admin.powerplatform.microsoft.us) |
| [https://app.powerbi.com/](https://app.powerbi.com/)                  | [https://app.powerbigov.us (GCC)](https://app.powerbigov.us)<br/><br/>[https://app.high.powerbigov.us (GCC High)](https://app.high.powerbigov.us)                  |

For detailed information about the US Government plans for Power Apps and Power BI, see:
- [Power Apps for US Government](https://docs.microsoft.com/power-platform/admin/powerapps-us-government)
- [Power BI for US Government](https://docs.microsoft.com/power-bi/service-govus-overview)


## Deploy the Hospital Emergency Response app

Perform the following steps to deploy the Hospital Emergency Response sample app for your organization.

- [Step 1: Sign up for Power Apps and create an environment](#step-1-sign-up-for-power-apps-and-create-an-environment)
- [Step 2: Install the app from Microsoft AppSource](#step-2-install-the-app-from-microsoft-appsource)
- [Step 3: Update the mobile app branding and tracking level](#step-3-update-the-mobile-app-branding-and-tracking-level)
- [Step 4: Bypass consent for mobile apps](#step-4-bypass-consent-for-mobile-apps)
- [Step 5: Add Azure Application Insights key to mobile apps for telemetry (optional)](#step-5-add-azure-application-insights-key-to-mobile-apps-for-telemetry-optional)
- [Step 6: Share canvas apps with users in your organization](#step-6-share-canvas-apps-with-users-in-your-organization)
- [Step 7: Set your mobile app as hero and featured app](#step-7-set-your-mobile-app-as-hero-and-featured-app)
- [Step 8: Share model-driven app with admins in your organization](#step-8-share-model-driven-app-with-admins-in-your-organization)

### Step 1: Sign up for Power Apps and create an environment

If you don't already have Power Apps, sign up for Power Apps and purchase an appropriate license.

More information:

-   [Power Apps Pricing](https://powerapps.microsoft.com/pricing/)
-   [Purchase Power Apps](https://docs.microsoft.com/power-platform/admin/signup-for-powerapps-admin)

After you have purchased Power Apps, create an environment with a Common Data Service database.

1.  Sign in to [Power Platform admin center](https://aka.ms/ppac).

2.  Create a Common Data Service environment with the database. More information: [Create and manage environments](https://docs.microsoft.com/power-platform/admin/create-environment)

    > [!IMPORTANT]
    > While creating the database, if you select a security group for the database, the apps can be shared *only* with users that are members of the security group.

3.  Create appropriate users in your environment. More information: [Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles)

### Step 2: Install the app from Microsoft AppSource

Follow the steps below to install Hospital Emergency Response app along with the configuration and sample data.

> [!NOTE]
> The installation process installs sample data for new installation only. If you have a prior installation of this app in your environment, the configuration and sample data won't be installed during the installation to ensure your existing data isn't overwritten.

1.  Navigate to [AppSource](https://appsource.microsoft.com/), and search for "Hospital Emergency Response".<br/>Alternatively, navigate to the app directly using this link: <https://appsource.microsoft.com/product/dynamics-365/mscrm.pphersapp>

2.  On the Hospital Emergency App page, select **Get It Now**.

    > [!div class="mx-imgBorder"] 
    > ![AppSource](media/appsource-01.png "App on AppSource")

3.  You are prompted to review the AppSource agreement terms. The dialog also shows the account that is being used to sign in. Select **Continue**. You might be prompted to verify your credentials.

4.  On the next page, select your environment where you want to install the app. Select the legal terms and privacy statements check boxes, and select **Agree**.

    > [!div class="mx-imgBorder"] 
    > ![AppSource](media/appsource-02.png "App on AppSource")

5.  You'll be taken to Dynamics 365 Admin Center where you can monitor the progress of your app installation.

    > [!div class="mx-imgBorder"] 
    > ![AppSource](media/appsource-03.png "Monitor app installation progress")

    > [!IMPORTANT]
    > It might take a while for the app to install.

6.  After the app is installed, navigate to [Power Apps](https://make.powerapps.com), and select your environment from the top-right corner. You will see new apps under **Apps**:

    > [!div class="mx-imgBorder"] 
    > ![New apps](media/conf-apps-new-apps.png "New apps")

    The installation also adds the configuration and sample data for the Hospital Emergency app.

Select the **Admin App** to open the model-driven app that lets you configure the rest of the deployment settings. More information: [What are model-driven apps?](https://docs.microsoft.com/powerapps/maker/model-driven-apps/model-driven-app-overview)

> [!div class="mx-imgBorder"] 
> ![Open Admin app](media/conf-admin-app-open.png "Open the Admin app")

The admin app has a number of entities where you can add and manage data for your hospital system. You can use the area picker in the lower part of the left navigation pane to select a different area.

### Step 3: Update the mobile app branding and tracking level

You can change the app icon, color scheme, or display name of the mobile apps to match the branding of your organization. You can also specify whether frontline workers can track information by location or facility using the mobile apps. You use **App** and **App Config** entities in the **Administration** area for these.

1.  Open the Admin App, and in the left navigation pane of the admin app, select **Administration** from the area picker, and then select **Apps**. This will show all the canvas app records you imported from the **App Import.xlsx** file.

    > [!div class="mx-imgBorder"] 
    > ![Admin apps](media/conf-admin-app-records.png "Admin apps")

1.  Open one of the app records by selecting it. 

    > [!div class="mx-imgBorder"] 
    > ![Power App ID field ](media/conf-powerapp-id-field.png "Update app info")

1.  In the app details page:
 
    1. Double-click the app icon, and select an icon file for the app from the **App Icons** folder. The image files are named intuitively so that you can easily select the correct icon. For example, select the "Emergency Response App.png" file for **Emergency Response App**. You can also select a custom image as per your organization branding.

    3. If necessary, update the **Description** or **Display Name** of the app.

    4. If necessary, update the **Hide App from Menu** value to set if the app should be displayed in the app list. As **Emergency Response App** is a container app, the value is set to **No** by default.

    5. If necessary, update the **App Display Rank** value to set the display position of app in the app list.

    6. If necessary, select a value in the **Tracking Level** field to specify if you want to track data in this mobile app at a **Location** or **Facility** level. More information: [Manage tracking level for mobile apps](configure-data-reporting.md#manage-tracking-level-for-mobile-apps)

    7. Select **Save**.

1.  Repeat steps 2 and 3 for each canvas app record under **Apps**.

1.  In the left pane, select **App Config**.

1.  Select the **Emergency Response App** record to open it for editing.

    1.  If necessary, update the colors for your app.

    2.  Select **Yes** or **No** in the **Device Sharing Enabled** field to specify whether a **Sign Out** option will be available in mobile apps or not. Selecting **Yes** will make the **Sign Out** option available. More information: [End shift - sign out](use.md#end-shift---sign-out) in the user guide.

    > [!div class="mx-imgBorder"] 
    > ![Device Sharing Enabled field](media/conf-device-sharing-enabled-field.png "Device Sharing Enabled field")

1.  Select **Save** in the lower-right corner to save your changes.

### Step 4: Bypass consent for mobile apps

You can bypass the consent prompt for each mobile app You must be a Tenant Admin to complete this step. Also, before you perform this step, you will need app ID of each mobile app (canvas app).

To get the app ID for your app, in the left navigation pane of the admin app, select **Administration** from the area picker and then select **Apps**. This displays all the mobile apps (canvas apps). Select a mobile app to view its app ID. Copy the app Id for each app to a notepad file.

> [!div class="mx-imgBorder"] 
> ![Get the app ID](media/conf-admin-get-app-id.png "Get the app ID")

Next do the following:

1.  Open Notepad, and copy this PowerShell script:

    ```powershell
    # MUST BE A TENANT ADMIN TO RUN THIS
    Install-Module -Name Microsoft.PowerApps.Administration.PowerShell
    Install-Module -Name Microsoft.PowerApps.PowerShell -AllowClobber
    Import-Module -Name Microsoft.PowerApps.Administration.PowerShell
    Import-Module -Name Microsoft.PowerApps.PowerShell
    
    # This call opens prompt to collect credentials 
    # (Azure Active Directory account and password) 
    # used by the commands
    Add-PowerAppsAccount
    
    # Change the App ID for each new app (APPGUIDHERE)
    Set-AdminPowerAppApisToBypassConsent -AppName APPGUIDHERE
    ```

2.  Replace the `APPGUIDHERE` value with the actual app ID of a canvas app.

3.  Save the file as .ps file.

4.  Run PowerShell as an administrator and execute the .ps file you just created.

5.  Repeat steps 2 - 4 for each canvas app.

### Step 5: Add Azure Application Insights key to mobile apps for telemetry (optional)

Optionally, you can use Azure Application Insights to collect detailed telemetry for your mobile apps (canvas apps) to get insights on the app usage. For detailed information about this, see [Analyze app telemetry using Application Insights](https://docs.microsoft.com/powerapps/maker/canvas-apps/application-insights)

### Step 6: Share canvas apps with users in your organization

For your frontline users to use and consume data using the canvas apps in their
mobile devices, the apps must be shared with them. It's easier to use Azure AD
groups to easily share apps with groups of users.

> [!IMPORTANT]
> Make sure the user or group you plan to share the apps with *already* have access to your environment. Typically, you would have already added users or group while [setting up your environment](#step-1-sign-up-for-power-apps-and-create-an-environment). Alternatively, you can follow the steps here to add users to your environment and provide appropriate access before sharing apps with them: [Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles).

1.  Sign in to [Power Apps](https://make.powerapps.com)

2.  In the left navigation pane, select **Apps** to view a list of all your
    apps.

3.  Select a mobile app (canvas app) and select **Share** in the banner.

    > [!div class="mx-imgBorder"] 
    > ![Share canvas apps](media/conf-share-canvas-apps.png "Share canvas apps")

4.  Specify the Azure AD group or users that you want to share this app with. As the app connects to Common Data Service data, you will also need to provide permissions to the entities. The sharing panel prompts you to manage security for the entities. Assign the **Emergency Response User** and **Common Data Service User** security roles to the entities used by this app and select **Share**.

    > [!div class="mx-imgBorder"] 
    > ![Share app with Azure AD group or users](media/conf-share-app-groups-users.png "Share app with Azure AD group or users")

5.  Repeat steps 3 and 4 for each mobile app.

Detailed information about sharing your apps: [Share a canvas app](https://docs.microsoft.com/powerapps/maker/canvas-apps/share-app)

### Step 7: Set your mobile app as hero and featured app

This step lets you set your mobile app as the hero and featured app within the **Power Apps** mobile app. You must be a Tenant Admin to complete this step.

Before you perform this step, you will need app ID of each mobile app (canvas app) that you want to set as hero and featured app. For info about getting app ID for a canvas app, see [Step 6: Bypass consent for mobile apps](#step-6-bypass-consent-for-mobile-apps)

Next, do the following:

1.  Open Notepad, and copy this PowerShell script:


    ```powershell
    # MUST BE A TENANT ADMIN TO RUN THIS
    Install-Module -Name Microsoft.PowerApps.Administration.PowerShell
    Install-Module -Name Microsoft.PowerApps.PowerShell -AllowClobber
    Import-Module -Name Microsoft.PowerApps.Administration.PowerShell
    Import-Module -Name Microsoft.PowerApps.PowerShell

    # This call opens prompt to collect credentials 
    # (Azure Active Directory account and password) 
    # used by the commands
    Add-PowerAppsAccount

    # Use the "Emergency Response App" App ID
    # To clear a featured app use Clear-AdminPowerAppAsFeatured

    #Change the App ID for each new app (APPGUIDHERE)
    Set-AdminPowerAppAsFeatured -AppName APPGUIDHERE

    # To clear a hero app use Clear-AdminPowerAppAsHero
    # Change the App ID for each new app (APPGUIDHERE)
    Set-AdminPowerAppAsHero -AppName APPGUIDHERE
    ```

2.  Replace the `APPGUIDHERE` value in the script with the actual app ID for the app you want to set as featured and hero respectively.

3.  Save the file as .ps file.

4.  Run PowerShell as an administrator and execute the .ps file you just created.
 

### Step 8: Share model-driven app with admins in your organization

For your admin users to use the admin app (model-driven app), it must be shared with them. It's easier to use Azure AD groups to easily share apps with a group of admin users.

> [!IMPORTANT]
> Make sure the user or group you plan to share the app with *already* have access to your environment. Typically, you would have already added users or group while [setting up your environment](#step-1-sign-up-for-power-apps-and-create-an-environment). Alternatively, you can follow the steps here to add users to your environment and provide appropriate access before sharing app with them: [Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles).

1. Sign in to [Power Apps](https://make.powerapps.com).

2. In the left navigation pane, select Apps to view a list of all your apps.

3. Select the model-driven app (**Admin App – Emergency Response App**) and select **Share** in the banner.

4. Specify the Azure AD group or admin users that you want to share this app with, assign the **Emergency Response Admin** security role, and select **Share**.

## Publish the Power BI dashboard

Publish the Power BI dashboard and share it with users in your organization so that they can use the dashboard for insights and decision making.

You can publish the Power BI dashboard using either of the following options: using the template app from the AppSource *or* using the **.pbit** file available in the deployment package.

### Option A: Publish using the template app from AppSource (Preferred Option)

Detailed information about using the template app from the AppSource is available here: [Connect to the Hospital Emergency Response Decision Support Dashboard](https://docs.microsoft.com/power-bi/connect-data/service-connect-to-health-emergency-response)

> [!IMPORTANT]
> This is an easier way to publish the Power BI dashboard than using the .pbit file option to publish. We recommend customers use this option instead of publishing using the .pbit file option. 

### Option B: Publish using the .pbit file in the deployment package

This section provides information on how you can use the **Emergency Response App.pbit** file available in the deployment package to publish the dashboard.

#### Prerequisites

- Download the deployment package (.zip file) from <https://aka.ms/emergency-response-solution>. After downloading, extract the .zip file to your computer. The .pbit file will be available in the P**ower BI Template** folder

- Power BI Premium Capacity or Power BI Pro licenses assigned to users accessing the report. 

- Create a workspace in Power BI where you publish the report. Sign into Power BI and create a workspace. More information: [Create the new workspaces in Power BI](https://docs.microsoft.com/power-bi/service-create-the-new-workspaces)

- Install Power BI Desktop from the Windows app store: <https://aka.ms/pbidesktop>

   > [!NOTE] 
   > If you have installed Power BI Desktop by downloading directly from the Download Center page as an executable in the past, remove it and use the one from the Microsoft Store. The Microsoft Store version will be updated automatically as new releases are available.
   >
   > If you can't install from Microsoft Store, install the latest non-Microsoft Store version from the [Download Center page](https://www.microsoft.com/download/details.aspx?id=58494).

- After installing Power BI Desktop from app store, run it, sign in using an account that has permission to publish Power BI apps in your organization.

#### Publish the dashboard using the .pbit file

1. Navigate to the location where you extracted the deployment package. You will find the **Emergency Response App.pbit** file under the **Power BI Template** folder.

2. Open the **Emergency Response App.pbit** file in Power BI Desktop. You'll will be prompted to type the following values:

    - **Organization_name**: Type your organization name that will be populated on the top-left corner of each report page.
    - **CDS_base_solution_URL**: Type the URL of your Common Data Service environment instance. For example: https://*[myenv]*.crm.dynamics.com

    > [!div class="mx-imgBorder"]
    > ![specify org name and base URL](media/pbi-pub-rep1.png)

    Select **Load**.

3. You will be prompted to enter credentials to connect to your Common Data Service environment. Select **Organizational account** > **Sign in** to specify your Common Data Service credentials.  

    > [!div class="mx-imgBorder"]
    > ![select-organizational-account](media/select-organizational-account.png)

4. After signing in, select **Connect** to connect to your data in Common Data Service.

5. On successful connection, your data will be displayed in the Power BI report. You'll be prompted to apply pending changes to your query; select **Apply changes**.

6. Select **Publish** to publish data to your Power BI workspace. You'll be prompted to save your changes; select **Save**.

    > [!div class="mx-imgBorder"]
    > ![select-refresh-publish](media/select-refresh-publish.png)

7. You'll be prompted to save the file as a .pbix file along with your Common Data Service environment information. Provide a name and save it on your computer.

8. After saving the .pbix file, you'll be prompted to publish the report. In the **Publish to Power BI** page, select the workspace where you want to publish, and then click **Select**.

12. The report becomes available in your workspace. Now, we will configure the data refresh settings for the dataset. Select the dataset in your workspace and select the **Schedule refresh** icon.  
    
    > [!div class="mx-imgBorder"]
    > ![schedule-refresh](media/schedule-refresh.png)

13. The first time you try to set the data refresh setting, you'll see the **Settings** page with a message stating that your credentials aren't valid. Under **Data source credentials**, select **Edit credentials** to specify your credentials.  

    > [!div class="mx-imgBorder"]
    > ![select-edit-credentials](media/select-edit-credentials.png)

14. In the next screen:
    - Select **Authentication method** as **OAuth2**.
    - Select **Privacy level setting for this data source** as **Organizational**.
    - Select **Sign in**.

    You'll be prompted to specify your credentials and sign in. Upon successful sign in, you'll return to the **Settings** page.

15. In the **Settings** page, expand **Scheduled refresh** and specify the required details for refreshing data based on a schedule. Select **Apply**.

    > [!div class="mx-imgBorder"]
    > ![Scheduled refresh](media/refresh-schedule.png)

    > [!NOTE] 
    > There are limits to how many times data can refresh. Power BI limits datasets on shared capacity to eight daily refreshes. If the dataset resides on a Premium capacity, you can schedule up to 48 refreshes per day in the dataset settings. More information: [Refresh data](https://docs.microsoft.com/power-bi/refresh-data#data-refresh)

16. Select your workspace name in the left pane, and then select **Create app** in the top-right corner.  

    > [!div class="mx-imgBorder"]
    > ![select-create-app](media/select-create-app.png)

17. On the app publishing page:

    1. On the **Setup** tab, specify the name and description of your app.

    2. On the **Navigation** tab, specify the location of the dashboard where you will publish it.

    3. On the **Permissions** tab, specify users or group who will be able to view this app. Make sure you select the **Install this app automatically** check box to install this app automatically for end users. More information: [Automatically install apps for end users](https://docs.microsoft.com/power-bi/service-create-distribute-apps#automatically-install-apps-for-end-users)  

        > [!div class="mx-imgBorder"]
        > ![select-install-apps-automatically](media/select-install-apps-automatically.png)

18. Select **Publish app.** For detailed information on publishing apps in Power BI, see [Publish your app](https://docs.microsoft.com/power-bi/service-create-distribute-apps#publish-your-app).

### After publishing the dashboard

To view the published Power BI dashboard, see [View Power BI dashboard](configure-data-reporting.md#view-power-bi-dashboard)

## Issues and feedback

- To report an issue with the Hospital Emergency Response sample app, visit <https://aka.ms/emergency-response-issues>.

- For feedback about the Hospital Emergency Response sample app, visit <https://aka.ms/emergency-response-feedback>.

## Next step

[Use the Hospital Emergency Response app](use.md)

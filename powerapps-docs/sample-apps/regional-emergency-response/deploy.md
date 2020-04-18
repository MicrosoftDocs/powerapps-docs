---
title: Configure Regional Hospital Emergency Response app | Microsoft Docs
description: Provides provides detailed instructions for hospital IT admins to deploy and configure the sample app for their organization.
author: KumarVivek
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/15/2020
ms.author: kvivek
ms.reviewer: kvivek
searchScope:
  - PowerApps
---
# Deploy the Regional Hospital Emergency Response solution

This guide is meant for IT admins in regional medical organizations to deploy the Regional Emergency Response Network solution. At the end of this deployment process, you will have an environment with the following:

- A web portal that enables individual hospitals to add and manage data related to their hospitals, regions, facilities, patients, supplies, and staff.

- An admin app that lets you configure and manage master data for the hospitals in your network and add/manage admin users from hospitals in your network who will be using the portals.

- A Power BI dashboard embedded in the portal for healthcare decision makers to get key insights.
Perform the following steps to deploy the Regional Emergency Response sample solution for your organization.

Estimated time to complete these steps: 35–40 minutes.

## Service URLs for US Government customers

The Regional Emergency Response solution is also available for US Government organizations. There is a different set of URLs to access Power Apps US Government environments and Power BI than the commercial version.

The commercial version of the service URL is used throughout this article. If you are a US Government organization, use the respective US Government URL for your deployment as mentioned here:


|Commercial version URL  |US Government version URL  |
|---------|---------|
|<https://make.powerapps.com>     |  <https://make.gov.powerapps.us> (GCC)       |
|<https://admin.powerplatform.microsoft.com>     |   <https://gcc.admin.powerplatform.microsoft.us> (GCC)      |
|<https://app.powerbi.com/></br>- <https://make.high.powerapps.us (GCC High)></br>-<https://high.admin.powerplatform.microsoft.us> (GCC High)</br>-<https://app.high.powerbigov.us> (GCC High)       |<https://app.powerbigov.us> (GCC)         |

For detailed information about the US Government plans for Power Apps and Power BI, see:

- [Power Apps for US Government](https://docs.microsoft.com/power-platform/admin/powerapps-us-government)
- [Power BI for US Government](https://docs.microsoft.com/power-bi/service-govus-overview)

## Step 1: Download the deployment package

Get the latest deployment package (.zip) from your Microsoft account representative.

Before extracting the .zip file, ensure that you unblock it.

1.	Right click the .zip file, select **Properties**.
2.	In the properties dialog box, select **Unblock**, and then select **Apply** followed by **OK**.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

On extracting the .zip file, you will see the following in the extracted folder:

|Folder  |Description  |
|---------|---------|
|Package     |  The folder contains the Package Deployer tool and the package that you will import later to set up the solution in your environment.       |
|Power BI Template     | Contains the Power BI Report template file (.pbit) that you will use to configure reporting.        |
|SampleData     |   Contains the sample master data files (.xlsx).      |

## Step 2: Sign up for Power Apps and create an environment

If you don't already have Power Apps, sign up for Power Apps and purchase an appropriate license.
More information:

-	Power Apps Pricing
-	Purchase Power Apps

After you have purchased Power Apps, create an environment with a Common Data Service database.

1.	Sign in to Power Platform admin center.

2.	Create a Common Data Service environment with the database. More information: Create and manage environments

    >[!IMPORTANT] 
    >While creating the database, if you select a security group for the database, the apps can be shared only with users that are members of the security group.

1.	Create appropriate users in your environment. More information: Create users and assign security roles
After you have created your environment, you can access it using the following URL: https://[myenv].crm.dynamics.com, where [myenv] is the name of your environment. Make a note of this environment URL.

## Step 3: Create a Power Apps portal in your environment

1.	Sign into Power Apps.

2.	Ensure that your newly created environment is selected in the top-right corner.

3.	In the left pane, select Apps, and then select New app > Portal.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

4.	In the Portal from blank page, specify appropriate values, and then select Create.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

Power Apps will start provisioning the portal for you, and the progress message will be displayed at the upper-right corner of the page.

NOTE: It might take a while to provision your portal.

After the portal is provisioned, it will appear in your Apps list in Power Apps. You can select the ellipsis (…) for your portal record and select Browse to view the starter portal.


> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

NOTE: Wait for the portal to be provisioned before proceeding to the next step.

## Step 4: Install the package

After your portal is provisioned, follow these steps to install the package that will configure the portal and install the admin app (model-driven app).
1.	Navigate to the location where you extracted the deployment file (.zip); you'll find a Package folder. Under the Package folder, run the PackageDeployer.exe file to run the tool to deploy the package.

2.	On the next screen, select Continue.

3.	You’ll be prompted to connect to your environment. Select Office 365 as the Deployment Type, select Show Advanced, and then type your credentials to connect to your environment.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

4.	Select Login to continue.

5.	If you have access to more than one Common Data Service environment, the next screen will prompt you to select the environment where you want to install the package. Select an environment and select Login.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

6.	On the next screen, select Next.

7.	The next screen displays you the environment name where the package will be installed. Review the information and select Next.

8.	The next screen validates if a starter portal is available on your environment. Select Next to continue with the installation.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???

9.	The next screen displays the installation status of the package. Please note that it might take a while for the package installation to complete.

10.	After the installation is complete, select Next.

11.	On the next screen, select Finish to complete and close the setup.
After the package is installed, you will find a new admin app in your Apps list.

> [!div class="mx-imgBorder"] 
> ![???](media/?.png "???


## Step 5: Configure and publish Power BI dashboard





## Step 6: Embed Power BI report in portal







## Step 7: Add a custom title and logo for your portal





## Step 8: Add a custom About page in your portal






## Step 9: Set up server-side synchronization of emails





## Step 10: Fix the Send Invitation process





## Step 11: Fix the Send Password Reset To Contact process






## Step 12: Verify Assign Web Roles to New Users process is enabled






## Step 13: Verify the Flow supply tracking flow is enabled






## Step 14: Share admin app with other admin users




## Next steps

The deployment steps are complete now. Business admins can refer to the 03-Configuration guide for business admin document to perform the following steps:

1.  Configure and manage the master data

2.	Create portal users to invite admin users from individual hospitals so that they can use portals to add and manage data and users.




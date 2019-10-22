---
title: Create a canvas app from Azure SQL Database | Microsoft Docs
description: Describes how to create canvas app from your data in Azure SQL Database
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 11/04/2019
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Create a canvas app from Azure SQL Database

[This topic is pre-release documentation and is subject to change.]

In this topic, you'll use data in your Azure SQL Database to create an app with PowerApps in minutes. You’ll have a fully functional app with your data that you can customize to fit your business needs and share  on any device.

> [!IMPORTANT]
> - This is a preview feature.
> - A preview feature may have limited availability and restricted functionality. A preview feature is available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- Your browser must have pop-ups enabled.
- You need an Azure subscription.
- You need access to an existing SQL Database.
- You need to allow PowerApps region [IP addresses](#app-ip-addresses) in SQL Database firewall settings.
- You need a valid PowerApps license or sign up for a [30 day trial license](../signup-for-powerapps.md).

## Create an app

1. Sign into [Azure Portal](https://portal.azure.com).
2. Navigate to your SQL Database.
3. Select PowerApps.

    
    ![PowerApps option in SQL Database options](./media/app-from-azure-sql-database/powerapps-link-azure-portal.png "PowerApps option inside SQL Database")

    > [!NOTE]
    > If you don't have a PowerApps license, you'll see a blue information bar with a link to start a trial. When you select to start trial, you'll be taken to a new tab where you'll be signed up for a license. Once complete, go back to the Azure portal and refresh the blade to continue.

4. Type a name for the app such as “Site Inspection”, “Fundraiser” or “Budget Tracker”.

5. Enter SQL authentication password and if required, change the username.
6. Select a table from the dropdown that you wish to use to create the app.

7. Click **Create**.


    ![Specify the information for your app](./media/app-from-azure-sql-database/powerapps-create-page-azure-portal.png "Specify the information for your app")

    The [PowerApps studio](https://create.powerapps.com/studio/) opens in a new tab. If pop-up is blocked, update browser to allow pop-ups and retry. Once created, you'll have a 3 page app with data from your SQL Database.

## Accessing your app

To access the created app again, go to [**make.powerapps.com**](https://make.powerapps.com).

## App environment and region

PowerApps app you create with this method uses the [default environment](https://docs.microsoft.com/power-platform/admin/environments-overview#the-default-environment) for the tenant and deploys to the region of this environment. You can find the region of a deployed PowerApps app or your tenant's default environment from the [admin center](https://docs.microsoft.com/power-platform/admin/regions-overview#how-do-i-find-out-where-my-app-is-deployed). To review all apps in a specific environment, go to [**make.powerapps.com**](https://make.powerapps.com), select the **Environment** from the ribbon and click **Apps** on the left.

## App IP addresses

PowerApps app IP addresses require access to connect to SQL Database. [PowerApps system requirements](limits-and-config.md#ip-addresses) lists the IP addresses that PowerApps uses depending on the region of the app.

You can use either a Transact-SQL stored procedure or the Azure portal to configure this access:

- Stored procedure [sp_set_firewall_rule](https://docs.microsoft.com/sql/relational-databases/system-stored-procedures/sp-set-firewall-rule-azure-sql-database?view=azuresqldb-current) for SQL Database or SQL Server level firewall rules.
- [Azure portal](https://docs.microsoft.com/azure/sql-database/sql-database-firewall-configure) for SQL Server level rules.

## Limitations

- The app name can only include a letter, digit, '-', '(', ')' or '_'.
- PowerApps requires SQL authentication to connect to SQL Database.
- You can select only one table while creating canvas app from the Azure portal. Customize the app after the app is created if you want to add more tables and other data sources by adding more data connections.
- The PowerApps app connects to SQL Database using firewall rules and does not use Azure Services or VNet for connectivity. For more information, read [allowing Azure services or VNet Service Endpoints](https://docs.microsoft.com/azure/sql-database/sql-database-vnet-service-endpoint-rule-overview).

## Other considerations

- The access of PowerApps app to SQL Database is implicitly shared to all users that you [share this app](share-app.md) with. Ensure the SQL authentication credentials have appropriate access for reading and writing data. </br> For example, you can create separate PowerApps apps that connect to the same SQL Database with different SQL authentication credentials to segregate read and read/write access.
- Review throttling limits, delegatable functions and operations, known issues and limitations of the [SQL Database](https://docs.microsoft.com/connectors/sql/) connector this feature uses for performance considerations.
- Create an app from [**make.powerapps.com**](https://make.powerapps.com) when you need to create an app for a non-default environment and a different region for the tenant using data from SQL Database.

## Next steps

In this quickstart, you created an app using data from your SQL Database using the Azure portal. As a next step, customize the app with controls, images and logic to better suit your business needs.

> [!div class="nextstepaction"]
> [Design the canvas app interface in PowerApps](add-configure-controls.md)

## See also

- [Share a canvas app in PowerApps](share-app.md) </br>
- [Add a data connection to a canvas app in PowerApps](add-data-connection.md#add-data-source)</br>
- [Learning path on Microsoft Learn: Customize apps in PowerApps](https://docs.microsoft.com/learn/modules/customize-apps-in-powerapps/)

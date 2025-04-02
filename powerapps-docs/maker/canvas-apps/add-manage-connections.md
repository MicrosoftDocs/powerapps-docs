---
title: Manage connections in canvas apps
description: Add, delete, and update connections from canvas apps to data sources such as SharePoint, SQL Server, and OneDrive for Business.
author: lancedMicrosoft

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 04/2/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
  - alaug
---
# Manage connections in canvas apps

In [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), create a connection to one or more data sources, delete a connection, or update its credentials.

Your canvas app's data connection can connect to SharePoint, SQL Server, Office 365, OneDrive for Business, Salesforce, Excel, and many other [data sources](connections-list.md).

Your next step after this article is to display and manage data from the data source in your app, as in these examples:

* Connect to OneDrive for Business, and manage data in an Excel workbook in your app.
* Update a list on a SharePoint site.
* Connect to SQL Server, and update a table from your app.
* Send email in Office 365.
* Send a tweet.
* Connect to Twilio, and send an SMS message from your app.

## Prerequisites

1. [Sign up](../signup-for-powerapps.md) for Power Apps.
2. Sign in to [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.

## Background on data connections

Most canvas apps use external information called **Data Sources** that is stored in cloud services. A common example is a table in an Excel file stored in OneDrive for Business. Apps are able to access these data sources by using **Connections**.

The most common type of data source is the table, which you can use to retrieve and store information. You can use connections to data sources to read and write data in Microsoft Excel workbooks, Microsoft Lists, SQL tables, and many other formats, which can be stored in cloud services like OneDrive for Business, DropBox, and SQL Server.

There are other kinds of data sources that aren't tables, such as email, calendars, twitter, and notifications.

Using the **[Gallery](controls/control-gallery.md)**, **[Display form](controls/control-form-detail.md)**, and **[Edit form](controls/control-form-detail.md)** controls, it's easy to create an app that reads and writes data from a data source. To get started, read the article [Understand data forms](working-with-forms.md).

In addition to creating and managing connections in [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), you also create connections when you do these tasks:

* Automatically generate an [app from data](app-from-sharepoint.md), such as a list created using Microsoft Lists.
* Update an existing app, or create one from scratch as [add a connection](add-data-connection.md) describes.
* Open an app that another user created and [shared with you](share-app.md).

> [!NOTE]
> If you want to use Power Apps Studio instead, open the **File** menu, and then click or tap **Connections**, [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) opens so that you can create and manage connections there.

## Create a new connection

1. If you haven't already done so, log in to [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. In the left navigation, expand **Data** and select **Connections**.
   
    ![Connections Manage.](./media/add-manage-connections/open-connections.png)
3. Select **New connection**.
   
    ![New connection.](./media/add-manage-connections/add-connection.png)
4. Select a connector in the list that appears, and then follow the prompts.
   
   ![Select a connector.](./media/add-manage-connections/choose-connection.png)
5. Select the **Create** button.
   
   ![Select Create.](./media/add-manage-connections/create-connection.png)
6. Follow the prompts. Some connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. Others such as **Microsoft Translator**, don't.
   
   For example, these connectors require additional information before you can use them.
   
   * [SharePoint](connections/connection-sharepoint-online.md)
   * [SQL Server](connections/sql-connection-overview.md)

The new connector appears under **Connections**, and you can [add it to an app](add-data-connection.md).

## Update or delete a connection

In the list of connections, find the connection that you want to update or delete, and then select the ellipsis (...) on the right of the connection.

![Update connection.](./media/add-manage-connections/auth-or-delete.png)

* To update the credentials for a connection, select the key icon, and then provide credentials for that connection.
* To delete the connection, select delete.
* Select the information icon to see the connection details.

## Consent dialog fine-grained permssions

The consent dialog presents **fine-grained** permissions to end users. Instead of asking the user to give permissions to all actions a connector can perform, the consent dialog lists the specific permissions that the app uses. The operations that an app uses are captured and stored in the app metadata when app is saved. For example, if an app is published with the specific Read action, then it will initially just request permission for the Read action. If then the author subsequently adds **Create**, **Update**, and **Delete** record actions then the consent dialog will be presented to the user again for the aggregated permissions of **Read**, **Create**, **Update**, and **Delete**. If the author subsequently removes the **Delete** records action, then the consent dialog isn't presented again. The permissions continue with the maximum set of actions that have ever been used in the app at any point. If you wish to publish an app that only shows reduced permissions, the app must be republished under a different name. 

The exception to this rule is for actions used in a Power Automate Flow that is embedded in a Power App. In this case **all** the actions are always shown for the actions used by a Power Automate flow.

## Manage the consent dialog appearance for custom connectors using Microsoft Entra ID OAuth

By default, when end-users launch canvas apps they’re presented a connection consent dialog before they’re able to access the app experience for the first time. It’s possible for admins to suppress this consent dialog for select connectors: 
* Microsoft First Party connectors (like SharePoint, Office 365 Users) and 
* Custom connectors using either Microsoft Entra ID OAuth or NoAuth (No Authentication)

### Suppress consent dialog for apps that use custom connectors using Microsoft Entra ID OAuth

To suppress consent dialog for apps created using Power Apps that connect through custom connectors using Microsoft Entra ID OAuth/NoAuth, follow the below steps.

#### Step 1. Provision Microsoft’s Azure API connections service principal in your Microsoft Entra tenant

Microsoft’s Azure API connectors service is used by all Power Apps using connectors. Provisioning this service in your tenant is a prerequisite for your custom applications, and custom connectors to pre-authorize this service to exercise single-sign-on capabilities with your custom applications and allow Power Apps to suppress the consent dialog.

A tenant admin must run the following PowerShell commands:

```Powershell
 Connect-MgGraph -Scope Application.ReadWrite.All -TenantId <target tenant id>
 New-MgServicePrincipal -AppId "fe053c5f-3692-4f14-aef2-ee34fc081cae" -DisplayName "Azure API Connections"
```

Example successful output:

![Add Azure API connections SPN to tenant](./media/add-manage-connections/custom_connector_oauth_add_SPN.png)

#### Step 2. Pre-authorize Microsoft’s Azure API connections service principal in your Microsoft Entra app
  
For each custom connector where consent is expected to be suppressed, authorize "Microsoft’s Azure API Connections" service principal to one of the scopes defined in your app.

The owner of the Microsoft Entra custom application used by a custom connector must add the app ID “fe053c5f-3692-4f14-aef2-ee34fc081cae” to one of the application scopes. Any scope can be created and used for single-sign-on to succeed.

To set the scope using Azure portal, go to [Azure portal](https://portal.azure.com) > Microsoft Entra ID > App Registrations > Select the relevant app > Expose an API > Add a client application > Add the app ID “fe053c5f-3692-4f14-aef2-ee34fc081cae” to one of the application scopes.

![Preauthorize Azure API connections to custom API 1](./media/add-manage-connections/custom_connector_oauth_preauthorize_1.png)
  
![Preauthorize Azure API connections to custom API 2](./media/add-manage-connections/custom_connector_oauth_preauthorize_2.png)
  
#### Step 3. Grant admin consent the client third-party Microsoft Entra app
  
For each custom connector using OAuth/NoAuth where consent is expected to be suppressed, an admin must use [Microsoft Entra’s grant tenant-wide admin consent to an application](/azure/active-directory/manage-apps/grant-admin-consent).

> [!NOTE]
> Admins have granular control on which custom applications, and the corresponding custom connector consent may be suppressed.  

#### Step 4. Update custom connector in Power Platform to attempt single-sign-on
  
For each custom connector using OAuth/NoAuth where consent is expected to be suppressed, a user with edit permissions on the custom connector must change the "Enable on-behalf-of login" value to "true".
  
The owner of the custom connector must choose to edit the connector, go to the **Security** section, and change the value in **Enable on-behalf-of login** from "false" to "true".

![Configure custom connector for single sign on](./media/add-manage-connections/custom_connector_oauth_enable_sso.png)
  
#### Step 5. Admin configures consent bypass for the app

In addition to the admin consent granted on a custom application in Microsoft Entra ID, which is used by a custom connector, an admin must also configure an app to bypass consent. For each app where consent is expected to be bypassed an admin must run the following command:

 ```Powershell
  Set-AdminPowerAppApisToBypassConsent -AppName <Power Apps app id>
```

### Remove consent suppression for apps that use custom connectors using Microsoft Entra ID OAuth/NoAuth

To remove consent suppression for a custom connector, an admin must perform at least one of the following actions:

1. Remove the tenant-wide admin consent grant to the application in Azure: [Microsoft Entra’s grant tenant-wide admin consent to an application](/azure/active-directory/manage-apps/grant-admin-consent).
1. Use the following Power Apps admin cmdlet to disable Power Apps’ attempt to suppress the consent dialog. [Clear-AdminPowerAppApisToBypassConsent](/powershell/module/microsoft.powerapps.administration.powershell/clear-adminpowerappapistobypassconsent)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

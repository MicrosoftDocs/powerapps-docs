---
title: Overview of connectors for canvas apps
description: Overview of all the available connections that you can use to build canvas apps.
author: lancedMicrosoft
ms.topic: overview
ms.custom: canvas
ms.collection: get-started
ms.reviewer: mkaur
ms.date: 06/19/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  - alaug
---

# Overview of connectors for canvas apps

Data is at the core of most apps, including apps you build in Power Apps. Data is stored in a *data source*, and you bring that data into your app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. Power Apps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, and Twitter. To get started adding data to a canvas app, see [Add a data connection in Power Apps](add-data-connection.md).

A connector might provide **tables** of data or **actions**. Some connectors provide only tables, some provide only actions, and some provide both. Also your connector might be either a standard or custom connector.

> [!NOTE]
  > Keep the number of connectors in a canvas app to a maximum of 10, and connection references to no more than 20. Going beyond these limits can lead to longer loading times for users when launching the app and can cause issues when saving the app.

## Tables

If your connector provides tables, add your data source, and then select the table in the data source that you want to manage. Power Apps retrieves table data into your app and updates data in your data source automatically. For example, add a data source that has a table named **Lessons**, and then set the **Items** property of a control, such as a gallery or a form, to this value in the formula bar:

 ![Plain data source Items property.](./media/connections-list/ItemPropertyPlain.png)

Specify the data that your app retrieves by customizing the **Items** property of the control that shows your data. Continuing the previous example, sort or filter the data in the **Lessons** table by using that name as an argument for the **Search** and **SortByColumn** functions. In this graphic, the formula set for the **Items** property specifies that the data is sorted and filtered based on the text in **TextSearchBox1**.

 ![Expanded data source Items property.](./media/connections-list/ItemPropertyExpanded.png)

For more information about customizing your formula with tables, see these articles:

  [Understand data sources in Power Apps](working-with-data-sources.md)<br> 
  [Generate an app from Excel data](get-started-create-from-data.md)<br> 
  [Create an app from scratch](get-started-create-from-blank.md)<br>
  [Understand tables and records in Power Apps](working-with-tables.md)

  > [!NOTE]
  > To connect to data in an Excel workbook, host it in a cloud storage service like OneDrive. For more information, see [Connect to cloud-storage from Power Apps](connections/cloud-storage-blob-connections.md).

## Actions

If your connector provides actions, select your data source as you did before. Instead of selecting a table as the next step, manually connect a control to an action by editing the **Items** property of the control that shows your data. The formula you set for the **Items** property specifies the action that retrieves data. For example, the app doesn't retrieve any data if you connect to Yammer and then set the **Items** property to the name of the data source. To populate a control with data, specify an action such as **GetMessagesInGroup(5033622).messages**.

![Action data source Items property.](./media/connections-list/ItemPropertyAction.png)

To handle custom data updates for action connectors, build a formula that includes the **Patch** function. In the formula, identify the action and the fields that bind to the action.

> [!NOTE]
> For action-based connectors, galleries and other controls don't page in more data automatically like they do for tabular connectors. For example, if you bind a tabular data source to a gallery, it retrieves the first set or page of records (for example, 100 records), and then pages in more data as the control requests it. For an action-based connector, it retrieves a "page" of data, but if the data requested exceeds the page size, the control doesn't automatically get the next page. 

For more information about how to customize your formula for custom updates, see these articles:

[Patch](functions/function-patch.md)<br />[Collect](functions/function-clear-collect-clearcollect.md)<br />[Update](functions/function-update-updateif.md)

Dynamic schema is a common type of result for action based connectors. Dynamic schema refers to the possibility that the same action might return a table with different columns depending on how it's called. Conditions that might cause the columns in the table to differ include input parameters, the user/role executing the action, and the group in which the user is working, among others. For example, SQL Server stored procedures might return different columns if run with different inputs, or an Azure DevOps instance might use custom fields that aren't available by default.

> [!NOTE]
> The [connector documentation](/connectors) shows dynamic schema results with this message **"The outputs of this operation are dynamic."** as the return value.

For more information about how to work with dynamic schema in Power Apps, see [Working with Dynamic values](untyped-and-dynamic-objects.md) for an overview and [Connect to Azure DevOps from Power Apps](connections/azure-devops.md) for a detailed example.

## Popular connectors

This table links to more information about popular connectors. For a complete list, see [All connectors](/connectors/connector-reference/).

| &nbsp; | &nbsp; |  
| --- | --- | 
|  [**Microsoft Dataverse**](connections/connection-common-data-service.md) | [**Cloud storage**](connections/cloud-storage-blob-connections.md) **
| [**Dynamics AX**](connections/connection-dynamicsax.md)|[**Excel**](connections/connection-excel.md)|
| [**Microsoft Translator**](connections/connection-microsoft-translator.md)| [**Office 365 Outlook**](connections/connection-office365-outlook.md)|
| [**Office 365 Users**](connections/connection-office365-users.md) |[**Oracle**](connections/connection-oracledb.md)|
| [**Power BI**](connections/connection-powerbi.md) |[**SharePoint**](connections/connection-sharepoint-online.md) |
| [**SQL Server**](connections/sql-connection-overview.md) |[**Twitter**](connections/connection-twitter.md) |

** Applies to Azure Blob, Box, Dropbox, Google Drive, and OneDrive.

## Standard and custom connectors

Power Apps provides *standard* connectors for many commonly used data sources. If Power Apps has a standard connector for the type of data source you want to use, use that connector. To connect to other types of data sources, like a service you built, see [Register and use custom connectors](../canvas-apps/register-custom-api.md).

## All standard connectors

Standard connectors don't require special licensing. For more information, see [Power Apps plans](https://powerapps.microsoft.com/pricing/).

Ask questions about a specific connector in the [Power Apps forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1), and suggest connectors you want to add or other improvements in [Power Apps Ideas](https://ideas.powerapps.com/).

## Security and types of authentication

As you author your app and create a connection to a data source, you might see that your choice of connector allows you to use different ways to authenticate. For instance, the SQL Server connector allows you to use Microsoft Entra Integrated, SQL Server Authentication, and Windows Authentication. Each type of authentication has different levels of security associated with it. It's important to understand what information and rights you share with users who use your application. The primary example in this article is SQL Server however, the principles apply to all types of connections.

> [!NOTE]
> - For detailed information about security considerations when using a relational database server, such as Microsoft SQL Server or Oracle, as the data source for an app, see [Use Microsoft SQL Server securely with Power Apps](connections\sql-server-security.md).  
> - Power Apps doesn't support **External member** identities. For more information, see [Properties of a Microsoft Entra B2B collaboration user](/azure/active-directory/external-identities/user-properties).  
  
### Microsoft Entra ID

This authentication is a secure type of connection. For example, SharePoint uses this type of authentication. SQL Server also allows for this type of authentication. When you connect, the Microsoft Entra service identifies you separately to SharePoint on your behalf. You don't have to supply a username or password. As an author, you can create and work with the data source with your credentials. When you publish your application and your application user logs in, they do so with their credentials. If the data is appropriately secured on a back-end, your users can only see what they're authorized to see based on their credentials. This type of security allows you to change rights for specific application users on the back-end data source after the application is published. For instance you can grant access, deny access, or refine what a user or set of users can see all on the back-end data source.

### Open-standard authorization (OAuth)

This type of connection is also secure. For example, Twitter uses this type of authentication. When you connect, **you must supply your user name and password.** As an author, you can create and work with the data source with your credentials. When you publish your application and your application user logs in, they must also supply their credentials. Therefore this type of connection is secure as your users must use their own credentials to access the data source service.

### Shared connections / Secure Implicit Connections

In a shared connection, the user name and password for the connection is supplied by the Power Apps author at the time the data source is created in the application. The connection authentication to the data source is then **Implicitly Shared** with end users. Once the application is published, the connection is also published and available to your users.  

Before January 2024, your end users could take the connection that is shared with them and create separate new applications. Your users can't see the user name or password, but the connection would be available to them. However, **after January 2024, all newly created shared connections are secured.** The old apps must be republished to be secure. The connection is no longer shared with end users. The published Power App talks to a connection proxy. The connection proxy only talks to the specific Power App for which it's linked. The connection proxy limits the actions that are sent to the connections to the ones in the Power App **{Get, Put/Patch, Delete}** for a given data source. If you have an app using the connections published before January 2024, you should republish your application and unshare any connections with end users that shouldn't have them.

In SQL Server, an example this type of connection is **SQL Server Authentication**. Many other database data sources provide a similar capability. When you publish your application, your users don't need to supply a unique user name and password. 


> [!NOTE]
> **You do not have correct permissions to use this connection** is an error message your end-users may encounter in the consent dialog. There are two situations that may cause this. First, the application may have a shared implicit connection that **isn't** a secure implicit connection. Sharing the connection with the end user resolves this issue but is **not** recommended because all shared connections should be secure implicit connections. The author should convert all connections in the application to be secure implicit connections to resolve this issue. Second, the connection may already be a secure implicit connection. Republishing may resolve this issue. If it doesn't, then a product bug should be filed.

#### Notification to update your apps (secure implicit connections)

If you have applications that might be upgraded to use this feature then you see a message on the Apps page. It indicates the number of apps that need your attention.  

   > [!div class="mx-imgBorder"]
   > ![Notification to update your apps.](./media/connections-list/attention-alert.png)

Select the link and it opens a side panel that lists all of the apps that need attention.  

   > [!div class="mx-imgBorder"]
   > ![Side panel.](./media/connections-list/app-needs-attention.png)

Select the *open* icon to the right of the app name to open and republish it. Continue with the following directions.

#### Enable secure implicit connections for an existing app

Open an existing [app open for editing](../../edit-app.md) with implicitly shared connections already published:

1. On the command bar, select **Settings** and search for **"Secure"**.
2. Update the feature switch appropriately to enable secure implicit connections.
3. Save and publish the app.

#### Unsharing

Once the app is published follow these steps to verify that sharing works correctly:

- Check if connections are shared with co-owners. If you don't want an end-user to get a connection, then uncheck the **Co-owner** checkbox.

   > [!div class="mx-imgBorder"]
   > ![Uncheck co-owner.](./media/connections-list/co-owner-property.png)

- To verify the feature works correctly, share the app with a different user who isn't an owner. Once you share the app, check the **Connections** list in the **Dataverse** tab in [Power Apps](https://make.powerapps.com) for that user. Verify that the user doesn't have a connection available.

- Open the **Sharing** panel to change the end-user's right to the connection. Choosing the **X** removes the user's access to the connection.

   > [!div class="mx-imgBorder"]
   > ![Can Use / Revoke.](./media/connections-list/can-use-revoke.png)

#### Use apps with a new secure implicit connection

When your app is republished and shared, then end-users don't have access to the connection but work with the hidden proxy connection. Users can't create a new app based on your original connection.

#### Limitations

1. All types of implicitly shared connections work such as action and tabular.
2. Server and database names are hidden in network traces but visible in the consent dialog. Column names aren't hidden.
3. For tabular connectors, we only limit CRUD actions such as Get, Post, Put, or Delete. If you have permissions to **Put**, then you have access to **Post**.
4. Action based connectors limit based on the specific API being used in the application.
5. Warnings are still enabled in sharing. The warning around implicitly shared connections still warns while in preview. However, your connection with this feature is secure – despite the warning.
6. Publishing to an entire tenant, as opposed to specific groups or individuals isn't supported.  
7. There's a known issue when importing an implicitly shared secure connection via a connection reference. The security isn't set properly in the target environment.
8. There's a known issue importing a solution using a service principal, causing import failure. A workaround is to share the connection with the service principal.

### Windows Authentication

This type of connection isn't secure because it doesn't rely on end-user authentication. Use Windows authentication when you need to connect to a data source that is **on-premises**. An example of this type of connection is to an on-premises server that has a SQL Server. The connection must go through a gateway. Since it goes through a gateway, the connector has access to all of the data on that data source. As a result, any information that you can access with the Windows credentials you supply are available to the connector. And once the application is published, the connection is also published and available to your users. This behavior means that your end users can also create applications using this same connection and access the data on that machine. Connections to the data source are also **Implicitly Shared** with users that the app is shared with. This type of connection might be valid when your data source only lives on an on-premises server and the data on that source is freely shareable.

## Data sources in solutions

Solutions help with [application lifecycle management](/power-platform/alm/overview-alm) and offer other ways to manage the lifecycle of **data sources**. If a canvas app is in a solution, [connection references](../data-platform/create-connection-reference.md) and [environment variables](../data-platform/environmentvariables.md) can be created to store information about the data sources. This setup makes it easy to change or reconnect data sources when you move solutions to different environments. 

## Rename data sources in apps

Learn how to rename data sources in an app, and understand the difference between tabular and action-based data sources. For more information, see [Rename Power Apps action-based data sources](rename-data-source.md).

## Connection consent dialog

When users open an app that uses connectors for the first time, they see a "connection consent" dialog for the following purposes.

1. To inform users about the data sources accessed by the app.

1. To outline the actions, a connector might or might not perform in an app. For example, for apps using the **Office 365 Users** connector:

    - This app is able to:
        - Read your full user profile
        - Read the full profile of all users
    - The app can't:
        - Modify or delete any user-profile information

1. To capture end-user consent to connect to the data sources that the app uses.

1. To facilitate manual end-user authentication, when needed.

For some connections, Power Platform can automatically authenticate a user to access a data source. However, if the automatic sign-in fails, this dialog prompts users to fix a connection by manually signing in. Power Platform can only attempt automatic sign-in for a connection when a data source preauthorizes Microsoft’s Azure API connections service principal, granting it permission to perform single sign-on for a user when a connection is created. For more information on single sign-on, see [What is single sign-on (SSO)?](/azure/active-directory/manage-apps/what-is-single-sign-on)

For model-driven apps that use custom pages, when there are multiple custom pages in an app, the consent dialog asks for data permissions for all of the connectors in all the custom pages even if they aren't opened.

The following image is an example of the connection consent dialog for an app connecting to a SharePoint site.  

![Power Apps consent dialog](./media/connections-list/power_apps_consent_dialog.png)

For select connectors, admins can suppress this dialog, and consent on behalf of end users to connect to a data source. The following table explains which types of connectors the consent dialog might be suppressed for an app.

> [!NOTE]
> If an admin suppresses the consent dialog but the platform can’t perform single-sign-on for an end-user, the dialog is presented to the user when they launch the app.

| Connector type                                                                                                                                           | Consent dialog suppressible? | Reference               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------------------|
| Microsoft connectors that support single sign-on (such as SharePoint, Office 365 users)                                                         | Yes                          | [Power Apps admin cmdlet](/powershell/module/microsoft.powerapps.administration.powershell/set-adminpowerappapistobypassconsent) |
| Connector accessing a non-Microsoft, partner service, such as Salesforce                                                                                  | No                           | Not applicable                    |
| Custom connectors using OAuth with Microsoft Entra ID as the identity provider. These custom connectors are built by organizations, and are only accessible by the users within the organization (for example, built by Contoso for only Contoso users) | Yes                           | [Manage Connections](add-manage-connections.md#manage-the-consent-dialog-appearance-for-custom-connectors-using-microsoft-entra-id-oauth)                    |

Microsoft Power Platform is only able to suppress the consent dialog for connections to data sources where:

1. There isn’t an obligation by the data source to show an explicit consent UI.
1. The data source preauthorizes Microsoft’s Azure API connections service principal to enable single-sign-on.
1. An admin configures an app to suppress the consent for the preceding connections.

The preauthorization of Microsoft’s Azure API connections service principal exists for Microsoft's first-party data sources, and might be configured by custom applications registered in a Microsoft Entra tenant that are used by custom connectors. An admin manages consent suppression on a per-app basis (as opposed to connector basis), so suppression is managed at the most granular app experience level&mdash;this level of granularity prevents consent suppression for an organization’s "approved apps" from inadvertently suppressing consent for apps that aren't approved or reviewed.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

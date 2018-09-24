---
title: Manage an on-premises data gateway for canvas apps | Microsoft Docs
description: Manage an on-premises data gateway and its connections
author: archnair
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/30/2016
ms.author: archanan
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Manage an on-premises data gateway in PowerApps
Install an on-premises data gateway to transfer data quickly and securely between a canvas app that's built in PowerApps and a data source that isn't in the cloud, such as an on-premises SQL Server database or an on-premises SharePoint site. View all gateways for which you have administrative permissions, and manage permissions and connections for those gateways.

With a gateway, you can connect to on-premises data over these connections:

* SharePoint
* SQL Server
* Oracle
* Informix
* Filesystem
* DB2

## Prerequisites
* The user name and password that you used to [sign up](../signup-for-powerapps.md) for PowerApps.
* Administrative permissions on a gateway. (You have these permissions by default for each gateway that you install, and an administrator of another gateway can grant you these permissions for that gateway.)
* A license that supports accessing on-premises data using an on-premises gateway. For more information, see the “Connectivity” section of the [pricing page](https://powerapps.microsoft.com/pricing/).
* Gateways and on-premises connections can only be created and used in the user's [default environment](working-with-environments.md).

## Install a gateway
1. In the left navigation bar of [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Gateways**.

    ![Gateways in left navigation bar](./media/gateway-management/manage-gateway.png)

2. If you don't have administrative permissions for a gateway, click or tap [Install a gateway now](http://go.microsoft.com/fwlink/?LinkID=820931) (or **New Gateway** in the upper-right corner), and then follow the prompts in the wizard that appears.

    ![Gateways Install](./media/gateway-management/no-gateway-installed.png)

    For details about how to install a gateway, see [Understand on-premises data gateways](gateway-reference.md).

## View and manage gateway permissions
1. In the left navigation bar of [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Gateways**, and then click or tap a gateway.

2. Add a user to a gateway by clicking or tapping **Users**, specifying a user or group, and then specifying a permission level:

   * **Can use**: Users who can create connections on the gateway to use for apps and flows, but cannot share the gateway. Use this permission for users who will run apps but not share them.
   * **Can use + share**: Users who can create a connection on the gateway to use for apps and flows, and automatically share the gateway when sharing an app. Use this permission for users who need to share apps with other users or with the organization.
   * **Admin**: Administrators who have full control of the gateway, including adding users, setting permissions, creating connections to all available data sources, and deleting the gateway.

For **Can use** and **Can use + share** permission levels, select the data sources that the user can connect to over the gateway.

## View and manage gateway connections
1. In the left navigation bar of [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Gateways**, and then click or tap a gateway.

2. Click or tap **Connections**, and then click or tap a connection to view its details, edit the settings, or delete it.

3. To share a connection, click or tap **Share**, and then add or remove users.

    > [!NOTE]
   > You can share only some types of connections, such as SQL Server. For more information, see [Share app resources](share-app-resources.md).

For more information about how to manage a connection, see [Manage your connections](add-manage-connections.md).

## Troubleshooting and Advanced Configuration
For more information on troubleshooting issues with gateways, or configuring the gateway service for your network, see [Understand on-premises data gateways](gateway-reference.md).

## Next steps
* Create an app that connects to an on-premises data source, such as [SQL Server](connections/connection-azure-sqldatabase.md) or [SharePoint](connections/connection-sharepoint-online.md).
* [Share an app](share-app.md) that connects to an on-premises data source.

---
title: Manage an on-premises data gateway in Power Apps
description: Learn about how to manage an on-premises data gateway and its connections.
author: arthiriyer
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/16/2020
ms.author: arthii
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Manage an on-premises data gateway in Power Apps

Install an on-premises data gateway to transfer data quickly and securely between a canvas app that's built in Power Apps and a data source that isn't in the cloud, such as an on-premises SQL Server database or an on-premises SharePoint site. View all gateways for which you have administrative permissions, and manage permissions and connections for those gateways. 

You can connect to on-premises data over the [connectors](/connectors/connector-reference/connector-reference-powerapps-connectors) that use data gateway.

## Prerequisites

* The user name and password that you used to [sign up](../signup-for-powerapps.md) for Power Apps.
* Administrative permissions on a gateway. (You have these permissions by default for each gateway that you install, and an administrator of another gateway can grant you these permissions for that gateway.)
* A license that supports accessing on-premises data using an on-premises gateway. For more information, see the [pricing page](https://powerapps.microsoft.com/pricing/).

## Install a gateway

To install a gateway, follow the steps in [Install an on-premises data gateway](/data-integration/gateway/service-gateway-install). Install the gateway in standard mode because the _on-premises data gateway (personal mode)_ is available only for Power BI.

## View and manage gateway permissions

1. In the left navigation bar of [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Gateways**, and then click or tap a gateway.

2. Add a user to a gateway by clicking or tapping **Users**, specifying a user or group, and then specifying a permission level:

   * **Can use**: Users who can create connections on the gateway to use for apps and flows, but cannot share the gateway. Use this permission for users who will run apps but not share them.
   * **Can use + share**: Users who can create a connection on the gateway to use for apps and flows, and automatically share the gateway when sharing an app. Use this permission for users who need to share apps with other users or with the organization.
   * **Admin**: Administrators who have full control of the gateway, including adding users, setting permissions, creating connections to all available data sources, and deleting the gateway.

For **Can use** and **Can use + share** permission levels, select the data sources that the user can connect to over the gateway.

> [!NOTE]
> **Can use** and **Can use + share** does not apply to custom connectors.

## View and manage gateway connections

1. In the left navigation bar of [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Gateways**, and then click or tap a gateway.

2. Click or tap **Connections**, and then click or tap a connection to view its details, edit the settings, or delete it.

3. To share a connection, click or tap **Share**, and then add or remove users.

    > [!NOTE]
   > You can share only some types of connections, such as SQL Server. For more information, see [Share app resources](share-app-resources.md).

For more information about how to manage a connection, see [Manage your connections](add-manage-connections.md).

## Troubleshooting and Advanced Configuration

For more information about troubleshooting issues with gateways, see [Troubleshoot the on-premises data gateway](/data-integration/gateway/service-gateway-tshoot). For more information about configuration, see [Use the on-premises data gateway app](/data-integration/gateway/service-gateway-app).

## Next steps

* [Install the on-premises data gateway](/data-integration/gateway/service-gateway-install).
* Create an app that connects to an on-premises data source, such as [SQL Server](connections/connection-azure-sqldatabase.md) or [SharePoint](connections/connection-sharepoint-online.md).
* [Share an app](share-app.md) that connects to an on-premises data source.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
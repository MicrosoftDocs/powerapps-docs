---
title: Share resources used in your canvas app | Microsoft Docs
description: Understand how you share resources that your canvas app uses in PowerApps
author: archnair
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 06/28/2016
ms.author: archanan
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Share canvas-app resources in PowerApps

Before you [share a canvas app](share-app.md), consider the types of resources on which it relies, such as one or more of the following:

* entities in Common Data Service for Apps

    For information about giving users access to this data, see [Manage entity permissions](share-app.md#manage-entity-permissions).
    
* a connection to a data source
* an on-premises data gateway
* a custom connector
* an Excel workbook or other service
* a flow

Some of these resources are shared automatically when you share the app. Other resources require you or the people with whom you share the app to take extra steps so that the app works as you expect.

You can also share your connections, custom connectors and on-premises data gateway with your entire organization.

## Connections

Some types of connections, such as SQL Server, are shared automatically, but others require users to create their own connections to the data source or sources in the app.

On [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), you can determine whether a connection will be shared automatically, and you can update sharing permissions. In the left navigation bar, click or tap **Manage**, click or tap **Connections**, and then click or tap a connection. If the **Share** tab appears, the connection will be shared automatically.

  ![Share tab in connection details page](./media/share-app-resources/shared-connections.png)

## On-premises data gateways
If you create and share an app that includes data from an on-premises source, the [on-premises data gateway](gateway-management.md) itself and certain types of connections to that gateway will be shared automatically. For any connection that isn’t shared automatically, you can share it manually (as the previous section shows) or let the app prompt users to create their own connections. To show the connection or connections with which a gateway has been configured:

1. Open [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Manage** in the left navigation bar, and then click or tap **Gateways**.
2. Click or tap a gateway, and then click or tap the **Connections** tab.

> [!NOTE]
> If you share one or more connections manually, you might need to reshare them under these circumstances:

* You add an on-premises data gateway to an app that you’ve already shared.
* You change the set of people or groups with whom you’ve shared an app that has an on-premises data gateway.

## Custom connectors
When you share an app that uses a custom connector, it is automatically shared, but users must create their own connections to it.

On [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), you can view or update permissions for a custom connector. In the left navigation bar, click or tap **Manage**, click or tap **Connections**, and then click or tap **New connection** (in the upper-right corner). Click or tap **Custom**, and then click or tap a custom connector to display details about it.

## Excel workbooks
If a shared app uses data to which not all users have access (such as an Excel workbook in a cloud-storage account), [share the data](share-app-data.md).

## Flows
If you share an app that includes a flow, users who run the app will be prompted to confirm or update any connections on which the flow relies. In addition, only the person who created the flow can customize its parameters. For example, you can create a flow that sends mail to an address that you specify, but other users can’t change that address.


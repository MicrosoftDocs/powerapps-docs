---
title: Connect to Oracle Database | Microsoft Docs
description: Learn how to connect to Oracle Database and use it for building apps in PowerApps.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 04/14/2017
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Connect to an Oracle database from PowerApps
List tables, and create, read, update and delete table rows in an Oracle database after you create a connection and build an app in PowerApps. The Oracle Database connection supports full delegation of filtering, sorting, and other functions but not triggers or stored procedures.

## Prerequisites
* Oracle 9 and later
* Oracle client software 8.1.7 and later
* Installation of an on-premises data gateway
* Installation of the Oracle client SDK

### Install an on-premises data gateway
To install a gateway, follow the steps in [this tutorial](../gateway-management.md).

An on-premises data gateway acts as a bridge, providing quick and secure data transfer between on-premises data (data that isn't in the cloud) and the Power BI, Microsoft Flow, Logic Apps, and PowerApps services. You can use the same gateway with multiple services and multiple data sources. For more information, see [Understand gateways](../gateway-reference.md).

### Install Oracle client
On the same computer as the on-premises data gateway, install the [64-bit ODAC 12c Release 4 (12.1.0.2.4) for Windows x64](http://www.oracle.com/technetwork/database/windows/downloads/index-090165.html). Otherwise, an error will appear if you try to create or use the connection, as the list of known issues describes.

## Create an app from a table in an Oracle database
1. In PowerApps Studio, click or tap **New** on the **File** menu (near the left edge).
   
   ![New option](./media/connection-oracledb/new-app.png)
2. Under **Start with your data**, click or tap the arrow.
   
      A list of connections that you already have appears.
3. Click or tap **New connection**.
   
   ![New connection](./media/connection-oracledb/new-connection.png)
4. In the list of connections, click or tap **Oracle Database**.
   
   ![New database](./media/connection-oracledb/oracle-db.png)
5. Specify the name of an Oracle server, a username, and a password.
   
    Specify a server in this format if an SID is required:<br>
    *ServerName*/*SID*
   
   ![Connection parameters](./media/connection-oracledb/connection-params.png)
6. Click or tap the gateway that you want to use, or install one.
   
    If your gateway doesn't appear after you install it, click **Refresh gateway list**.
   
   ![New gateway](./media/connection-oracledb/choose-gateway.png)
7. Click or tap **Create** to create the connection.
   
   ![New](./media/connection-oracledb/create-button.png)
8. Click or tap the **default** dataset.
   
   ![New](./media/connection-oracledb/choose-dataset.png)
9. In the list of tables, click or tap the table that you want to use.
   
   ![New](./media/connection-oracledb/choose-table.png)
10. Click **Connect** to create the app.
    
    ![New](./media/connection-oracledb/connect-button.png)

PowerApps creates an app that has three screens and shows data from the table that you selected:

* **BrowseScreen1**, which lists all entries in the table.
* **DetailScreen1**, which provides more info about a single entry.
* **EditScreen1**, in which users can update an entry or create an entry.

![New](./media/connection-oracledb/afd-app.png)

## Next steps
* To save the app that you've just generated, press Ctrl-S.
* To customize **BrowseScreen1** (which appears by default), see [Customize a layout](../customize-layout-sharepoint.md).
* To customize **DetailsScreen1** or **EditScreen1**, see [Customize a form](../customize-forms-sharepoint.md).

## Known issues, tips, and troubleshooting
1. Cannot reach the Gateway.
   
    This error appears if the on-premises data gateway can't connect to the cloud. To check the status of your gateway, sign in to powerapps.microsoft.com, click or tap **Gateways**, and then click or tap the gateway that you want to use.
   
    Make sure that your gateway is running and can connect to the Internet. Avoid installing the gateway on a computer that may be turned off or asleep. Also try restarting the on-premises data gateway service (PBIEgwService).
2. System.Data.OracleClient requires Oracle client software version 8.1.7 or greater.
   
    This error appears if the Oracle client SDK isn't installed on the same computer as the on-premises data gateway. To resolve this issue, [install the official provider](https://go.microsoft.com/fwlink/p/?LinkID=272376).
3. Table '[Tablename]' does not define any key columns.
   
    This error appears if you're connecting to a table that doesn't have a primary key, which the Oracle Database connection requires.
4. As of this writing, stored procedures, tables with composite keys, and nested object types in tables aren't supported.


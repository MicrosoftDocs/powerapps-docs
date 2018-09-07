---
title: Optimize canvas-app performance | Microsoft Docs
description: Follow the best practices in this topic to boost the performance of canvas apps that you create in PowerApps. 
author: anneta,yingchin
manager: giodl
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/31/2018
ms.author: anneta,yingchin
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Optimize canvas-app performance in PowerApps
Microsoft is working hard to improve the performance of all apps that run on the PowerApps platform. 
But you can follow the best practices in this topic to boost the performance of apps that you create.

When you open an app, it goes through these phases of execution before showing any user interface: 
1. **Authenticate the user** - Prompts you, if you’ve never opened the app before, to sign in with credentials for whatever connections
the app needs. If you opened the app again, you might be prompted again, depending on your organization’s security policies. 
2. **Get metadata** - Retrieves metadata such as on which version of the PowerApps platform the app runs and from which sources it must 
retrieve data. 
3. **Initialize the app** - Performs any tasks specified in the OnStart property. 
4. **Render screens** - Renders the first screen of the app with controls that it has populated with data. If you open other screens, 
the app renders them by using the same process.  

# Limit data connections 
**Don’t connect to more than 30 data sources from the same app**. Apps prompt new users to sign in to each connector, so every 
additional connector increases the amount of time that the app needs to start. As an app runs, each connector requires CPU resources,
memory, and network bandwidth when the app requests data from that source. 

You can quickly measure your app’s performance by turning on Developer Tools in [Microsoft Edge](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/network) or [Google Chrome](https://developers.google.com/web/tools/chrome-devtools/network-performance/) while running the app. Your app is more likely to take longer than 15 seconds to return data if it frequently requests
data from more than 30 data sources, such as Common Data Service for Apps, Azure SQL, SharePoint, and Excel on OneDrive.  

# Limit number of controls 
**Don’t add more than 500 controls to the same app**. PowerApps generates an HTML DOM to render each control. The more controls you add,
the more generation time PowerApps needs. 

You can, in some cases, achieve the same result and have the app starts faster if you use a gallery instead of individual controls. In
addition, you might want to reduce the number of control types on the same screen.  Some controls (such as PDF viewer, data table and
combo-box) pull in large execution script and take longer to render. 

# Optimize OnStart function
Use the **ClearCollect** function to cache data locally if it doesn’t change during the user session. Also, use the **Concurrent** 
function to load data sources simultaneously.

As [this reference topic](https://docs.microsoft.com/powerapps/maker/canvas-apps/functions/function-concurrent) demonstrates, you can
use **Concurrent** to cut the amount of time an app needs to load data in half.

Without the Concurrent function, this formula loads each of four tables one at a time:

	ClearCollect( Product, '[SalesLT].[Product]' );
	ClearCollect( Customer, '[SalesLT].[Customer]' );
	ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' );
	ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' )

You can confirm this behavior in the Developer Tools for your browser:

	![Serial ClearCollect](./media/perfconcurrent1.png)
	
You can enclose the same formula in the Concurrent function to reduce the overall time the operation needs:

	Concurrent(	
		ClearCollect( Product, '[SalesLT].[Product]' );
		ClearCollect( Customer, '[SalesLT].[Customer]' );
		ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' );
		ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' ))
		
With this change, the tables are fetched in parallel: 

	![Parellel ClearCollect](./media/perfconcurrent2.png)	

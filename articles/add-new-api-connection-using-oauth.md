<properties
    pageTitle="Create or Add a connection to PowerApps | Microsoft PowerApps"
    description="Use an API in your PowerApp to connect to OneDrive, DropBox, Twitter, SQL, Office 365, Salesforce, SharePoint, and more"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="MandiOhlinger"
    manager="dwrede"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/23/2015"
   ms.author="mandia"/>

# Create a connection in PowerApps

[AZURE.VIDEO nb:cid:UUID:0156313a-0d00-80c4-fa80-f1e592051e49]

Connections in PowerApps allow you to easily access your data while building apps or logic flows. PowerApps includes commonly-used connections, including: Office 365, Salesforce, Excel, Dropbox, SharePoint, SQL, Twitter, and more. 

For example, you can use connections to:

- Get Excel data from your OneDrive or Dropbox account.
- Connect to Office 365 and send email. 
- Create a Twitter connection to send a tweet. 
- Update a list on a SharePoint site.


### Prerequisites
- Install [PowerApps](http://aka.ms/powerappsinstall). Create a new app or open an existing PowerApp, and sign into your work account on [PowerApps](https://web.powerapps.com) or  sign into PowerApps on Windows. 
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).
- Your IT Administrator added connections for you to use. [PowerApps APIs List](https://azure.microsoft.com/documentation/articles/powerapps-register-from-available-apis) includes the connections available for your IT Administrator. 


## Create a new connection in your app

1.	Go to the **Connections** tab. In this tab, you see **My connections** and **Available Connections**:  
![][1]  

	- **My Connections** lists all the connections you created. You can add these connections in the apps you create.  
	- **Available Connections** lists the APIs that were added by an IT Administrator within your company. These connections are available for you create, and then add to your apps.  

2.	Select **Available Connections**, and select the connection you want to create. In this tutorial, we are creating a OneDrive connection:  
![][2]  

3.	Select the “**+**” icon, and sign in with your OneDrive username and password.  If you are prompted to provide access, then authorize your consent. This allows  your PowerApp to use this OneDrive on your behalf.
4.	Once you have successfully signed up, your connection is now listed in **My Connections**:  
![][3]

Now that the connection is created, you can add it to your app.  

## Summary and next steps
In this topic, you created a new connection, and authorized PowerApps to use this connection within any apps you create. Now that you know how to add a connection, you can add more from the list of **Available Connections**. Or, do some more fun stuff with your app. 

- [Create a PowerApp from a set of data](get-started-create-from-data.md) 
- [Use line and pie charts](use-line-pie-bar-chart.md)
- [Add a collection to show your data](create-update-collection.md)
- [Use a logic flow to complete several tasks](using-logic-flows.md)


[1]: ./media/add-new-api-connection-using-oauth/connectionstab.png
[2]: ./media/add-new-api-connection-using-oauth/availableconnections.png
[3]: ./media/add-new-api-connection-using-oauth/myconnections.png
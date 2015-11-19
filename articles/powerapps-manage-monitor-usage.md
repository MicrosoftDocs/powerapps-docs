
<properties
	pageTitle="Check your app usage in PowerApps | Microsoft Azure"
	description="IT Pro: See all apps, APIs, users, app requests, and update permissions in the Azure portal"
	services="powerapps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="11/18/2015"
   ms.author="litran"/>


# Manage and secure your apps
Once you create your app service environment and add APIs and their connections,  users in your organization can start consuming these APIs and connections. You can also manage all apps created in your organization. These options include:

- See the different apps within your app service environment, including PowerApps, web apps, logic apps, mobile apps and more.
- See all the APIs used by specific apps.
- View and manage user access to the apps within the app service environment. 
- View and manage user access to the APIs and their connections. 

Remember, your app service environment is yours to add other apps, including web apps and logic apps. You can then open PowerApps Enterprise to see and manage these apps.


## Add PowerApps administrators
After PowerApps Enterprise is enabled and ready to be used, you can add administrators, monitor the requests made to your app service environment, and monitor other apps within your app service environment.

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. Go to **Settings**.
3. Select **Admin**:  

	![][1]  

4. Select **Add**.
5. Select the **Owner** role:  

	![][2]  

	> [AZURE.IMPORTANT] Make sure that you select **Owner** role if you are to assign someone as a PowerApps Admin. Other roles listed won't give them full access to manage PowerApps. 

6. Select users or groups.
7. Select **OK** to add a PowerApps Admin.

When you add Administrators to PowerApps, the users and groups you add as administrators can:

- Add other users as PowerApps administrators.
- Manage all apps as well as their user access.
- Cannot change the billing.

> [AZURE.IMPORTANT] PowerApps Administrators cannot make changes to the App Service Environment until they are given the Owner role on the App Service Environment's resource group. To do this, see the steps within this [article](powerapps-get-started-azure-portal.md).

Once given the Owner role on the App Service Environment's resource group, the PowerApps administrators can also: 

- Create and configure APIs and their connections.
- Make changes to the PowerApps settings, including the App Service Environment.
- Add other users and groups and give them roles and permissions to the APIs, connections and the App Service Environment. 


## Manage your PowerApps and other types of apps
Once you enable PowerApps and your app service environment, you can add other apps, like web apps and logic apps to the same App Service Environment. After you do this, they are listed under *All apps* along with PowerApps. You can click on each type of app to browse through the apps. 

### PowerApps

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. From the **All apps** tile, select **PowerApps**:  
![][3]  
3. Select a PowerApps to view details of the app, including:  
	- The APIs the app uses
	- Users and groups who have access to the app 
	- App's analytics (coming soon)

#### Add a PowerApps

You cannot add a PowerApps through the Azure portal. To do it today, you need to go to [PowerApps portal](https://web.powerapps.com)

#### Delete your apps created in PowerApps
As a PowerApps Admin, you can delete any app, including PowerApps and other types of apps in your app service environment. To delete your app, select the **All apps** tile, select your app, and then select **Delete**:
  
![][4]


#### Add user or group access to an app
As a PowerApps admin, you can add or remove users and groups to PowerApps.

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. In the **All apps** tile, select **PowerApps**
	
	![][3]  

3. Select a PowerApps such as **Service Desk**.
 
4. Select **App user access**:  

	![][5]

5. Select **Add**. 
6. Select a role:  
	- **Can Edit**
	- **Can View**
7. Select users or groups.
8. Select **OK**.

### Logic apps

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. From the **All apps** tile, select **Logic apps**:  

	![][8]  
3. Select a Logic apps to view details of the app. Make sure you select the right subscription for PowerApps to have the correct Logic apps displayed.

	![][7]  

	> [AZURE.IMPORTANT] At public preview, you might see the inconsistency in the count of Logic apps in browsing blade vs. the count displayed on the main PowerApps blade. That is because we are displaying all Logic apps across all hosting plans and not filtering the Logic apps under the App Service Environment deployed for PowerApps. We will be fixing it shortly.

	**To learn more about Logic apps and how to manage them, please follow [these instructions](https://azure.microsoft.com/en-us/documentation/services/app-service/logic/)**

### Web Apps

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. From the **All apps** tile, select **Web apps**:  
	![][9]  

	**To learn more about Web apps and how to manage them, please follow [these instructions](https://azure.microsoft.com/en-us/documentation/services/app-service/web/)**

### Mobile Apps

1. In the [Azure portal](https://portal.azure.com/), open **PowerApps**.
2. From the **All apps** tile, select **Mobile apps**:  
	![][10]  

	**To learn more about Mobile apps and how to manage them, please follow [these instructions](https://azure.microsoft.com/en-us/documentation/services/app-service/mobile/)**


## Review the security options
Different security methods are used, depending on what you're doing. Here's what you need to know:

- **Subscription administrator**: These administrators control billing and are responsible for signing up your company for PowerApps Enterprise. Only Subscription Administrators can request to enable PowerApps within your company's Azure subscription. 

- **Runtime user access**: There are three different types of runtime user access: 
	- **App user access**: This permission controls if the user of the app *Can edit* the app or *Can view* the app.
	- **API user access**: This permissions controls the runtime access. If users have this permission, he or she can use the API in their app. Users either have permission or don't have permission to use the API at runtime. 
	- **Connection user access**: *Can view* and *Can edit* are the runtime user permissions available for a connection. When you add an API (or connection profile) and create its connection, you grant users and groups these specific permissions:  
		![][6]  

		For example, you can give the Sales group within your company *Can edit* permission to a connection of a SQL connector API. User with *Can edit* permission will be able to use the connection in their apps as well as edit the connection configuration. User with *Can view* permission will be able to use the connection in their apps but can't modify the connection configuration such as connection string. 

- **Role-based access control** (RBAC): Many Azure offerings use role-based access control to determine who can do what. In PowerApps, RBAC is used in a couple of places:  
	- When you first enter the PowerApps portal, you can add and manage users who should be administrators of the PowerApps. 
	- When you create the App Service Environment, you add users or groups to PowerApps, and you can remove users or groups from PowerApps. For example, you can add specific Administrator groups within your company to the *Owners* role; which allows them to create APIs and connections. These APIs and connections are then added to apps created in PowerApps.
	- When you add users to apps like Web apps, Logic apps, Mobile apps or Logic apps. You can choose the role for these users.  
		
		Adding users and assigning roles is just like using [Role-based access control](https://azure.microsoft.com/documentation/articles/role-based-access-control-configure/) within Azure. Some roles include:   

		Role | Description
		--- | ---
		Contributor | Manages everything except grant access to users.
		Reader | Can view everything, but can't make any changes.
		Owner | Can manage everything and grant users access.

Using these roles, you can grant userA **Can View** permission to a Twitter daily app and userB **Can Edit** permission to ShuttleBus app. You can grant userB access on all APIs. You can really get granular with these rights or add everyone with a specific role. It really depends on your business needs. 


## Summary and next steps
In this topic, you read about the different options to manage your PowerApps and the security methods implemented within PowerApps. 

Now that your Azure portal experience is configured, let's start creating your  apps in PowerApps. These are good starters:

[Create an app from a template in PowerApps](get-started-test-drive.md)  
[Create an app from data in PowerApps](get-started-create-from-data.md)  
[Create an app from scratch in PowerApps](get-started-create-from-blank.md)


[1]: ./media/powerapps-manage-monitor-usage/addadmin.png
[2]: ./media/powerapps-manage-monitor-usage/selectrole.png
[3]: ./media/powerapps-manage-monitor-usage/PowerApps.png
[4]: ./media/powerapps-manage-monitor-usage/deleteapp.png
[5]: ./media/powerapps-manage-monitor-usage/appuseraccess.png
[6]: ./media/powerapps-manage-monitor-usage/selectpermission.png
[7]: ./media/powerapps-manage-monitor-usage/alllogicapps.png
[8]: ./media/powerapps-manage-monitor-usage/logicapps.png
[9]: ./media/powerapps-manage-monitor-usage/webapps.png
[10]: ./media/powerapps-manage-monitor-usage/mobileapps.png




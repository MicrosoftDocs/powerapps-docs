<properties
	pageTitle="What is PowerApps Enterprise and how to get started | Microsoft Azure"
	description="Get started with PowerApps Enterprise and create App Service Environment"
	services="powerapps"
	documentationCenter="" 
	authors="linhtranms"
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

# What is PowerApps Enterprise?

PowerApps Enterprise is a new Microsoft Azure service. PowerApps Enterprise extends creating mobile apps to business users within your company and allows IT Admins to tightly manage these apps. 

Using an Office-style interface with ribbons and Excel formulas, business users can create apps that:

- Show data using line, pie, and bar charts, just like you can in Excel.
- Create user interfaces that include buttons, inserting text, and formatting a date.
- Add multiple-choice controls including list boxes, drop-down lists, and radio buttons.
- Upload images, take a picture, and play audio/video files.
- Use 'backend' systems like Excel and SQL Server to display and update information.
- Add pre-built App Service connectors to your apps that connect to PaaS programs like Twitter and SharePoint.

IT Admins can manage apps created by business users in their company, including:

- Manage these apps and manage user access to these apps.
- Create APIs and connections to different data sources. 
- Manage user access for APIs and connections to these data sources. 

## How do I get started?

First of all, determine if you need to create a new Azure Active Directory (Azure AD) tenant. If you already have an AD tenant, then simply enable PowerApps Enterprise in the Azure portal, add your APIs and connections, and start managing!

If you don't have an AD tenant, then create a new AD tenant, enable PowerApps Enterprise in the Azure portal, add your APIs and connections, and start managing!

This topic lists the specifics.

## Step 1: Create a new or use an existing Azure AD tenant

To get started with PowerApps Enterprise, you need an Azure Active Directory (Azure AD) tenant. A tenant is a dedicated instance of the Azure AD service. 

When your organization or company signs up for a Microsoft Azure cloud service such as Microsoft Intune or Office 365, your organization automatically receives and owns an AD tenant. Each AD tenant is distinct and separated from other Azure AD tenants. 

Use the following steps to determine if you already have a tenant or how to create a new one.

##### Have an existing Office 365 subscription
If you have an existing Office 365 subscription (or Microsoft Dynamic CRM Online, Enterprise Mobility Suite, or other Microsoft services), you have a free subscription to Azure Active Directory. You can use Azure AD to create and manage user and group accounts. If you can’t sign into the Azure portal, chances are you need to activate the subscription. To do so, go to the [Azure classic portal](https://manage.windowsazure.com/), and complete a one time registration process. Use these [steps](https://technet.microsoft.com/library/dn832618.aspx) to gain access to your Azure AD tenant. 

##### Have an existing Azure subscription associated with a Microsoft account
If you have previously signed up for an Azure subscription with your individual Microsoft Account (hotmail or live), you already have a tenant! In the [Azure classic portal](https://manage.windowsazure.com/), **Default Tenant** is listed under **All Items** and under **Active Directory**. You are free to use this tenant as you see fit - but you may want to create an Organizational administrator account.

To do so, use the following steps. Alternatively, you may wish to create a new tenant and create an administrator in that tenant following a similar process.

1.	Sign in to the [Azure classic portal](https://manage.windowsazure.com/) with your individual account.
2.	Select **Active Directory**” in the left menu bar. 
3.	Select **Default Directory** in the list of available directories.
4.	Select the **Users** tab at the top. There is a single user listed with “Microsoft account” in the Sourced From column.
5.	Select **Add User** at the bottom. 
6.	In **Add User Form**, enter the following details:  
	Property | Description
--- | ---
Type of User | New user in your organization
User name | Choose a user name for this administrator
First Name/Last Name/Display Name | Enter your values
Role | Global Administrator
Alternate Email Address | Enter your value
Optional | Enable Multi-Factor Authentication  
	
	Select the **CREATE** button to complete and to display the temporary password.

When finished, record this temporary password for the new administrative user. To change the temporary password, sign in to [https://login.microsoftonline.com](https://login.microsoftonline.com) with this new user account and change the password. You can also send the password directly to the user, using an alternative e-mail.


##### Have an existing Azure subscription associated with an organization account
If you have previously signed up for an Azure subscription with your organizational account, then you already have a tenant. In the [Azure classic portal](https://manage.windowsazure.com/), the tenant is listed under **All Items** and also under **Active Directory**. You are free to use this tenant as you see fit. You can also create a new tenant using the **New** menu in the task bar at the bottom.

##### Have none of the above and want to start from scratch
If none of the above applies to you, then go to the [https://account.windowsazure.com/organization](https://account.windowsazure.com/organization) to sign up for Azure with a new organization. Once signed up, you have your own Azure AD tenant with your chosen domain name. In the [Azure classic portal](https://manage.windowsazure.com/), you can see tenant in **Active Directory** in the left menu.

#### Create new or use existing Azure subscription
Now that you have your AD tenant, you can create a new or use an existing Azure subscription. The Azure AD subscription includes several editions. For PowerApps Enterprise, you can use the Free edition. However, if you need to use AAD Proxy to create hybrid connectivity to on-premises data, you need the Basic or Premium edition. 

[Azure Active Directory editions](../active-directory-editions.md) lists more features. 


## Step 2: Sign up for PowerApps Enterprise in your Azure work subscription
> [AZURE.NOTE] The following steps require the subscription Administrator to sign-in to the Azure portal and submit a request. 

Now that you have your AD tenant and an Azure subscription, your work subscription administrators can sign up for PowerApps Enterprise. The Admin can also add users within your company to 'administer' PowerApps, including giving users permissions, and manage the PowerApps published to your Azure subscription. 

To sign-up your company, the **subscription administrator** submits a request for *@yourCompany.com* email accounts. Use the following steps to sign-up:

1. In the [Azure portal](https://portal.azure.com/), sign-in to your work subscription.
2. Select **Browse All** in the task bar:  
![Browse for PowerApps][1]  
3. In the list, you can scroll to find **PowerApps**. You can also select **Resources**, and type in *powerapps*:  
![Search for PowerApps in Resources][2]  
4. Select **Get an invitation**:  
![Get an invitation][3]  

An email opens that is sent to the PowerApps group. After you submit your request, the PowerApps team reviews the information you provided. There is no ETA on approval and each scenario is considered on a case-by-case basis. Until your request is reviewed, an **Access denied** message may display in PowerApps in the Azure portal.


If the request is approved, you can then: 

- Add users within your company and using [role-based access control](../role-based-access-control-configure.md), give these users PowerApps Admin roles to access the PowerApps Enterprise portal.
- Create a dedicated App Service Environment to host your PowerApps.
- Create APIs and connections to run within your dedicated app service environment.
- In addition to PowerApps, you can add additional apps to your app service environment, including web apps, mobile apps, and logic apps.

In the following example, the Contoso company signed-up for PowerApps. In this new **PowerApps** blade, you can see a summary of the different type of apps created using this app service environment. In **Manage APIs**, you can see a summary of the Microsoft-created APIs (Microsoft managed) and see the Contoso-created APIs (IT managed):  

![Sample company PowerApps blade][4]  

In **All apps**, you can select the different app types to see all those apps. For example, you can select **Logic apps** and see all those apps listed, including *Twitter daily* and *Link forms*. You can also see all the APIs used by your logic apps, including Bing, Facebook, Twitter, and more:  
![][6]  

#### Users who have no access
Users who are not subscription administrators nor assigned the PowerApps administrator role cannot view the PowerApps Enterprise blade. Instead, they see a *No Access* message:  

![No Access PowerApps blade][5]  

## Step 3: Create an App Service Environment
Create an app service environment to host your PowerApps APIs and connections, as well as mobile apps, web apps, API apps, and logic apps. 

An app service environment is an isolated and dedicated environment that securely runs all of your apps. Compute resources are per app service environment and are exclusively dedicated to running only your apps. When you sign-up for PowerApps Enterprise, a dedicated app service environment is used to host the APIs and connections used by your PowerApps. This app service environment is a "special" type of app service environment. Specifically: 

- You can use this app service environment for whatever you want. It's tied to your company, not the subscription.
- You configure APIs and connections to be used by your PowerApps. But, you can also add web apps, mobile apps, logic apps, and API apps to this same app service environment. 
- Billing is fixed and included with PowerApps.  
- Scale is automatically managed for you. You don't have to monitor the environment to determine if additional compute resources are needed.

The regular Azure app service environment has different features. See [Introduction to App Service Environment](https://azure.microsoft.com/documentation/articles/app-service-app-service-environment-intro) for those details.

#### Requirements to get started

- Azure company subscription
- The Subscription Administrator within your company [signed up your company for PowerApps](powerapps-get-started-azure-portal.md) Enterprise.
- You are signed into the Azure portal as the PowerApps Administrator ("owner" of PowerApps) or the Subscription Administrator.

### Create an app service environment
> [AZURE.NOTE] If you do not see the option to create the app service environment, then it is already created for your tenant. To view the details, select **Settings** to open the app service environment.

1. In the [Azure portal](https://portal.azure.com/), sign-in with your work account. For example, sign-in with *yourUserName*@*YourCompany*.com. When you do this, you are automatically signed in to your company subscription.
 
2. Select **Browse All** in the task bar:  
![Browse for PowerApps][1]
  
3. In the list, you can scroll to find PowerApps. You can also select **Resources**, and type in *powerapps*:  
![Search for PowerApps in Resources][2]  

4. In the **PowerApps** blade, select **Create App Service Environment to get started** or select **App Service Environment** under *Settings*:  
![][7]
  
5. Next, enter the name, select the subscription you want to use, select or create a new resource group, select a Virtual network, and then select **Add**:  
![][8]   
	Some pointers:
	- For the name, be specific. If different departments within your company will have their own app service environment, you can include that in the name. For example, you can name it *HRApps* or *ContosoITApps*. You can also name it by its purpose. For example, you can name it *FieldSalesGroupApps* or *GlobalSupportApps*. If your company will use one app service environment for all your apps, you can name it *ContosoApps*.
	- Resource groups acts as containers for items that are related. If your apps use a database server, then you can create your apps and your database server within the same resource group. All items within the resource group are deployed together, updated together, and even deleted together. See [Azure Resource Manager overview](https://azure.microsoft.com/documentation/articles/resource-group-overview) for more specific information.

6. Select **Add** to complete creating the app service environment. 

Remember, you can also add web apps and mobile apps to this app service environment. In fact, it's your environment to add anything you want. 

### Add Administrator(s) to manage the app service environment
To get access to the app service environment and create APIs and connections, users must be added as the Owner role.

When you create the app service environment, you add users or groups to PowerApps, and you can remove users or groups from PowerApps. For example, you can add specific Administrator groups within your company to the *Owners* role; which allows them to grant users access to PowerApps and more.

1. Select your app service environment.
2. Select the RBAC icon to manage permissions:  
![][9]  
3. Select **Add**.
4. Select the **Owner** role.
5. Select the users or groups you want to manage this app service environment.
6. Select **OK**.

Adding users and assigning roles is just like using [Role-based access control](https://azure.microsoft.com/documentation/articles/role-based-access-control-configure) within Azure. Some roles include:  

Role | Description
--- | ---
Contributor | Manages everything, but can't grant access to users.
Reader | Can view everything, but can't make any changes.
Owner | Can manage everything and grant users access.

Using these roles, you can make userA an Owner of the app service environment. You can make groupB a Contributor of the app service environment. You can remove userC from all roles. You can really get granular with these rights or add everyone as a Reader. It really depends on your business needs. 



## Summary and next steps
Now that you're company is signed up for PowerApps and created an app service environment, you can add APIs and connections. These APIs and their connections are used by PowerApps or other kinds of apps.

[Add APIs and connections](powerapps-create-new-connector.md)  
[Monitor your PowerApps apps](powerapps-manage-monitor-usage.md)


[1]: ./media/powerapps-get-started-azure-portal/browseall.png
[2]: ./media/powerapps-get-started-azure-portal/allresources.png
[3]: ./media/powerapps-get-started-azure-portal/signup.png
[4]: ./media/powerapps-get-started-azure-portal/powerappsblade.png
[5]: ./media/powerapps-get-started-azure-portal/noaccess.png
[6]: ./media/powerapps-get-started-azure-portal/alllogicapps.png
[7]: ./media/powerapps-get-started-azure-portal/createase.png
[8]: ./media/powerapps-get-started-azure-portal/aseproperties.png
[9]: ./media/powerapps-get-started-azure-portal/addaseowner.png


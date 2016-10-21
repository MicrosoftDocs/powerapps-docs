<properties
	pageTitle="Overview of Environments | Microsoft PowerApps"
	description="What environments are, how to use them"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/20/2016"
   ms.author="ricksal"/>


# Environments Overview
Environments are a new concept in PowerApps. Put simply, anything within an environment, lives and dies within that environment. An environment is a space to store, manage, and share your organization’s business data, apps, and flows. They also serve as containers to separate apps that may have different roles, security requirements, or target audiences. How you leverage environments depends on your organization and the apps you are trying to build, for example:
1.	You may choose to only build your apps in a single environment.
2.	You might create separate environments that group the Test and Production versions of your apps.
3.	You might create separate environments that correspond to specific teams or departments in your company, each containing the relevant data and apps for each audience.
4.	You might also create separate environments for different global branches of your company.  


## Environment scope
An environment is bound to a geographic location, like the US. When you create a flow in an environment, that flow is routed to all datacenters in that geographic location.  Any items you create in that environment, including connections, gateways, flows using Microsoft Flow, and more, are also bound to the location.

Let's say you want to create an app that inserts data somewhere. Your options are:

•	Insert data into an Excel file, and store the Excel file in a cloud storage account, such as OneDrive.

•	Create your own SQL database, and store your data in it.

•	Create a database using the [Microsoft Common Data Service](data-platform-intro.md) to store your data.

Every environment can have zero or one Common Data Service, which is basically storage for your apps. The ability to create a database for your environment depends on the license you purchase for PowerApps. For more information see [Billing, Licensing, and SKUs](pricing-billing-skus.md).

When you create an app in an environment, that app is only permitted to connect to the data sources that are also deployed in that same environment, including connections, gateways, flows, and Common Data Services databases.  For example, let’s consider a scenario where you have created two environments named ‘Test’ and ‘Dev’ and created a Common Data Service database in each of the environments. If you create an app in the ‘Test’ environment, it will only be permitted to connect to the ‘Test’ database, it wont be able to connect to the ‘Dev’ database.  

There will be a process to move resources between environments. For more information, see [Migrate resources](environment-and-tenant-migration.md).

## Environment permissions

Environments have two built-in roles that provide access to permissions within an environment:

*	Environment Admin can perform all administrative actions on an environment including the following:

	o	Add or remove a user or group from either the Environment Admin or Environment Maker role

	o	Provision a Common Data Service database for the environment

	o	Manage the runtime permissions to the environment’s database (if it exists)

	o	View and manage all resources created within an environment

	o	Set Data Loss Prevention policies. For more information see the link to the DLP article.

*	Environment Maker can create new resources within an environment including apps, connections, custom APIs, gateways, and flows using Microsoft Flow.  Users or groups assigned to this role are not automatically given access to the environment’s database (if it exists) and must be given access separately. For more information, see the link to database security.

Users or groups can be assigned to either of these two roles by an Environment Admin from the PowerApps admin center. For more information see [Environment Administration](environment-administration.md).

## The default environment
A single default environment is automatically created by PowerApps for each tenant and shared by all users in that tenant. Whenever a new user signs-up for PowerApps they are automatically added to the Maker role of the default environment. The default environment is created in region that is closest to the default region of the AAD tenant.

> [AZURE-NOTE] No users will be added to the Environment Admin role of the default environment automatically. For more informaton, see [Environment Administration](environment-administration.md).

The default environment is named as follows: “<AAD tenant name> (default)”

![](./media/environments-overview/choose-environment.png)

## PowerApps Preview users
Now that PowerApps is in general availability (GA) any user that participated in the PowerApps preview will see some changes in their experience with the introduction of environments.  The following table lists what U.S. users and non-U.S. users can expect:

| User | What happens |
|-------|--------------|
|Preview user that created a Common Data Service database*|You will see an environment called “<Your name>’s environment” that contains your preview CDM database and any other apps that you built against the database. You will be added to the Maker role of this environment.|
|Preview user in U.S. | All the apps (except any that connected to a CDM database) that were built during the PowerApps preview period will be available in the default environment.|
|Preview user not in U.S. | In addition to the default environment, you also see an environment called “<AAD tenant name> (from preview)” that contains all the apps (except any that connector to a CDM database) that were built during the PowerApps preview period. You will be added to the Maker of this environment.|

A *Preview user* is someone who was using Microsoft Flow before it's release to General Availability (GA).

*Within X weeks of general availability (GA), the environments containing preview content will be marked as read-only. Users of these environments are asked to migrate their content to the default environment or another custom environment as soon as possible.*

## Choosing an environment
With the introduction of environments, you will now see a new experience when you come to https://web.powerapps.com.  The apps, connections, and other items that are visible in the site will now be filtered based on the current environment that is selected.  Your current environment is specified in the environment picker in the top bar on the right. To choose a different environment, click or tap the picker, and a list of available environments appears. Click or tap the one you wish to enter.

NOTE: An environment will show up in the picker for you if you meet one of the following conditions:
1.	You are a member of the ‘Admin’ role for the environment
NOTE: the user who creates an environment is automatically added to the ‘Admin’ role.
2.	You are a member of the ‘Maker’ role for the environment
NOTE: all users are automatically added to the ‘Maker’ role of the default environment.
3.	You are not an ‘Admin’ or ‘Maker’ of the environment, but you have been given ‘Contributor’ access to at least one app within the environment. For more information, see [share an app](share-app.md).
NOTE: in this case, you will not be able to create new apps in this environment. You will only be able to modify the existing apps that have been shared with you.

![](./media/environments-overview/choose-environment.png)


## Creating an environment

### Who can create environments

Your license determines whether you can create environments.

|License|Environment creation is allowed|
|-------|-------------------------------|
|PowerApps P2|√|
|PowerApps P2 Trial|√|
|Dynamics 365 Plans|x|
|Office 365 Plans|x|
|Dynamics 365 Apps and Teams Plans|x|

There is a limit of 5 environments that can be created per user.

At present you cannot delete an environment.

### What tools can create environments?

You can create environments from the PowerApps admin center. For more information, see [Environment Administration](environment-administration.md).

You cannot create environments from PowerApps Studio or PowerApps Mobile.

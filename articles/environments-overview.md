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
   ms.date="10/19/2016"
   ms.author="ricksal"/>

# Environments Overview
Environments are a new concept in PowerApps. Put simply, anything within an environment, lives and dies within that environment. They serve as containers to separate apps that may have different roles (Test, Production), security requirements, target audiences, or whatever category you wishto specify.

## Environment scope
An environment is bound to a geographic location, like the U.S. When you create a flow in an environment, that flow is routed to all datacenters in that geographic location (like the U.S.). If you delete the environment, then all flows within that environment are also deleted. This applies to any items you create in that environment, including connections, gateways, PowerApps, and more.

Let's say you want to create a flow that inserts data somewhere. Your options are:

•	Insert data into an Excel file, and store the Excel file in a cloud storage account, such as OneDrive.

•	Create your own SQL Database, and store your data in it.

•	Use Common Data Model to store your data.

Every environment can have zero or one Common Data Model, which is basically storage for your flows. Access to a Common Data Model depends on the license you purchase; it is not included with the Free license.

## Choosing an environment

Your current environment is specified in the environment picker in the top bar on the right. To choose a different environment, press or click the picker, and a list of available environments appears. Click or press the one you wish to enter.

![](./media/environments-overview/choose-environment.png)

## The default environment

The Default environment is available for every user, and is shared by all users. This environment has a U.S. tenant, and a non-U.S. tenant.

Now that Flow is in general availability (GA), the following table lists what U.S. users and non-U.S. users can expect:

| User | What happens |
|-------|--------------|
|Preview user in U.S. | Automatically uses the default environment|
|Preview user not in U.S. | Choose to use an environment; or use the legacy experience, which is no environment. With the legacy experience, existing flows can be updated, but new flows cannot be created.|
|New user in the U.S. | Automatically uses the default environment|
|New user not in the U.S. | Automatically uses the default environment|

A *Preview user* is someone who was using Microsoft Flow before it's release to General Availability (GA).



## Creating an environment

### Who can create environments

Your license determines whether you can create environments.

These licenses allow environment creation:

* PowerApps P2
* PowerApps P2 Trial
* Dynamics 365 Plans

These licenses do not allow environment creation:

* Seeded Office 365 Plans
* Dynamics 365 Apps and Teams Plans

There is a limit of 5 environments that can be created per user.

At present you cannot delete an environment.

### What tools can create environments?

You can create environments from the following tools:

* Power Apps Admin portal
* In-line from the PowerApps portal

You cannot create environments from the Studio, WebAuth, or Client experiences.

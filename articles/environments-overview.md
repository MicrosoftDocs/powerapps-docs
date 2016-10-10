<properties
	pageTitle="Overview of Environments | Microsoft PowerApps"
	description="What environments are, how to use them"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="hero-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/10/2016"
   ms.author="ricksal"/>

# Environments Overview
Environments are a new concept in PowerApps. Put simply, anything within an environment, lives and dies within that environment.

## Environment scope
An environment is bound to a geographic location, like the U.S. When you create a flow in an environment, that flow is routed to all datacenters in that geographic location (like the U.S.). If you delete the environment, then all flows within that environment are also deleted. This applies to any items you create in that environment, including connections, gateways, PowerApps, and more.

Let's say you want to create a flow that inserts data somewhere. Your options are:

•	Insert data into an Excel file, and store the Excel file in a cloud storage account, such as OneDrive.

•	Create your own SQL Database, and store your data in it.

•	Use Common Data Model to store your data.

Every environment can have zero or one Common Data Model, which is basically storage for your flows. Access to a Common Data Model depends on the license you purchase; it is not included with the Free license.

## The default environment
The Default environment is available for every user, and is shared by all users. This environment has a U.S. tenant, and a non-U.S. tenant. Now that Flow is in general availability (GA), the following table lists what U.S. users and non-U.S. users can expect:

User | What happens |

Preview user in U.S. | Automatically uses the default environment
Preview user not in U.S. | Choose to use an environment; or use the legacy experience, which is no environment. With the legacy experience, existing flows can be updated, but new flows cannot be created.
New user in the U.S. | Automatically uses the default environment
New user not in the U.S. | Automatically uses the default environment

A *Preview user* is someone who was using Microsoft Flow before it's release to General Availability (GA).

## Create an environments
1.	In the Flow admin center, select Environments. Any existing environments are displayed.
2.	Select Add environment. Enter the following info:

	Property | Description
	Name | Enter the name of your environment, such as Dev/Test, or Sandbox.
	Location | Choose the location to host your environment. We recommend using a location closest to your users. For example, if your Flow app users are in London, then choose a Europe location. If your Flow app users are in New York, then choose a U.S. location.

	Create database automatically | Check this setting to create the Common Data Model. The Common Data Model is available with some licenses. So if you don't see this property, then it's not included with your license.

3.	Select Create. Your new environment is listed.

## Manage your environments
1.	In the Flow admin center, select Environments.
2.	Select an environment to open its properties. The General properties show more details, including who "owns" each environment, its geographic location, and when it was created. You can also upgrade your plan in these properties.
3.	In the Access properties, Admin and Maker are listed. Use these properties to give users Admin privileges, or Maker privileges to the environment.

	Task | Maker | Admin

	Create Flows | ✔ | ✔

	Delete Flows | ✔ | ✔

	And so on...


4. In Resources, all the items within the environment are listed, including Flows, Connections, Custom APIs, Gateways, and PowerApps.

## Frequently asked questions
Can I migrate a Flow in my U.S. environment, to a Europe environment?

No, flows cannot be moved between environments. Currently, recreate the flow in the new environment.

Which license includes Common Data Model?

Office 365 Business Premium (Plan P2)

Can the Common Data Model be used outside of an environment?

No. Common Data Model requires an environment.

What regions include Microsoft Flow?

Microsoft Flow supports all the same regions that Office 365 supports. Microsoft does not publicly advertise all datacenters, but the Office 365 datacenter map provides more information.

How do I create my own custom environment?

Office 365 Business (Plan P1) and Office 365 Business Premium (Plan P2) license users can create their own environments, in addition to the default environment. Other Office 365 licenses, such as Free, cannot create their own environments

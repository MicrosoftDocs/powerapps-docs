---
title: Introduction to solutions | Microsoft Docs
description: Learn how solutions are used to create model apps.
services: ''
suite: powerapps
documentationcenter: na
author: "shmcarth" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Introduction to solutions

*Solutions* are how customizers and developers author, package, and maintain units of software that extend Common Data Service(CDS) for Apps. For example, Dynamics 365 for Sales, Marketing, Customer Service apps are composed of solutions. Customizers and developers distribute solutions so that organizations can use Common Data Service for Apps to install and uninstall the business functionality defined by the solution.

Every customization that you make to CDS for Apps, or to a previously installed solution, is part of a solution. Every change you apply is tracked and any dependencies can be calculated. When you export a managed solution, it contains all the changes that have been applied for that solution into a file that you can then import into a different CDS for Apps environment.

If you intend to transport customizations or extensions between different CDS for Apps environments or distribute solutions using AppSource, you must understand the solution framework.

## Managed and unmanaged solutions

There are two types of solutions: *managed* and *unmanaged*.

A **managed** solution is a completed solution that is intended to be distributed and installed. 
- You cannot edit the components of a managed solution.
- You cannot export a managed solution.
- You can add unmanaged customizations to components of a managed solution. When you do this, you create a dependency between your unmanaged customizations and the managed solution. When a dependency exists, the managed solution cannot be uninstalled until you remove the dependency.
- When a managed solution is deleted (uninstalled), all the customizations and extensions included with it are removed.

  > [!IMPORTANT]
  > When you uninstall a managed solution, the following data is lost: data stored in custom entities that are part of the managed solution and data stored in custom attributes that are part of the managed solution on other entities that are not part of the managed solution.

An **unmanaged** solution is one that is still under development or isn’t intended to be distributed. 
- While a solution is unmanaged, you can continue to add and remove components to it. 
- You can export an unmanaged solution to transport unmanaged customizations from one environment to another.
- When an unmanaged solution is deleted, only the solution container of any customizations included in it is deleted. All the unmanaged customizations remain in effect and belong to the default solution. 
- When the unmanaged solution is complete and you want to distribute it, export it as a managed solution.

  > [!NOTE]
  > You cannot import a managed solution into the same environment that contains the originating unmanaged solution. To test a managed solution, you need a separate environment to import it into.

## Solution publishers

Each solution is linked to a solution publisher. The solution publisher provides information about how to contact the publisher as well a customization prefix value. The default value is `new`.

When any schema changes are included as part of a solution, the solution publisher customization prefix is prepended to the name of the schema items. Any custom actions also have this value appended to them. This is valuable because it allows for easy recognition of which solution added the schema item or custom action. It is not required for all schema items and custom actions in a solution to use the same customization prefix, but it is strongly recommended.

> [!IMPORTANT]
> Before you start creating a solution, you should create a solution publisher record and create a new solution linked to it. You should make sure the customization prefix represents a value that makes sense for you. 

Your choice of solution publisher is important in case you want to publish an update to a solution you have shipped. An update can only be applied to a managed solution with the same publisher as the original managed solution. 

More information: [Maintain managed solutions > Create managed solution updates](/dynamics365/customer-engagement/developer/maintain-managed-solutions#create-managed-solution-updates)

## Create a solution publisher and solution 

To create a  solution publisher and a solution you need to navigate to the CDS for Apps Customization area.

From [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)

1. Select the *Waffle* icon at the top left corner
2. In the fly out, select **All apps**.
3. Look for the **CDS for Apps - custom app**.
 You may want to click the ellipses (...) and choose **Pin this app** so it will be easier to navigate to next time.
4. Click the **CDS for Apps - custom app** app and select it.
5. Navigate to **Settings** > **Customization** > **Customizations**.

From [home.dynamics.com](http://home.dynamics.com/)

1. Look for the **CDS for Apps - custom** tile and click it.
2. Navigate to **Settings** > **Customization** > **Customizations**.

### Create a solution publisher

1. From the customizations area, select **Publishers**.
2. Click **New**.
3. In the publisher form enter a **Display Name**. A **Name** value will be generated based on the display name. You can accept the generated value or specify a new one.
4. In the **prefix** field, specify the customization prefix that should be appended to any custom schema items you add when developing your solution. The default value is `new`. Choose a value that represents your organization and will help people identify which components installed in their system came from your solution.
5. An **Option Value Prefix** value will be generated based on your choice for customization prefix. This is a value that will be appended to any values for option set options you add to attributes in your solution. This value will help identify any options you add to your solution.
6. In the **Contact Details** section of the form, you may add any contact information you want to provide for people who install your solution.
7. Click **Save and Close** when you are done.

### Create a solution

1. From the customizations area, select **Solutions**.
2. Click **New**.
3. In the solution form enter a **Display Name**. A **Name** value will be generated based on the display name. You can accept the generated value or specify a new one.
4. In the **Publisher** field look up the publisher you created in [Create a solution publisher](#create-a-solution-publisher)
5. In the **Version** field select an appropriate version for your solution, such as 1.0.0.0.
6. Click **Save** when you are done.

> [!IMPORTANT]
> Whenever you create a new solution component that will be included in this solution, use this solution, or another solution associated with the same solution publisher to add it.
> Solution components created in the context of a solution associated to a different solution publisher can be added to this solution, but they may have inconsistent customization prefix values set.

## Solution layering

It is possible for two managed solutions to be installed which contradict each other or for some customizations applied to the environment to override a managed solution. How does this work?

It works because Common Data Service for Apps evaluates managed solutions by the order in which they are installed and any customizations that are not in a managed solution are evaluated last.

The following diagram introduces how managed solutions and unmanaged customizations interact to control what is included at runtime in the application.

![Diagram showing solution layering](media/solution-layering.png)

In this example, default behavior defined in the system solution is overridden or appended by managed solutions. Any unmanaged customizations can then override or append customizations that are then visible in the application.

More information: [Introduction to solutions > Unmanaged and managed solutions](/dynamics365/customer-engagement/developer/introduction-solutions#managed-and-unmanaged-solutions)

## Managed properties

When you distribute a managed solution, anyone who installs your solution can include their own unmanaged customizations to it. Those unmanaged customizations can then be added to a solution that they distributed as a managed solution that depends on your solution. But what if you don’t want people to do this? As the publisher of the managed solution you can use managed properties to disable specific customizations for the components of your managed solution.

More information: [Use managed properties](use-managed-properties.md)

## Modular solutions

You can use the solution framework to create a discrete set of components that provide a set of functionalities. Each managed solution can be installed and uninstalled to return the customer’s deployment to its original state. Each managed solution you create runs on top of the system solution and can access the capabilities of that underlying solution.

You can also build managed solutions that run on top of other solutions to create a set of functionalities that can be shared by different solutions. In this way, you can build and maintain a common module as a solution to support multiple solutions. Because of this, customers only need to install the solutions that are right for them and you don’t need to include the same shared functionality in every solution. If you need to push out an update to solution that supports multiple solutions, you only need to update the common module.

Customers, System Implementers, and other ISVs can then build solutions on top of your solutions to achieve the specific customizations they require.

When a set of business functionality is composed with multiple solutions, these are called packages. You can use the *Package Deployer* to combine multiple solutions into a single installable unit.

## Deploy solution packages

Use the *Package Deployer* to create a custom installer for a package that can include 
- One or more solution files.
- Flat files or exported configuration data files. 
- Custom code that can run before, while, or after the package is deployed.
- HTML content specific to the package that can display at the beginning and end of the deployment process. This can be useful to provide a description of the solutions and files that are deployed in the package.

More information: [Create packages for the CDS for Apps Package Deployer](package-deployer/create-packages-package-deployer.md).

## Team development of solutions

A solution file is a single binary file that does not lend itself to source code control or team development. There is no way for multiple developers to work on the custom components in the solution.

The *SolutionPackager* tool resolves the problem of source code control and team development of solution files. The tool identifies individual components in the compressed solution file and extracts them out to individual files. The tool can also re-create a solution file by packing the files that had been previously extracted. This enables multiple people to work independently on a single solution and extract their changes into a common location. Because each component in the solution file is broken into multiple files, it becomes possible to merge customizations without overwriting prior changes. A secondary use of the SolutionPackager tool is that it can be invoked from an automated build process to generate a compressed solution file from previously extracted component files without needing an active CDS for Apps instance.

More information: [Solution tools for team development](/dynamics365/customer-engagement/developer/solution-tools-team-development)

### See also

[Common Data Service for Apps Developer Overview](overview.md)

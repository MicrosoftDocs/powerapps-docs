---
title: Introduction to solutions | Microsoft Docs
description: Learn how solutions are used to create model apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/20/2018
ms.author: jdaly
---
# Introduction to solutions

> [!NOTE]
> This topic provides a high-level overview of important concepts related to solutions for model app developers. For complete and detailed information about solutions see the Dynamics 365 Developer Guide topic [Package and distribute extensions using solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)


*Solutions* are how customizers and developers author, package, and maintain units of software that extend the Common Data Service (CDS). Customizers and developers distribute solutions so that organizations can use the CDS to install and uninstall the business functionality defined by the solution.

Every customization that you make to the CDS is part of a solution. Every change you apply is tracked and any dependencies can be calculated. When you export a solution, it contains all the changes that have been applied for that solution into a file that you can then import into a different CDS environment.

If you intend to transport customizations or extensions between different CDS environments or distribute solutions using AppSource, you must understand the solution framework.

## Unmanaged and managed solutions

There are two types of CDS solutions: *managed* and *unmanaged*. 
- A **managed** solution is a completed solution that is intended to be distributed and installed. When a managed solution is deleted (uninstalled), all the customizations and extensions included with it are removed.
- An **unmanaged** solution is one that is still under development or isn’t intended to be distributed. When an unmanaged solution is deleted, only the solution container of any customizations included in it is deleted. All the customizations remain in effect. When the unmanaged solution is complete and you want to distribute it, export it and package it as a managed solution.

You cannot edit the components of a managed solution, but you can apply additive changes to the components of a managed solution within your own unmanaged solutions. When you do this you create a dependency between your customizations and the managed solution. When a dependency exists the managed solution cannot be uninstalled until you remove the dependency.

You cannot import a managed solution into the same environment that contains the originating unmanaged solution. To test an managed solution,you need a separate environment.

## Solution publishers

Each solution is linked to a solution publisher. The solution publisher provides information about how to contact the publisher as well a common customization prefix value.

When any schema changes are included as part of a solution, the solution publisher customization prefix is appended to the name of the schema items. This is valuable because it allows for easy recognition of which solution added the schema item. It is not required for all schema items in a solution to use the same customization prefix, but it is strongly recommended.

> [!IMPORTANT]
> Before you start creating a solution that you may distribute, you should create a solution publisher record and create a new solution linked to it. You should make sure the customization prefix represents a value that makes sense for you. The default value is `new`.

Your choice of solution publisher is important in case you want to publish an update to a solution you have shipped. An update can only be applied to a managed solution with the same publisher as the original managed solution. More information [Create managed solution updates](/dynamics365/customer-engagement/developer/maintain-managed-solutions#create-managed-solution-updates)

## Solution layering

It is possible for two managed solutions to be installed which contradict each other or for some customizations applied to the environment to override a managed solution. How does this work?

It works because CDS evaluates managed solutions by the order in which they are installed and any customizations that are not in a managed solution are evaluated last.

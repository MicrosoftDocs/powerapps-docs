<properties
	pageTitle="User function | Microsoft PowerApps"
	description="Reference information, including syntax, for the User function in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# User function in PowerApps #

Returns information about the current user.

## Description ##

The **User** function returns a [record](working-with-tables.md#records) of information about the current user:

| Property | Description |
|----------|-------------|
| **User()!Email** | Email address of the current user. |
| **User()!FullName** | Full name of the current user, including first and last names. |
| **User()!Image** | Image of the current user. |

## Syntax ##

**User**()

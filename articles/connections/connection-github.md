<properties
	pageTitle="Overview of the GitHub connection | Microsoft PowerApps"
	description="See the available GitHub functions, responses, and examples"
	services=""	
	suite="powerapps"
	documentationCenter="" 	
	authors="MandiOhlinger"	
	manager="erikre"	
	editor="" 
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="04/26/2016"
ms.author="mandia"/>

#  GitHub

![GitHub](./media/connection-github/githubicon.png)

GitHub is a web-based Git repository hosting service. It offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features.

You can display this information in a text box on your app. For example, you can manage issues within a GitHub repository using controls within your app. 

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[CreateIssue](connection-github.md#createissue) | Creates an issue |
|[IssueOpened](connection-github.md#issueopened) | An issue is opened |
|[IssueClosed](connection-github.md#issueclosed) | An issue is closed |
|[IssueAssigned](connection-github.md#issueassigned) | An issue is assigned  |


## CreateIssue
Create an issue: Creates an issue 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|repositoryOwner|string|yes|Repository owner|
|repositoryName|string|yes|Repository name|
|issueBasicDetails| |yes|Issue details|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|title|string|Yes | Issue title |
|body|string|Yes |Issue body |
|assignee|string|Yes | Issue assignee|
|number|string|No |Issue id |
|state|string|No | Issue state|
|created_at|string|No | Issue created time|
|repository_url|string|No | Repository url|


## IssueOpened
When an issue is opened: An issue is opened 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|title|string|Yes | Issue title |
|body|string|Yes |Issue body |
|assignee|string|Yes | Issue assignee|
|number|string|No |Issue id |
|state|string|No | Issue state|
|created_at|string|No | Issue created time|
|repository_url|string|No | Repository url|


## IssueClosed
When an issue is closed: An issue is closed 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|title|string|Yes | Issue title |
|body|string|Yes |Issue body |
|assignee|string|Yes | Issue assignee|
|number|string|No |Issue id |
|state|string|No | Issue state|
|created_at|string|No | Issue created time|
|repository_url|string|No | Repository url|


## IssueAssigned
When an issue is assigned: An issue is assigned 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|title|string|Yes | Issue title |
|body|string|Yes |Issue body |
|assignee|string|Yes | Issue assignee|
|number|string|No |Issue id |
|state|string|No | Issue state|
|created_at|string|No | Issue created time|
|repository_url|string|No | Repository url|


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.

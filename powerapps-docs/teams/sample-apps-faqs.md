---
title: Frequently Asked Questions (FAQs) and answers when using sample app templates | Microsoft Docs
description: Learn about the Frequently Asked Questions (FAQs) and answers when using sample app templates.
author: msftsamperl

ms.topic: faq
ms.custom: 
ms.date: 10/05/2020
ms.subservice: teams
ms.author: saperlmu
ms.reviewer: mkaur
contributors:
  - msftsamperl
  - mduelae
---

# Frequently Asked Questions (FAQs) for sample app templates

In this article, learn about the frequently asked questions and the answers about using the sample app templates.

> [!IMPORTANT]
> For any issues, feedback, support, or changes related to sample app templates, go to https://github.com/microsoft/teams-powerapps-app-templates/issues and submit an issue or a pull request.

## When I try to install a sample app template, I get an error that the app is already in the team.

You may see the following error when you try to install a sample app template in a team that already has the app installed, but you’re not the app owner, or the team owner.

`This app is already in this team` <br>
`To update it, you must be its owner or a team owner.`

When this happens, use the installed app, or install the app in a different team.

## How can I move an app to another channel in the same Team?

For the steps to move an app, go to [Move an app to another Teams channel in the same team](publish-and-share-apps.md#move-an-app-to-another-teams-channel-in-the-same-team).

## How do I delete the sample data from the sample app templates?

For the steps to delete sample data from the sample app templates, go to [Remove sample data](customize-sample-apps.md#remove-sample-data).

## Planner tasks are created with “Former Member” instead of the name of the assigned user

When you assign a task in the Issue reporting, or Inspection apps who isn't a member of the Teams team, the user's name on the task will show as "Former member".
To correctly display the user's name, add the user to the Team where the app is installed.

![Former member.](media\sample-apps-faqs\former-member.png "Former member")

## Why can't I create tasks in Inspection app?

If a user isn't allowed to create tasks using a mobile device in the Inspection app:

1. Open **Manage inspections** in Power Apps Studio.

1. Select **Settings**.

1. In the Planner drop-down, select the Planner that you want to use.

1. **Save**

## Inspection app forms are slow

If your inspection forms are loading slowly, reduce the size of images used in the inspection steps. Users can't interact with the form before all images on the form are loaded.


[!INCLUDE[footer-include](../includes/footer-banner.md)]

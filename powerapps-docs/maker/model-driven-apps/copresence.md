---
title: Discover who's working on an app in Power Apps
description: The copresence feature in model-driven app lets you know who's working on the app 
author: Mattp123
ms.author: matp
ms.service: "powerapps"
ms.subservice: mda-maker
ms.topic: how-to
ms.date: 09/05/2023
ms.custom: template-how-to
---
# Discover who's working on an app

Find who's working on an app at the same time as you with copresence. Copresence provides the following benefits:

- Icons and names of people who have the app open and might be making changes are displayed.
- Contact those people working on the app via email or Teams.
- On the left navigation pane, the structure of the app is displayed letting you know what part of the app is being worked on.
- Receive notification for saved changes made from other makers. Then, you'll be prompted to refresh the app to stay on the latest version so as not to lose your work or overwrite other's work later. More information: [Notifications](#notifications)
- The name of the maker who made the first save or the last save is displayed.

> [!IMPORTANT]
> Most Power Platform environments have [coauthoring](coauthoring.md). In case your tenant doesn’t have coauthoring yet, you'll have the copresence experience that is described in this article.

:::image type="content" source="media/co-authoring.png" alt-text="Copresence feature in app designer":::
1. Command bar displays makers currently working in the app and allows you to chat or email them.
1. Left navigation indicates what app component the maker is working on.

## How copresence works

The first time someone joins your app in app designer while you working on it a notice appears that indicates other people are also working on the app. Advice is given to check with the other makers about the order you plan to make changes. Notice that it's possible that the other makers in the app might not want to save their changes.

Icons of copresent makers appear in both the toolbar area and the left navigation pane showing where other makers are working in the app.

When you have several tabs open, your icon is displayed in the left navigation pane as well. This way you’ll always see if you have more than one tab open, which helps you find the one you want to continue working on.

On the right side of the app designer toolbar, all the makers that have this app open are displayed. If  more than four makers are present, a +n, such as +1 or +30, is displayed that expands with all the makers’ names. Select a name to display **Send email** and **Chat in Teams** links to contact that person.

## Notifications

You may be working on the app, or you may be idle, but once someone else saves a change to the app, you’ll receive a notification in the upper bar indicating that another maker made changes. When this occurs, you're advised to refresh to be at the latest version so as not to lose changes you make afterwards.

> [!TIP]
> - If you weren’t expecting anyone to make changes to the app, and spent a long time adding changes, we recommend you contact the person immediately. For example, it might happen that another maker saved something minor and you can agree that your changes may overwrite their changes. In this case, do not select refresh, instead select save to present the option to overwrite changes.
> - We recommend that you to always stay at the latest version of the app and refresh when others save changes. If you were idle and didn't make changes and see this notification, select refresh.
>

If you've ignored or closed the refresh notification, you won’t be at the latest version of the app. At the time when you select save, you're prompted with a choice: refresh (and lose your changes) or overwrite (and lose other maker's changes).

> [!TIP]
> We recommend you chat with the team or the person who made the last change. Copresence provides the name of the maker to alert you before you overwrite their changes.

## Known copresence limitations and issues

- There may be a delay up to 20 seconds between when new members join the app and when you see their presence and location.
- There may also be a delay up to one minute between when someone saves a change and when you get a notification about the change. However, if there's a conflict, you'll always get the prompt to choose whether to refresh or overwrite when you try to save.
- Making a comment on a new page or area triggers a background save and if your app isn't on the latest version you'll be prompted to either refresh or overwrite.
- Instead of copresence, your environment may have coauthoring, which allows app change merges to occur in real-time with seamless collaboration. More information: [Coauthoring in model-driven apps (preview)](coauthoring.md) 

## See also

[Collaboration in model-driven apps](collaboration-model-driven-apps.md)
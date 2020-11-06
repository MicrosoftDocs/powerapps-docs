---
title: "Manage page permissions for a portal | MicrosoftDocs"
description: "Learn about how to manage page permissions for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/16/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Manage page permissions

## Overview

Page permissions control access to the webpages to portal users. You can also allow pages to be available anonymously for public access. Depending on business requirements, you can manage the inheritance of page permissions from a parent page to a child page. A page can have child web files (such as downloadable documents). Hence, you can also manage the inheritance of page permissions from a page to its child web files.

You can manage page permissions in two ways:

- Portals Studio
- Portal Management app

Portals Studio simplifies the configuration of webpage access permissions using the Portal Management app. Managing page permissions inside the Portal Management app is referred to as the *Web Page Access Control Rules*.

## Manage page permissions using portals Studio

Power Apps portals Studio allows you to edit the customize your portal. Page permission management using portals Studio is quicker and more efficient compared to using the Portal Management app. You may still need to use the Portal Management app for managing page permissions of legacy areas. However, using the portals Studio to manage page permissions is the recommended method.

To get started with managing page permissions using portals Studio:

1. Go to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left pane.

1. Select your portal.

1. Select **Edit** to open the portal in portals Studio.

    More information: [Edit the portal](../manage-existing-portals.md#edit), [portals Studio anatomy](../portal-designer-anatomy.md)

1. Select a page that you want to manage permissions for.

    ![Select page in portals Studio](media/webpage-access-control/select-page.png "Select page in portals Studio")

1. 

## Manage page permissions using Portal Management app

Web page access control rules are rules that you create for your site to control both the publishing actions that a web role can perform across the pages of your website and to control which pages are visible by which web roles. The webpage access entity has the following attributes:


|    Name     |                                                                                                                                                                  Description                                                                                                                                                                   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    Name     |                                                                                                                                                        A descriptive name for the rule.                                                                                                                                                        |
|   Website   |                                                                                                           The website that this rule applies to; must match the website of the page to which this rule is applied. Filters Web Page.                                                                                                           |
|  Web Page   |                            The webpage that this rule applies to. The rule will affect not only the page but all child pages of the page, therefore making this attribute select the branch of the website to which the rule will apply. If a rule is applied to the home page, it will apply to the entire portal.                            |
|    Right    |                                                                                                                                    [Grant change](#grant-change) or [Restrict read](#restrict-read) below.                                                                                                                                     |
|    Scope    | <ul><li><strong>All content</strong>: All descendant content is included in security validation.</li><li><strong>Exclude direct child web files</strong>: All child web files directly related to this webpage are excluded from security validation. This does not exclude child's descendants.</li></ul>By default, All content is selected. |
| Description |                                                                                                                                                     (Optional) A description of the rule.                                                                                                                                                      |

After creating a new access control rule, associate it with a page. This will cause it to affect both the page you assign the rule to and all child pages&mdash;in other words, the entire branch of the website.

There are two types of access control rules: Grant Change and Restrict Read.

### Grant Change

Grant Change allows a user in a web role associated with the rule to publish content changes for this page and all child pages of this page. Grant Change takes precedence over restrict read. For example, you might have a news section of the site, which you want to be editable by users in the news editor web role. These users might not have access to the entire site, and certainly can't edit the entire site, but within this branch they have full content publishing authority. You would create a webpage access control rule called grant news publishing to news editors.

Next, you would set the right to grant change and the webpage to the parent page of the entire news branch of your site. You would then assign this web role to any contacts you want to designate as news editors. Note that one user can have many web roles.

A Grant Change rule should always be present in any portal that you wish to enable front-side editing for. This rule will apply to the home page of the site, thus making it the default rule for the entire site. This rule will be associated with a web role that is to represent the administrative role for the site. Users who are to be given front-side content publishing rights will be assigned to this role.

### Restrict read

The Restrict Read rule is used to limit viewing of a page (and its child pages) and its content to specific users. Whereas grant change is a permissive rule (it grants the ability to do something to its users), restrict read is a restrictive rule in that it restricts an action to a limited set of users. For example, you might have a section of the site meant to be used by employees only. You might restrict read of this branch to only people in the employee web role. You would create a new rule called restrict read to employees only.

You would then set the right to restrict read and the page to the page at the top of the branch which is to be read only by employees. You would then associate this rule with the employee web role and then assign users to this role.

> [!Note]
> If you apply the **Restrict Read** right to the root 'home' page of a website and select **Exclude direct child web files** as the **Scope**, the home page's direct child web files will be accessible to all users.

### See also

[Create web roles for portals](create-web-roles.md)  
[Add record-based security using entity permissions for portals](assign-entity-permissions.md)

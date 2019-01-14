---
title: "Include filtering attributes with plug-in registration | MicrosoftDocs"
description: "If no filtering attributes are set for a plug-in registration step, then the plug-in will execute every time an update message occurs for that event."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 12/12/2018
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Include filtering attributes with plug-in registration

**Category**: Performance

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

If no filtering attributes are set for a plug-in registration step, then the plug-in will execute every time an update message occurs for that event.  A combination of no filtering attributes and auto-save functionality could lead to unnecessary plug-in executions causing undesirable behavior and degrade performance.

<a name='guidance'></a>

## Guidance

Most plug-ins registered for an entity's update message do not need to execute on all updates. Usually, there is only a need to process certain logic when a specific attribute or attributes have changed. In order to prevent extra processing in the environment, minimize the logic needed in a plug-in and all the update to complete as quickly as possible, it is highly recommended that plug-in step registrations also include filtering attributes for update messages.

![Plug-in Registration Step with Filtering Attributes](../media/plugin-registration-step-with-filtering-attributes.png)

<a name='additional'></a>

## Additional information

Filtering attributes are a list of entity attributes that, when changed, cause the plug-in to execute.  These attributes can be set when registering the plug-in using the Plug-in Registration tool. If no attributes are set, then the plug-in will execute every time an update message occurs. Updates can occur for a variety of reasons. When auto-save is turned on in the environment, it can occur multiple times during the session of user when on an entity form. If filtering attributes are not specified, then the plug-in will execute for any attribute change to the designed entity.

<a name='seealso'></a>

### See also

[Plug-in design](/dynamics365/customer-engagement/developer/write-plugin#plug-in-design)<br />
[Walkthrough: Register a plug-in using the plug-in registration tool](/dynamics365/customer-engagement/developer/walkthrough-register-plugin-using-plugin-registration-tool)
[Disable auto-save](/dynamics365/customer-engagement/customize/manage-auto-save)
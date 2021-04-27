---
title: Create and manage website bindings
description: Learn how to create and manage website bindings in portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Create and manage website bindings

In a portal, the default method of selecting a website is finding a website by matching the name of the website defined in the web.config file of that particular portal. Website bindings provide alternative methods of selecting a website by using the host name when loading a portal or path of the request to select the appropriate website. This eliminates the need to modify separate web.config files for each version of a specific website. This streamlines the deployment of portals across various development, staging, and production environments. Furthermore, this allows a common portal codebase to operate multiple websites.

## Manage website bindings

Website bindings can be created, edited, and deleted within  Power Apps portals. 

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Website Bindings**.

3. To create a new website binding, select **New**.

4. To edit an existing website binding, select the website binding name.

5. Enter appropriate values in the fields.

6. Select **Save & Close**.

### Website binding attributes

These are the attributes common to all bindings.

|Name|Description|
|-----|----------|
|Name| A title to identify the website binding when viewing the records.|
|Website|The [website](websites.md) that should be selected by the portal.|
|Release Date|A date that determines when the website is allowed to be selected.|
|Expiration Date|A date that determines when the website will stop being selected.|
|||

#### Application Settings

Specify values for these attributes for an application level binding. This binding maps based on IIS website or application.

|Name|Description|
|-----|----------|
|Site Name|The name of the IIS website.|
|Virtual Path|The name of the IIS application under the website.|
|||

For Azure websites and cloud services, the site name and virtual path values are determined by the <Site> and <VirtualApplication> nodes of the **ServiceDefinition.csdef** file.

```
<ServiceDefinition>
  <WebRole>
    <Sites>
      <Site name=Dynamics Portals>
        <VirtualApplication name=customer-portal/>
```

### See also
[Create and manage websites](websites.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
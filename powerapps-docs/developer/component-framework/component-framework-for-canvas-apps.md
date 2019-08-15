---
title: PowerApps component framework for canvas apps  | Microsoft Docs
description: Create custom components for canvas apps
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 08/31/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5d100dc3-bd82-4b45-964c-d90eaebc0735
---

# PowerApps component framework for canvas apps

> [!IMPORTANT]
> This feature is still experimental and disabled by default. For more information, see [Experimental and preview features](working-with-experimental.md).

PowerApps component framework enables developers and app makers to create custom components to use in an app or across apps. PowerApps component framework gives the ability for the developers to enhance the user experience for the users to view and work with data. For example:

- Replace a field that displays a numeric text value with a dial or slider component.

Component developers and app makers can utilize modern web practices and also harness the power of external libraries to create advanced user interactions. The framework automatically handles component lifecycle, retains application business logic and optimizes the performance. more information: [PowerApps component framework overview](overview.md) 

## Prerequisites

1. System Administrator privileges is required to enable PowerApps component feature in the environment.


## Enable PowerApps component framework feature

To enable PowerApps component feature:

1. Sign in to [PowerApps](https://powerapps.microsoft.com/en-us/).

2. Click on the **Settings** icon and select **Admin Center**
    
    ![Settings admin center](media/select-admin-center-from-settings.png "Settings admin center") 

3. Select the environment where you want to enable this feature and click on **...** and select **Settings**

4. Under the **Products** tab, select **Features**

5. From the list of available features, turn on the switch under the **PowerApps component framework for canvas apps**

## Implementing custom components

After you enable the feature in your environment, the next step is to implement the custom component. [Implement sample component](implementing-controls-using-typescript.md) topic demonstrates step by step process to create custom components right from implementing custom logic, debug process, and creating a solution zip file.

## Add components to an app

To add custom components to an app:

1. Navigate to PowerApps Studio.
2. Select the app that you want to add the custom component.
3. Click on **Insert** > **Components** > **Import component** > 
 
    ![Insert components](media/insert-components-import.png "Insert components")

4. Select **Code (experimental)** tab and add a component from the list and click on **Import**. This adds the sample component in the **Components** menu

    ![Import sample component](media/import-component-add-sample-component.png "Insert sample component")

5. Navigate to **Components** and select the component to add it to the app.

   ![Add sample component](media/add-sample-component-from-list.png "Add sample component")

## Known limitations

1. PowerApps component framework doesn't support adding of multiple components to an app.

## See also


[PowerApps component framework overview](overview.md)<br/>
[Implement sample component](implementing-controls-using-typescript.md)
<!--[Capabilities and limitations of PowerApps component framework for canvas apps](capabilities-and-limitations-for-canvas-apps.md)-->
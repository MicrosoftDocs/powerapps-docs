---
title: Component library application lifecycle management (ALM)
description: Learn about the application lifecycle management (ALM) with component libraries
author: hemantgaur
ms.subservice: canvas-developer
ms.topic: article
ms.date: 04/19/2022
ms.author: hemantg
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - hemantgaur
  - tapanm-msft
---

# Component library application lifecycle management (ALM)

A [component library](component-library.md) is a special type of canvas app that can contain one or more canvas components and these library components can then be used by all the other canvas apps in the environment. This provides a way to create reusable shared components across all apps in an environment, unlike [app level components](create-component.md#components-in-canvas-apps) which are restricted to one app. A component from a component library can be used by first importing it into a canvas app and then adding it to app screen. Any further updates in the component definition from the component library will prompt app maker to review and incorporate the change [on demand](component-library.md#method-2-proactive-check-for-updates) or when the [app is opened for editing](component-library.md#method-1-component-update-notification-on-app-edit). Component libraries and dependent apps can also be moved to another environment using standard [Dataverse solutions](/power-platform/alm/solution-concepts-alm).

> [!NOTE]
> Term "import," component used here refers to importing component from component library to an app and should not be confused with "importing" a solution into Datavese.

When a component from a component library is imported into a canvas app, that component's definition is copied into the definition of the canvas app itself. Once a component definition has been imported, the app is "self-contained" as far as that component definition is concerned: The app maker can choose to [edit component](component-library.md#library-component-customization) and create local instances of the component within the app. At this point there is no direct link to the component library from where the component originated. Significantly, this self-containment characteristic even applies if the canvas app is subsequently migrated to a different environment where the component library is not present. In the target environment, an app author can continue creating instances of the imported component definition, and the app can still be published and played. No new updates will be prompted or received in the app in this case. In order to maintain the relationship from app to component library it is important to not edit the component in the app, instead use the master definition in the component library.

**Canvas apps and Component libraries solution support**

Inline with the other solution object dependencies, if a canvas app uses a control from component library it will have a dependency on that component library. In order to move an app to the new environment you will need to either package the library inside the same solution or install library as a pre-requisite. Later when the component library with the updated component is imported via solution into the target environment, existing apps can get the new component definitions using the normal [component update flow](component-library.md#update-a-component-library).

**Creating and Exporting component library in a solution**

You can either create a component library directly from within the solution or add it to existing solution via solutions add existing component library button.

Animation - Gif: [Adding component library to solution.](https://microsoft-my.sharepoint.com/:i:/p/hemantg/Ed0CDoi6AINFpZeQFPEnW6cBZmRq1Jd7WE7t3TlMR7EyBw?e=9pyje5)

When a component library is saved in an environment which has Dataverse available, component library is automatically added to the default solution. Note that the unique logical name is generated for the component library which also has the default CDS publisher prefix. This is to ensure that the solution system is aware of its presence and can link dependencies from apps which use library logical name.

Note: Component libraries created before the component ALM feature rollout need to be edited, published, and editor closed explicitly before they are enabled for ALM capabilities. You can check the component library ALM readiness by its presence in the default solution.

![Graphical user interface  text  application  email Description automatically generated](media/image1.png)

Component libraries inside solution also supports "allow customization" managed properties which govern the behavior of component inside the app.

![Graphical user interface  text  email Description automatically generated](media/image2.png)

If "Allow customizations" is turned off and solution is exported to target environment. component cannot be edited inside the app which uses this component.

![Graphical user interface  text  application  email Description automatically generated](media/image3.png)

Apps which use components from the component library will be marked as dependent in the solutions infrastructure. Note that this applies to all apps which are added to any Dataverse solution in a given environment. Users can still create apps outside dataverse/solutions but these non-dataverse apps will not have any solution depedencies. Users can later add these apps to solutions to make them part of solution ALM.

Gif : [Show solution dependecies](https://microsoft-my.sharepoint.com/:i:/p/hemantg/ESHBpcFUxLVMk0ri-kWQZtQBatfbhuDjfVGpK2fro33bTQ?e=aIgteR)

If a solution which just has a app using component from library is imported and target environment does not has the right component library, users will see import failed message due to missing depedency.

![Graphical user interface  application Description automatically generated](media/image4.png)

Users can either pre-install the library solution or bundle it with the app inside the same solution to make app available in the target environment. The app will have the dependency created in the target environment. When the library is updated and newer component version is imported via solutions, app will get notification and can get the change.

GIF - [UpdateFromLibrary.gif](https://microsoft-my.sharepoint.com/:i:/p/hemantg/EcKXl-evzcBHo5QLFMV0opEBYskdjFjY4ruEAhAWMDkvpg?e=5q9JvO)

If managed properties of the component library is set to say "allow customizations " = false, library cannot be edited in the target environment.

Note that the dependencies are calculated based on the latest published state of an app. So if you restore the older version which does not uses a library component, depedency will be removed in the app and hence solutions. Importing the component into the app from library without actually using it also creates dependency as library component remains available for use via insert menu.

Tip: If you edit the Library component in the consuming app it creates a local copy. At this point the library component is still available for use in the insert pane. In order to remove the dependency completely you can delete the compoent from insert menu -&gt; Library component -&gt; Remove from app

**Best practices and troubleshooting**

1.  Limit the number of components in a library to 20 to get optimal performance. Plan and create multiple component libraries ahead of time as the number of components in them will grow over time. This will also reduce the solution payload as apps are moved across the environment.

2.  There is a delay from when the component library is published to when it is available to the application and can take up to 5 minutes.

3.  If the app is not able to receive the update from the library component in the target environment where the solution is installed. Please check the following:

    -   Determine the component library logical name from the solution view. Use default solution if library is not explicitly added to solution.

Download app using the library component to local computer using File -&gt;save as -&gt; This computer. Rename the downloaded file to have zip extension and inspect Properties. Json for LibraryDependencies. This should have the matching library logical name.

.

-   Solution consumers:, please check that the canvas app has properly identified the component libraries as [solution dependencies](https://docs.microsoft.com/en-us/power-platform/alm/solution-concepts-alm#solution-dependencies). If the solution does not properly identify the component libraries as solution dependencies, that means the app dependency to the component library link has not been created properly. Please check with the solution provider to resolve the issue.

-   Solution publishers, please check that component libraries are saved with

-   library logical name in the solution and it is same as one referenced in msapp.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
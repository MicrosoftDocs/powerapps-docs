<properties
	pageTitle="Resources within environments | Microsoft PowerApps"
	description="Resources within environments"
	services="powerapps"
	documentationCenter="na"
	authors="aftowen"
	manager="robinr"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/19/2016"
   ms.author="anneta"/>

# Resources within environments #
Every app that you create in PowerApps is located in an [environment](environments-overview.md), which contains resources that you create or modify during the development process. Typically, development is done in the same environment that is used by the organization's end users. This environment is known as the default environment. It's relatively easy to manage resource changes in the same environment. You validate the changes to make sure that all critical business processes and applications are functional, and then you release the app.

Sometimes, development and testing are done in separate environments, and changes are moved to the default environment when they are ready to be used by end users. There are several reasons why you might use separate environments. For example, you might have used a separate environment when you initially evaluated the system. Alternatively, you might want to minimize the risk that is involved when changes are made to the default environment. Separate environments provide isolation, because you make your changes in an environment that isn't the default environment. Depending on the extent of the risks, you might create an additional staging environment. In this case, you have a development environment, a staging environment, and a default environment.

When an app is ready to release to the larger organization, you need to move it and its resources to the new environment. For example, [export data in entities to Excel](data-platform-interactive-excel.md), import the data into a database in another environment, and [move the app itself](environment-and-tenant-migration.md).

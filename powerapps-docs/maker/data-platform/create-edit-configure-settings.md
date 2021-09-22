---
title: "Use settings to provide tailored app experiences | MicrosoftDocs"
description: "Use settings to provide tailored app experiences."
Keywords: settings, settings environment value, settings app value, model-driven app
author: aneesa
ms.subservice: dataverse-maker
ms.author: aneesa
ms.reviewer: matp
manager: kvivek
ms.date: 09/22/2021
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Settings overview 
Settings are solution components that enable makers and administrators to quickly configure and customize apps to provide a tailored app experience. Using settings makers and administrators can enable or disable features or configure feature behaviors for one specific app or all apps within an environment.

Settings are made up of three sub-components: Setting definition, Setting environment value and Setting app value.

Setting definition specifies the base metadata of the settings like its name, description, data type, default value and more.

Settting environment value can be used to override the default value, as specified in the setting definition, for an environment. Setting environment value applies to all apps in that environment.
If a setting environment value exists for a setting, all apps in that environment will get that value instead of the setting's default value. If no setting environment value exists for a setting, all apps in that environment will get the setting's default value.

Settting app value can be used to override both the default value, as specified in the setting definition, as well as any setting environment value created for that setting in that environment. Setting app value applies to one specific app.
If a setting app value exists for a setting, all apps in that environment will get that value instead of the setting's default value. If no setting environment value exists for a setting, all apps in that environment will get the setting's default value.

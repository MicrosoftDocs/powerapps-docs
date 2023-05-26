---
title: use-cached-webresource Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-cached-webresource.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-cached-webresource`

Don't use a relative or absolute URL that retrieves a web resource from the server rather than from the cache. Web resource URLs should always be relative to ensure caching support. Additionally, don't include `/WebResources/` within the URL path as it will refer to the caller's default organization.

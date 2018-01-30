---
title: API connector FAQ | Microsoft Docs
description: Find answers to questions about requirements, triggers, and other areas.
services: ''
suite: powerapps
documentationcenter: na
author: mgblythe
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/06/2017
ms.author: mblythe

---
# API connector FAQ (PowerApps)
## Requirements
**Q:** If I am not an ISV, can I still build a connector?

**A:** To release a connector publicly, we require that you either own the underlying service or present explicit rights to use the API.

**Q:** Can I build a connector without REST APIs?

**A:** No. In order to build an API connector, you are required to support stable HTTP REST APIs for your service.

**Q:** What are the supported authentication types?

**A:** We support the following standards of authentication:

* OAuth2.0 (includes Azure Active Directory)
* API Key
* Basic Authentication

## Triggers
**Q:** Can I build triggers without webhooks? 

**A:** API connectors for Microsoft Flow and Logic Apps allow you to build webhook-based triggers only. If you have a request for other forms of implementation, please contact [condevhelp@microsoft.com](mailto:condevhelp@microsoft.com) along with more details about your API.

## Miscellaneous
**Q:** My APIs use a dynamic host. How do I implement this in the OpenAPI?

**A:** The API connector feature doesn't support dynamic hosts. Please use a static host for development and testing purposes. During submission, talk to your Microsoft contact regarding the dynamic implementation.

**Q:** Do you support Postman Collection V2?

**A:** No, Postman V2 is currently not supported.

**Q:** Do you support OpenAPI 3.0?

**A:** No, OpenAPI 2.0 is currently the only supported version.


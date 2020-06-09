---
title: Use the Web API for portals | Microsoft Docs
description: Learn how to use the portals Web API to create, read, update and delete Common Data Service entities.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/05/2020
ms.author: tapanm
ms.reviewer:
---

# Portals Web API

## Retrieve an entity record 

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api

Difference:

[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) --> [Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)

## Create an entity record

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/create-entity-web-api

Difference:

[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) --> [Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)

No OData-EntityId: [Portal URI]/_api/v1.0/accounts(7eb682f1-ca75-e511-80d4-00155d2a68d1)

### Associate entity records on create

New addition: 

Example JSON for creating annotation via Web API
{
        "new_attribute1": "test attribute 1",
        "new_attribute2": "test attribute 2",
        "new_comments": "test comments",
        "new_recordurl": recordURL,
        "new_feedback_Annotations":
            [
                {
                    "notetext": "Screenshot attached",
                    "subject": "Attachment",
                    "filename": file.name,
                    "mimetype": file.type,
                    "documentbody": base64str,
                }
            ]
    }

“documentbody” will contain the attachment as base64 string.

!! Portal Web API will not  --> @Neeraj - Incomplete sentence. What will portals Web API NOT...?

## Update and delete entities using the Web API

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api

Difference:

[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) --> [Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)

## Associate and disassociate entities using Web API

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/associate-disassociate-entities-using-web-api

Difference:

[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) --> [Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)

## Use Web API actions

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/use-web-api-actions 

Difference:

[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) --> [Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)

## Next steps

[Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)

### See also

- [Web API overview](web-api-overview.md)
- [Web API samples](web-api-samples.md)


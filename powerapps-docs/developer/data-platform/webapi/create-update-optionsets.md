---
title: "Create and update choices (option sets) using the Web API (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about creating and updating choices in Microsoft Dataverse."
ms.date: 06/07/2023
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: NHelgren # GitHub ID
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Create and update choices (option sets) using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Typically, you use *global* option sets to set table columns so that different columns can share the same set of options, which are maintained in one location. Unlike *local* option sets which are defined only for a specific column, you can reuse global option sets. You will also see them used in request parameters in a manner similar to an enumeration.  

> [!NOTE]
> You can only change an existing managed option set if you are the publisher. In order to make a change such as rename option or delete option on these option sets, an Upgrade must be made to the solution that added the option set. More information: [Upgrade or update a solution](../../../maker/data-platform/update-solutions.md)

When you define a global option set using a POST request to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions`, 
we recommend that you let the system assign a value. You do this by passing a **null** value when you create the 
new `OptionMetadata` instance. When you define an option, it will contain an option value prefix specific to the 
context of the publisher set for the solution that the option set is created in. 
This prefix helps reduce the chance of creating duplicate option sets for a managed solution, 
and in any option sets that are defined in environments where your managed solution is installed. For more information, see [Merge option set options](/power-platform/alm/how-managed-solutions-merged#merge-option-set-options).

## Messages

The following table lists the messages that you can use with global option sets.  
  
|Message|Web API Operation|  
|--|--|
|`CreateOptionSet`|Use `POST` request to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions`.|
|`DeleteOptionSet`|Use `DELETE` request to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions(`*metadataid*`)`.|
|`RetrieveAllOptionSets`|Use `GET` request to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions`.| 
|`RetrieveOptionSet`|Use `GET` request to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions(`*metadataid*`)`.|

The following table lists the messages you can use with local and global option sets

|Message|Web API Operation|  
|--|--|
|`DeleteOptionValue`<br />Deletes one of the values in a global option set.|[DeleteOptionValue Action](xref:Microsoft.Dynamics.CRM.DeleteOptionValue)
|`InsertOptionValue`<br />Inserts a new option into a global option set.|[InsertOptionValue Action](xref:Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action)| 
|`InsertStatusValue`<br />Inserts a new option into the global option set used in the `Status` column.|[InsertStatusValue Action](xref:Microsoft.Dynamics.CRM.InsertStatusValue)|
|`OrderOption`<br />Changes the relative order of the options in an option set.|[OrderOption Action](xref:Microsoft.Dynamics.CRM.OrderOption)|
|`UpdateOptionSet`|Use `PUT` request with a [OptionSetMetadataBase EntityType](xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase) to *[Organization URI]*`/api/data/v9.2/GlobalOptionSetDefinitions(`*metadataid*`)`<br />Only those properties defined by the `OptionSetMetadataBase` can be updated. This does not include the options. Use other actions to make changes to options.|
|`UpdateOptionValue`<br />Updates an option in a global option set.|[UpdateOptionValue Action](xref:Microsoft.Dynamics.CRM.UpdateOptionValue)|
|`UpdateStateValue`<br />Inserts a new option into the option set used in the `Status` column.|[UpdateStateValue Action](xref:Microsoft.Dynamics.CRM.UpdateStateValue)|

## Examples

- [Create a global option set](#create-a-global-option-set)
- [Create a choice column using a global option set](#create-a-choice-column-using-a-global-option-set)
- [Insert options](#insert-options)
- [Update options](#update-options)
- [Order options](#order-options)
- [Delete Option](#delete-option)
- [Insert status value](#insert-status-value)

### Create a global option set

//TODO

**Request**

```http
POST [Organization Uri]/api/data/v9.2/GlobalOptionSetDefinitions
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 2769

{
  "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
  "Options": [
    {
      "Value": 727000000,
      "Label": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Red",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        ],
        "UserLocalizedLabel": {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Red",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      }
    },
    {
      "Value": 727000001,
      "Label": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Yellow",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        ],
        "UserLocalizedLabel": {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Yellow",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      }
    },
    {
      "Value": 727000002,
      "Label": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Green",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        ],
        "UserLocalizedLabel": {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Green",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      }
    }
  ],
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Color Choice",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Color Choice",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Colors",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Colors",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "Name": "sample_colors",
  "OptionSetType": "Picklist"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/GlobalOptionSetDefinitions(1d733907-4d05-ee11-8f6e-000d3a993550)
```

### Create a choice column using a global option set

//TODO

**Request**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1465

{
  "@odata.type": "Microsoft.Dynamics.CRM.PicklistAttributeMetadata",
  "AttributeType": "Picklist",
  "AttributeTypeName": {
    "Value": "PicklistType"
  },
  "SourceTypeMask": 0,
  "GlobalOptionSet@odata.bind": "/GlobalOptionSetDefinitions(1d733907-4d05-ee11-8f6e-000d3a993550)",
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Colors Global Picklist Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Colors Global Picklist Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Colors",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample Colors",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_Colors"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(25733907-4d05-ee11-8f6e-000d3a993550)
```

### Insert options

**Request**

```http
POST [Organization Uri]/api/data/v9.2/InsertOptionValue
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 612

{
  "AttributeLogicalName": "sample_choice",
  "EntityLogicalName": "sample_bankaccount",
  "Value": 727000005,
  "Label": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Echo",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Echo",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "SolutionUniqueName": "examplesolution"
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InsertOptionValueResponse",
  "NewOptionValue": 727000005
}
```

### Update options

To update individual options you must use the [UpdateOptionValue Action](xref:Microsoft.Dynamics.CRM.UpdateOptionValue). The following example updates the `TrueOption` from the Boolean column example in [Create a Boolean column](#create-a-boolean-column) and changes the label so that it is `Up` rather than `True`. Because this is a 'local' option set, it uses `AttributeLogicalName` and `EntityLogicalName`. For a global option set, use the `OptionSetName` parameter instead.

**Request**

```http
POST [Organization Uri]/api/data/v9.2/UpdateOptionValue HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "AttributeLogicalName": "new_boolean",
  "EntityLogicalName": "new_bankaccount",
  "Value": 1,
  "Label": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Up",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Up",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "MergeLabels": true
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

### Order options

**Request**

```http
POST [Organization Uri]/api/data/v9.2/OrderOption
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 253

{
  "EntityLogicalName": "sample_bankaccount",
  "AttributeLogicalName": "sample_choice",
  "Values": [
    727000002,
    727000000,
    727000003,
    727000001,
    727000005,
    727000004
  ],
  "SolutionUniqueName": "examplesolution"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

### Delete Option

**Request**

```http
POST [Organization Uri]/api/data/v9.2/DeleteOptionValue
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 116

{
  "AttributeLogicalName": "sample_choice",
  "EntityLogicalName": "sample_bankaccount",
  "Value": 727000004
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

### Insert status value

**Request**

```http
POST [Organization Uri]/api/data/v9.2/InsertStatusValue
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 609

{
  "AttributeLogicalName": "statuscode",
  "EntityLogicalName": "sample_bankaccount",
  "Label": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Frozen",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Frozen",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "StateCode": 1,
  "SolutionUniqueName": "examplesolution"
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InsertStatusValueResponse",
  "NewOptionValue": 727000000
}
```

### See also

[Customize choices](../org-service/metadata-option-sets.md)<br />
[Create and edit global choices overview](../../../maker/data-platform/create-edit-global-option-sets.md)<br />
[Create a choice](../../../maker/data-platform/custom-picklists.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

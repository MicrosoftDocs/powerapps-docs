---
title: "Create and update column definitions using the Web API"
description: "Learn about creating and updating Dataverse table column definitions using the Web API."
ms.date: 06/07/2023
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Create and update column definitions using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can perform all the same operations on column definitions using the Web API that you can with the Organization service. This article focuses on working with column definitions (metadata) using the Web API.


## Create columns

You can create table columns (entity attributes) at the same time you create the table definition by including the JSON definition of the attributes in the `Attributes` array for the entity you post in addition to the string attribute that serves as the primary name attribute. If you want to add attributes to an entity that is already created, you can send a `POST` request including the JSON definition of them to the entity `Attributes` collection-valued navigation property.

The following examples show how to create different kinds of columns

- [Create a string column](#create-a-string-column)
- [Create a money column](#create-a-money-column)
- [Create a datetime column](#create-a-datetime-column)
- [Create a boolean column](#create-a-boolean-column)
- [Create a customer lookup column](#create-a-customer-lookup-column)
- [Create a decimal column](#create-a-decimal-column)
- [Create an integer column](#create-an-integer-column)
- [Create a memo column](#create-a-memo-column)
- [Create a choice column](#create-a-choice-column)
- [Create a multi-select choice column](#create-a-multi-select-choice-column)

### Create a string column

The following example uses these properties to create a string column.  
  
|[StringAttributeMetadata](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`new_BankName`|  
|`DisplayName`|Bank Name|  
|`Description`|Type the name of the bank.|  
|`RequiredLevel`|`None`|  
|`MaxLength`|100|  
|`FormatName`|`Text`|  
  
The following example creates a string column using the properties and adds it to the `sample_bankaccount` table.

The URI for the attribute is returned in the response.
  
 **Request:**

```http 
POST [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "AttributeType": "String",  
 "AttributeTypeName": {  
  "Value": "StringType"  
 },  
 "Description": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Type the name of the bank",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "DisplayName": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Bank Name",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "RequiredLevel": {  
  "Value": "None",  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
 },  
 "SchemaName": "new_BankName",  
 "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",  
 "FormatName": {  
  "Value": "Text"  
 },  
 "MaxLength": 100  
}  
  
```  
  
 **Response:**

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f01bef16-287c-e511-80d2-00155d2a68d2)  
```  
  
<a name="bkmk_createMoney"></a>

### Create a money column

The following example uses these properties to create a money attribute.  
  
|[MoneyAttributeMetadata](xref:Microsoft.Dynamics.CRM.MoneyAttributeMetadata) properties|Values|  
|--------------------------------|------------|  
|`SchemaName`|`new_Balance`|  
|`DisplayName`|Balance|  
|`Description`|Enter the balance amount.|  
|`RequiredLevel`|None|  
|`PrecisionSource`|`2` <br />**Note:**  For information on the valid values for PrecisionSource, see [MoneyType](../entity-attribute-metadata.md#money_type). The value `2` means that the level of decimal precision matches [TransactionCurrency.CurrencyPrecision](/power-apps/developer/data-platform/reference/entities/transactioncurrency#BKMK_CurrencyPrecision) that is associated with the current record.|
  
The following example creates a money attribute using the properties and adds it to the `sample_bankaccount` table. The URI for the attribute is returned in the response.  
  
 **Request:**

```http   
POST [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "AttributeType": "Money",  
 "AttributeTypeName": {  
  "Value": "MoneyType"  
 },  
 "Description": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Enter the balance amount",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "DisplayName": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Balance",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "RequiredLevel": {  
  "Value": "None",  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
 },  
 "SchemaName": "new_Balance",  
 "@odata.type": "Microsoft.Dynamics.CRM.MoneyAttributeMetadata",  
 "PrecisionSource": 2  
}  
```  
  
 **Response:**

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f11bef16-287c-e511-80d2-00155d2a68d2)  
```  
  
<a name="bkmk_createDateTime"></a>

### Create a datetime column

The following example uses these properties to create a datetime attribute.  
  
|[DateTimeAttributeMetadata](xref:Microsoft.Dynamics.CRM.DateTimeAttributeMetadata) properties|Values|  
|-----------------------------------|------------|  
|`SchemaName`|`new_Checkeddate`|  
|`DisplayName`|`Date`|  
|`Description`|The date the account balance was last confirmed.|  
|`RequiredLevel`|`None`|  
|`Format`|`DateOnly` **Note:**  For the valid options for this property, see [DateTimeFormat EnumType](xref:Microsoft.Dynamics.CRM.DateTimeFormat)|  
  
The following example creates a datetime attribute using the properties and adds it to the `sample_bankaccount` table.
 The URI for the attribute is returned in the response.  
  
 **Request:**

```http 
POST [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "AttributeType": "DateTime",  
 "AttributeTypeName": {  
  "Value": "DateTimeType"  
 },  
 "Description": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "The date the account balance was last confirmed",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "DisplayName": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Date",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "RequiredLevel": {  
  "Value": "None",  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
 },  
 "SchemaName": "new_Checkeddate",  
 "@odata.type": "Microsoft.Dynamics.CRM.DateTimeAttributeMetadata",  
 "Format": "DateOnly"  
}  
```  
  
 **Response:**

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(fe1bef16-287c-e511-80d2-00155d2a68d2)  
```  

### Create a boolean column

The following example uses these properties to create a boolean column.  
  
|[BooleanAttributeMetadata](xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata) properties|Values|  
|-----------------------------------|------------|  
|`SchemaName`|`new_Boolean`|  
|`DisplayName`|Sample Boolean|  
|`Description`|Boolean Attribute|  
|`RequiredLevel`|`None`|  
|`OptionSet.TrueOption`|True|
|`OptionSet.FalseOption`|False|  
  
The following example creates a boolean attribute using the properties and adds it to the entity with the `LogicalName` value of `new_bankaccount`. The URI for the attribute is returned in the response.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='new_bankaccount')/Attributes HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.type": "Microsoft.Dynamics.CRM.BooleanAttributeMetadata",
  "AttributeType": "Boolean",
  "AttributeTypeName": {
    "Value": "BooleanType"
  },
  "DefaultValue": false,
  "OptionSet": {
    "TrueOption": {
      "Value": 1,
      "Label": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "True",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        ]
      }
    },
    "FalseOption": {
      "Value": 0,
      "Label": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "False",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        ]
      }
    },
    "OptionSetType": "Boolean"
  },
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Boolean Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Boolean",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "new_Boolean"
}
```

**Response:**

```http
HTTP/1.1 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='new_bankaccount')/Attributes(38d20735-6817-ed11-b83e-00224837179f)
```

<a name="bkmk_CreateCustomerLookup"></a>

### Create a customer lookup column

Unlike other attributes, a customer lookup attribute is created using the [CreateCustomerRelationships Action](xref:Microsoft.Dynamics.CRM.CreateCustomerRelationships).

The parameters for this action require the definition of the lookup attribute and a pair of one-to-many relationships. A customer lookup attribute has two one-to-many relationships: one to the account entity and the other one to contact entity.  
  
 The following example uses these properties to create a customer lookup attribute.  
  
|Customer lookup attribute properties|Values|  
|------------------------------------------|------------|  
|`SchemaName`|`new_CustomerId`|  
|`DisplayName`|Customer|  
|`Description`|Sample Customer Lookup Attribute|  
  
The example creates a customer lookup attribute, `new_CustomerId`, and adds it to the custom entity:  `new_bankaccount`. The response is a [CreateCustomerRelationshipsResponse ComplexType"](xref:Microsoft.Dynamics.CRM.CreateCustomerRelationshipsResponse).  
  
 **Request:**

```http
POST [Organization URI]/api/data/v9.2/CreateCustomerRelationships HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
  
{  
    "OneToManyRelationships": [{  
        "SchemaName": "new_bankaccount_customer_account",  
        "ReferencedEntity": "account",  
        "ReferencingEntity": "new_bankaccount"  
    }, {  
        "SchemaName": "new_bankaccount_customer_contact",  
        "ReferencedEntity": "contact",  
        "ReferencingEntity": "new_bankaccount"  
    }],  
    "Lookup": {  
        "AttributeType": "Lookup",  
        "AttributeTypeName": {  
            "Value": "LookupType"  
        },  
        "Description": {  
            "@odata.type": "Microsoft.Dynamics.CRM.Label",  
            "LocalizedLabels": [{  
                "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
                "Label": "Sample Customer Lookup Attribute",  
                "LanguageCode": 1033  
            }],  
            "UserLocalizedLabel": {  
                "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
                "Label": "Sample Customer Lookup Attribute",  
                "LanguageCode": 1033  
            }  
        },  
        "DisplayName": {  
            "@odata.type": "Microsoft.Dynamics.CRM.Label",  
            "LocalizedLabels": [{  
                "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
                "Label": "Customer",  
                "LanguageCode": 1033  
            }],  
            "UserLocalizedLabel": {  
                "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
                "Label": "Customer",  
                "LanguageCode": 1033  
            }  
        },  
        "SchemaName": "new_CustomerId",  
        "@odata.type": "Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata"  
    }  
}  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CreateCustomerRelationshipsResponse",  
    "RelationshipIds": [  
        "a7d261bc-3580-e611-80d7-00155d2a68de", "aed261bc-3580-e611-80d7-00155d2a68de"  
    ],  
    "AttributeId": "39a5d94c-e8a2-4a41-acc0-8487242d455e"  
}  
  
```

### Create a decimal column

The following example uses these properties to create a decimal column. 
  
|[DecimalAttributeMetadata](xref:Microsoft.Dynamics.CRM.DecimalAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`sample_Decimal`|  
|`DisplayName`|Sample Decimal|  
|`Description`|Decimal Attribute|  
|`RequiredLevel`|`None`|  
|`MaxValue`|100.0|  
|`MinValue`|0.0|
|`Precision`|1|
  
The following example creates a decimal attribute using the properties and adds it to the `sample_bankaccount` table.

The URI for the attribute is returned in the response.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1370

{
  "@odata.type": "Microsoft.Dynamics.CRM.DecimalAttributeMetadata",
  "AttributeType": "Decimal",
  "AttributeTypeName": {
    "Value": "DecimalType"
  },
  "MaxValue": 100.0,
  "MinValue": 0.0,
  "Precision": 1,
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Decimal Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Decimal Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Decimal",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample Decimal",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_Decimal"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(dba9c0df-4c05-ee11-8f6e-000d3a993550)
```



### Create an integer column

The following example uses these properties to create an integer column. 
  
|[IntegerAttributeMetadata](xref:Microsoft.Dynamics.CRM.IntegerAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`sample_Integer`|  
|`DisplayName`|Sample Integer|  
|`Description`|Integer Attribute|  
|`RequiredLevel`|`None`|  
|`MaxValue`|100|  
|`MinValue`|0|
|`Format`|None|
  
The following example creates an integer column using the properties and adds it to the `sample_bankaccount` table.

The URI for the column is returned in the response.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1392

{
  "@odata.type": "Microsoft.Dynamics.CRM.IntegerAttributeMetadata",
  "AttributeType": "Integer",
  "AttributeTypeName": {
    "Value": "IntegerType"
  },
  "MaxValue": 100,
  "MinValue": 0,
  "Format": "None",
  "SourceTypeMask": 0,
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Integer Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Integer Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Integer",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample Integer",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_Integer"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(17aac0df-4c05-ee11-8f6e-000d3a993550)
```

### Create a memo column

The following example uses these properties to create a memo column.  
  
|[MemoAttributeMetadata](xref:Microsoft.Dynamics.CRM.MemoAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`sample_Memo`|  
|`DisplayName`|Sample Memo|  
|`Description`|Memo Attribute|  
|`RequiredLevel`|`None`|  
|`MaxLength`|500|  
|`Format`|TextArea|  
  
The following example creates a memo column using the properties and adds it to the `sample_bankaccount` table.

The URI for the attribute is returned in the response.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1384

{
  "@odata.type": "Microsoft.Dynamics.CRM.MemoAttributeMetadata",
  "AttributeType": "Memo",
  "AttributeTypeName": {
    "Value": "MemoType"
  },
  "Format": "TextArea",
  "ImeMode": "Disabled",
  "MaxLength": 500,
  "IsLocalizable": false,
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Memo Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Memo Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Memo",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample Memo",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_Memo"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(b12d3cee-4c05-ee11-8f6e-000d3a993550)
```

### Create a choice column

The following example uses these properties to create a local choice column.  
  
|[PicklistAttributeMetadata](xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`sample_Choice`|  
|`DisplayName`|Sample Choice|  
|`Description`|Choice Attribute|  
|`RequiredLevel`|`None`|  
|`OptionSet`|value:`727000000`, label:**Bravo**<br />value:`727000001`, label:**Delta**<br />value:`727000002`, label:**Alpha**<br />value:`727000003`, label:**Charlie**<br />value:`727000004`, label:**Foxtrot**<br />|
  
The following example creates a local column using the properties and adds it to the `sample_bankaccount` table.

The URI for the attribute is returned in the response.

> [!NOTE]
> For an example showing how to create a choice column with a global option set, see [Create a choice column using a global option set](create-update-optionsets.md#create-a-choice-column-using-a-global-option-set)

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 4524

{
  "@odata.type": "Microsoft.Dynamics.CRM.PicklistAttributeMetadata",
  "AttributeType": "Picklist",
  "AttributeTypeName": {
    "Value": "PicklistType"
  },
  "SourceTypeMask": 0,
  "OptionSet": {
    "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
    "Options": [
      {
        "Value": 727000000,
        "Label": {
          "@odata.type": "Microsoft.Dynamics.CRM.Label",
          "LocalizedLabels": [
            {
              "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
              "Label": "Bravo",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Bravo",
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
              "Label": "Delta",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Delta",
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
              "Label": "Alpha",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Alpha",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        }
      },
      {
        "Value": 727000003,
        "Label": {
          "@odata.type": "Microsoft.Dynamics.CRM.Label",
          "LocalizedLabels": [
            {
              "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
              "Label": "Charlie",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Charlie",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        }
      },
      {
        "Value": 727000004,
        "Label": {
          "@odata.type": "Microsoft.Dynamics.CRM.Label",
          "LocalizedLabels": [
            {
              "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
              "Label": "Foxtrot",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Foxtrot",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        }
      }
    ],
    "IsGlobal": false,
    "OptionSetType": "Picklist"
  },
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Choice Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Choice Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Choice",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample Choice",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_Choice"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(eed205fb-4c05-ee11-8f6e-000d3a993550)
```

### Create a multi-select choice column

The following example uses these properties to create a local multi-select choice column.
  
|[MultiSelectPicklistAttributeMetadata](xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata) properties|Values|  
|---------------------------------|------------|  
|`SchemaName`|`sample_Choice`|  
|`DisplayName`|Sample Choice|  
|`Description`|Choice Attribute|  
|`RequiredLevel`|`None`|  
|`OptionSet`|value:`727000000`, label:**Appetizer**<br />value:`727000001`, label:**Entree**<br />value:`727000002`, label:**Dessert**|
  
The following example creates a local multi-select choice column using the properties and adds it to the `sample_bankaccount` table.

The URI for the attribute is returned in the response.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 3404

{
  "@odata.type": "Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata",
  "AttributeType": "Virtual",
  "AttributeTypeName": {
    "Value": "MultiSelectPicklistType"
  },
  "SourceTypeMask": 0,
  "OptionSet": {
    "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
    "Options": [
      {
        "Value": 727000000,
        "Label": {
          "@odata.type": "Microsoft.Dynamics.CRM.Label",
          "LocalizedLabels": [
            {
              "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
              "Label": "Appetizer",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Appetizer",
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
              "Label": "Entree",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Entree",
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
              "Label": "Dessert",
              "LanguageCode": 1033,
              "IsManaged": false
            }
          ],
          "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Dessert",
            "LanguageCode": 1033,
            "IsManaged": false
          }
        }
      }
    ],
    "IsGlobal": false,
    "OptionSetType": "Picklist"
  },
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "MultiSelect Choice Attribute",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "MultiSelect Choice Attribute",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample MultiSelect Choice",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample MultiSelect Choice",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_MultiSelectChoice"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(afd63201-4d05-ee11-8f6e-000d3a993550)
```

  
<a name="bkmk_updateAttribute"></a>
 
## Update a column

As mentioned in [Update table definitions](create-update-entity-definitions-using-web-api.md#bkmk_updateEntities), data model entities are updated using the HTTP `PUT` method with the entire JSON definition of the current item. This pattern applies to entity attributes and entities. Just like with entities, you can overwrite labels using the `MSCRM.MergeLabels` header with the value set to `false`, and you must publish customizations before they're active in the system.  

Using the boolean attribute created in [Create a Boolean column](#create-a-boolean-column) above, we must first retrieve the entire attribute.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='new_bankaccount')/Attributes(LogicalName='new_boolean')/Microsoft.Dynamics.CRM.BooleanAttributeMetadata HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('new_bankaccount')/Attributes/Microsoft.Dynamics.CRM.BooleanAttributeMetadata/$entity",
  "MetadataId": "38d20735-6817-ed11-b83e-00224837179f",
  "HasChanged": null,
  "AttributeOf": null,
  "AttributeType": "Boolean",
  "ColumnNumber": 35,
  "DeprecatedVersion": null,
  "IntroducedVersion": "1.0.0.0",
  "EntityLogicalName": "new_bankaccount",
  "IsCustomAttribute": true,
  "IsPrimaryId": false,
  "IsValidODataAttribute": true,
  "IsPrimaryName": false,
  "IsValidForCreate": true,
  "IsValidForRead": true,
  "IsValidForUpdate": true,
  "CanBeSecuredForRead": true,
  "CanBeSecuredForCreate": true,
  "CanBeSecuredForUpdate": true,
  "IsSecured": false,
  "IsRetrievable": false,
  "IsFilterable": false,
  "IsSearchable": false,
  "IsManaged": false,
  "LinkedAttributeId": null,
  "LogicalName": "new_boolean",
  "IsValidForForm": true,
  "IsRequiredForForm": false,
  "IsValidForGrid": true,
  "SchemaName": "new_Boolean",
  "ExternalName": null,
  "IsLogical": false,
  "IsDataSourceSecret": false,
  "InheritsFrom": null,
  "CreatedOn": "2022-08-08T22:19:49Z",
  "ModifiedOn": "2022-08-08T22:19:49Z",
  "SourceType": 0,
  "AutoNumberFormat": null,
  "DefaultValue": false,
  "FormulaDefinition": "",
  "SourceTypeMask": 0,
  "AttributeTypeName": {
    "Value": "BooleanType"
  },
  "Description": {
    "LocalizedLabels": [
      {
        "Label": "Boolean Attribute",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "2b5545d2-a59b-4503-8846-95665283b41f",
        "HasChanged": null
      }
    ],
    "UserLocalizedLabel": {
      "Label": "Boolean Attribute",
      "LanguageCode": 1033,
      "IsManaged": false,
      "MetadataId": "2b5545d2-a59b-4503-8846-95665283b41f",
      "HasChanged": null
    }
  },
  "DisplayName": {
    "LocalizedLabels": [
      {
        "Label": "Sample Boolean",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "e6b8d06c-067e-4ab0-a9a8-32f520b25e36",
        "HasChanged": null
      }
    ],
    "UserLocalizedLabel": {
      "Label": "Sample Boolean",
      "LanguageCode": 1033,
      "IsManaged": false,
      "MetadataId": "e6b8d06c-067e-4ab0-a9a8-32f520b25e36",
      "HasChanged": null
    }
  },
  "IsAuditEnabled": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyauditsettings"
  },
  "IsGlobalFilterEnabled": {
    "Value": false,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyglobalfiltersettings"
  },
  "IsSortableEnabled": {
    "Value": false,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyissortablesettings"
  },
  "IsCustomizable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "iscustomizable"
  },
  "IsRenameable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "isrenameable"
  },
  "IsValidForAdvancedFind": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifysearchsettings"
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "CanModifyAdditionalSettings": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyadditionalsettings"
  },
  "Settings": []
}
```

Then, change the properties you want to change.

|[BooleanAttributeMetadata](xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata) properties|Old Values|New Values|
|-----------------------------------|------------|------------|
|`DisplayName`|Sample Boolean|Sample Boolean Updated|
|`Description`|Boolean Attribute|Boolean Attribute Updated|
|`RequiredLevel`|`None`|`ApplicationRequired`|

> [!NOTE]
> If you want to update the options, you must send a different request. More information: [Update options](create-update-optionsets.md#update-options).

Now you can send the `PUT` request with the modified properties:

**Request:**

```http
PUT [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='new_bankaccount')/Attributes(LogicalName='new_boolean') HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
MSCRM.MergeLabels: true
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.type": "Microsoft.Dynamics.CRM.BooleanAttributeMetadata",
  "MetadataId": "e160ff9b-6f17-ed11-b83e-00224837179f",
  "HasChanged": null,
  "AttributeOf": null,
  "AttributeType": "Boolean",
  "ColumnNumber": 35,
  "DeprecatedVersion": null,
  "IntroducedVersion": "1.0.0.0",
  "EntityLogicalName": "new_bankaccount",
  "IsCustomAttribute": true,
  "IsPrimaryId": false,
  "IsValidODataAttribute": true,
  "IsPrimaryName": false,
  "IsValidForCreate": true,
  "IsValidForRead": true,
  "IsValidForUpdate": true,
  "CanBeSecuredForRead": true,
  "CanBeSecuredForCreate": true,
  "CanBeSecuredForUpdate": true,
  "IsSecured": false,
  "IsRetrievable": false,
  "IsFilterable": false,
  "IsSearchable": false,
  "IsManaged": false,
  "LinkedAttributeId": null,
  "LogicalName": "new_boolean",
  "IsValidForForm": true,
  "IsRequiredForForm": false,
  "IsValidForGrid": true,
  "SchemaName": "new_Boolean",
  "ExternalName": null,
  "IsLogical": false,
  "IsDataSourceSecret": false,
  "InheritsFrom": null,
  "CreatedOn": "2022-08-08T23:12:55Z",
  "ModifiedOn": "2022-08-08T23:12:55Z",
  "SourceType": 0,
  "AutoNumberFormat": null,
  "DefaultValue": false,
  "FormulaDefinition": "",
  "SourceTypeMask": 0,
  "AttributeTypeName": {
    "Value": "BooleanType"
  },
  "Description": {
    "LocalizedLabels": [
      {
        "Label": "Boolean Attribute Updated",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "b370f0dd-329f-434e-8b9f-b6eb47d0141f",
        "HasChanged": null
      }
    ],
    "UserLocalizedLabel": {
      "Label": "Boolean Attribute Updated",
      "LanguageCode": 1033,
      "IsManaged": false,
      "MetadataId": "b370f0dd-329f-434e-8b9f-b6eb47d0141f",
      "HasChanged": null
    }
  },
  "DisplayName": {
    "LocalizedLabels": [
      {
        "Label": "Sample Boolean Updated",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "63a9e5f1-e730-40cb-a410-495367d5856d",
        "HasChanged": null
      }
    ],
    "UserLocalizedLabel": {
      "Label": "Sample Boolean Updated",
      "LanguageCode": 1033,
      "IsManaged": false,
      "MetadataId": "63a9e5f1-e730-40cb-a410-495367d5856d",
      "HasChanged": null
    }
  },
  "IsAuditEnabled": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyauditsettings"
  },
  "IsGlobalFilterEnabled": {
    "Value": false,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyglobalfiltersettings"
  },
  "IsSortableEnabled": {
    "Value": false,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyissortablesettings"
  },
  "IsCustomizable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "iscustomizable"
  },
  "IsRenameable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "isrenameable"
  },
  "IsValidForAdvancedFind": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifysearchsettings"
  },
  "RequiredLevel": {
    "Value": "ApplicationRequired",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "CanModifyAdditionalSettings": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "canmodifyadditionalsettings"
  },
  "Settings": []
}

```

**Response:**

```http
HTTP/1.1 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='new_bankaccount')/Attributes(LogicalName='new_boolean')
```

### See also

[Use the Web API with Microsoft Dataverse metadata](use-web-api-metadata.md)  
[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
[Model table relationships using the Web API](create-update-entity-relationships-using-web-api.md)  
[Work with table definitions using the Organization service](../org-service/work-with-metadata.md)  
[Column (attribute) definitions](../entity-attribute-metadata.md)  
[Web API Metadata Operations Sample](web-api-metadata-operations-sample.md)  
[Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

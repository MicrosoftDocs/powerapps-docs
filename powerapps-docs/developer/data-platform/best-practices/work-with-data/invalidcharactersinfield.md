---
title: "Manage invalid characters | Microsoft Docs"
description: Describes how to manage invalid characters.

ms.date: 08/09/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly"
ms.subservice: dataverse-developer
ms.author: "pehecke"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Manage invalid characters

There are a set of characters that cannot be saved in string or memo columns. When an application saves data containing these characters to Dataverse, the following error will occur:

Name: `InvalidCharactersInField`<br />
Hexadecimal error code : `80040278`<br />
Error Number: `-2147220872`<br />
Description: `The field '{0}' contains one or more invalid characters.`<br />

Dataverse uses the [System.Xml.XmlConvert.VerifyXmlChars(String) Method](/dotnet/api/system.xml.xmlconvert.verifyxmlchars) for every string value passed to these columns. This error is thrown on the first invalid character encountered.

You may encounter these characters in email content that includes replies or when text is copied from another source which may have characters to control presentation.

To prevent this error you can:

- HTML encode the content before saving.

- Remove the individual invalid characters, use the [System.Xml.XmlConvert.IsXmlChar(Char) Method](/dotnet/api/system.xml.xmlconvert.isxmlchar) as shown in the following example:

  ```csharp
  static string RemoveInvalidXmlChars(string text) {
      var validXmlChars = text.Where(ch => XmlConvert.IsXmlChar(ch)).ToArray();
      return new string(validXmlChars);
  }
  ```


### See Also

[Work with data using code in Dataverse (Power Apps)](../../work-with-data.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]


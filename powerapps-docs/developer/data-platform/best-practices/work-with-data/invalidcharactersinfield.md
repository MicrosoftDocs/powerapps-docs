---
title: "Manage invalid characters | Microsoft Docs"
description: "Describes how to manage invalid characters with the Dataverse API. Only allowed characters can be used or an error is thrown."
ms.date: 06/20/2025
ms.topic: article
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# Manage invalid characters

There is a set of characters that can't be saved in string or memo columns. When an application saves data containing these characters to Dataverse, the following error occurs:

Name: `InvalidCharactersInField`<br />
Hexadecimal error code: `80040278`<br />
Error Number: `-2147220872`<br />
Description: `The field '{0}' contains one or more invalid characters.`<br />

Dataverse uses the [System.Xml.XmlConvert.VerifyXmlChars(String) Method](/dotnet/api/system.xml.xmlconvert.verifyxmlchars) for every string value passed to these columns. This error is thrown on the first invalid character encountered.

You might encounter these characters in email content that includes replies or when text is copied from another source that might have characters to control presentation.

To prevent this error, you can:

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


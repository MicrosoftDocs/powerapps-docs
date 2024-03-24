> [!TIP]
> With .NET, you can generate a `BlockId` using this code:
> 
> ```csharp
> string blockId = Convert.ToBase64String(Encoding.UTF8.GetBytes(Guid.NewGuid().ToString()));
> ```
>
> Also with .NET, if you set the `byte[]` data to a `JObject` `BlockData` property, the `byte[]` is Base64-encoded when you set the [HttpRequestMessage.Content](xref:System.Net.Http.HttpRequestMessage.Content) using `JObject.ToString()`.
With each request, increment the `Offset` value by the number of bytes requested in the previous request.  For example, the following values were used to download a file that is `25870370` bytes in seven requests:

|Request number|Offset|BlockLength|Remaining|
|---------|---------|---------|---------|
|1|`0`|`4194304`|`25870370`|
|2|`4194304`|`4194304`|`21676066`|
|3|`8388608`|`4194304`|`17481762`|
|4|`12582912`|`4194304`|`13287458`|
|5|`16777216`|`4194304`|`9093154`|
|6|`20971520`|`4194304`|`4898850`|
|7|`25165824`|`4194304`|`704546`|

> [!NOTE]
> The requested `BlockLength` value can be constant. It isn't required to be adjusted for the last request in the example above where only `704546` bytes remained.
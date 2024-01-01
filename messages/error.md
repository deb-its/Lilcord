# An error has occured!

> Solution 1

Check ```dist/config.json``` for any syntax errors.

Your config file must look like this:
```json
{"zoom": 1.0, "first_launch": false} <- "zoom can be any number"
                                     <- "first_launch can be false or true"
```
--------------------
> Solution 2

If there is no ```dist/config.json```, create one and add
```json
{"zoom": 1.0, "first_launch": true}
```

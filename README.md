# Model-Generator


Generate code for basic models from JSON schema. 


## Languages
- [ ] Java
- [ ] Groovy
- [ ] Kotlin
- [ ] TypeScript


## To Do
* Protected properties?
* folder structure for generated java classes


## Possible Enhancements
* Java: Constructor generation
* Java: toString, hashCode, equals


## Example Input
```JSON
{
    "id": "http://json-schema.org/thing",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Cat",
    "description": "A cat",
    "type": "object",
    "extends": "Common/Thing.json",
    "properties": {
        "breed": {
            "type": "string"
        },
        "color": {
            "type": "string"
        }
    }
}
```


## Commands
* Run tests ```python -m unittest```


## References
* https://schema.org/docs/schemas.html
* https://json-schema.org/understanding-json-schema/index.html
* https://www.jsonschemavalidator.net/
* Inspiration https://app.quicktype.io/